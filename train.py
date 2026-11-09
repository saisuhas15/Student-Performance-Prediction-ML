import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

import joblib

# Step 1: Download dataset
data = fetch_ucirepo(id=320)

X = data.data.features
y = data.data.targets

# Step 2: Add G1 and G2 to features if they are in targets
if "G1" not in X.columns:
    X["G1"] = y["G1"]

if "G2" not in X.columns:
    X["G2"] = y["G2"]

# Step 3: Select features
features = [
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]

X = X[features]

# Final target
y = y["G3"]

print("Dataset loaded successfully!")
print(X.head())

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 5: Train model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel training completed!")

# Step 6: Evaluate model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(
    mean_squared_error(y_test, predictions)
)

r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

# Step 7: Save model
joblib.dump(model, "student_model.joblib")

print("\nModel saved successfully!")