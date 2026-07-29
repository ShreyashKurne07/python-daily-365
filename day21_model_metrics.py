def evaluate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return round(precision, 3), round(recall, 3), round(f1, 3)

tp, fp, fn = 85, 12, 8
prec, rec, f1 = evaluate_metrics(tp, fp, fn)

print("--- Model Evaluation Summary ---")
print(f"Precision: {prec}")
print(f"Recall:    {rec}")
print(f"F1-Score:  {f1}")
