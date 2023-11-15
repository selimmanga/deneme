import numpy as np

# 0 boyutlu dizi
a = np.array(5)
print(a)
print(type(a))

# 1 boyutlu dizi
a = np.array([1, 2, 3, 4, 5, 6])
b = np.arange(1, 7) # arange(): belirlenen aralıkta sayıları kullanarak dizi üretir ÖR: arange(1, 7) ve 7 dahil değil
c = np.linspace(1, 6, num=6, dtype=int) # linspace(1, 6, dtype=int): 1'den 6'ya 6 eş parçaya bölerek sayı üret ve hepsini int yap (1 ve 6 dahil)
print("a\n", a)
print("b\n", b)
print("c\n", c)

# 1'den 6'ya 6 eş parçaya bölerek sayı üret
# 1 ---> 2 ---> 3 ---> 4 ---> 5 ---> 6
# Aralarındaki mesafe aynı

print(type(a)) # değişkenin türü
print("ndim\n", a.ndim) # dizinin hangi boyut olduğu
print("shape\n", a.shape) # dizinin şekli (satır ve sütun sayısını söyler)
print("size\n", a.size) # dizideki eleman sayısı
print("dtype\n", a.dtype) # dizideki değerlerin türü

# 2 boyutlu diziler
a = np.array ([[3, 5, 7],
               [6, 0, 1],
               [6, 7, 4]]) # 2 boyutlu dizi

b = np.arange(1,7).reshape(2,3) # 1'den 6'ya kadar sayı üret ve 2 satır, 3 sütundan oluştur (tek boyuttan iki boyuta geçirme yöntemi)
print("a\n", a)
print("b\n", b)

birler = np.ones(shape=(3,4), dtype=float) # 1'lerden liste oluştur
sifirlar = np.zeros(shape=(2,2), dtype=int) # 0'lardan liste oluştur
birim_matris = np.eye(5) # 5 satır ve 5 sütunlu birim matris oluşturur, soldan aşağı çapraza doğru tüm değerleri 1 gerisi 0'dır
ayni_degerler = np.full(shape=(5,5), fill_value=9) # 5 e 5'lik matris oluştur ve tüm değerlerini 9 yap

# Birim matrisin sembolü = I

print("birler\n", birler)
print("sıfırlar\n", sifirlar)
print("birim matris\n", birim_matris)
print("aynı değerler\n", ayni_degerler)

bos_degerler = np.empty((3, 6), dtype=np.uint8) # 8 bitlik işaretsiz tam sayı üret: uint8
print("boş değerler\n", bos_degerler)
bos_degerler.fill(7)
print("doldurulan değerler\n", bos_degerler)

# 2 boyutlu dizilerde verilere erişim
a = np.array([[1, 2, 3],
              [4, 5, 6]])
# sayilar[satır, sütun] (ikisi de index), ÖR: sayilar[1, 2]: 1. satır 2. sütun

# Dilimleme
a = np.array([[1, 2, 3, 4],
              [4, 5, 6, 7],
              [7, 8, 9, 10]])
print(a)
print("1. satırın hepsi\n", a[0, :]) # 1. satırdaki tüm sütunlar
print("1. sütunun hepsi\n", a[:, 0]) # 1. sütundaki tüm satırlar
print("ilk 2 satırdaki değerler\n", a[0:2, :]) # 1. ve 2. satırdaki tüm değerler
print("ilk 2 sütun\n", a[:, 0:2]) # 1. ve 2. sütundaki tüm değerler

# 2. satırdan 3. satıra, 2. sütundan 3. sütuna tüm değerler
print("2. ve 3. satır, 3. ve 4. sütun\n", a[1:3, 2:4])

# Rassal Sayılar
a = np.random.randint(low=2, high=6, size=(3, 4)) # 2 ve 6 arasında 3 satır, 4 sütundan oluşan bir dizi üret [low, high)

