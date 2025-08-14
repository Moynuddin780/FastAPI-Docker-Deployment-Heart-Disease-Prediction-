import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load dataset
df = pd.read_csv("E:\Jupyter Programs\heart.csv")  # from Kaggle dataset

# 2. Features & target
X = df.drop("target", axis=1)
y = df["target"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Save model
joblib.dump(model, "model/heart_model.joblib")
print("Model saved to model/heart_model.joblib")
