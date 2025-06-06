import gradio as gr
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env file
load_dotenv()

# Placeholder for your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize LangChain OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    max_tokens=150
)

SYSTEM_PROMPT = "You are FitMate, a helpful fitness assistant."

def chat_with_gpt40(user_message, chat_history):
    # Convert chat_history to LangChain message format
    messages = [SystemMessage(content=SYSTEM_PROMPT)]
    for user, ai in chat_history:
        messages.append(HumanMessage(content=user))
        messages.append(AIMessage(content=ai))
    messages.append(HumanMessage(content=user_message))
    try:
        response = llm(messages)
        reply = response.content
    except Exception as e:
        reply = f"Error: {str(e)}"
    chat_history.append((user_message, reply))
    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# FitMate Chatbot\nYour AI Fitness Assistant")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message")
    clear = gr.Button("Clear")

    def clear_chat():
        return [], ""

    msg.submit(chat_with_gpt40, [msg, chatbot], [msg, chatbot])
    clear.click(clear_chat, [], [chatbot, msg])

demo.launch() 