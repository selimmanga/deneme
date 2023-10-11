# Değişken: içerisinde veri sakladığımız bellek birimleridir
# En önemli 3 özellik: Değer, İsim ve Tür

isim = "selim"
print(isim)

### "Değişken oluşturma kuralları" ###
# Türkçe karakter kullanılamaz
# Rakamla başlayamayız
# Kullanabileceğimiz tek özel karakter "_"
# Python'a özgü anahtar kelimeleri kullanamayız
# Bir değerde *10** gibi bir değer varsa onun yerine "e" yazabiliriz. ÖR: "6.02*10**-23" yerine "6.02e-23"

yas = 30
vize1 = 96
sehir = "İstanbul"
kitap_sayisi = 5

print("Yaşım", yas, "İlk vizem", vize1,".", sehir,"da yaşıyorum.", kitap_sayisi,"kitap okudum.")

# Kullanıcıdan değer alma
# input() fonksiyonu ile yapabiliriz
# string olan bir değeri integera çevirmek için int() fonksiyonu içerisinde yazılır. Aynı şekil diğer fonksiyonları da yazabiliriz float gibi

isim = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
yas = int(input("Yaşınızı girin: "))
kilo = float(input("Kilonuzu girin: "))
boy = float(input("Boyunuzu girin: "))

print("Ad: ", isim)
print("Soyad: ", soyad)
print("Yaşınız: ", yas)
print("Kilonuz: ", kilo)
print("Boyunuz: ", boy)

# Çemberin çevresini hesaplayan programı yazın

pi = 3.14
yaricap = float(input("Yarıçapı giriniz: "))
cevre = 2*pi*yaricap
print("Yarıçapı ", yaricap, "olan çemberin çevresi: ", cevre)



# Final ve Vize notu girilen öğrencinin not ortalamasın hesaplayan programı yazın

vize = int(input("Vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))
gno = (vize*40/100) + (final*60/100)
print("Genel not ortalamanız: ", gno)

# IF-ELSE
### Yapı ###
# if koşul:
#     koşul doğruysa çalışacak olan kod
#else:
#     koşul doğru değilse çalışacak olan kod

if(gno > 40):
  print("Dersten geçtiniz.")
else:
  print("Büte kaldınız.")

# Kullanıcıdan yaşını isteyiniz, eğer 18 yaşında veya büyükse ehliyet alabilsin değilse alamasın

yas = int(input("Yaşınızı girin: "))

if (yas >= 18):
  print("Ehliyet alabilirsiniz.")
else:
  print("Ehliyet alamazsınız.")

# Kullanıcıya bilmece sorun bilirse tebrik edin, bilemezse doğru cevabı yazdırın
# upper() fonksiyonu girilen metni tamamen büyük yazdırır

cevap = input("Çarşıdan aldım bir tane eve geldim bin tane, bu nedir?").upper()

if (cevap == "NAR"):
  print("Tebrikler doğru cevap!")
else:
  print("Yanlış cevap.")

# Birden fazla koşul için else if kullanılır kısaca elif: olarak yazılır

# Ortalaması 0 ile 30 arasında olan öğrencilerin harf notu "FF", 40 ile 60 arasında olanlar için "CC", 60 ile 100 arasındaysa "AA"

vize = int(input("Vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))
gno = (vize*40/100) + (final*60/100)

if(gno >= 0 and gno <= 40):
  print("Ortalamanız: ", gno)
  print("Harf notunuz: FF")
elif (gno <= 60):
  print("Ortalamanız: ", gno)
  print("Harf notunuz: CC")
else:
  print("Ortalamanız: ", gno)
  print("Harf notunuz: AA")

# Dolmuşa binen kişinin öğrenci olup olmadığına bakın, öğrenci ise 10 TL, değilse 15 TL alın
# Ne kadar para üstü alacağını da ekrana yazdıralım
# lower() fonksiyonu upper() fonksiyonunun tam tersi olarak metni tamamen küçük harflerle yazdırır

ogr = input("Öğrenci misin?  e, h ").lower()
para = float(input("Kaç paran var? "))

if(ogr == "e"):
  if (para < 10):
    print("Dolmuştan inin.")
  else:
    print("Para üstünüz: ", para-10)

if(ogr == "h"):
  if (para < 15):
    print("Dolmuştan inin.")
  else:
    print("Para üstünüz: ", para-15)
