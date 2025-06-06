# FitMate

A simple fitness chatbot app using Gradio and OpenAI GPT-4o mini.

## How to Run

1. Create a virtual environment using uv:
   ```bash
   uv venv venv
   ```
2. Activate the virtual environment (Windows PowerShell):
   ```bash
   venv\Scripts\Activate
   ```
3. Install dependencies using uv:
   ```bash
   uv pip install -r requirements.txt
   ```
4. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
5. Start the app:
   ```bash
   python app.py
   ```

The app will launch in your browser.

## Deployment

This app is ready for deployment on Hugging Face Spaces (Gradio interface).
