import gradio as gr

from chatbot import chatbot_response


def respond(message, history):

    if not message:
        return "", history

    answer = chatbot_response(message)

    history.append((message, answer))

    return "", history


with gr.Blocks(
    title="Internship Support Assistant"
) as demo:

    gr.Markdown(
        """
        # 🎓 Internship Support Assistant

        Your AI-powered assistant for internship questions,
        guidance and support.
        """
    )

    chatbot = gr.Chatbot(
        label="💬 Conversation",
        height=500
    )

    message = gr.Textbox(
        placeholder="Ask your internship question...",
        label="Your Question"
    )

    send = gr.Button(
        "Send"
    )

    clear = gr.Button(
        "Clear Chat"
    )

    send.click(
        respond,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    message.submit(
        respond,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    clear.click(
        lambda: [],
        outputs=chatbot
    )


demo.launch()