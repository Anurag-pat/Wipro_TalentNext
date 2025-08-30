"""
Use Case: Rating Prediction

Create a model that will predict the rating based on the feedback of the customer.

Feature: Text

Label: Stars

Dataset: yelp.csv

The dataset can be downloaded from https://www.kaggle.com/datasets 
"""

import pandas as pd

df = pd.read_csv("yelp.csv")
print(df.head())
print(df.info())
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text) 
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

df["clean_text"] = df["text"].apply(clean_text)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=5000)  
X = tfidf.fit_transform(df["clean_text"])

y = df["stars"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))