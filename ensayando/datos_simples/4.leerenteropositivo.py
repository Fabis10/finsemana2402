#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta  n . La suma de los  n  
# primeros enteros positivos puede ser calculada de la siguiente forma:
#suma=n(n+1)2

n = int(input("Escriba un numero entero positivo "))
suma = n * (n + 1) / 2
print ("La suma de los primeros enteros positivos desde 1 hasta " + str(n) + " es " + str(suma))

# n = int(input("Escribe un numero entero positivo "))
# suma = n *(n + 1) / 2 
# inicio = 1
# print ("La suma desde" + str(inicio) + " hasta " + str(n) + " es " + str(suma))
