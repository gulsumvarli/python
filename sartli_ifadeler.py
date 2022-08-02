
#sartli ifadeler
#bu bölümde sartli ifadleer ya da if else yapilarını göreceğiz
#sartli ifade bir yargidir 
#true ya da false olan ifadelerdir
#mantiksal operatörler ile ifade edilir.

#sart operatorleri

# x == y >> x y'ye esit midir 
# x !=   >> x y'ye esit degil midir

from cgi import print_arguments
from re import A, X
from tkinter import N
from tkinter.tix import Tree
x=12
y=8
print("x == y :", X == y)

#mantiksal operatorler

#and : ve(her iki tarafda True ise sonuc true, taraflardan biri False ise sonuc False)
#or : veya(her iji taraftan biri True ise True )

print(True and True)

a=6 == 6 
print(a)

b=6 == 8 
print(b)

#and 
print("....and....")
print("{0} and {1}: {2}".format(a, b, a and b))
print("{0} or  {1}: {2}".format(a, b, a or b))

#if yapisi
# bilgisayar programlarında yukarıdan asagi dogru calisir
# siz belli sartlara gore, farkli bolumleri calistirmak isteyebilirsiniz,kodu dallandırmak

x = 7 
if(X > 0):
    print("{} sayisi 0'dan buyuktur".format(x))

x = 9
if (x >0 and x <= 10):
    print("{} sayisi 0'dan buyuk ve 10'dan kucuk esittir".format(x))

#else yapisi
#cogu zaman bir kosul yerine geldgi ya da gelmedigi zaman bunun alternatifleri lazim olur
# bu durumlar için if blogundan sonra else blogu calistirilir

#eger x sayisi cift ise ekrana cift yaz
#degilse tek yaz

tek_mi_cift_mi=int(input("lütfen bir sayi giriniz:"))
if (tek_mi_cift_mi %2== 0):
    print("girdiğiniz sayi cift sayidir")
else:
    print("sayi tektir")

#elif yapisi
#2 den fazla durumlarda kullanilir 
#if-elif-else

def pozitif_mi():
    n= int(input("lütfen sayi giriniz:"))
    if (n>0):
        print("pozitif sayi")
    elif (n==0):
        print("notr")
    else:
        print("negatif")
pozitif_mi()

#kullanicidan 1-7 arası sayi iste 
#fonk bu sayiya gore hangi gun olduguna karar verip kullaniciya donsun

def haftanin_gunleri():
    gun_numarasi=int(input("lütfen bir gün numarasi gir:(1 ile 7 arasında)"))
    gun_adi = ""
    if gun_numarasi==1:
        print("pazartesi")
    elif gun_numarasi==2:
        print("salı")
    elif gun_numarasi==3:
        print("cars")
    elif gun_numarasi==4:
        print("pers")
    elif gun_numarasi==5:
        print("cuma")
    elif gun_numarasi==6:
        print("cumartesi")
    elif gun_numarasi==7:
        print("pazar")
    else:
        print("1 ile 7 arası sayi girmedniz") 
    return gun_adi    
haftanin_gunleri()

#iç içe -nested- şartlı ifadeler:
# NOT operatoru
#bu yargıyı true veya false tersine cevirmek icin kullanilir
#degilse gibi okunabilir

#not ile if kullanimi
if not x == 5:
    print("x 5'e esit degildir")
else:
    print("x 5'e esittir")

#onemli not: ifler içeri girmek için trueya ihtiyac duyarlar 
#diyelim ki bir kosul saglandiktan sonra on kosul icinde baska bir kosula bakmamız laızm 
#bunun icin iceride tekrar bir kosul yapisi kurmamız laızm
#ic ice kosul yapisidir( NESTED )

x=300
y=30
if x == y:
    print("x ile y aynı")
else:
    if x > y:
        print("x, yden buyuktur")
    #gereksiz kod REDUNTANT
    #elif x == y:
    #print("x ile y ayni")
    else:
        print("x yden kucuktur")

#örn
#kullanicidan bir sayi isteyin
# bu sayi 10dan kucuktur 
  #tek ise 10 dan kucuk tek
  #cift ise 10dan kucuk cift 
#sayi 10dan buyukse 
  #tek - tek
  #cift - cift 

def sayi_tek_mi():
    sayi=int(input("sayi:"))
    if sayi>10:
        if sayi %2 == 0:
            print("sayi 10dan buyuk ve cifttir")
        else:
           print("sayi 10dan buyuk ve tek")
    elif sayi<10:
         if sayi %2 == 1:
            print("sayi 10dan kucuk ve tek")
    else :
            print("sayi 10dan kucuk ve cift")
sayi_tek_mi()

# RECURSION - Kendi kendini cagirmak
#bir fonk baska fonk cagirılabildigi gb kendisi de cagirabilir
#buna "RECURSION" denir 

#örn
#verilen bir sayidan geriye dogru 0'a kadar sayan fonk
#NOT: recursionlarda "durma kosulu" cok onemlidir.eger fonk nerede duracagini bilmezse sonsuz donguye girer

def geri_say(n):
    #ilk once durma kosulunu yazmamiz lazim
    if n<0:
        print("program sonu")
    else:
        print(n)
        geri_say(n-1)
geri_say(50)

#simdi kendisine verilen metni geriye dogru syaan fonk
def metni_yaz(metin, n):
    if n <= 0:
        return
    else:
        print(metin)
        metni_yaz(metin, n-1)
metni_yaz("machine learning", 5)

def metni_yaz(metin, n):
    if n <= 0:
        return
    else:
        print("{0} : {1}".format(n, metin))
        metni_yaz(metin, n-1)
metni_yaz("mazhine learning")