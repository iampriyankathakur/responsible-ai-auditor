import pandas as pd
from fairness_metrics import compute_fairness

def run_audit(data_path, preds_path, sensitive_col="gender"):
    df = pd.read_csv(data_path)
    preds = pd.read_csv(preds_path)
    
    fairness_results = compute_fairness(
        df["loan_approved"],
        preds["loan_approved_pred"],
        df[sensitive_col]
    )
    return fairness_results
