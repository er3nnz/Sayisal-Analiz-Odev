from cmath import cos

#programa cos(x) değişkenini tanimlamak için math kütüphanesinden ekliyoruz

terimSayisi=int(input("Taylor Serisinin Eleman Sayisini Giriniz..."))

ekseniKestigiNokta=float(input("Verilen Fonksiyonun X eksenini Kestigi Noktayi Giriniz..."))

# verilen cosx ifadesinindeki x değeri için input aliyoruz ve gercek degeri sisteme tanimliyoruz
gercekDeger = cos(ekseniKestigiNokta)

#formuldeki sabitler icin değisken tanimliyoruz..
degisken=ekseniKestigiNokta

# Taylor Serisi Sonucu Ile Gercek Fonksiyonun Degerinin Farkini Tasidigimiz Degisken
yaklasikDeger=0

faktoriyel=1

#Hatanin sonucunu dondurecek olan deger
kesmeHatasi=0

i=0

while i<terimSayisi :

    i += 1

    j=1

    while j<terimSayisi :
        j*=2
        degisken=degisken**j

    while j < terimSayisi:
        j*=2
        faktoriyel*=j

  # Taylor Serisindeki (-1)^terimsayisi ifadesinden dolayi isaret kontrolu yapiyoruz

    if i % 2 != 0:
       yaklasikDeger = yaklasikDeger - degisken / faktoriyel
    else:
       yaklasikDeger = yaklasikDeger + degisken / faktoriyel

    taylorYaklasimi = gercekDeger - yaklasikDeger

    print('*********************************')
    print()

    # .real kütüphanesi ile cıktı aldıgımızda ekrana yansitilan 0j degerlerinden kurtuluyoruz..

    gercekSonuc1 = taylorYaklasimi.real
    gercekSonuc = gercekDeger.real

    # str tur donusumcusu ile değerlerimizin ciktisini aliyoruz

    print("Fonksiyonda Kullanilan X Degeri :"+str(ekseniKestigiNokta))
    print("Gercek Deger : " + str(gercekSonuc))
    print("Taylor Yaklasimi : " + str(gercekSonuc1))
    print("Aradaki Farkin Yaklasik Degeri : " + str(-yaklasikDeger))


    print()
    print('*********************************')







