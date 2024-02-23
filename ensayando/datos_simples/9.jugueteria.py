# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y 
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será 
# enviado.

payaso = int(input("Escriba el total de payasos vendidos: "))
muñeca = int(input("Escriba el total de muñecas vendidas: "))
peso_payaso = 112
peso_muñeca = 75
suma_peso_payaso = payaso  * peso_payaso
suma_peso_muñeca = muñeca * peso_muñeca
peso_total_payaso = "{:,.0f}".format(suma_peso_payaso).replace(",", ".")#Para poner . en vez de , replace(",", ".")
peso_total_muñeca = "{:,.0f}".format(suma_peso_muñeca).replace(",", ".")#Para poner . en vez de , replace(",", ".")

print(f"El total de payasos vendidos es de {payaso} con un peso cada payaso de {peso_payaso} para un total de peso de {peso_total_payaso} gramos")
print(f"El total de muñecas vendidas es de {muñeca} con un peso cada muñeca de {peso_muñeca} para un total de peso de {peso_total_muñeca} gramos")


# payasos = int(input("Escriba el numero total de payasos vendidos en el ultimo pedido "))
# muñecas = int(input("Escriba el numero total de muñecas vendidas en el ultimo pedido "))
# peso_payasos = 112
# peso_muñecas = 75
# suma_payasos = payasos * peso_payasos
# suma_muñecas = muñecas * peso_muñecas
# print("El numero total de payaso vendidos fue de " + str(payasos) + " y el numero total de muñecas vendidas fue de " + str(muñecas))
# print("El peso total del paquete de los payasos es de " + str(payasos * peso_payasos) + "gramos")
# print("El peso total del paquete de las muñecas es de " + str(muñecas * peso_muñecas) + "gramos")



# # Definir los pesos de payasos y muñecas
# peso_payaso = 112
# peso_muñeca = 75

# # Calcular el peso total de los paquetes
# peso_total_payasos = num_payasos * peso_payaso
# peso_total_muñecas = num_muñecas * peso_muñeca

# # Mostrar los resultados al usuario
# print(f"El número total de payasos vendidos fue de {num_payasos} y el número total de muñecas vendidas fue de {num_muñecas}.")
# print(f"El peso total del paquete de payasos es de {peso_total_payasos} gramos.")
# print(f"El peso total del paquete de muñecas es de {peso_total_muñecas} gramos.")


