# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:39:23 2022

@author: ummug
"""

#değişkenler

#değişken bir atıftır
#bilgisayarın hafızasında,o değere ait adresin ismidir

#atama(assignment) işlemi,yeni bir değişken yaratır ve ona bir değer atar

bilgi=("python adı, Monthy Python ve Kutsal Kase dizisinden gelir")
print(bilgi)

pi=3.1415
print(pi)

#değişken isimleri

#seçtiğiniz değişken ismi anlamlı, kendi adına konuşan isimler
#genelde snake_case isimlendirme kullanılır.

#exmp:
#ortalama_hiz
#sesli_harfler

#sayi ile başlayamaz
#boşluk karakteri olamaz
#özel karakter bulunduramaz
#keyword(anahtar kelime) içeremez

#Önemli : pythonda büyük-KÜÇÜK eşit değildir

#pythonda veri tipleri

#text(metin) tipi: str
#numerik tipler: int,float
#liste tipleri: list,tuple, range (listelerde görcez)
#ilişki tipi: dict (sözlük dictionaryde görcez)
#küme tipi: set 
#boolean tipi: bool

metin="bu bir metin tipidir"
type(metin)

tam_sayi= 16
type(tam_sayi)

kesirli_sayi= 4.6
print(type(kesirli_sayi))

type(kesirli_sayi)

liste= [1, 2, 3, 4, 5]
print(liste)
type(liste)

uclu= ('A', 'B', 'C')
print(uclu)
print(type)

onluk= range(10)
print(onluk)
type(onluk)

sozluk = {
    "ad" : "Musa" , 
    "soyad" : "Arda" ,
    "programlama" : "python"
    }
print(sozluk)
type(sozluk)

kume= set({1, 2, 3, 4, })

dogru= True
yanlis= False
print(dogru)
print(yanlis)
type(dogru)


