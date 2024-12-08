# utils/summarizer.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

def generate_summary(text):
    """
    Generates a summary for the financial report using OpenAI GPT-3.

    Args:
        text (str): Input text.

    Returns:
        str: Generated summary.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following financial report:\n\n{text}",
        max_tokens=200,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary
