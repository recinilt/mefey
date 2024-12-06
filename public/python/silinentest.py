def son_bes_esit_mi(liste):
    # Listenin uzunluğu 5'ten kısa ise False döndür
    if len(liste) < 5:
        return False
    # Son 5 elemanı al ve hepsinin aynı olup olmadığını kontrol et
    return all(x == liste[-1] for x in liste[-5:])

# Örnek kullanım
liste = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(son_bes_esit_mi(liste))  # True döner

liste2 = [1, 2, 3, 4, 5, 5, 5, 5, 6]
print(son_bes_esit_mi(liste2))  # False döner
