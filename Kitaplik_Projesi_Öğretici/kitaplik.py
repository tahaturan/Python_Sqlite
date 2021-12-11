import sqlite3 #burada sqlite veri tabanımızı programımıza dahil ediyoruz
#ilk olarak bizim daha veritabanımız bulunmuyor biz veritabanımızı bu şekilde kurabiliriz
con = sqlite3.connect("kütüphane.db")
""" 
ilk olarak connection yani bağlantıyı simgeleyen bir değişken olusutoyoruz 'con' diye 
daha sonra sqlite3 ün içindeki sqlite3.connect() fonksiyomuzu kullanıyoruz burada bu fonksiyona ben bir tane sqlite 
veritabanı olusturup buna bağlmak istiyorum diyoruz kısaca 
daha sonra içine olusturmak istediğimiz veritabanının ismini giriyoruz
con = sqlite3.connect("kütüphane.db") şeklinde uzantısının .db olması lazım Dikkat!!
ve bu ifade eğer bulundugumuz dizinde Kütüphane diye bir veri tabanı yoksa bunu olusturacak ve bağlanıcak
eğer varsada sadece bağlantı işemini yapıcak yani yeni olustumucak 
ve kullandıgımız 'con' değişkenimiz bu bağlatıyı simgelicek
 """
#biz artık olusuturdugumuz veritabanı üstünde işlemler gerçekleştiricez bunun içinde bizim bir imleçe ihtiyacımız var
cursor=con.cursor()
""" burada demek istediğimiz ben bağlantımın üstünde bir imleç olusturmak istiyorum
ve bunu 'cursor' değişkenine atamak istiyorum
imlemizi olusturduk ve 'cursor' değişkenine tanımladık
artık database üzerindendeki bütüm işlemlerimizi bu 'cursor' üzerinden gerçekleştirebiliriz.
"""

#Tablo Oluşturma
#Tablo Olsutumak İçin bir fonksiyon yazalım
def tablo_olustur():
    #tablo olsuturmak için imlecimize tanımlı olan bir fonksiyonu kullanıcaz.
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (İsim TEXT,Yazar TEXT, Yayin_Evi TEXT,Sayfa_Sayisi INT)")
    con.commit() #işlemlerimizin gerçekleşmesi için eğer demezsek yukarıdaki sorgumuz çalısmayacaktır.
    """ 
    execute burada çalıstır anlamına geliyor ve bunun içine sql sorgusu girmemiz gerekiyor
    CREATE TABLE IF NOT EXISTS tablo_ismi şeklinde tablomuzu olusturabiliriz.
    buradaki IF NOT EXISTS ifadesi eğer öyle bir tablo yoksa olustur varsa hiç bişi yapma demek
    CREATE TABLE tablo_ismi şeklinde de olusturabilirdik fakat aynı isimde başka bir tablo varsa bu hata verecektir
    """
    #foksiyonumzu olusturduk

#Tabloya Veri Ekleme
def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES ('İstanbul Hatırası','Ahmet Ümit','Everst',561)")
    con.commit() #işmemizin veri tabanında çalıstırmak için yezdık yazmazsak çalısmaz
    """
    veri eklemeyi INSERT INTO tablo_ismi VALUES(tablomuzdaki alanalra göre sırasıyla ne eklemek istiyorsak yazıyoruz)
    NOT: INSERT INTO yu insert into şeklinde küçük harf ilede yazabilirdik bi sorun olusmazdı ama genelde büyük yazılır.
    """


