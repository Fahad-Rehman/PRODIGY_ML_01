import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#Load the data
PROCESSED_VAL_PATH = "data/processed/val_processed.csv"
MODEL_PATH = "results/linear_regression_model.pkl"

val_data = pd.read_csv(PROCESSED_VAL_PATH)
X_val = val_data.drop("SalePrice", axis=1)
y_val = val_data["SalePrice"].values

linear_model = joblib.load(MODEL_PATH)

# Predictions
preds = linear_model.predict(X_val)


# Metrics
mse = mean_squared_error(y_val, preds)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_val, preds)
r2 = r2_score(y_val, preds)

with open("results/model_performance.txt", "w") as f:
    f.write(f"MSE: {mse}\n")
    f.write(f"RMSE: {rmse}\n")
    f.write(f"MAE: {mae}\n")
    f.write(f"R2: {r2}\n")

print(f"Saved metrics to model_performance.txt")

# Actual vs Predicted plot
plt.figure(figsize=(8, 8))
plt.scatter(y_val, preds, alpha=0.6)
Min = min(min(y_val), min(preds))
Max = max(max(y_val), max(preds))
plt.plot([Min, Max], [Min, Max], linestyle='--')
plt.xlabel("Actual SalePrice")
plt.ylabel("Predicted SalePrice")
plt.title("Actual vs Predicted")
plt.tight_layout()
plt.savefig("results/plots/actual_vs_predicted.png")
plt.close()


# Residuals plot
residuals = y_val - preds
plt.figure(figsize=(8, 6))
plt.scatter(preds, residuals, alpha=0.6)
plt.axhline(0, linestyle='--')
plt.xlabel("Predicted SalePrice")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residuals vs Predicted")
plt.tight_layout()
plt.savefig("results/plots/residuals_plot.png")
plt.close()


print("Plots saved")