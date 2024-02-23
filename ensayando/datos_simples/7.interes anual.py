
invertir = float(input("Por favor escriba la cantidad a invertir: "))
interes = float(input("Por favor escriba el interés anual: "))
años = int(input("Por favor escriba el número de años de la inversión: "))

# Fórmula corregida para el interés compuesto
capital_obtenido = invertir * (1 + (interes / 100)) ** años

# Formatear la salida con notación de coma para mejorar la legibilidad
capital_formateado = "{:,.2f}".format(capital_obtenido)

print(f"El valor que le corresponde por su inversión es de {capital_formateado}")





# peso = input("¿Cual es su peso en kg? ")
# estatura = input("¿Cual es su estatura? ")
# imc = round(float(peso) / float(estatura)**2,2)
# print("Su masa corporal es", str(imc))

# invertir = float(input("Por favor escriba el valor a invertir "))
# interes = float(input("Por favor escriba el interes solicitado "))
# años= int(input("Escriba los años que va a estar invertido la plata "))
# ganancia = str(round(invertir * (interes / 100 + 1) ** años, 2))
# print ("El capital final es de ", (ganancia))

# invertir = float(input("Por favor escriba el valor a invertir: "))
# interes = float(input("Por favor escriba el interés porcentual anual: "))
# años = int(input("Escriba el número de años que va a estar invertido el dinero: "))

# # Calcula la ganancia sin redondear
# ganancia = invertir * (1 + (interes / 100)) ** años

# # Redondea la ganancia antes de imprimir
# print("El capital final es de", round(ganancia, 2))



# cantidad = float(input("¿Cantidad a invertir "))
# interes = float(input("Interes procentual anual "))
# años = int(input("¿Años?"))
# print("Capital final: " + str(round(cantidad * (interes / 100 +1 ) ** años, 2)))