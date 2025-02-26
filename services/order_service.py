import re
import json

class OrderService:
    def parse_orders(self, ai_response):
        try:
            entry_price = re.search(r"Entry Price: ([\d.]+)", ai_response).group(1)
            take_profit = re.search(r"Take-Profit Price: ([\d.]+)", ai_response).group(1)
            stop_loss = re.search(r"Stop-Loss Price: ([\d.]+)", ai_response).group(1)
            return entry_price, take_profit, stop_loss
        except AttributeError:
            print('📢 Error parsing AI response:', ai_response)
            exit(1)

    # show only important fields to the user
    def display_formatted_orders(self, order, tp_order, sl_order):
        displayed_order = self.format_order(order)
        displayed_tp = self.format_order(tp_order)
        displayed_sl = self.format_order(sl_order)

        displayed_orders = {
            "Order": displayed_order,
            "Take Profit": displayed_tp,
            "Stop Loss": displayed_sl
        }
        return json.dumps(displayed_orders, indent=4)
    
    @staticmethod
    def format_order(order):
        return {
            "orderId": order['orderId'],
            "side": order['side'],
            "status": order['status'],
            "symbol": order['symbol'],
            "price": order[(OrderService.get_price_key(order['price']))],
            "origQty": order['origQty']
        }
         
    @staticmethod
    def get_price_key(price):
        if (price == '0.00'):
            return 'stopPrice'
        return 'price'        
        
