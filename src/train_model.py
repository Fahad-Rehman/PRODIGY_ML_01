import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#Load the processed train data
PROCESSED_TRAIN_PATH = "data/processed/train_processed.csv"
PROCESSED_VAL_PATH = "data/processed/val_processed.csv"

train_data = pd.read_csv(PROCESSED_TRAIN_PATH)
val_data = pd.read_csv(PROCESSED_VAL_PATH)

X_train = train_data.drop("SalePrice", axis=1)
y_train = train_data["SalePrice"]


X_val = val_data.drop("SalePrice", axis=1)
y_val = val_data["SalePrice"]

# Fit model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

#Save the model
model_path = "results/linear_regression_model.pkl"
joblib.dump(linear_model, model_path)
print(f"Model saved to {model_path}")

#save predictions on validation set for quick inspection
val_preds = linear_model.predict(X_val)
val_out = pd.DataFrame({"Actual": y_val, "Predicted": val_preds})
val_out.to_csv("results/val_predictions.csv", index=False)
print(f"Validation predictions saved")
