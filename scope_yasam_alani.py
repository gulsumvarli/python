# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:44:48 2022

@author: ummug
"""

#scope - yasam alanı:
#pythonda değişkenler tanımlandıkları alanda ve o alanın alt alanlarında geçerlidir
#buna "scope" yani yaşam alanı denir
#pythonda scope girinti(indent) ile tanımlanır

#fonskiyon scopu içinde bir değişken tanımlayalım
def scope():
    scope_degiskeni= 100
    print(scope_degiskeni)
scope()

#değişkenin scopeunun dışından ona ulaşmaya çalışırsak python interpreter hatası verir > NameError
#ama daha üstte yani " Global Scopeta tanımlanmış bir değişlene erişebilirsiniz

kisa= 4
uzun= 6

#en tepede tanımlanmış kısa ve uzun değişkenlerine tüm fonksiyonlar erişebilir

def cevre():
    dikdortgen_cevresi=2*( kisa*  uzun)
    print(dikdortgen_cevresi)
    
cevre()

#peki global scope içindeki bir değişkeni fonk içinden değiştirebilir miyiz?
#global scopeu değiştimreye calisan fonk:

def global_degisken_degistir():
    kisa=400
    print(kisa)
global_degisken_degistir()

print(kisa)

#fonk içinden değiştirmemize ragmen globaldeki değişkenin değeri değişmedi
#sebep: python globaldeki 'kisa' değişkenine dokunmadı
#siz fonk içinde kisa değişkenine atama yaptığınız anda python size yeni bir değişken tanımlar
#glıbaldeki değişkenin kopyasıdır.bu yeni kopya sadece fonksiyon scopeu içinde yaşar

#çözümü:
#global scopeteki değişkeni değiştirmek istiyotsak
#değişken başına "global" anahtar kelimesi yazıllır

#fonk tekrar çağıralım

def global_degisken_degistir():
    global kisa
    kisa=400
    print(kisa)
global_degisken_degistir()

print(kisa)
    