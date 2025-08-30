"""
1. Perform Text Preprocessing on SMSSpamCollection Dataset. The dataset can be downloaded from  https://www.kaggle.com/datasets
"""

import pandas as pd

df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
print(df.head())

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)   
    return text

df["clean_message"] = df["message"].apply(clean_text)

from nltk.tokenize import word_tokenize
import nltk
nltk.download("punkt")

df["tokens"] = df["clean_message"].apply(word_tokenize)

from nltk.corpus import stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

df["tokens"] = df["tokens"].apply(lambda x: [word for word in x if word not in stop_words])


from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
df["tokens"] = df["tokens"].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

df["final_text"] = df["tokens"].apply(lambda x: " ".join(x))