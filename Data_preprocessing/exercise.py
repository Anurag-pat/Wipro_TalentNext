"""
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset can be downloaded from 
https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download
"""

import pandas as pd
import numpy as np


df = pd.read_csv("melb_data.csv")


print(df.shape)
print(df.info())
print(df.describe().T)  


df.drop_duplicates(inplace=True)


df.drop(['Address', 'SellerG', 'Date'], axis=1, inplace=True)


num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]



print(df.isnull().sum())


for col in num_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)


cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)


df = pd.get_dummies(df, drop_first=True)


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_cols = num_cols.drop('Price')  
df[scaled_cols] = scaler.fit_transform(df[scaled_cols])


import seaborn as sns
import matplotlib.pyplot as plt

corr = df.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr, cmap="coolwarm", center=0)
plt.show()
