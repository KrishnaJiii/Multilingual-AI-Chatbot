import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class MultiLingualchatbot:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found")

        self.client = Groq(api_key=api_key)

    def chat_stream(self, prompt, language="English", history=None):
        """
        Generator that streams response word-by-word
        """

        if history is None:
            history = []

        messages = [
            {
                "role": "system",
                "content": f"You are a helpful assistant. Always reply in {language}."
            }
        ]

        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        # 🔥 STREAMING RESPONSE
        stream = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            stream=True
        )

        full_response = ""

        for chunk in stream:
            if chunk.choices[0].delta.content:
                word = chunk.choices[0].delta.content
                full_response += word
                yield word  # send piece by piece

        return full_response
