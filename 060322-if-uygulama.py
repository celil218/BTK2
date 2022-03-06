"""
Kullanıcı yıl sonu ortalaması girsin. Ortalama 85 üstü ise taktir, 70 üstü ise teşekkür,
bunların dışında ise hiçbirşey alamadınız desin.
"""
ortalama = int(input("Ortalamayı Giriniz:"))
if ortalama>=85:
    print("Taktir aldınız TEBRİKLER")
elif ortalama>=70:
    print("Teşekkür aldınız Tebrikler :)")
else:
    print("Hiçbir şey alamadınız bir daha ki sefere")