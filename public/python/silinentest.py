import re

def check_arrows(text):
    # Regex to find the lines with "15m=>", "1h=>" and "4h=>" with downward arrows
    pattern_15m = r'15m=>.*🔻'
    pattern_1h = r'1h=>.*🔻'
    pattern_4h = r'4h=>.*🔻'

    if re.search(pattern_15m, text) and re.search(pattern_1h, text) and re.search(pattern_4h, text):
        run_function()

def run_function():
    print("Fonksiyon çalıştı!")

# Metni yazın
text = """
Marketteki Tüm Coinlere Olan Nakit Girişi Raporu.
Kısa Vadeli Market Alım Gücü: 2,5X
Marketteki Hacim Payı:%96,1

15m=> %48,0 
1h=> %46,8 🔻
4h=> %49,2 🔻
12h=> %49,2 🔻
1d=> %50,0 🔼

En çok nakit girişi olanlar.(Sonunda 🔼 olanlarda nakit girişi daha sağlıklıdır)
Nakitin nereye aktığını gösterir. (Nakit Göçü Raporu)

DOGE Nakit: %10,8 15m: %46 🔻🔻🔻🔻🔻
...
"""

# Fonksiyonu çağırın
check_arrows(text)
