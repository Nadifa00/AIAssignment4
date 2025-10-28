# --- Import Libraries ---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.datasets import load_breast_cancer

# --- Load and Preprocess Data ---
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# Map target to priority: 0 (Malignant) -> "High", 1 (Benign) -> "Low"
df['priority'] = df['target'].apply(lambda x: 'High' if x == 0 else 'Low')

# --- Split Data ---
X = df[data.feature_names]
y = df['priority']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Train Model ---
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Evaluate Model ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, pos_label='High') # F1 for "High Priority" class

print("Performance Metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1-Score (High Priority): {f1:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))