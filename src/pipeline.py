import argparse, json
from auditor import run_audit

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to dataset CSV")
    parser.add_argument("--preds", required=True, help="Path to predictions CSV")
    args = parser.parse_args()

    results = run_audit(args.data, args.preds)
    print("📊 Fairness Audit Results:")
    print(json.dumps(results, indent=2))

    with open("reports/audit_report.md", "w") as f:
        f.write("# Fairness Audit Report\n\n")
        f.write(json.dumps(results, indent=2))
