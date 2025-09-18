import pandas as pd
from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference

def compute_fairness(y_true, y_pred, sensitive_features):
    mf = MetricFrame(
        metrics={"selection_rate": selection_rate},
        y_true=y_true,
        y_pred=y_pred,
        sensitive_features=sensitive_features
    )
    return {
        "selection_rate": mf.by_group.to_dict(),
        "demographic_parity_diff": demographic_parity_difference(y_true, y_pred, sensitive_features=sensitive_features)
    }
