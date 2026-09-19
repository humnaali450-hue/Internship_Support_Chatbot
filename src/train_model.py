import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

from preprocessing import preprocess_text


# Create models directory
os.makedirs("models", exist_ok=True)


# Load dataset
df = pd.read_csv("data/internship_faq.csv")


# Preprocess questions
df["processed_question"] = df["question"].apply(
    preprocess_text
)


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=5000
)


# Train TF-IDF
X = vectorizer.fit_transform(
    df["processed_question"]
)


# Save vectorizer
joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)


# Save chatbot model data
joblib.dump(
    {
        "data": df,
        "matrix": X
    },
    "models/chatbot_model.pkl"
)


print("Model trained successfully!")
print(f"Total FAQs: {len(df)}")