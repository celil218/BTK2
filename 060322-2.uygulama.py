#Kullanıcıdan, isim, soyisim, telefon numarası alarak bir listeye atayın.

bilgiler=[]#Boş liste tanımlar
isim = input("İsim")
soyisim = input("Soyisim")
telefon = input("Telefon Numarası")
bilgiler.append(isim)#Append listenin sonuna eleman ekler.
bilgiler.append(soyisim)
bilgiler.append(telefon)
print(bilgiler)
print("--------------------------")
print("İsim:", bilgiler[0])
print("Soyisim:", bilgiler[1])
print("Telefon Numarası:", bilgiler[2])
print("--------------------------")