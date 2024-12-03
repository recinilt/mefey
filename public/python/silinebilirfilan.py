import pandas as pd

# Verilen liste
data = [
    ["BTCUSDT", 2.1, 2.2, 2.3, 2.2, 2.2, 2.2, 2.4, 2.5, 2.4],
    ["LTCUSDT", 2.1, 2.2, 2.3, 2.2, 2.2, 2.2, 2.4, 2.5, 2.4],
    ["XRPUSDT", 2.1, 2.2, 2.3, 2.2, 2.2, 2.2, 2.4, 2.5, 2.4],
    ["UNIUSDT", 2.9, 2.2, 2.3, 2.4, 2.2, 2.2, 2.1, 2.2, 2.0],
]

# EMA hesaplama fonksiyonu
def calculate_ema(values, period):
    return pd.Series(values).ewm(span=period, adjust=False).mean().tolist()

# EMA'yı yukarı kıranları bulma
def find_ema_cross(data):
    crossing_pairs = []
    for row in data:
        coin = row[0]
        prices = row[1:]
        ema2 = calculate_ema(prices, 2)
        ema3 = calculate_ema(prices, 3)
        
        # EMA'nın yukarı kırıldığı anları kontrol et
        for i in range(1, len(prices)):
            if ema2[i] > ema3[i] and ema2[i-1] <= ema3[i-1]:
                crossing_pairs.append(coin)
                break  # Bir kez yukarı kırılması yeterli
    return crossing_pairs

# Yukarı kıranları bul
result = find_ema_cross(data)
print("EMA'yı yukarı kıranlar:", result)
