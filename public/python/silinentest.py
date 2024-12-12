import re

def parse_text_line_by_line_safe_SSR(text):
    # Split the text into lines
    lines = text.strip().split("\n")
    
    # Prepare the result list
    results = []
    
    # Process each line
    for line in lines:
        parts = line.split()
        
        # Skip lines that don't have enough parts or contain header titles
        if len(parts) < 10 or not parts[1].replace(',', '').replace('.', '').isdigit():
            continue

        symbol = parts[0]
        price = float(parts[1].replace(',', '.'))
        trend_string = [p == '+' for p in parts[2:7]]
        smart_score = float(parts[7].replace(',', '.')) if parts[7] != 'NULL' else None
        trend_score = float(parts[8].replace(',', '.')) if parts[8] != 'NULL' else None
        minor_trend_score = float(parts[9].replace(',', '.')) if parts[9] != 'NULL' else None
        
        # Append the parsed data to the result list
        results.append([symbol, price, trend_string, smart_score, trend_score, minor_trend_score])
    
    return results

# Sample report text, typically this function will receive the full report as argument


metin1 = """
Akıllı Skoru En Fazla Olan Coinler
Symbol Price TrendString SmartScore TrendSore MinorTrendScore
AVAXUSDT 54,53 + + + + + 54,47 1,6 1,6 
TRXUSDT 0,3080 + + + + - 28,15 2,2 1,3 
LINKUSDT 28,20 + + + + + 16,20 1,9 1,7 
AAVEUSDT 369,4 - + + + + 8,91 3,1 2,4 
COWUSDT 0,6016 + + + + + 8,16 NULL 2,4 
OPUSDT 2,588 + + + + + 8,00 1,1 1,3 
CRVUSDT 1,133 + + + + + 7,66 2,4 1,1 
SOLUSDT 233,4 + + + + + 7,49 1,6 1,1 
BTCUSDT 101648 + + + + + 7,21 1,7 1,1 
LTCUSDT 124,1 + + + + - 6,68 1,6 1,2 
MASKUSDT 4,271 + + + + + 6,55 1,3 1,6 
IOUSDT 4,369 - + + + + 6,53 NULL 1,8 
TIAUSDT 7,518 + + + + - 6,22 0,8 1,1 
LDOUSDT 2,342 + + + + + 6,12 1,1 2,0 
SUIUSDT 4,673 - + + + + 6,07 3,3 1,6 
ALTUSDT 0,1813 + + + + + 5,98 NULL 1,3 
ETHUSDT 3948 + + + + + 5,97 1,4 1,1 
BNBUSDT 719,6 + + + + - 5,36 1,4 1,1 
BLURUSDT 0,3919 + + + + - 5,28 NULL 1,3 
CTKUSDT 0,9732 + + + + + 5,10 1,3 1,5 
APTUSDT 13,89 + + + + + 4,95 1,5 1,3 
SANDUSDT 0,8003 + + + + - 4,94 1,9 1,1 
NEARUSDT 7,276 + + + + - 4,93 1,5 1,2 
DIAUSDT 0,9352 + + + + + 3,59 1,8 1,3 
XRPUSDT 2,430 + - + + + 3,54 3,7 1,1 
EIGENUSDT 5,124 + + + + + 3,43 NULL 1,4 
TROYUSDT 0,006327 + + + + + 3,40 2,5 2,1 
FTMUSDT 1,280 + + + + + 3,27 2,1 1,2 
DOGEUSDT 0,4162 + + + - - 2,98 2,9 1,0 
ARBUSDT 1,063 - + + + - 2,91 1,0 1,1 

Canlı olan coin sayısı:0 olduğu için piyasa iştahsız görünüyor
Tüm coinlerin günlük alış baskısı %50 altında(49,80 olduğu için piyasa halen risk barındırıyor. Kurnaz avcı öneri yapabilir fakat bu tür piyasadalarda terste kalma ihtimalin daha yüksektir. .

Kurnaz Avcı Modülünün Size Seçtiği Güvenilir Olabilecek Coinler: 
ALT TS:NULL MTS:1,3 PT:1,017
 Dk:49✅ Kar:%0,1 🙂 Grafik (http://tradingview.com/chart/?symbol=BINANCE:ALTUSDT)

APT TS:1,5 MTS:1,3 PT:1,027
 Dk:264✅ Kar:%-1,1 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:APTUSDT)

DIA TS:1,8 MTS:1,3 PT:1,019
 Dk:9 Kar:%-0,1 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:DIAUSDT)

FTM TS:2,1 MTS:1,2 PT:1,040
 Dk:138✅ Kar:%-1,4 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:FTMUSDT)

Kurnaz Avcı Mantığını Anlamak Dokunun /EKurnazAvci


Bu raporun mantığını anlamak için dokun: /ESSR
"""



