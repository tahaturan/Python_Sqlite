import time

from kütüphane import *
#burada binr önceki yazmıs oldugumuz kütüphane.py dosyamızı bir modül gibi kullanıyoruz aslında

print("""
**********************************
Kütüphane Programımıza Hoşgeldiniz.
----------------------------------
1-)Kitapları Göster
2-)Kitap Sorgulama
3-)Kitap Ekle
4-)Kitap Sil
5-)Baskı Yükselt
----------------------------------
Çıkmak için 'q' ya basınız....
************************************

""")
kutuphane = Kutuphane()

while True:
    islem=input("Yapmak İstediğiniz İşlemi Giriniz: ")
    if islem=="q" or islem=="Q":
        print("Kütüphane Programından Çıkış Yapılıyor...")
        time.sleep(1)
        print("Çıkış Başarılı...")
        break
    elif islem=="1":
        print("********Kitaplar*******")
        kutuphane.kitaplari_goster()
    elif islem=="2":
        kitap_ismi=input("Kitap İsmini Giriniz: ")
        print("{} Kitabı Sorgulanıyor...".format(kitap_ismi))
        time.sleep(2)
        kutuphane.kitap_sorgula(kitap_ismi)
    elif islem=="3":
        isim=input("Kitap İsmi: ")
        yazar=input("Yazarı: ")
        yayinevi=input("Yayınevi: ")
        tur=input("Türü: ")
        baski_sayisi=int(input("Baskı Sayısı: "))
        kitap=Kitap(isim,yazar,yayinevi,tur,baski_sayisi)
        print("Kitap Kütüphaneye Ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(kitap)
        print("Ekleme İşlemi Başarılı...")
    elif islem=="4":
        silinecek_kitap=input("Silmek İstediğiniz Kitap İsmi: ")
        if kutuphane.kitap_sil(silinecek_kitap)==True:
            print("Silme İşlemi Yapılıyor...")
            time.sleep(2)
            kutuphane.kitap_sil(silinecek_kitap)
            print("Silme İşlemi Başarılı...")
        else:
            print("Zaten {} Kitabı Kütüphanede Bulunmamakta...".format(silinecek_kitap))

    elif islem=="5":
        baski_yukseltilecek_kitap=input("Hangi Kitabın Baskını Yükseltmek İstersiniz: ")
        print("Baskı Yükseltme İşlemi Yapılıyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(baski_yukseltilecek_kitap)
        print("Baskı Yükseltme İşlemi Yapıldı...")
    else:
        print("Geçerli Bir İşlem Giriniz!!! ")

