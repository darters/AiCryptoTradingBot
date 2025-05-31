import os
from dotenv import load_dotenv
from api_services.ai_service import AiService
from api_services.binance_service import BinanceService
from services.candle_service import CandleService
from services.order_service import OrderService
from utils.input_handler import get_user_input

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TESTNET_API = os.getenv('BINANCE_TESTNET_API')
SECRET_API = os.getenv('BINANCE_SECRET_API')

def initialize_services():
    ai_service = AiService(OPENAI_API_KEY)
    binance_service = BinanceService(TESTNET_API, SECRET_API)
    candle_service = CandleService()
    order_service = OrderService()  
    return ai_service, binance_service, candle_service, order_service

def main():
    # BTCUSDT, 1h, 2025-02-22 19:00:00, current_time, 0.01
    # symbol, interval, start_time, end_time, quantity = get_user_input()
    ai_service, binance_service, candle_service, order_service = initialize_services()
    symbol = "BTCUSDT"
    interval = "1h"
    start_time = "2024-02-26 12:00:00"
    end_time = "2024-02-26 20:00:00"


if __name__ == "__main__":
    main()

