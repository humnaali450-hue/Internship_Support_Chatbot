import joblib
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess_text


# Load trained model
vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

model = joblib.load(
    "models/chatbot_model.pkl"
)


df = model["data"]
X = model["matrix"]


def chatbot_response(user_question, threshold=0.20):

    if not user_question or user_question.strip() == "":
        return "Please enter a question."


    # Greetings
    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if user_question.lower().strip() in greetings:
        return (
            "Hello! 👋 I'm your Internship Support Assistant. "
            "How can I help you today?"
        )


    # Thank you
    thanks = [
        "thanks",
        "thank you",
        "thanks a lot"
    ]

    if user_question.lower().strip() in thanks:
        return (
            "You're welcome! 😊 "
            "Feel free to ask me anything about your internship."
        )


    # Preprocess question
    processed_question = preprocess_text(
        user_question
    )


    # Convert question into vector
    user_vector = vectorizer.transform(
        [processed_question]
    )


    # Calculate similarity
    similarities = cosine_similarity(
        user_vector,
        X
    )[0]


    # Find best match
    best_index = np.argmax(similarities)

    best_score = similarities[best_index]


    # Return answer
    if best_score >= threshold:

        return df.iloc[best_index]["answer"]


    return (
        "I'm sorry, I don't have enough information "
        "to answer that question. Please contact your "
        "internship supervisor or HR department."
    )