import pandas

COLUMNS = ["Open time", "Open price", "High price", "Low price", "Close price", "Volume", "Close time", "Quote Volume", 
           "Trades", "Taker buy base", "Taker buy quote"]

class CandleService:
    def display_candle_info(self, data, last_candle):
        cleaned_data = [row[:-1] for row in data]
        displayed_data = pandas.DataFrame(cleaned_data, columns=COLUMNS)
        displayed_data["Open time"] = pandas.to_datetime(displayed_data["Open time"], unit='ms')
        displayed_data["Close time"] = pandas.to_datetime(displayed_data["Close time"], unit='ms')
        if last_candle:
            cleaned_last_data = [[float(last_candle)]]
            displayed_last_data = pandas.DataFrame(cleaned_last_data, columns=["Last price"])
        return displayed_data, displayed_last_data

