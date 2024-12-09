def extract_usdt_coins(text, start_keyword, end_keyword):
    # Start ve end keyword arasındaki metni bul
    start_index = text.find(start_keyword)
    end_index = text.find(end_keyword, start_index)

    # Eğer end_keyword bulunamazsa, metnin sonuna kadar al
    if end_index == -1:
        end_index = len(text)
    
    # Belirlenen aralıktaki metni al
    section = text[start_index:end_index]
    
    # Her satırı döngüye sok ve "USDT" ile bitenleri bul
    usdt_coins = []
    for line in section.splitlines():
        if 'USDT' in line:
            coin = line.split()[0]  # Boşluklara göre ayır ve ilk elemanı (coin adını) al
            usdt_coins.append(coin)
    
    return usdt_coins

# Örnek metin ve anahtar kelimeler
text = """Trend Skoru Raporu Yorumları

Market Altcoin Gücü(0-100):95,9

Güçlü Yükseliş Yapanlar Yükseliş Skoru
OMUSDT 4,71
XRPUSDT 3,83
HBARUSDT 3,66
PEPEUSDT 3,35
DOGEUSDT 3,14
XVGUSDT 3,03
RSRUSDT 3,00
SUIUSDT 2,98
ALGOUSDT 2,64
JASMYUSDT 2,54

Güçlü Yükseliş Trendinde Olup En Ucuz Olanlar Yükseliş Skoru"""

# Fonksiyonu çağır ve sonuçları yazdır
coins = extract_usdt_coins(text, "Güçlü Yükseliş Yapanlar Yükseliş Skoru", "Güçlü Yükseliş Trendinde Olup En Ucuz Olanlar Yükseliş Skoru")
print(coins)