#Kullanıcan Veri Almak İçin yapalım Birde
def veri_ekle_kullanici(kitap_isim,yazar_isim,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES (?,?,?,?)",(kitap_isim,yazar_isim,yayinevi,sayfa_sayisi))
    con.commit()
    """
    burada değerler içine yazdıgımız '?' leri aslında format metodu gibi 
    format metodunda nasıl {} parantez koyup sonuna .format(gelmesini istediğimiz değer) şeklinde yapıyorsak
    buda aynı mantık fonksiyonumuz  adet parametre alsın dedik ve VALUES kısmını (?,?,?,?),(1,2,3,4) şeklinde yazdık
    buradaki 1 değeri 1.soru işaretine 2 değeri 2.soru işaretine 3 değeri 3 e 4 değeri ise 4.soru işaretine atanıcak
    işte bu şekilde kullanıcan da veri alabiliriz veri tabanlarımız için
    """
#Verileri almak için bir fonksiyon yazalım
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall() #bu fonksiyon tablomuzdan aldıgımız tüm verileri bize dönücek ve liste şeklinde dönecek
                        #ondan bir listeye eşitledik bunuda
    print("********Kiptaplık Tablsounun Bilgileri*********")
    kitap=1
    for i in liste:
        print(kitap)
        print("İsim: {}\nYazar: {}\nYayınevi: {}\nSayfa Sayısı: {}".format(i[0],i[1],i[2],i[3]))
        print("------------------")
        kitap+=1
        """
        Burada kitaplık tablomuzdaki tüm verileri aldık ve daha düzenli ekrana yazılmasını için for döngüsüyle biçimlendirdik
        """
def verileri_al2(): #2.sorgu yöntemimizi test ediyoruz
    cursor.execute("SELECT İsim,Sayfa_Sayisi FROM kitaplik") #sadece İsim ve Sayfa sayısını almak istedik
    liste = cursor.fetchall() #yine aynı şekilde verilerimizi bize liste şeklinde dönecek
    for i in liste:
        print("isim: {} Sayfa Sayısı: {}".format(i[0],i[1]))

def verileri_al3(): #bir koşula bağlı olarak çekmek için
    cursor.execute("SELECT * FROM kitaplik where Yayin_Evi ='Doğan Kitap'")
    """
    burada demek istediğimiz yayın evi Doğan Kitap olanları getir sadece diyoruz
    """
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def verileri_guncelle(eski_yayin_evi,yeni_yayin_evi): #yayın evini güncellemek için yazdıgımız fonksiyon
    cursor.execute("UPDATE kitaplik set Yayin_Evi = ? where Yayin_Evi = ? ",(yeni_yayin_evi,eski_yayin_evi))
    """
    burada 2 tane parametre almasını söyledik fonksiyonumuza eski_yayın_evi ve yeni_yayin_evi diye
    fonksiyonumuzun amacı eski yayın evinin değerini giricez sonrada yeni yayın evi değerini giricez 
    sonrada eski yayın evi değerlerini yeni yayın evine girdiğimiz değer ile güncellicek
    işemin en sonunda tabloda bir sorgu çalıstıracagımız için commit() fonksiyonunu kullanıyoruz
    """
    con.commit()

def verileri_sil(yazar):#yazar isimine göre verileri silen fonksiyon
    cursor.execute("DELETE FROM kitaplik where Yazar = ?",(yazar,))
    """
    burada fonksiyonumuz bir yazar değeri alacak kullanıcan ve girilen yazar değerine göre tablodan o verileri silecek
    tekrardan tabloda güncelleme değişiklik olacagından dolayı commit() fonksiyonunu kulladık
    """
    con.commit()

# tablo_olustur() #tablo olusturmak için fonksiyonumuzu çağırdık
#veri_ekle() # verimizi eklemek için fonksiyonumuzu çağırdık
#Kullanıcan Veri Alma
"""
kitap_isim=input("Kitap İsimi: ")
yazar_isim=input("Yazar İsmi: ")
yayinevi=input("Yayinevi: ")
sayfa_sayisi=int(input("Sayfa Sayısı: "))
veri_ekle_kullanici(kitap_isim,yazar_isim,yayinevi,sayfa_sayisi)
print("Ekleme Başarılı...")
"""

#TABLODAN VERİLERİ ÇEKME
"""
Bunun için 3 tane sorgumuz var önce onları anlatayım
1-) SELECT * FROM tablo_ismi = Bu sorgumuz tablomuzdaki tüm verileri alır
2-) SELECT isim,yazar FROM tablo_ismi = Bu sorgu ise sadece belirttiğimiz alanları alır
3-) SELECT * FROM tablo_ismi where sayfa_saiyisi > 250 burada ise where ifadesi bir kosul belirtiyor
    ve o kosulu sağlayan verileri alamızı sağlar
"""
#1.sorgu yöntemi
"""
verileri_al()
"""
#2.sorgu yöntemi
"""
verileri_al2()
"""
#3.sorgu yöntemi
"""
verileri_al3()
"""

#TABLODAKİ VERİLERİ GÜNCELLEME
"""
'UPDATE tablo_ismi set değiştilcek_alan ='ne ile değiştircez' where değiştilcek_alan ='neyi değiştircez' şeklinde kullanılır'
"""
"""
eski_yayin=input("Değiştirmek İstediğiniz Yayın Evi: ")
yeni_yayin=input("Değiştireceğiniz Yeni Yayın Evi: ")
verileri_guncelle(eski_yayin,yeni_yayin)
"""


#VERİLERİ SİLME
"""
'DELETE FROM tablo_ismi where yazar='Ahmet Ümit' ' şeklinde kullanımı vardır 
"""
"""
yazar_ismi=input("Silmesini İstediğiniz Yazar: ")
verileri_sil(yazar_ismi)
print("Veriler Silindi...")
"""
#Diyelim ki datebase üzerinde işlemlerimiz bitti o zaman da dosya işlemlerindeki gibi bağlantımızı kapatmamız gerekiyor
con.close()

