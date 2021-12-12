import sqlite3
import time

con = sqlite3.connect("kullanici.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS kullanici (İsim TEXT,Soyisim TEXT, Kullanici_Adi TEXT,Sifre TEXT,Email TEXT)")
con.commit()
class Kullanici():
    def __init__(self,isim="Null",soyisim="Null", kullanici_adi="Null",sifre="Null",email="Null"):
        self.isim=isim
        self.soyisim=soyisim
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre
        self.email=email

    def tablo_olustur(self):
        pass
    def kayit(self):
        con.execute("INSERT INTO kullanici VALUES (?,?,?,?,?)",(self.isim,self.soyisim,self.kullanici_adi,self.sifre,self.email))
        con.commit()
    def giris(self,kullanici_adi,sifre):
        cursor.execute("SELECT Kullanici_Adi,Sifre FROM kullanici where Kullanici_Adi=? and Sifre=?",(kullanici_adi,sifre))
        liste=cursor.fetchall()
        for i in liste:
            if i[0] == kullanici_adi and i[1] == sifre:
                print("Giriş Başarılı")
                return True
            elif i[0] == kullanici_adi and i[1] != sifre:
                print("Şifreniz Yanlış")
            elif i[0] != kullanici_adi and i[1]==sifre:
                print("Kullanıcı Adı Yanlış")
            else:
                print("Kullanıcı Adı Ve Şifre Yanlış")
    def bilgileri_al(self):
        cursor.execute("SELECT * FROM kullanici")
        veriler=cursor.fetchall()
        kullanici_sayisi=1
        for i in veriler:
            time.sleep(3)
            print("Kullanıcı: {}".format(kullanici_sayisi))
            print("İsim: {}\nSoyisim: {}\nKullanıcı Adı: {}\nSifre: {}\nEmail: {}".format(i[0],i[1],i[2],i[3],i[4]))
            print("-------------------------")
            kullanici_sayisi+=1
    def kullanici_adi_guncelle(self,yeni_kullanici_adi,eski_kullanici_adi):
        cursor.execute("UPDATE kullanici set Kullanici_Adi =? where Kullanici_Adi=?",(yeni_kullanici_adi,eski_kullanici_adi))
        con.commit()
    def sifre_guncelle(self,yeni_sifre,eski_sifre):
        cursor.execute("UPDATE kullanici set Sifre =? where Sifre=?",(yeni_sifre,eski_sifre))
        con.commit()
    def kayit_sil(self,kullanici_adi):
        cursor.execute("DELETE FROM kullanici where Kullanici_Adi =?",(kullanici_adi,))
        con.commit()



kullanici=Kullanici()
while True:
    print("""
    *********ANASAYFA********
    ----------------------
    1-)Giriş Yap
    2-)Kayıt Ol
    3-)Çıkış
    ----------------------
    """)
    try:
        islem=int(input("Yapmak İstediğiniz İşlem: "))
        if islem==1:
            kullanici_adi = input("Kulllanıcı Adınızı Giriniz: ")
            sifre = input("Şifrenizi Griniz: ")
            print("Giriş Yapılıyor...")
            time.sleep(1)
            giris =kullanici.giris(kullanici_adi,sifre)
            if giris == True:
                print("*****HOŞGELDİNİZ*******")
                while True:
                    try:
                        print("""
                        *******İşlemler********
                        -----------------------
                        1-)Tüm Kullanıcı Bilgilerini Al
                        2-)Kullanıcı Adı Değiştir
                        3-)Şifre Değiştir
                        4-)Kaydı Sil
                        5-)Ana Menü
                        """)
                        kullanici_islem=int(input("Yapmak İstediğiniz İşlem: "))
                        if kullanici_islem ==1:
                            print("Bilgiler Ekrana Yazılıyor...")
                            time.sleep(1)
                            kullanici.bilgileri_al()
                        elif kullanici_islem==2:
                            eski_kullanici_adi=input("Eski Kullanıcı Adınızı Giriniz: ")
                            yeni_kullanici_adi=input("Yeni Kullanıcı Adınızı Giriniz: ")
                            kullanici.kullanici_adi_guncelle(yeni_kullanici_adi,eski_kullanici_adi)
                            print("Kullanıcı Adı Güncelleniyor...")
                            time.sleep(1)
                            print("Güncelleme Başarılı")
                        elif kullanici_islem==3:
                            eski_sifre=input("Eski Şifrenizi Giriniz: ")
                            yeni_sifre = input("Yeni Şifrenizi Giriniz: ")
                            kullanici.sifre_guncelle(yeni_sifre,eski_sifre)
                            print("Şifre Güncelleniyor...")
                            time.sleep(1)
                            print("Güncelleme Başarılı")
                        elif kullanici_islem==4:
                            print("Silme İşlemi Yaplıyor...")
                            kullanici.kayit_sil(kullanici_adi)
                            time.sleep(1)
                            print("Silme İşlemi Başarılı!!!")
                            break
                        elif kullanici_islem==5:
                            print("Ana Menüye Dönülüyor...")
                            time.sleep(1)
                            break
                        else:
                            print("Geçerli Bir İşlem Giriniz!!!")
                    except ValueError:
                        print("Geçerli Bir İşlem Giriniz!!!")

        elif islem==2:
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            email = input("Email Adresini Giriniz: ")
            kullanici_adi = input("Kulllanıcı Adınızı Giriniz: ")
            sifre = input("Şifrenizi Griniz: ")
            kullanici=Kullanici(isim,soyisim,kullanici_adi,sifre,email).kayit()
            print("Kayıt Yapılıyor...")
            time.sleep(1)
            print("Kayıt Başarılı")

        elif islem==3:
            print("Uygulamadan Çıkış Yapılıyor...")
            time.sleep(1)
            print("Çıkıs Başarılı Tekrar Bekleriz :))")
            break
        else:
            print("Geçerli Bir İşlem Giriniz!!!")

    except ValueError:
        print("Geçerli Bir İşlem Giriniz!!!")

con.close()
