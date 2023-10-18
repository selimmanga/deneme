print("Merhabah\n" * 41)

print("Benim adım Selim Manga,", 22, "yaşındayım", 70, "kiloyum")

print("En yakın arkadaşım Burak. Onunla", 45, "yıldır tanışıyorum")
# Python kodlarını yorumlayıcı çalıştırır

print(25 + 5) # toplama
print(25 - 5) # çıkarma
print(25 / 5) # bölme
print(25 // 5) # tamsayılı bölme (cint)
print(25 * 5) # çarpma
print(25 % 5) # mod
print(2 ** 5) # üs alma

print(3 * 2 + 5)
print(3 * (2+5))
print(27 / 3 / 3)
print(2 ** 3 / 4)

# işlem öncelikleri

print(type(6))
print(type("merhaba"))
print(type(104.5))
# girilen değerin türünü veren kod

print(True)
print(False)
print(type(True))
# "bool" türü tercihlerde kullanılır

# Karşılaştırma operatörleri

print(50 > 25) # true
print(25 >= 25) # true
print(50 < 15) # false
print("Selim" == "selim") # false
print("Selim" != "mahir") # true
print(18 <= 17) # false

# Mantıksal operatörler

# "ve" operatörü (and)
print(True and True) # true - 1
print(False and True) # false - 0
print(False and False) # false - 0
print(True and False) # false - 0

print(5>0 and 5<10) # true
print(8 != 6 and 5 > 2 and "Selim" != "ali") # true

# "veya" operatörü (or)
print(True or True) # true - 1
print(False or True) # true - 1
print(False or False) # false - 0
print(True or False) # true - 1

print(6 < 9 or 8 > 17) # true
print("a" == "k" or "b" != "c" or 8 - 8 == 0) # true

# "and" ve "or" bir arada kullanma

print("A" == "B" or (7 < 9 and 8 < 12)) # true
