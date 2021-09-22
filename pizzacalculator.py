invoerS = int(input('hoeveel small pizzas wilt u chappen : '))
aantalSmallPizzas = invoerS
PrijsSmallPizaas = 6.50
InvoerM = int(input('hoeveel medium pizzas wilt u chappen : '))
aantalMediumPizaas = InvoerM
prijsMediumPizzas = 9.50
invoerL = int(input ('hoeveel large pizzas wilt u chappen : '))
aantalLargePizzas = invoerL
prijsLargePizzas = 11.50
invoerFxl = int(input('hoeveel Familie XL pizzas wilt u chappen : '))
aantalFxlPizzas = invoerFxl
prijsFxlpizzas = 14.50

totaalprijs = int(invoerS) * float(PrijsSmallPizaas) + int(InvoerM) * float(prijsMediumPizzas) + int(invoerL) * float(prijsLargePizzas) + int(invoerFxl) * float(prijsFxlpizzas)


print(f"{invoerS}x small pizza's : €{PrijsSmallPizaas*aantalSmallPizzas} : ")
print(f"{InvoerM}x medium pizza's : €{prijsMediumPizzas*aantalMediumPizaas} : ")
print(f"{aantalLargePizzas}x large pizza's (€{prijsLargePizzas*aantalLargePizzas} : ")
print(f"{aantalFxlPizzas}x familie XL pizza's (€{prijsFxlpizzas*aantalFxlPizzas} : ")

print(" bij de NewOminoos kosten de pizzas " + str(totaalprijs) + " voor de " + str(invoerS)
      + " small pizzas,  " + str(InvoerM) + " medium pizza,  " +   str(invoerL)  + " large pizzas,4  " + str(invoerFxl) + " familie XL pizza")





