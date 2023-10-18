""" Değişken Değerini Değiştirme """
toplam = 0
toplam = toplam + 1 # toplam değişkenine 1 ekle
toplam = toplam + 2 # toplam değişkenine 2 ekle

""" Kısayol: +-= operatörü """
toplam += 4 # toplam değişkenine 4 ekle
toplam -= 7 # toplam değişkeninden 7 çıkar
toplam *= 3 # toplam değerini 3 ile çarp
toplam /= 3 # toplam değerini 3 e böl
toplam **= 3 # toplam değerinin 3. kuvvetini al

""" Alt satıra geçme operatörü """

print("Selim\n" * 5) # alt alta 5 defa selim yazdıracak 
# new line = yeni satıra geç

""" Döngüler """
""" for i in range(5) 
    KODU BURAYA YAZ """

# 1 ile 10 arasındaki sayıları ekrana yazdır 
for i in range(10): # range(5) bize [0, 1, 2, 3, 4] listesini oluşturur
    print(i+1)
    
# Kısayol
for i in range(1, 11): # 1 den 10'a kadar olan sayıları. 11 dahil değil
    print(i)

# 2 şer saydırma
for i in range(1, 11, 2): # 1 den başla, 11 e kadar say, 2 şer arttır
    print(i) # [1, 3, 5, 7, 9]
    
# -2 şer saydırma
for i in range(11, 1, -2): # 11 den başla, 1 e kadar say, -2 şer arttır
    print(i) # [11, 9, 7, 5, 3]

# 7 ile 19 arasındaki sayıların toplamını bulunuz
# Temiz bir sonuç almak için toplam değişkeni oluşturup döngüden önce döngünün dışında 0'a eşitlemeliyiz
toplam = 0
for i in range(7, 20):
    toplam += i # for döngüsünün dışında yazmak için "for" ile aynı hizada yazmalıyız
    
print("Sonuç: ", toplam)
"""For döngüsünün içindeki kod bloğunun her bir çalışmasına yineleme denir"""

# 10 ile 3 arasındaki tek sayıları yan yana yazınız
for i in range(10, 2, -1): # [10, 9, 8, 7, 6, 5, 4, 3]
       if i % 2 != 0:
           print(i, end=" ") 
print(" ")           
"""
print fonksiyonunun içinde gizli bir end parametresi vardır, 
bunun varsayılan değeri \n olduğu için yan yana yazar. 
Eğer bunu end=" " yaparsak yan yana boşluk bırakarak yazdırabiliriz.
"""

# "Selim" ismindeki sesli harfleri ekrana yazdırınız ve kaç tane olduğunu saydırın
sayac = 0
for i in "Selim":
    if i.lower() in "aeıioöuü":
        print(i, end=" ")
        sayac += 1
print(sayac, "tane ünlü harf vardır.")

# Kullanıcıdan şifre girmesini isteyin ve 3 hak verin, eğer 3 defa yanlış girerse kullanıcıyı engelleyin

parola = "şafak"
for i in range(3):
    giris = input("Parolayı girin: ")
    if giris == parola:
        print("Parolayı doğru girdiniz, hoş geldiniz.")
        break # döngüyü sonlandıran kod
    else:
        print("Yanlış parola girdiniz. Kalan hakkınız ", 2-i)

# Girilen bir sayının faktöriyelini hesaplayınız
sayi = int(input("Bir sayı giriniz: "))
carpim = 1
for i in range(1, sayi+1): # [1, 2, 3, 4, 5]
    carpim *= i
print(sayi, "! =", carpim)


"""While Döngüswü

while KOŞUL:
    WHILE KOD BLOĞU    

"""

# 1 ile 100 arasında sayı girilene kadar kullanıcıdan sayı isteyelim
sayi = int(input("Sayı girin: "))
while sayi < 1 or sayi > 100:
    sayi = int(input("Lütfen 0 ile 100 arasında bir sayı girin: "))
    
# Kullanıcı bye diyene kadar kullanıcıdan sayı isteyin (sonsuz döngü)

while True: # True yerine herhangi bir doğru koşul da yazılabilir ÖR: 1 == 1 gibi
    cevap = input("Çıkış için 'bye' yazınız: ").lower()
    if cevap == "bye":
        break
    
# Şu şekilde de yazılabilir
while input("Çıkış için 'bye' yazınız: ").lower() != "bye":
    pass # Pass komutu geç anlamında kullanılır 