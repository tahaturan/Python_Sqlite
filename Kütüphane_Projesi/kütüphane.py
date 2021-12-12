import sqlite3
import time


class Kitap():
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return ' Kitap ismi: {}\n Yazarı: {}\n Yayınevi: {}\n Türü: {}\n Baski Sayısı:{}\n-------------------'.format(self.isim,
                                                                                                   self.yazar,
                                                                                                   self.yayinevi,
                                                                                                   self.tur, self.baski)
class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglati=sqlite3.connect("kütüphane.db") #kütüphane diye veritabanı olusturmak istiyoruz dedik
        self.cursor=self.baglati.cursor() #burada ise kütüphane içinde işlem yapabilmek için imlecimizi olusturduk

        sorgu= "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT, yayinevi TEXT,tür TEXT,baskı_sayısı INT)"
        #sorgumuzu önceden yazdık daha iyi olacagını düşündüğüm için
        self.cursor.execute(sorgu) # sorgumuzu çalıstırdık
        self.baglati.commit() #sorgmuzun veritabanına işlenmesi için commit() fonksiyonunu kullandık
    def baglatiyi_kes(self):
        self.baglati.close()

    def kitaplari_goster(self):
        sorgu="SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if len(kitaplar) ==0:
            print("Kütüphanede Kitap Bulunmamaktadır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
                """
                burada böyle yapmamızın sebebi biz yukarıda kitap sınıfı olusturmustuk 
                ve ekrana basmak için fonksiyonunu yazmıstık burada tekrar yazmaktansa for döngüsü her bir kitap için
                bir Kitap objesi olusturup onu ekrana yazıcak
                """
    def kitap_sorgula(self,isim):
        sorgu="SELECT * FROM kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitap=self.cursor.fetchall()
        if len(kitap)==0:
            print("Kütüphanede Böyle Bir Kitap Yok!!!")
        else:
            for i in kitap:
                kitabimiz=Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitabimiz)
    def kitap_ekle(self,kitap):
        sorgu="INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglati.commit()

    def kitap_sil(self,isim):
        sorgu1="SELECT * FROM kitaplar where isim=?"
        self.cursor.execute(sorgu1,(isim,))
        kitap=self.cursor.fetchall()
        if len(kitap)==0:
            return False
        else:
            sorgu = "DELETE FROM kitaplar where isim=?"
            self.cursor.execute(sorgu, (isim,))
            self.baglati.commit()
            return True
    def baski_yukselt(self,isim):
        sorgu = "SELECT * FROM kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitap=self.cursor.fetchall()
        if len(kitap) ==0:
            print("Kütüphanede Böyle Bir Kitap Yok!!!")
        else:
            baski=kitap[0][4]
            baski+=1
            sorgu2 = "UPDATE kitaplar set baskı_sayısı=? where isim=?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglati.commit()


































