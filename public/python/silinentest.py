import threading
import queue
import time

def timed_input(prompt, timeout, default):
    q = queue.Queue()
    
    # Kullanıcı girdisini okuyan fonksiyon
    def get_input():
        try:
            user_input = input(prompt)
            q.put(user_input)
        except EOFError:
            q.put(None)
    
    # Girdi okuma fonksiyonunu her döngüde çalıştır
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    
    # Belirtilen süre kadar bekle
    input_thread.join(timeout)
    
    # Kullanıcıdan gelen veri veya zaman aşımı kontrolü
    if not q.empty():
        return q.get()
    else:
        print(f"\nZaman aşımı! Otomatik olarak önceki cevap ({default}) kullanılıyor.\n")
        return default

# Başlangıç değeri
previous_answer = "Varsayılan"

# While döngüsü
while True:
    try:
        # Kullanıcıdan girdi al
        user_input = timed_input("Cevabınızı girin (5 saniye içinde): ", 5, previous_answer)
        
        # Çıkış için kontrol
        if user_input.lower() == "exit":
            print("Programdan çıkılıyor...")
            break
        
        # Cevabı ekrana yaz ve önceki cevap olarak güncelle
        print(f"Girilen cevap: {user_input}")
        previous_answer = user_input
        
        # Döngüde devam etmeden önce kısa bir ara ver (isteğe bağlı)
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nProgram manuel olarak durduruldu.")
        break
