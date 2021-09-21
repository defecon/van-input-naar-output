invoerS = input('hoeveel small pizzas wilt u chappen')
aantalSmallPizzas = invoerS
PrijsSmallPizaas = 6.50
InvoerM = input('hoeveel medium pizzas wilt u chappen')
aantalMediumPizaas = InvoerM
prijsMediumPizzas = 9.50
invoerL = input ('hoeveel large pizzas wilt u chappen')
aantalLargePizzas = invoerL
prijsLargePizzas = 11.50
invoerFxl = input('hoeveel Familie XL pizzas wilt u chappen')
aantalFxlPizzas = invoerFxl
prijsFxlpizzas = 14.50

totaalprijs = int(invoerS) * float(PrijsSmallPizaas) + int(InvoerM) * float(prijsMediumPizzas) + int(invoerL) * float(prijsLargePizzas) + int(invoerFxl) * float(prijsFxlpizzas)


print(" bij de NewOminoos kosten de pizzas " + str(totaalprijs) + " voor de " + str(invoerS)
      + " small pizzas,  " + str(InvoerM) + " medium pizza,  " +   str(invoerL)  + " large pizzas,4  " + str(invoerFxl) + " familie XL pizza")





