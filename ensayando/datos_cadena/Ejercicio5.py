# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase 
# invertida.

# Solicitar al usuario que introduzca una frase
frase = input("Introduzca una frase cualquiera: ")

# Invertir la frase utilizando el slicing con paso negativo
frase_invertida = frase[::-1]

# Imprimir la frase invertida
print(frase_invertida)


# frase = input("Introduce una frase: ")
# print(frase[::-1])