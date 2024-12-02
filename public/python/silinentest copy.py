import ccxt
import pandas as pd
import ta
from binance.client import Client
from binance.enums import *
import time

# Binance borsasına bağlan
exchange = ccxt.binance()
binance_api="PhtkBtWNspyWWUwjQX9rDekZPxVAN6blRvnBUzQsrhlrO4xbvzWvrJCtXircFfPU"
binance_secret="iAJFQwVXHRVXvA2ffjxb5dxd5nlHEFZjv2yP12FzqUSXxic7mz02rILS54YWOEOH"
binanceclient = Client(binance_api, binance_secret)


# USDT çiftlerini al
markets = exchange.load_markets()
usdt_pairs = [symbol for symbol in markets if symbol.endswith('USDT') and 'future' in markets[symbol]['info']]
print(usdt_pairs)

def get_ohlcv(symbol):
    # 5 dakikalık periodun 25 geriye dönük bilgilerini al
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='5m', limit=25)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def calculate_ema(df, short_period=14, long_period=25):
    df['ema_short'] = ta.trend.ema_indicator(df['close'], window=short_period)
    df['ema_long'] = ta.trend.ema_indicator(df['close'], window=long_period)
    return df

def find_crossing_coins(usdt_pairs):
    crossing_coins = []
    for pair in usdt_pairs:
        df = get_ohlcv(pair)
        df = calculate_ema(df)
        if df['ema_short'].iloc[-1] > df['ema_long'].iloc[-1] and df['ema_short'].iloc[-2] <= df['ema_long'].iloc[-2]:
            crossing_coins.append(pair)
    return crossing_coins

def get_symbol_precision(symbol):
    try:
        info = binanceclient.futures_exchange_info()
        for item in info['symbols']:
            if item['symbol'] == symbol.upper():
                return int(item['quantityPrecision'])
    except Exception as e:
        print(f"Error: {e}")
        return None

mylonglist=[]
def buy_position(symbol, leverage, amount,liste):
    #if is_above_last_period_average(io1d[len(io1d)-1],io1d,smaperiod):
    try:
        binanceclient.futures_change_leverage(symbol=symbol, leverage=leverage)
        #binanceclient.futures_change_margin_type(symbol=symbol, marginType=ISOLATED)
        precision = get_symbol_precision(symbol)
        if precision is None:
            print("Precision could not be determined.")
            return

        quantity = round(amount * leverage / float(binanceclient.get_symbol_ticker(symbol=symbol.upper())['price']), precision)
        
        order = binanceclient.futures_create_order(
            symbol=symbol.upper(),
            side='BUY',
            type='MARKET',
            quantity=quantity,
            leverage=leverage
        )
        print(order)
        #hesapla(symbol, "buy",1)
        #eklesil(symbol,liste,"ekle")
        mylonglist.append(symbol)
        time.sleep(5)  # 5 saniye bekle
    except Exception as e:
        print(f"Error: {e}")


# Kesişim noktası halindeki coinleri bul

while True:
    # USDT çiftlerini al
    markets = exchange.load_markets()
    usdt_pairs = [symbol for symbol in markets if symbol.endswith('USDT') and 'future' in markets[symbol]['info']]
    print(usdt_pairs)
    crossing_coins = find_crossing_coins(usdt_pairs)
    print(crossing_coins)
    if crossing_coins:
        for c in crossing_coins:
            buy_position(c,7,2,mylonglist)
    print(mylonglist)
    time.sleep(300)
