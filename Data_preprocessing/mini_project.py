"""
Use-Case: House Price Prediction

Dataset: melb_data.csv

The dataset can be downloaded melb_data.csv | Kaggle

Perform the following tasks:

1. Load the data in dataframe (Pandas)

2. Handle inappropriate data

3. Handle the missing data

4. Handle the categorical data
"""



import pandas as pd


df = pd.read_csv("melb_data.csv")


print(df.head())


print(df.info())

df.drop_duplicates(inplace=True)


df.drop(['Address', 'SellerG', 'Date'], axis=1, inplace=True)



print(df.isnull().sum())


df.dropna(axis=1, thresh=0.5*len(df), inplace=True)


num_cols = df.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)


cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)


# One-Hot Encoding for categorical features
df = pd.get_dummies(df, drop_first=True)

print(df.head())
