invertir = float(input("Digite cual es la cantidad a invertir: "))
interes = float(input("Digite el interes: "))
años = int(input("Digite los años: "))
interes_interes = round(invertir * (interes / 100 + 1)  ** años, 2)
print(interes_interes)
print("Capital final es de: " + str(round (invertir * (interes / 100 +1) ** años, 2))) # este sirve y es mas 
# complejo, pero sirve
# print ("El total de las ganacias es de " + str(float(invertir) ))