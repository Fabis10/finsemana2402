vendido = int(input("Por favor escriba el numero de panes vendidos que no son del dia "))
precio_pan = 3.49
descuento_barra_pan = 0.60 #Descuento porcentaje
descuento = vendido * descuento_barra_pan
descuento_total =  vendido * precio_pan * (1 - descuento_barra_pan)
asdasd = vendido * 0.40
# print("El numero de panes vendidos que no son del dia son: " + str(vendido))
print("El precio habitual de una barra de pan es de: "+ str(precio_pan) + "€")
print("El descuento que se le hace a una barra de pan que no es del dia es de: " + str(descuento_barra_pan * 100) + "%")
print("El coste final es de " + str(round(descuento_total, 2)) + "€")




# barra_pan = 3.49
# descuento = 60
# venta = int(input("Escribe el número de barras vendidas que no son del dia: "))
# costo_sin_descuento = venta * barra_pan
# descuento_real = descuento / 100
# descuento_aplicado = costo_sin_descuento * descuento_real
# costo_con_descuento = costo_sin_descuento - descuento_aplicado

# print(f"El numero total de barras de pan vendidas que no son del dia son de {venta}")
# print(f"El precio habitual de una barra de pan es de {barra_pan}€")
# print(f"El descuento que se le hace por no ser del dia es de {descuento}%")
# print(f"El costo total sin descuento es de {costo_sin_descuento}€")
# print(f"El descuento aplicado es del {descuento_aplicado}€")
# print(f"El valor a pagar con descuento es de {costo_con_descuento}€")














# pan_no_vendido = int(input("Por favor, escriba el número de panes vendidos que no son del día: "))
# precio_pan = 3.49
# descuento = 0.60  # Porcentaje de descuento

# # Calcular el costo total con descuento
# coste_total = pan_no_vendido * precio_pan * (1 - descuento)

# print("El número de barras de pan vendidas que no son del día es " + str(pan_no_vendido))
# print("El precio habitual del pan es de: " + str(precio_pan) + "€") 
# print("El descuento que se le da a una barra de pan es de " + str(descuento * 100) + "%")
# print("El coste final total es de " + str(round(coste_total, 2)) + "€")



# pan = 3.49
# descuento = 60

# compra = int(input("Por favor escriba el numero de panes comprados que no son del dia: "))
# costo_pan = pan * compra
# descuento_pan = costo_pan * (descuento / 100)
# precio_final = costo_pan - descuento_pan

# format_costo_pan = "{:,.2f}".format(costo_pan).replace(",",".")
# format_descuento_pan = "{:,.2f}".format(descuento_pan).replace(",",".")
# format_precio_final = "{:,.2f}".format(precio_final).replace(",",".")

# print(f"El precio habitual de un pan es de {pan}€")
# print(f"El descuento que se le hace a el pan que no es del dia es del {descuento}%")
# print(f"El costo de su pedido sin descuento seria de {format_costo_pan}€")
# print(f"El descuento que se le hace a su pedido es de {format_descuento_pan}€")
# print(f"El precio final de su pedido es de {format_precio_final}€")



