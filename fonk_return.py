# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:24:29 2022

@author: ummug
"""

#fonk değer dönmesi(return):
#fonk işlerini bitirdikten sonra geriye değer dönebilirler
#buna geriye değer "return" etmek denir 
#ve " return" anahtar kelimesi ile sağlanır 

#kendisine parametre olarak verilen bir sayının küpünü hesaplayıp geri dönen fonk
def cube(n):
    #sayinin kupunu hesapla
    n_kup= n**3
    
    #bu küp değerini geri dön 
    return n_kup

#şimdi fonk çağırdığımız zaman, fonk bize bir değer döner 
#o değeri alıp bir değişkene ataybilriz
sayi= 5
kup= cube(5)
print(kup)

n=4
dordun_kupu=cube(4)
print(dordun_kupu)

#birleşim - chain 

n=6
print(cube(n))

#geriye değer dönmeyen fonklara """ Void """ denir    

# docstring - fonksiyonun dokümantrasyonu :
#fonk hakkında yardım alalım

help(cube) #??? sor sıkıntılı 

#docstringi olan bir fonk yazalım
def ustel_hesapla(sayi, ust):
    """
       Bu fonk üstel hesaplama yapar
       parametreler: int sayi, int ust
       sonuc: verilen sayinin,verilen üstünü döner
    """
import math 
ustel=sayi**ustel
ustel_hesapla= math.pow(sayi, ust)  ####?????? sorun ne
print(ustel_hesapla)
help(ustel_hesapla)

#hazır metod ve attributelar
#pythonda nesnelerin hazır metodları ve hazır attribituteleri(ozellikleri) vardır
#bunlara kısa yollardan erişiilebilir

#docstring icin > _doc_
ustel_hesapla.__doc__(ustel_hesapla)
print(ustel_hesapla.__doc__(ustel_hesapla))

