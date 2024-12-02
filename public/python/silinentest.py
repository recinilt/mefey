from telethon import TelegramClient, events
from binance.client import Client
import asyncio
import re
import random
import time
from binance.enums import *
import requests
import json

# API ayarları
telegram_api_id = '21560699'
telegram_api_hash = '5737f22f317a7646f9be624a507984c6'
phone_number = '+905056279048'
target_user = 'tradermikabot'  # Hedef kullanıcının kullanıcı adı
alert_user = 'reccirik_bot'  # Bildirim gönderilecek kullanıcı adı
binance_api="PhtkBtWNspyWWUwjQX9rDekZPxVAN6blRvnBUzQsrhlrO4xbvzWvrJCtXircFfPU"
binance_secret="iAJFQwVXHRVXvA2ffjxb5dxd5nlHEFZjv2yP12FzqUSXxic7mz02rILS54YWOEOH"
binance_api_reccirik2="nKdNVSLZZo4hQnEI1rg7xU1cxZnPWHN4OePu8Yzc3wH3TptaLxBxwhBjUIjrFrAD"
binance_secret_reccirik2="WJSYPws6VnoJkMIXKqgu1CVSha9Io6rT7g8YEiNKbkG3dzdBF7vwZ6fWkZwvlH5S"


################################################## Değişkeler:
#binance future listesi
binanceclient = Client(binance_api, binance_secret)
exchange_info = binanceclient.futures_exchange_info()
symbols = exchange_info['symbols']
mysymbols3=[]
for s in symbols:
    mysymbols3.append(s["symbol"]),
# Telegram Client'ı oluşturun
telegram_client = TelegramClient('session_name', telegram_api_id, telegram_api_hash)
#patterler
pattern = r'\b\w+usdt\b(?:\s+\S+){1}\s+(\S+)'
pattern2 = re.compile(r'(\w+USDT)\s+\S+\s+(\S+)\s+(?:\S+\s+){7}(\S+)')
patternSDV = r"✅✅(\w+)"
patternSDVtek = r"✅ (\w+)"
patternSDVasagicift = r"🔻🔻(\w+)"
patternSDVasagitek = r"🔻 (\w+)"
patternKA = r'\b(\w+)\s+TS:'
#Global değişkenler
mycost=1
myleverage=11
komutlar=["io","io","io","io","io","io","io","io","io","io","io","io","io","io","io","io","io","iof","ssr","marketanaliz","ka","ci s d 5m","acc","grio","dayhigh","p btc","ap","io","sdv"]
kactanbuyuk=17
mysent49=["sdv","marketanaliz","io","ci i d 5m","ka","iof"]
mysent4849=["nls io xxx++","nls io xxxx+","nls io xx+++","nls io x++++","nls io x+++", "p btc","p btc","p btc","p btc","p btc","p btc","p btc","p btc"]
mysent48=["sdv","io","ci i d 5m","iof"]
#mytextio = ["15m=> %57,2 🔼 1h=> %51,9 🔼 4h=> %52,2 🔼 12h=> %48,5 🔻 1d=> %48,9 🔻 En çok nakit girişi olanlar.(Sonunda 🔼 olanlarda nakit girişi daha sağlıklıdır) Nakitin nereye aktığını gösterir. (Nakit Göçü Raporu) BTC Nakit: %18,8 15m: %68 🔼🔼🔼🔻🔻 XLM Nakit: %11,3 15m: %58 🔼🔼🔼🔼🔼 SOL Nakit: %5,7 15m: %68 🔼🔼🔼🔻🔻 ETH Nakit: %5,4 15m: %59 🔼🔻🔻🔻🔻 DOGE Nakit: %4,6 15m: %45 🔻🔼🔼🔻🔻 XRP Nakit: %4,4 15m: %54 🔼🔼🔼🔻🔻 ADA Nakit: %2,3 15m: %56 🔼🔼🔼🔻🔻 FTM Nakit: %1,8 15m: %78 🔼🔼🔼🔻🔻 USDC Nakit: %1,6 15m: %46 🔻🔻🔼🔼🔼 SAND Nakit: %1,6 15m: %55 🔼🔼🔼🔻🔼 DOT Nakit: %1,6 15m: %66 🔼🔼🔼🔼🔼 PNUT Nakit: %1,5 15m: %50 🔻🔻🔼🔼🔼 NEAR Nakit: %1,3 15m: %59 🔼🔼🔼🔻🔻 PEPE Nakit: %1,3 15m: %62 🔼🔼🔼🔻🔻 LRC Nakit: %1,2 15m: %53 🔼🔼🔼🔼🔼 AVAX Nakit: %1,0 15m: %55 🔼🔼🔼🔻🔻 WLD Nakit: %0,9 15m: %47 🔻🔻🔻🔻🔻 SEI Nakit: %0,9 15m: %59 🔼🔻🔻🔻🔻 FET Nakit: %0,9 15m: %48 🔻🔼🔻🔻🔻 LTC Nakit: %0,8 15m: %65 🔼🔼🔼🔻🔻 WIF Nakit: %0,8 15m: %64 🔼🔼🔼🔻🔻 LINK Nakit: %0,8 15m: %60 🔼🔼🔼🔻🔻 PYR Nakit: %0,8 15m: %55 🔼🔼🔼🔼🔼 BNB Nakit: %0,8 15m: %32 🔻🔻🔻🔻🔻 SHIB Nakit: %0,7 15m: %57 🔼🔼🔼🔻🔼 NOT Nakit: %0,6 15m: %54 🔼🔻🔼🔼🔼 TIA Nakit: %0,6 15m: %43 🔻🔻🔻🔼🔼 SLF Nakit: %0,6 15m: %56 🔼🔼🔼🔼🔼 LDO Nakit: %0,6 15m: %64 🔼🔼🔼🔻🔼 MANA Nakit: %0,5 15m: %62 🔼🔼🔻🔻🔼 Piyasa ciddi anlamda risk barındırıyor. Alım Yapma! Günlük nakit giriş oranı (1d satirindaki değer) %50 üzerine çıkarsa risk azalacaktır. Bu değer %49 altında oldukça piyasaya bulaşma! Kısa vadede tüm coinlere olan nakit girişini beğendim :). Bu modülün mantığını anlamak için bu kelimeye dokun: /EInOut"]
mytextio=["merhaba"]
mylonglar=[]
myshortlar=[]
mylonglarKA=["SUNUSDT"]
mylonglarSDV=[]
myshortlarSDV=[]
mylonglarCi=[]
myshortlarCi=[]
mylonglarMA=[]
mylonglarIOF=[]
myshortlarIOF=[]
ciraporu=0
karaporu=0
sdvraporu=0
maraporu=0
iofraporu=0
io1d=[49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1,49.1]
altustsinir=[48.1,49.5]
mybuys=[]
mysells=[]
hesapkitap=[]
smaperiod=3
myacc=[]




