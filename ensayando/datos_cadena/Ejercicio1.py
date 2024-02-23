# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como el número introducido.

# nombre = input("¿Cómo te llamas? ")
# n = input("Introduce un número entero: ")
# print((nombre + "\n") * int(n))



# Pedir el nombre del usuario y un número entero
nombre_usuario = input("Por favor, introduce tu nombre: ")
numero = int(input("Ahora, introduce un número entero: "))

# Imprimir el nombre del usuario tantas veces como el número ingresado
for nombre in range(numero):
    print(nombre_usuario)



