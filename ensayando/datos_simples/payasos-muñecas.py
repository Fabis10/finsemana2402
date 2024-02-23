# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y 
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que 
# será enviado.
pedido_payasos = int(input("Por favor digite el numero de payasos vendidos en el ultimo pedido: "))
pedido_muñecas = int(input("Por favor digite el numero de muñecas vendidos en el ultimo pedido: "))
peso_payaso = pedido_payasos * 112 
peso_muñeca = pedido_muñecas * 75
print("El peso total del paquete de payasos es de "+ str(peso_payaso) + "kg" + " y el peso total del paquete de muñecas es de " + str(peso_muñeca) +"kg")
print("El peso total de ambos paquetes es de " + str(peso_payaso + peso_muñeca) + "kg")