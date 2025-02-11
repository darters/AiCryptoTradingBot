from openai import OpenAI

class AiService:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def send_request_to_chgpt(self, question):
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant, with short answers"},
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return completion.choices[0].message.content

