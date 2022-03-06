#Karşılaştırma Operatörleri
"""
Büyüktür = >
Küçüktür = <
Küçük Eşit = <=
Büyük Eşit = >=
Eşittir = ==
Eşit Değildir = !=
"""
cinsiyet = input("Bir harf giriniz:")

if cinsiyet=="e" or cinsiyet=="E": #or 2 şarttan biri doğru ise çalışır.
    print("Cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet=="k" or cinsiyet=="K": #2. veya daha sonraki şartları eklemek içim elif kullanılır.
    print("Cinsiyet olarak kadın girdiniz")
    print("Şuan da elif içinden mesaj veriyorum")
else: #Şartların dışında herhangi birşey girilirse çalışır
    print("Ben sana e yada k gir demedim mi?")
print("Şuan if dışındasın,if in bitti!")
