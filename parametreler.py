# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:30:00 2022

@author: ummug
"""

#parametreler - argümanlar :
#çoğu zaman fonksiynlar parametrelere ihtiyaç duyarlar.
#parametre fonksiyonun çalışması için kendisine iletilen girdilerdir
#parametreler fonksiyon çağrılırken iletilitr.

#diyelim ki kendisine iletilen sayının karesini alan bir fonksiyon yazmak istiyoruz
def karesini_yaz(sayi):
    
    #sayının karesini al 
    karesi= sayi**2
    
    #sayinin karesini yaz
    print(karesi)

#şimdi bu fonksiyonun parametre ile çağıralım 
karesini_yaz(6)
karesini_yaz(8)

#iki parametre alan bir fonk tanımlayalım
#iki parametre: kisa_kenar, uzun_kenar
# fonl diktdörtgn alanını hesaplayalım 

def dikdortgen_alani_hesapla(kisa_kenar, uzun_kenar):
    dikdortgen_alani = kisa_kenar * uzun_kenar
    print(dikdortgen_alani)
    
dikdortgen_alani_hesapla(4, 6)

#örnek
#daha önce tanımladığınız ogrenci_bilgileri fonksiyonunu bu sefer parametrik yapalım
def ogrenci_ilk_adi(ilk_adi):
    print("adı: klark")
def ogrenci_soyadi(soyadi):
    print("soyadı: kent")
def ogrenci_yasi(yas):
    print("yaşı: 28")
def ogrenci_dili(dil):
    print("kullandığı dil: python")


def ogrenci_bilgileri(ilk_adi, soyadi, yas, dil):
    ogrenci_ilk_adi(ilk_adi)
    ogrenci_soyadi(soyadi)
    ogrenci_yasi(yas)
    ogrenci_dili(dil)

ogrenci_bilgileri("klark", "kent", "28", "python")
    
    

    