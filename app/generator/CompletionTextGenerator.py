import os
import openai
from app.config import settings
from typing import List, Dict
import json


class CompletionTextGenerator:
    initial_messages: List =  [
        {"role": "system", "content": "Your task is to make short product description from this information. Use ecommerce-style text, do not use complex words, be user-friendly, keep description short, do not add any technical information that is not listed in attributes json"},
    ]

    def __init__(self):
        openai.api_key = settings.openai.api_key

    def generate_description(self, title_text: str, attribute_dict: Dict[str, Dict]) -> str:
        messages = self.initial_messages.copy()
        messages.append({"role": "user", "content": f"Product title: {title_text}"})
        messages.append({"role": "user", "content": f"Product attributes in json format: {json.dumps(attribute_dict)}"})
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = chat_completion.choices[0].message.content
        return answer
