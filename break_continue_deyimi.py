# break ve continue deyimi 

# -- BREAK --
"""
bazen dongu tamamlanmadan cıkmamiz gerekir 
bunun icin - break - kullanilir
"""

#harfleri yazarken eger bosluk karakteri gorurse dnguden cik
metin = input("lutfen bir metin giriniz:")
for harf in metin:
    if harf == " ":
        break
    #bosluk degilse devam 
    print(harf)

#30 dan 100e kadar olamn sayilari yazalim
#eger sayi 11in karti ise yazip dongudn cikalim
for i in range(30,101):
    if i % 11 == 0:
        print(i)
        break 
    else:
        print(i)

    
# --- CONTINUE --- dongunun bir sonraki adimina atla
#bazen dongu icinde donerken bir kosula gore o andaki adımı atlayip 
#bir sonraki adima gecmemiz gerekir 

#orn 
#1 den 10a kadar olan cift sayiları continue kullanarak yazalim
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

#verilen metnn harlferini yaz, yazarken boslk karakteri gorursek yazma,bosluk disindakileri yaz
metin = input("lutfen bir metin giriniz:")
for harf in metin :
    if harf == " ":
        continue
    #bosluk degilse
    print(harf)

# NOT :
"""
BREAK : Direkt donguyu BİTİRİR.
CONTINUE : Bulundugu elemanı gecerek donguye DEVAM EDER.
"""