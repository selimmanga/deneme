meyveler = []
meyveler = input("Dört adet meyve yazınız: ").split(",")
print(meyveler)

fiyatlar = input("Meyvelerin fiyatlarını girin: ").split(" ")
fiyatlar = list(map(float, fiyatlar))
print(fiyatlar)

for i in range(len(meyveler)):
    print("1 kg", meyveler[i], fiyatlar[i], "TL")

# iki listeyi birleştirip gezmek için:
# for döngüsünde iki listeyi gezmek için zip fonksiyonu kullanılır
for meyve, fiyat in zip(meyveler, fiyatlar):
    print("1 kg", meyve, fiyat, "TL")