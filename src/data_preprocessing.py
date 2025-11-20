import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

train_path = "data/train.csv"
test_path = "data/test.csv"

#load train data
train_data = pd.read_csv(train_path)


#selecting our features
data = train_data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath', 'SalePrice']].copy()
data['TotalBath'] = data['FullBath'] + (0.5 * data['HalfBath'])

#Dropping fullBath and HalfBath
data.drop(['FullBath', 'HalfBath'], axis=1, inplace=True)

#checking for missing values
Check_null = data.isnull().sum()
print(f'Null values in train data: \n{Check_null}')

# Split into train/validation
train_df, val_df = train_test_split(data, test_size=0.2, random_state=42)
    
#saving the data into csv for training
train_df.to_csv("data/processed/train_processed.csv", index=False)
val_df.to_csv("data/processed/val_processed.csv", index=False)
print(f"Saved processed train data and validation data")

#Working on test data
test_data = pd.read_csv(test_path)

#selecting our features
test = test_data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath']].copy()

#Dropping fullBath and HalfBath
test['TotalBath'] = test['FullBath'] + (0.5 * test['HalfBath'])
test.drop(['FullBath', 'HalfBath'], axis=1, inplace=True)

#checking for missing values
test_null = test.isnull().sum()
print(f'Null values in Test: \n{test_null}')

#saving the test data into csv for evaluation
test.to_csv("data/processed/test_processed.csv", index=False)
print(f"Saved processed test")