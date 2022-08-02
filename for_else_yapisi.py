# FOR - ELSE YAPISI : 
"""
bazen bir for dongusunun düzgun tamamlanıp tamamlanmadıgını kontrol etmemiz gerekir 
eger for dongusu bir elemanı icin calismamissa, 'break' ifade cagrilmissa, o zaman duzguun calismamis demektir
bunun icin for- else yapisi kullanilir.
"""
#orn:
# 2 ile 10 arasindaki sayilari yaz,eger 7nin kati ise donguden cik
# duzgun calismissa "dongu duzgun calisti" diye yaz 
for i in range(2, 10):
    print(i)
    if i % 7 == 0:
        break 
else:
    print("dongu duzgun calisti")

#17 olursa:

for i in range(2, 10):
    print(i)
    if i % 17 == 0:
        break 
else:
    print("dongu duzgun calisti")

# dongu hic if'in icine girmedi "break" olmadı 
# yani duzgun calisti "else" yapisina ugramadı 


