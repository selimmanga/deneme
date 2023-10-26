class Araba:
    teker_sayisi = 4
    beygir_gucu = 90
    model = 94 
    marka = "BMW"

    def __init__(self, ts, bg, mdl, mrk):
        self.teker_sayisi = ts
        self.beygir_gucu = bg
        self.model = mdl
        self.marka = mrk

    def __str__(self):
        bilgi = "Teker Sayısı: " + str(self.teker_sayisi) + "\nBeygir Gücü: " + str(self.beygir_gucu) + "\nModeli: " + str(self.model) + "\nMarkası: " + str(self.marka)
        return bilgi
    
burakin_arabasi = Araba(4, 700, "Mustang 1987", "Ford")  
yusuf_arabasi = Araba(4, 500, "M5", "BMW")

class Ogrenci:
    ogr_ad = "Selim"
    ogr_soyad = "Manga"
    ogr_no = 39
    ogr_yas = 22
    ogr_bolum = "Bilgisayar Programcılığı"

    def __init__(self, ad, soyad, no, yas, bolum):
        self.ogr_ad = ad
        self.ogr_soyad = soyad
        self.ogr_no = no
        self.ogr_yas = yas
        self.ogr_bolum = bolum

    def __str__(self):
        bilgi = "Ad: " + str(self.ogr_ad) + "\nSoyad: " + str(self.ogr_soyad) + "\nÖğrenci No: " + str(self.ogr_no) + "\nYaşı: " + str(self.ogr_yas) + "\nBölümü: " + str(self.ogr_bolum)
        return bilgi
    
Burak = Ogrenci("Burak Arda", "IŞIK", 21, 21, "Bilgisayar Programcılığı")   


