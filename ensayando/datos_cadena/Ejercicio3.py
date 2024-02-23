# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
# muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número 
# de letras que tienen el nombre.

# Solicitar al usuario que escriba su nombre
nombre = input("Por favor escriba su nombre: ")

# Definir el número máximo de intentos
intentos_maximos = 5

# Inicializar el contador de intentos
intentos = 0

# Iniciar un bucle para limitar el número de intentos
while intentos < intentos_maximos:
    # Verificar si el nombre contiene dígitos
    if any(char.isdigit() for char in nombre):
        # Si el nombre contiene dígitos, imprimir un mensaje de error y solicitar el nombre nuevamente
        print("Por favor, escriba un nombre sin números.")
        nombre = input("Por favor, escriba su nombre nuevamente: ")
        intentos += 1  # Incrementar el contador de intentos
    else:
        # Si el nombre no contiene dígitos, imprimir algunas características del nombre y salir del bucle
        print(f"Su nombre en mayúsculas es {nombre.upper()}")
        print(f"Su nombre tiene un total de {len(nombre)} caracteres")  # La función len cuenta la longitud de la cadena
        break







# # nombre_mayusculas = nombre.upper()
# # numero_de_letras = len(nombre)
# # print(f"Su nombre en mayusculas es {nombre_mayusculas} con un total de digitos de {numero_de_letras}")
# while True:
#     nombre = input("Por favor escriba su nombre completo: ")
#     if not any (char.isdigit() for char in nombre):
#         print(f"Su nombre completo en mayusculas es {nombre.upper()}")
#         print(f"El numero total de su nombres es de {len(nombre)}")
#         break
#     else:
#         print (f"Weon, pero escribe un nombre sin numeros.")










