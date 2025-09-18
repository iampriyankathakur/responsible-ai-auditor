import shap
import matplotlib.pyplot as plt

def explain_model(model, X, output_path="reports/shap_summary.png"):
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig(output_path)
    return output_path
