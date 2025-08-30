import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


"""
1. Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be downloaded from https://www.kaggle.com/datasets  
"""
mall = pd.read_csv("Mall_Customers.csv")

print(mall.head())
print(mall.info())
print(mall.describe())


sns.countplot(x="Gender", data=mall)
plt.title("Gender Distribution")
plt.show()


sns.histplot(mall["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()


sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Gender", data=mall)
plt.title("Income vs Spending Score")
plt.show()


sns.heatmap(mall.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()



"""
2. Perform Exploratory Data Analysis for the dataset salary_data. The dataset can be downloaded from https://www.kaggle.com/datasets
"""
salary = pd.read_csv("Salary_Data.csv")


print(salary.head())
print(salary.info())
print(salary.describe())


sns.histplot(salary["YearsExperience"], bins=10, kde=True)
plt.title("Years of Experience Distribution")
plt.show()


sns.histplot(salary["Salary"], bins=10, kde=True)
plt.title("Salary Distribution")
plt.show()


sns.scatterplot(x="YearsExperience", y="Salary", data=salary)
plt.title("Experience vs Salary")
plt.show()


print(salary.corr())
sns.heatmap(salary.corr(), annot=True, cmap="viridis")
plt.show()




"""
3.Perform Exploratory Data Analysis for the dataset Social Network Ads. The dataset can be downloaded from https://www.kaggle.com/datasets
"""
ads = pd.read_csv("Social_Network_Ads.csv")


print(ads.head())
print(ads.info())
print(ads.describe())


sns.countplot(x="Gender", data=ads)
plt.title("Gender Distribution")
plt.show()


sns.histplot(ads["Age"], bins=15, kde=True)
plt.title("Age Distribution")
plt.show()


sns.histplot(ads["EstimatedSalary"], bins=15, kde=True)
plt.title("Salary Distribution")
plt.show()


sns.countplot(x="Purchased", hue="Gender", data=ads)
plt.title("Purchase Decision by Gender")
plt.show()


sns.scatterplot(x="Age", y="EstimatedSalary", hue="Purchased", data=ads)
plt.title("Age vs Salary (Purchased Highlighted)")
plt.show()


sns.heatmap(ads.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