metin2="""Akıllı Skoru En Fazla Olan Coinler
Symbol Price TrendString SmartScore TrendSore MinorTrendScore
AVAXUSDT 54,53 + + + + + 54,47 1,6 1,6 
TRXUSDT 0,3080 + + + + - 28,15 2,2 1,3 
LINKUSDT 28,20 + + + + + 16,20 1,9 1,7 
AAVEUSDT 369,4 - + + + + 8,91 3,1 2,4 
COWUSDT 0,6016 + + + + + 8,16 NULL 2,4 
OPUSDT 2,588 + + + + + 8,00 1,1 1,3 
CRVUSDT 1,133 + + + + + 7,66 2,4 1,1 
SOLUSDT 233,4 + + + + + 7,49 1,6 1,1 
BTCUSDT 101648 + + + + + 7,21 1,7 1,1 
LTCUSDT 124,1 + + + + - 6,68 1,6 1,2 
MASKUSDT 4,271 + + + + + 6,55 1,3 1,6 
IOUSDT 4,369 - + + + + 6,53 NULL 1,8 
TIAUSDT 7,518 + + + + - 6,22 0,8 1,1 
LDOUSDT 2,342 + + + + + 6,12 1,1 2,0 
SUIUSDT 4,673 - + + + + 6,07 3,3 1,6 
ALTUSDT 0,1813 + + + + + 5,98 NULL 1,3 
ETHUSDT 3948 + + + + + 5,97 1,4 1,1 
BNBUSDT 719,6 + + + + - 5,36 1,4 1,1 
BLURUSDT 0,3919 + + + + - 5,28 NULL 1,3 
CTKUSDT 0,9732 + + + + + 5,10 1,3 1,5 
APTUSDT 13,89 + + + + + 4,95 1,5 1,3 
SANDUSDT 0,8003 + + + + - 4,94 1,9 1,1 
NEARUSDT 7,276 + + + + - 4,93 1,5 1,2 
DIAUSDT 0,9352 + + + + + 3,59 1,8 1,3 
XRPUSDT 2,430 + - + + + 3,54 3,7 1,1 
EIGENUSDT 5,124 + + + + + 3,43 NULL 1,4 
TROYUSDT 0,006327 + + + + + 3,40 2,5 2,1 
FTMUSDT 1,280 + + + + + 3,27 2,1 1,2 
DOGEUSDT 0,4162 + + + - - 2,98 2,9 1,0 
ARBUSDT 1,063 - + + + - 2,91 1,0 1,1 

Canlı olan coin sayısı:0 olduğu için piyasa iştahsız görünüyor
Tüm coinlerin günlük alış baskısı %50 altında(49,80 olduğu için piyasa halen risk barındırıyor. Kurnaz avcı öneri yapabilir fakat bu tür piyasadalarda terste kalma ihtimalin daha yüksektir. .

Kurnaz Avcı Modülünün Size Seçtiği Güvenilir Olabilecek Coinler: 
ALT TS:NULL MTS:1,3 PT:1,017
 Dk:49✅ Kar:%0,1 🙂 Grafik (http://tradingview.com/chart/?symbol=BINANCE:ALTUSDT)

APT TS:1,5 MTS:1,3 PT:1,027
 Dk:264✅ Kar:%-1,1 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:APTUSDT)

DIA TS:1,8 MTS:1,3 PT:1,019
 Dk:9 Kar:%-0,1 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:DIAUSDT)

FTM TS:2,1 MTS:1,2 PT:1,040
 Dk:138✅ Kar:%-1,4 🤕 Grafik (http://tradingview.com/chart/?symbol=BINANCE:FTMUSDT)

Kurnaz Avcı Mantığını Anlamak Dokunun /EKurnazAvci


Bu raporun mantığını anlamak için dokun: /ESSR"""


# Calling the function to parse the provided SSR report text
cikti1=parse_text_line_by_line_safe_SSR(metin1)
cikti2=parse_text_line_by_line_safe_SSR(metin2)
print(cikti1)
print(cikti2)