# Aritmetik işlemler
x = np.eye(3) # 3 e 3 lük birim matris üret
y = np.arange(1, 10).reshape(3,3)
print("x\n", x)
print("y\n", y)
print("x+y\n", x+y)
print("x-y\n", x-y)
print("x*y\n", x*y)
print("x/y\n", x/y)
print("x%y\n", x%y)
print("x**y\n", x**y)


#Lineer Cebir işlemleri
x = np.array([1,2,3,4,5,60])
y = np.array([5,6,7,8,9,10])
print("y-5\n", y-5)               # tüm değerlerden 5 çıkar
print("x*2\n", x*2)               # tüm değerleri 2 ile çarp
print("x**2\n", x**2)              # tüm değerlerin karesini al
print("sin(x)\n", np.sin(x))         # tüm değerlerin sinüsünü al
print("e^x\n", np.exp(x))         # tüm değerlerin e^x den geçir

z = np.dot(x,y)          # iç çarpım (dot product)
print("x.y\n", z)
x = y.reshape(3,2)       # 3x2 lik hale getir
y = y.reshape(2,3)       # 2x3 lik hale getir
print("x\n", x)
print("y\n", y)
print("yT", y.T)               # transpoz işlemi (satırları sütun, sütunları satır yapar)
print("x matmul y \n", np.matmul(x,y))    # matris çarpımı (1. matrisin satır sayısı ile 2. matrisin sütun sayısı aynı olmak zorunda. Matrisleri çarparken transpoz işlemi kullanılır)

# Toplam fonksiyonları
x = np.arange(1,6)
x[2] = 1            # 3.degeri 1 yap
print(x)
print("toplam\n", np.sum(x))
print("ortalama\n", np.mean(x))
print("max\n", np.max(x))
print("maksimumun indeksi\n", np.argmax(x))
print("median\n", np.median(x)) # önce sıralayıp daha sonra ortanca sayıyı almak için kullanılır
print("eşsiz değerler\n", np.unique(x))


# Belli bir eksende toplam fonksiyonları
a = np.arange(1,7).reshape(2,3)
print("a\n", a)
x = np.sum(a, axis=0)    # satırları üst üste koy topla
y = np.sum(a, axis=1)    # her satırdaki tüm değerleri topla
print("axis=0 toplam\n", x)
print("axis=1 toplam\n", y)


# Mantıksal Operatörler
a = np.arange(1,7).reshape(2,3)
print("a\n",         a)
print("a>5\n",       a>5)  # 5 ten büyük olup olmama
print("a[a>5]\n",    a[a>5])           # 5 ten büyük olan değerleri getir
print("a%2== 0\n",   a%2 ==0)         # çift sayı mı
print("where a>2\n", np.where(a>2)) # hangi indeksteki değerler 2 den büyük
print("all(a)\n",    np.all(a))        # tüm değerlere bakıp True mu False mu olduğunu kontrol eder, hepsi true ise true, false ise false yazar
print("all a>1\n",   np.all(a>1))     # tüm değerler 1 den büyük mi ?
print("any(a)\n",    np.any(a))     # 0 dan ve False dan farklı değer var mı ?
sifirlar = np.zeros((3,3))
print("any sıfırlar\n", np.any(sifirlar))     # 0 dan ve False dan farklı değer var mı ?
print("any a>8\n",      np.any(a>8))          # 8 den büyük bir değer var mı ?


# İki diziyi birleştirme
a = np.arange(1,7).reshape(2,3)
b = np.random.randint(7, size=(2,3))
print("a\n", a)
print("b\n", b)
print("üst üste koy\n", np.vstack([a,b]))
print("yan yana koy\n", np.hstack([a,b]))

# Dosya İşlemleri

from google.colab import drive
drive.mount('/content/drive')

dosya = "/content/drive/My Drive/myo_yapay_zeka/sayisal_veri.csv"
veri = np.loadtxt(dosya, delimiter=",", skiprows=0)
veri

ortalama = np.mean(veri, axis=0)
print(ortalama)
maks = np.max(veri, axis=0)
veri = (veri - ortalama)

veri = veri/ maks
veri

np.savetxt('islenmis_sayisal_veri.csv', veri, delimiter=',')
