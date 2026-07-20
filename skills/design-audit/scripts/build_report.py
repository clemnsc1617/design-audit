#!/usr/bin/env python3
"""Build a self-contained design-audit HTML report from findings.json.

Usage:
    python3 build_report.py <findings.json> [-o report.html] [--no-inline]

Python 3 stdlib only. Validates findings.json against the contract documented in
assets/findings.schema.json (hand-rolled checks - no jsonschema dependency),
base64-inlines screen images (unless --no-inline), injects the data into
assets/report-template.html, and writes one self-contained HTML file.

Fails loudly: the first invalid field aborts the build with its JSON path.
"""

import argparse
import base64
import json
import mimetypes
import sys
from pathlib import Path

VERDICTS = {"pass", "partial", "fail", "na"}
GRADES = {"A", "B", "C", "D", "F", None}
DIM_IDS = {"US", "VD", "AC", "CO", "UF"}
BUCKETS = {
    "mobile app (iOS)", "mobile app (Android)", "mobile app (OS indeterminate)",
    "mobile web", "desktop web", "desktop app", "responsive pair",
}
CONVENTIONS = {"HIG", "Material 3", "web"}
INPUT_TYPES = {"screenshot", "url", "figma", "video"}


def die(path, msg):
    sys.exit(f"findings.json invalid at {path}: {msg}")


def need(obj, key, typ, path, nullable=False):
    if key not in obj:
        die(f"{path}.{key}", "missing required key")
    v = obj[key]
    if v is None:
        if nullable:
            return v
        die(f"{path}.{key}", "must not be null")
    if typ is float:
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            die(f"{path}.{key}", f"expected number, got {type(v).__name__}")
    elif not isinstance(v, typ) or isinstance(v, bool) and typ is int:
        die(f"{path}.{key}", f"expected {getattr(typ, '__name__', typ)}, got {type(v).__name__}")
    return v


def need_pct(obj, key, path):
    v = need(obj, key, float, path)
    if not 0 <= v <= 100:
        die(f"{path}.{key}", f"{v} outside 0-100")
    return v


def validate(d):
    if not isinstance(d, dict):
        die("$", "top level must be an object")
    for k in ("meta", "platform", "dimensions", "scorecard", "screens", "findings", "advisories", "flow"):
        if k not in d:
            die(f"$.{k}", "missing required section")

    # meta
    m, p = d["meta"], "$.meta"
    need(m, "title", str, p)
    date = need(m, "date", str, p)
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        die(f"{p}.date", f"'{date}' is not YYYY-MM-DD")
    if need(m, "inputType", str, p) not in INPUT_TYPES:
        die(f"{p}.inputType", f"must be one of {sorted(INPUT_TYPES)}")
    overall = need(m, "overall", int, p, nullable=True)
    if overall is not None and not 0 <= overall <= 100:
        die(f"{p}.overall", f"{overall} outside 0-100")
    if m.get("grade") not in GRADES:
        die(f"{p}.grade", f"must be A-F or null, got {m.get('grade')!r}")
    if (overall is None) != (m.get("grade") is None):
        die(f"{p}.grade", "overall and grade must be null together")
    need(m, "summary", str, p)
    for k in ("assumptions", "limitations"):
        for i, s in enumerate(need(m, k, list, p)):
            if not isinstance(s, str):
                die(f"{p}.{k}[{i}]", "expected string")

    # platform
    pl, p = d["platform"], "$.platform"
    pscreens = need(pl, "screens", list, p)
    if not pscreens:
        die(f"{p}.screens", "must not be empty")
    for i, s in enumerate(pscreens):
        pp = f"{p}.screens[{i}]"
        need(s, "screenId", str, pp)
        if need(s, "bucket", str, pp) not in BUCKETS:
            die(f"{pp}.bucket", f"unknown bucket {s['bucket']!r}")
        if need(s, "conventionSet", str, pp) not in CONVENTIONS:
            die(f"{pp}.conventionSet", f"unknown convention set {s['conventionSet']!r}")
        if not need(s, "signals", list, pp):
            die(f"{pp}.signals", "must list at least one deciding signal")

    # dimensions
    dims, p = d["dimensions"], "$.dimensions"
    if len(dims) != 5:
        die(p, f"expected exactly 5 dimensions, got {len(dims)}")
    seen, weight_sum = set(), 0.0
    for i, dim in enumerate(dims):
        pp = f"{p}[{i}]"
        did = need(dim, "id", str, pp)
        if did not in DIM_IDS:
            die(f"{pp}.id", f"unknown dimension {did!r}")
        if did in seen:
            die(f"{pp}.id", f"duplicate dimension {did!r}")
        seen.add(did)
        need(dim, "name", str, pp)
        scored = need(dim, "scored", bool, pp)
        weight = need(dim, "weight", float, pp, nullable=True)
        score = need(dim, "score", float, pp, nullable=True)
        if scored:
            if weight is None or score is None:
                die(pp, "scored dimension needs non-null weight and score")
            if not 0 <= score <= 100:
                die(f"{pp}.score", f"{score} outside 0-100")
            weight_sum += weight
        elif weight is not None or score is not None:
            die(pp, "unscored dimension must have null weight and score")
    if seen and weight_sum and abs(weight_sum - 1.0) > 0.001:
        die(f"{p}[*].weight", f"scored weights sum to {weight_sum}, expected 1.0")

    # scorecard
    sc, p = d["scorecard"], "$.scorecard"
    if not sc:
        die(p, "must not be empty")
    crit_ids = set()
    for i, row in enumerate(sc):
        pp = f"{p}[{i}]"
        cid = need(row, "criterionId", str, pp)
        crit_ids.add(cid)
        if need(row, "dimension", str, pp) not in DIM_IDS:
            die(f"{pp}.dimension", f"unknown dimension {row['dimension']!r}")
        if cid.split("-")[0] != row["dimension"]:
            die(f"{pp}.criterionId", f"{cid} does not match dimension {row['dimension']}")
        need(row, "standard", str, pp)
        need(row, "source", str, pp)
        v = need(row, "verdict", str, pp)
        if v not in VERDICTS:
            die(f"{pp}.verdict", f"unknown verdict {v!r}")
        need(row, "reasoning", str, pp)
        if v == "na" and not row.get("naReason"):
            die(f"{pp}.naReason", "required when verdict is na (an N/A without a reason is a bug)")

    # screens
    scr, p = d["screens"], "$.screens"
    if not scr:
        die(p, "must not be empty")
    screen_ids = set()
    for i, s in enumerate(scr):
        pp = f"{p}[{i}]"
        sid = need(s, "id", str, pp)
        if sid in screen_ids:
            die(f"{pp}.id", f"duplicate screen id {sid!r}")
        screen_ids.add(sid)
        need(s, "label", str, pp)
        need(s, "image", str, pp)
    if screen_ids != {s["screenId"] for s in pscreens}:
        die("$.platform.screens", "screenIds must exactly match $.screens[].id")

    # findings
    fnd, p = d["findings"], "$.findings"
    marker_ids = set()
    for i, f in enumerate(fnd):
        pp = f"{p}[{i}]"
        fid = need(f, "id", int, pp)
        if fid in marker_ids:
            die(f"{pp}.id", f"duplicate marker id {fid}")
        marker_ids.add(fid)
        if need(f, "screenId", str, pp) not in screen_ids:
            die(f"{pp}.screenId", f"{f['screenId']!r} not in screens")
        if need(f, "criterionId", str, pp) not in crit_ids:
            die(f"{pp}.criterionId", f"{f['criterionId']!r} not in scorecard")
        sev = need(f, "severity", int, pp)
        if not 0 <= sev <= 4:
            die(f"{pp}.severity", f"{sev} outside 0-4")
        for k in ("title", "evidence", "fix", "source"):
            need(f, k, str, pp)
        need_pct(f, "x", pp)
        need_pct(f, "y", pp)
        if ("w" in f) != ("h" in f):
            die(pp, "w and h must appear together (region box) or not at all (point marker)")
        if "w" in f:
            need_pct(f, "w", pp)
            need_pct(f, "h", pp)

    # advisories
    for i, a in enumerate(d["advisories"]):
        pp = f"$.advisories[{i}]"
        need(a, "title", str, pp)
        need(a, "note", str, pp)

    # flow
    fl, p = d["flow"], "$.flow"
    for k in ("observed", "missing", "suggestedNext"):
        for i, s in enumerate(need(fl, k, list, p)):
            if not isinstance(s, str):
                die(f"{p}.{k}[{i}]", "expected string")


