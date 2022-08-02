# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:40:00 2022

@author: ummug
"""

#fonksiyonlar
#belli bir işlevi yerine getirmek içi yazılmış özel kod parçasıdır
#çağrıldığı zama çalışır
#isteğe göre parametre(girdi) alabilirler
#isteğe göre,geriye bir değer dönebilirler

#fonksiyon çağırma
#fonksiyon_adi()

#parametre ile fonksiyon çağırma
#fonksiyon_adi(parametre_1,parametre_2)

#fonksiyonlar kod tekrarını önler

#matematik fonksiyonlar (math modülü)))

# modül "birbiriyle ilgili fonksiyonların ve dsyaları bir arada tutan dosya kümeleridir

#math nasil içeri alınr
import math 

#math modülünü görelim
print(math)

#pythda help özelliği vardır
help(math)

#math modülü içindeki bir fonksiyonu "." ile çağrılır
math.pi
print(math.pi)

#examp
#yarıçapı 1 cm çember çevresi?
#cevre=  2 * pi * r 
r =  10
cevre=  2 * math.pi * r 
print(cevre)

# 30 derece sinüsü

derece= 30
radyan= math.radians(derece)
print(radyan)

#fonksiyonların birleşimi 
import math
derece= 30
sinus= math.sin(math.radians(derece))
print(sinus)

#chain "fonksiyonları zincirlemek"

#fonksiyon tanımlamak
#tanımlamak "definition

#parametresiz fonksiyon tanımlamak
def fonksiyon_adi():
    print("ilk fonksiyon")
    
#fonksiyonu çağırmak 
fonksiyon_adi()

#indent "pyth de indent yapısı ile kod bölümleridir
#indent "tab" , "4 space"


