import os
from service.ai_service import AiService
from service.candle_service import CandleService
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def main():
    ai_service = AiService(OPENAI_API_KEY)
    candle_service = CandleService('BTC', '1d', '2025-02-05 01:00:00', '2025-02-11 01:00:00')
    info_candle = candle_service.fetch_candle_info()
    candles = candle_service.display_candle_info(info_candle)
    
    print(candles)
    print(ai_service.send_request_to_chgpt(f"{candles} Identify the market type: bullish, bearish, high volatility, low volatility, or other. Respond with only one of these categories"))




if __name__ == "__main__":
    main()

