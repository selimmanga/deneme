import random # random kütüphanesi
random.seed(60) # random fonksiyonunu aynı yerden başlatmak için kullanılan kod, buraya istediğimiz sayıyı girebiliriz
print(random.randint(5, 10)) # Rastgele tam sayı üretmek için randint fonksiyonunu kullanıyoruz, randint(a, b): a: alt sınır b: üst sınır

sayilar = []

for i in range(5):
   zar = random.randint(1, 6)
   sayilar.append(zar)
print(sayilar)

for i in range(len(sayilar)):
   print(i+1, ".sayı =", sayilar[i])

# range kullanmadan sayılar kümesini gezmek için
for i in sayilar:
   print(i)

# Hem sayıyı hem de indeksini gezmek için:
# enumerate: hem sayıyı hem indeksini yazdırır
for i, sayi in enumerate(sayilar):
   print(i, sayi)


# Birbirinden farklı rastgele sayılar üretmek için
# sample: havuz oluşturup örnek alır ve farklı değerler üretir

#farkli_sayilar.sort()
#print(farkli_sayilar)

farkli_sayilar = random.sample(range(1, 50), 10)
print(sorted(farkli_sayilar)) 

iki_kat = []

for i in farkli_sayilar:
   #if i % 2 == 1: -> sadece tek sayıların 2 katını almak için kullanıyoruz
   iki_kat.append(i*2)
print(sorted(iki_kat))

# List Comprehension
# Yukardaki işlemi tek satırda ve daha hızlı şekilde yazdırdık
iki_kat = [i*2 for i in farkli_sayilar]
print(sorted(iki_kat))

# Her sayının küpünü alalım 
kupler = [i*2 for i in farkli_sayilar] # sonuna if i % 2 == 1 eklersek sadece tek sayıların küpünü alır