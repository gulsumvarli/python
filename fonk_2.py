# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:43:51 2022

@author: ummug
"""

#fonksiyonların birleşimi:
import math

derece=30
sinüs=math.sin(math.radians(derece))
print(sinüs)

print("adı: Ahmet")
print("yaşı: 24")
print("dili:pyth")

#bidaha yazdırmak istersek:

#parametresiz fonksiyon tanımla

def ogrenci_adi():
    print("adı: Ahmet")
def ogrenci_yasi():
    print("yaşı: 24")
def ogrenci_dili(): 
    print("dili:pyth")

#butun ogrenci bilgileri:
def ogrenci_bilgileri():
    ogrenci_adi()
    ogrenci_yasi()
    ogrenci_dili()        
ogrenci_bilgileri()

#öğrencinin adı ve soyadını ayrı ayrı yazmak istersek:
def ogrenci_ilk_adi():
    print("adı: cemile")
    
def ogrenci_soyadi():
    print("soyadi:aslan")
    
def ogrenci_adii():
    ogrenci_ilk_adi()
    ogrenci_soyadi()
    
ogrenci_adii()
ogrenci_bilgileri()

#işleme sırası - execution flow:
#python kodu ilk satırdan itibaren çalıştırmaya başlar
#ve aşağı doğru iner
#eğer bir fonksiyon çağrılmasına denk gelirse
#önce gider, o fonksiyonu çalıştırır,bitmesini bekler, geri döner 
#kaldığı yerden aşağı doğru çalışmaya devam eder.

    