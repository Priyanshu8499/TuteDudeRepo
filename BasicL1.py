
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import(confusion_matrix,
                            precision_score,
                            recall_score,
                            roc_curve,
                            roc_auc_score)

# binary classification dataset
X, y = make_classification(
    n_samples=10000,
    n_features=10,
    n_informative=5,
    n_redundant=0,
    n_classes=2,
    flip_y=0.2,
    random_state=42,

)

# 2. train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3.LogisticRegression

log_model = LogisticRegression()
log_model.fit(X_train, y_train)


y_prob_log = log_model.predict_proba(X_test)[:, 1]

# print(y_prob_log)

# 4. threshold

threshold = 0.5
y_pred = (y_prob_log  >= threshold).astype(int)


# 5. confusion metrics

cm  = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = cm.ravel()

print("Confusion matrix")
print(cm)

# 6. Performance Metrics
TPR = TP / (TP + FN)   # Sensitivity / Recall
FPR = FP / (FP + TN)
TNR = TN / (TN + FP)   # Specificity
FNR = FN / (FN + TP)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\nPerformance Metrics:")
print(f"TPR (Sensitivity/Recall): {TPR:.4f}")
print(f"FPR: {FPR:.4f}")
print(f"TNR (Specificity): {TNR:.4f}")
print(f"FNR: {FNR:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")

# 8. ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob_log)
auc_score = roc_auc_score(y_test, y_prob_log)

#  9. Plot ROC Curve
plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc_score:.4f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Logistic Regression")
plt.legend()
plt.grid()
plt.show()