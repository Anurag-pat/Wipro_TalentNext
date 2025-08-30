"""
1.Use Case: Sales Prediction

Create a model which will predict the sales based on campaigning expenses.

Dataset: Advertising.csv

The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following task.

Load the data in the DataFrame.

Perform Data Preprocessing

Handle Categorical Data

Perform Exploratory Data Analysis

Build the model using Multiple Linear Regression

Use the appropriate evaluation metrics
"""
import pandas as pd


df = pd.read_csv("Advertising.csv")


print(df.head())
print(df.info())
print(df.describe())


print(df.isnull().sum())
df.drop_duplicates(inplace=True)


import seaborn as sns
import matplotlib.pyplot as plt


sns.pairplot(df)
plt.show()


sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.scatterplot(x="TV", y="Sales", data=df)
plt.show()
sns.scatterplot(x="Radio", y="Sales", data=df)
plt.show()
sns.scatterplot(x="Newspaper", y="Sales", data=df)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R² Score:", r2)




"""
2. Use Case: Diabetes Prediction

Consider the PIMA Indians diabetes dataset. Create a Model for diabetes prediction based on the features mentioned in the dataset.

Dataset: PIMA Indians diabetes dataset.

The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following tasks.

Load the data in the DataFrame.

Perform Data Preprocessing

Perform Exploratory Data Analysis

Build the model using Logistic Regression and K-Nearest Neighbour

Use the appropriate evaluation metrics
"""