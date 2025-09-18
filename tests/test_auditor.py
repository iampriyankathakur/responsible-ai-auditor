from src.auditor import run_audit

def test_run_audit():
    results = run_audit("data/sample_dataset.csv", "data/sample_predictions.csv")
    assert "selection_rate" in results
