import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Diabetes.csv")


print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())  


import numpy as np


cols_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in cols_with_zero:
    df[col] = df[col].replace(0, np.nan)   
    df[col].fillna(df[col].median(), inplace=True)  


print(df["Outcome"].value_counts())
df["Outcome"] = df["Outcome"].astype("category")





sns.countplot(x="Outcome", data=df)
plt.title("Diabetes Outcome Distribution")
plt.show()


df.hist(figsize=(12,10), bins=20)
plt.suptitle("Feature Distributions")
plt.show()


for col in df.columns[:-1]:
    plt.figure(figsize=(6,4))
    sns.boxplot(x="Outcome", y=col, data=df)
    plt.title(f"{col} vs Outcome")
    plt.show()


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df, hue="Outcome")
plt.show()