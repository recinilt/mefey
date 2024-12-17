import threading
import time
import queue

class StoppableThread(threading.Thread):
    def __init__(self, target, *args, **kwargs):
        super().__init__()
        self._stop_event = threading.Event()
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            while not self._stop_event.is_set():
                self._target(*self._args, **self._kwargs)
                time.sleep(0.1)
        except Exception as e:
            print(f"Thread hata verdi: {e}")

    def stop(self):
        self._stop_event.set()

# Kullanıcı input'unu timeout ile almak
def timed_input(prompt, timeout):
    q = queue.Queue()

    def input_thread():
        try:
            q.put(input(prompt))
        except EOFError:
            q.put(None)

    thread = threading.Thread(target=input_thread, daemon=True)  # Daemon thread
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("Süre doldu, cevap verilmedi.")
        return None
    else:
        return q.get()

# Thread içinde çalışacak fonksiyon
def ask_name():
    result = timed_input("İsim? ", 5)
    if result:
        print(f"Girilen isim: {result}")
    else:
        print("Zaman aşımı! İsim girilmedi.")

# Thread başlatma ve durdurma fonksiyonları
def start_thread(target_function):
    t = StoppableThread(target=target_function)
    t.daemon = True  # Daemon thread olarak işaretle
    t.start()
    return t

def stop_thread(thread):
    thread.stop()
    thread.join(1)  # Thread kapanması için max 1 saniye bekle
    print("Thread durduruldu.")

# Kullanım örneği: While Döngüsü
if __name__ == "__main__":
    try:
        while True:  # Döngü başlat
            print("\nYeni döngü başlıyor...")
            
            # Kullanıcıdan input almak için thread başlat
            thread = start_thread(ask_name)
            
            # 5 saniye bekle
            time.sleep(5)
            
            # Thread'i durdur
            stop_thread(thread)
            
            # Diğer işlemler
            print("Diğer işlemler devam ediyor...\n")
            
            # Döngüyü sonlandırmak için bir kontrol ekleyelim
            if input("Çıkmak için 'q' tuşuna basın, devam etmek için Enter'a basın: ").strip().lower() == 'q':
                print("Program sonlandırılıyor...")
                break
    except KeyboardInterrupt:
        print("Program durduruldu.")
