#!/usr/bin/env python3
"""Detect time-series outliers with a rolling median and MAD."""
from __future__ import annotations
import argparse, csv, json, statistics, sys
from pathlib import Path

def median(values):
    return statistics.median(values)

def detect(rows, value_column, time_column=None, window=5, threshold=3.5):
    history=[]; anomalies=[]; skipped=0
    for row_number,row in enumerate(rows, start=2):
        raw=row.get(value_column,"")
        try: value=float(raw)
        except (TypeError,ValueError): skipped+=1; continue
        if len(history)>=window:
            baseline=history[-window:]
            center=median(baseline)
            deviations=[abs(x-center) for x in baseline]
            mad=median(deviations)
            distance=abs(value-center)
            score=(distance/(1.4826*mad)) if mad else (0.0 if distance==0 else None)
            flagged=(distance>0 if mad==0 else score>threshold)
            if flagged:
                anomalies.append({"row":row_number,"time":row.get(time_column,"") if time_column else "",
                    "value":value,"baseline_median":center,"mad":mad,
                    "score":"infinite" if score is None else round(score,4)})
        history.append(value)
    return {"rows_analyzed":len(history),"rows_skipped":skipped,"anomaly_count":len(anomalies),"anomalies":anomalies}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file",type=Path); ap.add_argument("--value-column",required=True)
    ap.add_argument("--time-column"); ap.add_argument("--window",type=int,default=5)
    ap.add_argument("--threshold",type=float,default=3.5); ap.add_argument("--json",action="store_true")
    ap.add_argument("--output",type=Path); args=ap.parse_args()
    if args.window<2: ap.error("--window must be at least 2")
    if args.threshold<=0: ap.error("--threshold must be positive")
    try:
        with args.file.open(newline="",encoding="utf-8-sig") as handle:
            reader=csv.DictReader(handle)
            if not reader.fieldnames or args.value_column not in reader.fieldnames: raise ValueError(f"missing value column: {args.value_column}")
            if args.time_column and args.time_column not in reader.fieldnames: raise ValueError(f"missing time column: {args.time_column}")
            report=detect(reader,args.value_column,args.time_column,args.window,args.threshold)
    except (OSError,ValueError) as exc: print(f"error: {exc}",file=sys.stderr); return 2
    rendered=json.dumps(report,indent=2)
    if args.output:
        if args.output.suffix.lower()==".csv":
            with args.output.open("w",newline="",encoding="utf-8") as handle:
                fields=["row","time","value","baseline_median","mad","score"]
                writer=csv.DictWriter(handle,fieldnames=fields); writer.writeheader(); writer.writerows(report["anomalies"])
        else: args.output.write_text(rendered,encoding="utf-8")
    if args.json or not args.output: print(rendered)
    return 1 if report["anomaly_count"] else 0
if __name__=="__main__": raise SystemExit(main())
