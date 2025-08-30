#Regression
"""
1. Predict the price of the car based on its features. Use appropriate evaluation metrics. Dataset : cars.csv 
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("cars.csv")
print(df.head())


df = pd.get_dummies(df, drop_first=True)


X = df.drop("Price", axis=1)   
y = df["Price"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print("Car Price Prediction")
print("MSE:", mse, "RMSE:", rmse, "R²:", r2)





"""
2. Create a model that can predict the profit based on its features . Use appropriate evaluation metrics.The Dataset can be downloaded from kaggle.com Dataset : 50_startups.csv 
"""


df = pd.read_csv("50_Startups.csv")
print(df.head())


df = pd.get_dummies(df, drop_first=True)


X = df.drop("Profit", axis=1)
y = df["Profit"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print("Startup Profit Prediction")
print("MSE:", mse, "RMSE:", rmse, "R²:", r2)



"""
3. Create a model that can predict the profit based on its features . Use appropriate evaluation metrics.The Dataset can be downloaded from kaggle.com Dataset : Salary_Data
"""


df = pd.read_csv("Salary_Data.csv")
print(df.head())


X = df[["YearsExperience"]]   
y = df["Salary"]              


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print("Salary Prediction")
print("MSE:", mse, "RMSE:", rmse, "R²:", r2)








#Classification
"""
1.Create a model that can predict the disease of cancer based on features given in the dataset. Use appropriate evaluation metrics. Dataset : cancer.csv 
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv("cancer.csv")
print(df.head())


df.drop(["id"], axis=1, inplace=True, errors="ignore")


X = df.drop("diagnosis", axis=1)   
y = df["diagnosis"].map({"M":1, "B":0})   


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Cancer Prediction Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


"""
2. Create a model that can predict that the customer has purchased item or not based on features given in the dataset. Use appropriate evaluation metrics. Dataset : Social_Ntetwork_Ads.csv
"""


df = pd.read_csv("Social_Network_Ads.csv")
print(df.head())


df.drop(["User ID"], axis=1, inplace=True, errors="ignore")


df = pd.get_dummies(df, drop_first=True)


X = df.drop("Purchased", axis=1)
y = df["Purchased"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Customer Purchase Prediction Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
