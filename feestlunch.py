invoer1 = input('Hoeveel Croissantjes wilt u?')
aantalCroissantjes=invoer1
prijsCroissantjes=0.39
invoer2 = input('hoeveel stokbroden wilt u?')
aantalStokbroden=invoer2
prijsStokborden=2.78
invoer3 = input("hoeveel kortingsbonnen heeft u")
aantalkortingsbonnen=invoer3
prijsKortingsbonnen=0.50
totaalPrijs=int(invoer1)*prijsCroissantjes + int(invoer2) * prijsStokborden + int(invoer3) / prijsKortingsbonnen


print(" de feestlunch kost je bij de bakker " + str(totaalPrijs) + " voor de " + str(invoer1)
      + " croissantjes en de " + str(invoer2) + " stokbroden "
      + "als de" +   str(invoer3) +   "kortingsbonnen nog geldig zijn!")