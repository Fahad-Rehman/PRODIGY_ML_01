# House Price Prediction - Linear Regression

## Internship Task 1 - Prodigy Infotech

## Project Overview

This project implements a linear regression model to predict house prices based on three key features: square footage, number of bedrooms, and number of bathrooms. The model is trained on housing data and evaluated using standard regression metrics.

## Project Structure
```text
house-price-prediction/
│
├── data/
│   ├── train.csv
│   ├── test.csv            # optional
│
├── src/
│   ├── data_preprocessing.py   # clean/select 3 features
│   ├── train_model.py          # train Linear Regression
│   └── evaluate_model.py       # metrics & plots
│
├── results/
│   ├── predictions.csv
│   ├── model_performance.txt
│   └── plots/
│       ├── actual_vs_predicted.png
│       └── residuals_plot.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Features Used
+ Square Footage: Above grade (ground) living area (`GrLivArea`)
+ Bedrooms: Number of bedrooms above basement level (`BedroomAbvGr`)
+ Bathrooms: Combination of full and half bathrooms (`FullBath` + `HalfBath`)

## Installation & Setup
1. Clone the Repository
```bash
git clone <repository-url>
cd Task1
```

2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Requirements
The `requirements.txt` file includes:
```text
numpy
pandas
matplotlib
seaborn
scikit-learn
```

## Usage
1. Data Preprocessing
```bash
python src/data_preprocessing.py
```
This script:

+ Loads the training data
+ Selects relevant features (square footage, bedrooms, bathrooms)
+ Handles missing values
+ Splits data into training and validation sets

2. Train the Model
```bash
python src/train_model.py
```
This script:

+ Trains a linear regression model
+ Saves the trained model
+ Generates initial predictions

3. Evaluate the Model
```bash
python src/evaluate_model.py
```
This script:

+ Calculates performance metrics (MSE, RMSE, R²)
+ Generates visualization plots
+ Saves results to the `results/` directory

## Output
After running all scripts, you'll find:

+ Model Performance: `results/model_performance.txt`
+ Predictions: `results/predictions.csv`
+ Visualizations:
    + `results/plots/actual_vs_predicted.png`
    + `results/plots/residuals_plot.png`

## Model Performance Metrics
The model is evaluated using:

+ Mean Squared Error (MSE)
+ Root Mean Squared Error (RMSE)
+ R-squared (R²) Score

## Results Interpretation
+ R² Score: Closer to 1 indicates better fit
+ Residuals Plot: Should show random scatter (no patterns)
+ Actual vs Predicted: Points should align closely to the diagonal line

## Contributing
This project was developed as part of Prodigy Infotech Internship Task 1. For questions or improvements, please follow standard git workflow:
```bash
git checkout -b feature/improvement
git commit -m "Description of changes"
git push origin feature/improvement
```

## License
This project is for educational purposes as part of the Prodigy Infotech internship program.