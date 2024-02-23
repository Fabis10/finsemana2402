# import re

# def quitar_letras(cadena):
#     # Utiliza una expresión regular para eliminar las letras
#     return re.sub('[a-zA-Z]', '', cadena)


# peso = input("¿Cuál es tu peso en kg? ")
# peso_procesado = ""
# for i in peso:
#     print(i)
#     if not i.isalpha():
#         peso_procesado += i
# print(peso_procesado)
# estatura = input("¿Cuál es tu estatura en metros? ")
# imc = round(float(peso)/float(estatura)**2,2)
# print("Tu índice de masa corporal es " + str(imc))

peso = float(input("Por favor digite su peso en kg "))
altura = float(input("Por favor digite su altura en metros "))
masa = round( peso / (altura **2), 2) #Se pone **2 porque es parte de la formula para dar la masa corporal
print("El indice de masa corporar es de ", masa)



# Peso = input("Por favor digite su peso en kg ")
# Estatura = input("Por favor digite su estatura en metros ")

# # Extrayendo la parte numérica de la cadena de peso
# peso_numerico = float(''.join(filter(str.isdigit, Peso)))

# # Extrayendo la parte numérica de la cadena de estatura
# estatura_numerica = float(''.join(filter(lambda x: x.isdigit() or x == '.', Estatura)))

# imc = round(peso_numerico / (estatura_numerica ** 2), 2)
# print("Tu índice de masa corporal es " + str(imc))
