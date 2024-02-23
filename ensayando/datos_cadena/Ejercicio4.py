# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del 
# país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un 
# número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


# telefonos =input("Por favor introduzca un numero de la siguiente manera: +xx-xxxxxxxx-xx: ")
# print(f"Su numero es {telefonos[4:-3]}")


# Solicitar al usuario que introduzca un número de teléfono en un formato específico
telefonos = input("Por favor introduzca un numero de la siguiente manera: +xx-xxxxxxx-xx: ")

# Dividir el número de teléfono utilizando el guion como separador
modi_telefonos = telefonos.split("-")

# Extraer la parte del número de teléfono ubicada en el índice 1 después de dividir
sacar_parte_del_numero = modi_telefonos[1]

# Imprimir la parte extraída del número de teléfono
print(sacar_parte_del_numero)





# tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
# print('El número de teléfono es ', tel[4:-3])
# # El número de teléfono es  913724710



# # Solicitar al usuario que ingrese el número de teléfono con el formato +34-913724710-56
# telefono = input("Por favor, ingrese el número de teléfono en el formato +34-XXXXXXXXX-XX: ")

# # Separar el número de teléfono en partes usando el guión "-"
# partes = telefono.split("-")

# # Extraer el número sin el prefijo y la extensión
# numero_sin_prefijo_extension = partes[1]

# # Mostrar el resultado
# print(f"El número de teléfono sin el prefijo y la extensión es: {numero_sin_prefijo_extension}")
