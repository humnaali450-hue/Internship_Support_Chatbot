from src.chatbot import chatbot_response


def test_report_question():

    response = chatbot_response(
        "How can I submit my internship report?"
    )

    assert response is not None


def test_supervisor_question():

    response = chatbot_response(
        "Who is my internship supervisor?"
    )

    assert response is not None


def test_unknown_question():

    response = chatbot_response(
        "What is the weather today?"
    )

    assert response is not None