karzararnumber=[]
karzararlistesi=[]
def karzararesapla(coin, quantity, entry, close, liste, pozisyon):
    kar=pozisyon * quantity * (float(close) - float(entry))
    karzararlistesi.append([liste,coin,kar])
    print(f"kar zarar litesi:{karzararlistesi}")
    #mykar=[]
    #for elem in reversed(karzararlistesi):
    #    if elem[1] == coin:
    #        mykar.append(float(k[2]))
    #        #print(elem[1])  # Son "kar" elemanının ikinci değeri
    #        break
    #for k in karzararlistesi:
        
    karzararnumber.append(kar)
    print(kar)
    print(sum(karzararnumber))


def close_position(coin,liste):
    # Mevcut pozisyonu kapat
    positions = binanceclient.futures_position_information(symbol=coin)
    for position in positions:
        if float(position['positionAmt']) != 0:
            side = SIDE_SELL if float(position['positionAmt']) > 0 else SIDE_BUY
            myquantity=abs(float(position['positionAmt']))
            karzararesapla(coin,myquantity,position['entryPrice'],get_price(coin),liste,-1 if side=="SIDE_BUY" else 1)
            order = binanceclient.futures_create_order(
                symbol=coin,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=myquantity
            )
            print(f"Pozisyon kapatıldı: {order}")
            #hesapla(coin, side, myquantity)
            #eklesil(coin,liste,"sil")
            time.sleep(5)  # 5 saniye bekle

def get_price(symbol):
    try:
        ticker = binanceclient.get_symbol_ticker(symbol=symbol.upper())
        return ticker['price']
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
close_position("SANTOSUSDT","mylonglarKA")