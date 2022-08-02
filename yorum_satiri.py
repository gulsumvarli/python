# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:05:59 2022

@author: ummug
"""

#pythonda yorum satırı

#DERLEYİCİ: kaynak kodu,makine diline çeviren yazılımdır.(compiler)
#compiler,kod yazımı tamamlanınca tek seferde tüm kodu mamkine diline çevirir.

#YORUMLAYICI: kaynak kodu,makine diline çevirir.(interpreter)
#interpreter, kod yazılırken çevirir. satır satır makine çevirir.

#yorum satırı interpreter tarafından göz ardı edilen satır.
#interpreter kod satırı gördügünde çalıştırmaz.

#pythonda tek satır yorum "#" diyezle yapılır.

#örn
#ort hız=gidilen mesafe/ gecen süre
gidilen_mesafe=450 
gecen_sure= 6 

ort_hız= gidilen_mesafe/ gecen_sure 
print(ort_hız)

#pythonda çok satır yorum

"""
çok satır yorum
pythonda çok satır yorum 
iki adet 3'lü tırnak ile gösterilir.

bu örnekte olduğu gibi.
"""

cok_satir_metin= "satir 1\nsatir 2\nsatir 3"
print(cok_satir_metin)

print("selam sana\ndemir adam...")

"""
    bu satır 1
      bu satır 2
         bu satır 3

"""
#öncelik sırası: Parantez, Üstel, Bölme, Çarpma, Toplama, Çıkarma
# B E D M A S 

#string(metin) islemleri
#pythonda stringler hem tek tırnak hem de cift tırnak ile gösterilir.
#dikkat etmeniz gereken tırnakların tutarlı olması 

metin_cift= "bu cift tirnakli bir metindir"
print(metin_cift)

metin_tek= 'bu da tek tirnakli bir metindir'
print(metin_tek)

#eger her ikisini kullanmanız gerekir ise 
metin_iki_icinde_bir_tirnak= "ılgaz anadolu'nun sen yüce bir dagisin"
metin_tek_icinde_iki_tırnak= 'alice söyle bagirdi : "kos tavsan,kos"'

#pythonda metinler str de aritmetik islemler yapılamaz
#istisna tplama ve cıkarma yapilabilir

birinci="gunesli"
ikinci="gunler"

print(birinci + ikinci)

#carpma

print( birinci * 5)
