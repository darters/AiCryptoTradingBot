class IndicatorService:
    @staticmethod
    def determine_trend(slope):
        if abs(slope) < 0.1:
            return "Sideways"
        if slope > 0:
            return "Uptrend"
        else: 
            return "Downtrend"

    @staticmethod
    def find_crossovers(ema12, ema21):
        crossovers = []
        for i in range(1, len(ema12)):
            if ema12[i-1] < ema21[i-1] and ema12[i] > ema21[i]:
                print(f"BULLISH crossover at index {i}: EMA12 {ema12[i]} crosses above EMA21 {ema21[i]}")
                crossovers.append((i, "Bullish"))
            elif ema12[i-1] > ema21[i-1] and ema12[i] < ema21[i]:
                print(f"BEARISH crossover at index {i}: EMA12 {ema12[i]} crosses below EMA21 {ema21[i]}")
                crossovers.append((i, "Bearish"))
        return crossovers
    
    @staticmethod
    def calculate_ema(data, period):
        alpha = float(2 / (period + 1))
        ema_values = [data[0]]    

        for i in range(1, len(data)):
            ema = alpha * data[i] + (1-alpha) * ema_values[i-1]
            ema_values.append(ema)
        return ema_values
    
    @staticmethod
    def linear_regression(prices):
        n = len(prices)
        x = list(range(1, n + 1))
        x_mean = sum(x) / n
        y_mean = sum(prices) / n

        numerator = sum((x[i] - x_mean) * (prices[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean)**2 for i in range(n))
        
        b = numerator / denominator
        a = y_mean - b * x_mean
        y_next = a + b * (len(prices) + 1)
        
        return round(a, 2), round(b, 2), round(y_next, 2)

