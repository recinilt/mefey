import re
def extract_coin_data_IOF2(text):
    import re
    # Regex pattern to find the relevant data
    pattern = r"(\w+USDT) (\d+,\d+)X Payı:%(\d+,\d+) Pahalılık:(\d+,\d+) ([🔼🔻]+)"
    results = []
    for match in re.finditer(pattern, text):
        symbol = match.group(1)
        multiplier = float(match.group(2).replace(',', '.'))
        share = float(match.group(3).replace(',', '.'))
        expensiveness = float(match.group(4).replace(',', '.'))
        trends = [True if x == '🔼' else False for x in match.group(5)]
        results.append([symbol, multiplier, share, expensiveness, trends])
    return results


example_text="""Marketteki Tüm Coinlere Olan en çok nakit girişi olanlar.
(Sonunda 🔼 olanlarda nakit girişi daha sağlıklıdır)
Nakitin nereye aktığını gösterir. (Nakit Göçü Raporu)
Symbol GİRİŞİGücü NakitGİRİŞİPayı MinorTrendScore(Pahalılık Değeri) AlışBaskınlığıÖzeti


LINKUSDT 3,9X Payı:%6,9 Pahalılık:1,6 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:LINKUSDT)
UNIUSDT 3,5X Payı:%5,9 Pahalılık:1,6 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:UNIUSDT)
OMUSDT 2,6X Payı:%0,7 Pahalılık:1,3 🔼🔼🔼🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:OMUSDT)
SUSHIUSDT 2,3X Payı:%2,4 Pahalılık:2,8 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:SUSHIUSDT)
VETUSDT 2,2X Payı:%1,0 Pahalılık:1,3 🔼🔼🔼🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:VETUSDT)
IRISUSDT 2,1X Payı:%0,4 Pahalılık:2,1 🔼🔼🔼🔼🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:IRISUSDT)
RUNEUSDT 2,0X Payı:%1,2 Pahalılık:1,1 🔻🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:RUNEUSDT)
DYDXUSDT 1,5X Payı:%1,1 Pahalılık:1,6 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:DYDXUSDT)
GALAUSDT 1,3X Payı:%1,4 Pahalılık:1,4 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:GALAUSDT)
AAVEUSDT 1,3X Payı:%0,6 Pahalılık:1,3 🔻🔻🔼🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:AAVEUSDT)
LQTYUSDT 1,2X Payı:%0,7 Pahalılık:1,9 🔼🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:LQTYUSDT)
BTCUSDT 1,1X Payı:%12,4 Pahalılık:1,0 🔻🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:BTCUSDT)
CRVUSDT 1,1X Payı:%1,2 Pahalılık:1,3 🔼🔻🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:CRVUSDT)
USDCUSDT 0,9X Payı:%6,5 Pahalılık:1,0 🔻🔼🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:USDCUSDT)
ADAUSDT 0,9X Payı:%2,4 Pahalılık:1,0 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:ADAUSDT)
ETHUSDT 0,8X Payı:%8,0 Pahalılık:1,1 🔻🔻🔼🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:ETHUSDT)
DOTUSDT 0,8X Payı:%0,9 Pahalılık:1,0 🔻🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:DOTUSDT)
1MBABYDOGEUSDT 0,7X Payı:%3,2 Pahalılık:3,3 🔼🔼🔻🔻🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:1MBABYDOGEUSDT)
FTMUSDT 0,7X Payı:%0,6 Pahalılık:1,0 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:FTMUSDT)
SANDUSDT 0,7X Payı:%0,7 Pahalılık:1,2 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:SANDUSDT)
PNUTUSDT 0,7X Payı:%2,2 Pahalılık:1,0 🔻🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:PNUTUSDT)
XRPUSDT 0,6X Payı:%9,4 Pahalılık:1,2 🔼🔻🔻🔼🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:XRPUSDT)
SUIUSDT 0,6X Payı:%1,5 Pahalılık:1,1 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:SUIUSDT)
PEPEUSDT 0,6X Payı:%9,2 Pahalılık:1,5 🔻🔼🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:PEPEUSDT)
BNBUSDT 0,6X Payı:%1,9 Pahalılık:1,0 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:BNBUSDT)
NEIROUSDT 0,5X Payı:%1,1 Pahalılık:1,1 🔼🔻🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:NEIROUSDT)
ALGOUSDT 0,5X Payı:%0,6 Pahalılık:1,1 🔼🔼🔻🔻🔻 Grafik (http://tradingview.com/chart/?symbol=BINANCE:ALGOUSDT)
DOGEUSDT 0,5X Payı:%10,5 Pahalılık:1,1 🔼🔻🔼🔼🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:DOGEUSDT)
SOLUSDT 0,5X Payı:%3,8 Pahalılık:1,0 🔻🔻🔻🔻🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:SOLUSDT)
HBARUSDT 0,4X Payı:%1,5 Pahalılık:1,3 🔻🔼🔻🔻🔼 Grafik (http://tradingview.com/chart/?symbol=BINANCE:HBARUSDT)


Bu modülün mantığını anlamak için bu kelimeye dokun: /EInOutFlow"""
# Test the improved function with the previous example text
print(extract_coin_data_IOF2(example_text))
