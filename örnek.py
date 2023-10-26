# Kullanıcıdan tek seferde 3 tane tam sayı isteyelim
sayilar = input("3 tane sayı girin: ").split(",") # split: parçalamak, virgüle göre parçalama yapacağı için "," yazdık
print(sayilar)

# Önce hangi karakteri kullanarak birleştirmek istediğimizi belirttik daha sonra join fonksiyonu ile birleştirme işlemini yaptık
sayilar_str = "-".join(sayilar)
print(sayilar_str)

# map fonksiyonu
# listedeki her bir elemanını bir fonksiyondan geçirir
# liste olarak döndürmesi için list parantezine aldık
sayilar = list(map(int, sayilar))
print(sayilar)

# Kullanıcıdan 4 adet meyve isteyelim ve listeye yazdıralım
meyveler = []

for i in range(4):
    meyve = input("Meyve adı giriniz: ")
    meyveler.append(meyve)

print(meyveler)

#2. yol
meyveler = input("Dört adet meyve yazınız: ").split(",")
print(meyveler)

fiyatlar = input("Meyvelerin fiyatlarını girin: ").split(" ")
fiyatlar = list(map(float, fiyatlar))
print(fiyatlar)