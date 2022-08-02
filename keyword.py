# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:59:02 2022

@author: ummug
"""

#keywords 

#pythondaki keywordsler, 'keyword' paketi içinde yer alır.
#import etmek 
#önce paketinizi import (içeri alma) edelim

import keyword

#şimdi keyword listesini alalım.
#bu listeyi bir degiskene atayalım

anahtar_kelimeler= keyword.kwlist

#simdi bu listeyi yazdir

print(anahtar_kelimeler)


#peki herhangi bir kelime python icin keyword mudur
#bunun icin keyword paketi icindeki iskeyword() metodunu kullanacaz

keyword.iskeyword('not')

