from openai import OpenAI

class AiService:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)

    def send_request_to_chgpt(self, question):
        try:
            completion = self.client.chat.completions.create(
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
        except Exception as e:
            print(f'📢 Error while sending request to AI: {e}')
            return None

    def get_orders(self, candles, last_candle):
        response = self.send_request_to_chgpt(f"""{candles} {last_candle} 
        Based on this market data, generate a trade signal with the following details:
        - Entry Price: Suggested price to enter the trade.
        - Stop-Loss Price: Suggested price to minimize risk.
        - Take-Profit Price: Suggested price to take profit.
        Respond only in the following structured format:
        Entry Price:
        Take-Profit Price: 
        Stop-Loss Price: 
        Estimated Entry Time: (time in hours/days)
        """)
        return response
    

