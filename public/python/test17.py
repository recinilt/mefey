import time
from binance.client import Client
from binance.enums import *

api_key = 'PhtkBtWNspyWWUwjQX9rDekZPxVAN6blRvnBUzQsrhlrO4xbvzWvrJCtXircFfPU'
api_secret = 'iAJFQwVXHRVXvA2ffjxb5dxd5nlHEFZjv2yP12FzqUSXxic7mz02rILS54YWOEOH'

client = Client(api_key, api_secret)

symbol = 'HBARUSDT'
leverage = 5
quantity = 20  # 20 HBAR harcanacak şekilde
initial_price = float(client.get_symbol_ticker(symbol=symbol)['price'])
lowest_price = initial_price
highest_price = initial_price

# Kaldıraç ayarla
client.futures_change_leverage(symbol=symbol, leverage=leverage)

def get_price_change_percentage(initial, current):
    return ((current - initial) / initial) * 100

def close_position():
    # Mevcut pozisyonu kapat
    positions = client.futures_position_information(symbol=symbol)
    for position in positions:
        if float(position['positionAmt']) != 0:
            side = SIDE_SELL if float(position['positionAmt']) > 0 else SIDE_BUY
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=abs(float(position['positionAmt']))
            )
            print(f"Pozisyon kapatıldı: {order}")
            time.sleep(10)  # 10 saniye bekle

while True:
    current_price = float(client.get_symbol_ticker(symbol=symbol)['price'])
    print("1 dk bekle")
    # En düşük ve en yüksek fiyatları güncelle
    if current_price < lowest_price:
        lowest_price = current_price
    if current_price > highest_price:
        highest_price = current_price
    
    # Long pozisyon açma koşulu
    if get_price_change_percentage(lowest_price, current_price) >= 3:
        close_position()
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=quantity * leverage  # 5x kaldıraçlı 100 HBAR
        )
        print(f"Long pozisyon açıldı: {order}")
        initial_price = current_price
        lowest_price = current_price  # Yeni başlangıç fiyatı olarak güncelle
    
    # Short pozisyon açma koşulu
    elif get_price_change_percentage(current_price, highest_price) >= 3:
        close_position()
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity * leverage  # 5x kaldıraçlı 100 HBAR
        )
        print(f"Short pozisyon açıldı: {order}")
        initial_price = current_price
        highest_price = current_price  # Yeni başlangıç fiyatı olarak güncelle
    
    time.sleep(60)  # 1 dakika bekle ve tekrar kontrol et