def inline_images(d, base_dir, no_inline):
    for i, s in enumerate(d["screens"]):
        img = s["image"]
        if img.startswith("data:"):
            continue
        path = (base_dir / img).resolve()
        if not path.is_file():
            die(f"$.screens[{i}].image", f"file not found: {path}")
        if no_inline:
            s["image"] = str(path)
            continue
        mime = mimetypes.guess_type(path.name)[0] or "image/png"
        if not mime.startswith("image/"):
            die(f"$.screens[{i}].image", f"not an image: {path} ({mime})")
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        s["image"] = f"data:{mime};base64,{data}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("findings", help="path to findings.json")
    ap.add_argument("-o", "--out", default=None, help="output HTML path (default: <findings-dir>/report.html)")
    ap.add_argument("--no-inline", action="store_true",
                    help="reference image files by absolute path instead of base64-inlining (use beyond ~10 screens)")
    args = ap.parse_args()

    findings_path = Path(args.findings)
    if not findings_path.is_file():
        sys.exit(f"not found: {findings_path}")
    try:
        data = json.loads(findings_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"findings.json is not valid JSON: {e}")

    validate(data)
    inline_images(data, findings_path.parent, args.no_inline)

    template_path = Path(__file__).resolve().parent.parent / "assets" / "report-template.html"
    if not template_path.is_file():
        sys.exit(f"template not found: {template_path}")
    template = template_path.read_text(encoding="utf-8")

    for token in ("{{TITLE}}", "{{AUDIT_JSON}}"):
        if token not in template:
            sys.exit(f"template is missing required token {token}")

    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("{{TITLE}}", data["meta"]["title"]).replace("{{AUDIT_JSON}}", payload)

    out = Path(args.out) if args.out else findings_path.parent / "report.html"
    out.write_text(html, encoding="utf-8")
    n_scored = sum(1 for x in data["dimensions"] if x["scored"])
    print(f"OK: {out}  ({len(data['screens'])} screen(s), {len(data['findings'])} finding(s), "
          f"{len(data['scorecard'])} scorecard rows, {n_scored} scored dimensions, "
          f"{out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
