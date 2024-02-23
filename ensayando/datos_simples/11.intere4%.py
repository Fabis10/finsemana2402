# inversion = float(input("¿Cual fue la suma que deposito como inversion? "))
# interes = 0.04
# balance1 = inversion * (1 + interes)
# print("El balance del primer año es de " + str(round(balance1, 2)))
# balance2 = balance1 * (1 + interes)
# print("El balance del segundo año es de " + str(round(balance2, 2)))
# balance3 = balance2 * (1 + interes) 
# print ("El balance del tercer año es de " + str(round(balance3, 2)))

# Sacar información
deposito = float(input("Escribe la cantidad de dinero a depositar: "))
interes = 0.04  # %

# Calcular y mostrar los ahorros para cada año
for i in range(1, 900):
    ganancia = deposito * (1 + interes) ** i
    ganancia_format = "{:,.2f}".format(ganancia).replace(",",".")
    print(f"La cantidad de ahorros tras el año {i} es de {ganancia_format}")


# #Sacar informacion
# deposito = float(input("Escribe la cantidad de dinero a depositar: "))
# interes = 0.04 #%

# #utilizacion bucle for
# for año in range (1,900):
#     deposito *= (1 + interes)
#     redondear_deposito = "{:,.2f}".format(deposito).replace(",",".")
#     print(f"La cantidad de ahorros tras el año {año} es de {redondear_deposito}")





# inversion = float(input("Escriba el valor total de la inversión: "))
# interes = 4 / 100

# balance1 = inversion * (1 + interes)
# print(f"La cantidad de ahorro tras el primer año es de {round(balance1, 2)}")

# balance2 = balance1 * (1 + interes)
# print(f"La cantidad de ahorro tras el segundo año es de {round(balance2, 2)}")

# balance3 = balance2 * (1 + interes)
# print(f"La cantidad de ahorro tras el tercer año es de {round(balance3, 2)}")

# balance4 = balance3 * (1 + interes)
# print(f"La cantidad de ahorro tras el cuarto año es de {round(balance4, 2)}")


# #Sacar informacion
# deposito = float(input("Escribe la cantidad de dinero a depositar: "))
# interes = 0.04 #%

# #utilizacion bucle for
# for año in range (1,900):
#     deposito *= (1 + interes)
#     redondear_deposito = "{:,.2f}".format(deposito).replace(",",".")
#     print(f"La cantidad de ahorros tras el año {año} es de {redondear_deposito}")













# inversion = float(input("Escriba el valor total de la inversion "))
# interes = 4 / 100
# balance1 = inversion * (1 + interes) 
# print ("La cantidad de ahorro tras la primera inversion es de " + str(balance1))
# balance2 = balance1 * (1 + interes)
# print("La cantidad de ahorro tras la segunda inversion es de " + str(balance2))
# balance3 = balance2 * (1 + interes)
# print("La cantidad de ahorro tras la tercera inversion es de " +  str(balance3))
# balance4 = balance3 * (1 + interes)
# print("La cantidad de ahrro tras la cuarta inversion es de " + str(balance4))
