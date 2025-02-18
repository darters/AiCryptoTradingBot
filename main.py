import os
import re
from datetime import datetime
from dotenv import load_dotenv
from service.ai_service import AiService
from service.candle_service import CandleService
from service.binance_service import BinanceService

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TESTNET_API = os.getenv('BINANCE_TESTNET_API')
SECRET_API = os.getenv('BINANCE_SECRET_API')

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    ai_service = AiService(OPENAI_API_KEY)
    candle_service = CandleService('BTCUSDT', '1h', '2025-02-18 08:00:00', current_time)
    binance_service = BinanceService(TESTNET_API, SECRET_API)

    binance_service.getBalance()

    # info_candle = candle_service.fetch_candle_info()
    # candles = candle_service.display_candle_info(info_candle)
    # print(candles)
    
    # response = ai_service.send_request_to_chgpt(f"""{candles} Based on this market data, generate a trade signal with the following details:
    #     - Entry Price: Suggested price to enter the trade.
    #     - Stop-Loss Price: Suggested price to minimize risk.
    #     - Take-Profit Price: Suggested price to take profit.
    #     Provide all prices as whole numbers without decimals
    #     Respond only in the following structured format:
    #     Entry Price:
    #     Stop-Loss Price: 
    #     Take-Profit Price: 
    #     Estimated Entry Time: (time in hours/days)
    #     """)
    # print(response)
    # entry_price = re.search(r"Entry Price: ([\d.]+)", response).group(1)
    # take_profit = re.search(r"Take-Profit Price: ([\d.]+)", response).group(1)
    # stop_loss = re.search(r"Stop-Loss Price: ([\d.]+)", response).group(1)


if __name__ == "__main__":
    main()

