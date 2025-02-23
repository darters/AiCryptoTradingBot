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
    symbol, interval, start_time, end_time, quantity = get_user_input()
    ai_service, binance_service, candle_service, order_service = initialize_services()

    candles, last_candle = binance_service.fetch_candle_info(symbol, interval, start_time, end_time)
    candels_info, last_candle_info = candle_service.display_candle_info(candles, last_candle)
    print(candels_info, f"\n {last_candle_info}")
    
    ai_response = ai_service.get_orders(candles, last_candle)
    print(ai_response)
    entry_price, tp, sl = order_service.parse_orders(ai_response)
    created_orders = binance_service.createOrders(symbol, entry_price, tp, sl, quantity)
    print(order_service.display_formatted_orders(*created_orders))

if __name__ == "__main__":
    main()


