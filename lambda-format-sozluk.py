"""Metin fonksiyonları"""

# format() fonksiyonu

name = "Selim"
sayi = 5
ucret = round(30.476, 1) # içerisindeki değeri en yakın sayıya yuvarlar, 
# virgülden sonra kaç basamak bırakacağımızı yazıyoruz

print("Adım", name, ", hedefi", sayi, "defa vurdum. Bana", ucret, "ödediler.")
print("Adım {}, hedefi {} defa vurdum. Bana {} TL ödediler.".format(name, sayi, ucret))
print(f"Adım {name}, hedefi {sayi} defa vurdum. Bana {ucret} TL ödediler.")


cumle = "SelimManga2001"
print(cumle.capitalize()) # Cümlenin sadece ilk harfini büyük yazdıran fonksiyon
print(cumle.upper()) # Tüm karakterleri büyük harfe çevirir
print(cumle.lower()) # Tüm karakterleri küçük harfe çevirir
print(cumle.title()) # Her kelimenin baş harfini büyültür
print(cumle.swapcase()) # Büyükleri küçük, küçükleri büyük yazdırır 
print(cumle.count("ma")) # Bir cümlede kaç defa "ma" yazıldığını verir
print(cumle.replace("8.15", "9.30")) # İstediğimiz kelimeyi başka istediğimiz bir kelime ile değiştirebiliriz
print(cumle.find("gece")) # Yazılan kelimenin cümle içindeki indeksini verir
print(cumle.rstrip()) # Cümlenin sağ tarafından başlayıp boşlukları siler
print(cumle.lstrip()) # Cümlenin sol tarafından başlayıp boşlukları siler
print(cumle.strip()) # Cümledeki bütün boşlukları siler
print(cumle.isalpha()) # Cümlenin harflerden oluşup oluşmadığını kontrol eder
print(cumle.isalnum()) # Cümlenin hem harf hem de sayılardan oluşup oluşmadığını kontrol eder

    
ulke = "Türkiye" 

"""Index yoluyla erişim"""
print(ulke[0]) # İlk harfini yazdırır (index: 0)
print(ulke[-1]) # Sondan 1. karakteri yazdırır (index: -1)

"""Dilimleme Yöntemi

degisken_adi[başlangıç_index : bitiş_index]
Eğer başlangıç ve bitiş aynı anda kullanılıyosa bitiş dahil değildir

dosya[1:5] = 5. index dahil değil

Değer girilmeyen yerin default indeksi 0'dır

"""
print(ulke[2:]) # 2 numaralı indexten başla sona kadar git
print(ulke[3:5]) # 3 numaralı indexten 5'e kadar git ve al ama 5'i dahil etme
print(ulke[:4]) # baştan 3 no'lu index dahil olmak üzere al

dosya_adi = "manzara.jpg"
print(dosya_adi[-4:]) # uzantı almak için
print(dosya_adi[:-4]) # dosyanın adı


print(f"Dosyanın adı {dosya_adi[:-4]}, dosyanın uzantısı {dosya_adi[-3:]}")
print("Dosyanın adı {}, dosyanın uzantısı {}".format(dosya_adi[:-4], dosya_adi[-3:]))

bolge = "Marmara"
print(bolge[:6])
print(bolge[-1:])
print(bolge[:-1])
print(bolge[:6:2]) # 0'dan başla 6'ya kadar 2 şer arttır
print(bolge[2:8:3]) # 2'den başla 8'e kadar 3 er arttır
print(bolge[::-1]) # Tersten yazdırır
    
"""SÖZLÜK

Anahtar : Değer formatında yazılır

"""

kelimeler = {"Kitap" : "Book", "Masa" : "Table", "Kalem" : "Pencil"}
print(kelimeler)
print(len(kelimeler)) # Kaç tane ikili olduğunu verir
print(kelimeler.keys()) # Sadece anahtarları yazdırmak için
print(kelimeler.values()) # Sadece değerleri yazdırmak için
print(kelimeler["Kalem"]) # İçine anahtarı yazdığımızda bu anahtara karşılık gelen değeri yazdırır

# Eklenenler
kelimeler["Elma"] = "Apple" # Sözlüğe yeni kelime ekler
kelimeler["Muz"] = "Banana"
print(kelimeler)

# Silme kodu
del kelimeler["Masa"] # 2.yol = kelimeler.pop("kalem")
print(kelimeler)

# Anahtarları alt alta yazdırmak için
for key in kelimeler.keys():
    print(key)
    
# Değerleri alt alta yazdırmak için
for value in kelimeler.values():
    print(value)    

# Her ikisini yazdırmak için
for key, value in kelimeler.items(): # items: elemanları gezdirmek için kullanıyoruz
    print(f"Anahtar: {key}, Değer: {value}") 
    
# Sözlükte anahtarla gezmek için
if "Muz" in kelimeler:
    print("Muz var")
else:
    print("Taze bitti")
    
# Sözlükte değerle gezmek için
if "Muz" in kelimeler.values():
    print("Banana exists")
else:
    print("Freshly out")    
     
"""Sözlük içinde sözlük"""

ailem = {
    "1. Çocuk": {"Ad" : "Cengiz",
                 "Yaş" : 22, 
                 "Boy" : 1.80},
    
    "2. Çocuk": {"Ad" : "Cafer",
                 "Yaş" : 11, 
                 "Boy" : 1.10}
}

print(ailem)
print(ailem["1. Çocuk"]["Boy"]) # 1. çocuğun boyunu yazdırmak için
print(ailem["2. Çocuk"]["Yaş"]) # 2. çocuğun boyunu yazdırmak için
   
# Sözlüğe 3. çocuğu ekledik
ailem["3. Çocuk"] = {"Ad": "Serpil",
                     "Boy": 1.60,
                     "Yaş": 20}

print(ailem)

# Daha estetik bir şekilde sırasıyla yazdırdık
for sira, ozellik in ailem.items():
    
    isim = ozellik["Ad"]
    yas = ozellik["Yaş"]
    boy = ozellik["Boy"]
    print(f"{sira} {isim} {yas} yaşında {boy} boyunda")

# fonksiyon tanımlarken varsayılan değer belirleme
# Kullanıcı hiçbir değer girmezse varsayılan sonuç 5'tir
def topla(a=0, b=5): 
    return a + b

def kare(x):
    return x ** 2

print(topla())
print(topla(7))
print(topla(b=8))
print(topla(a=6, b=8))
   
# Anonim fonksiyon tanımlama, istediğimiz adı verip daha kısa yazabiliyoruz
kareal = lambda x : x ** 2
print(kareal(3))

# Sözlükteki kullanımı
muzo = lambda x : x ["Muz"]
print(muzo(kelimeler))

cocuk1 = lambda x : x["1. Çocuk"]["Yaş"]
print(cocuk1(ailem))

toplam = lambda x, y : x + y
print(toplam(3, 5))

  