    # Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por 
    # pantalla la misma frase pero con la vocal introducida en mayúscula.

# frase = input("Escribe una frase: ")
# vocal = input("Escribe una vocal (a,e,i,o,u): ")
# print(f"Su frase es {frase} con la vocal {vocal.upper()}")

#ESTA SI SE INTRODUCE UNA VOCAL QUE NO ES, SOLO PIDE LA VOCAL Y NO VOLVER A ESCRIBIR LA FRASE

# Bucle para solicitar una frase sin números
while True:
    # Solicitar al usuario que escriba una frase
    frase = input("Por favor escriba una frase: ")
    
    # Verificar si la frase contiene dígitos
    if any(char.isdigit() for char in frase):
        # Si la frase contiene dígitos, imprimir un mensaje de error y continuar solicitando una nueva frase
        print("Por favor, escribe una frase sin números.")
    else:
        # Si la frase no contiene dígitos, salir del bucle y continuar con el siguiente bloque de código
        break

# Bucle para solicitar una vocal y realizar la sustitución
while True:
    # Solicitar al usuario que ingrese una vocal
    vocal = input("Por favor ingrese una vocal: ")
    
    # Convertir la vocal a minúsculas para realizar una comparación insensible a mayúsculas y minúsculas
    vocal_replace = vocal.lower()
    
    # Verificar si la vocal es una de las vocales permitidas
    if vocal_replace in "aeiou":
        # Si la vocal es válida, realizar la sustitución y mostrar la nueva frase
        nueva_frase = frase.replace(vocal_replace, vocal.upper())
        print(nueva_frase)
        
        # Salir del bucle
        break
    else:
        # Si la vocal no es válida, imprimir un mensaje de error y continuar solicitando una nueva vocal
        print("Por favor, escriba una vocal.")


# while True:  
#     frase = input("Escriba una frase: ")
    
#     if any (char.isdigit() for char in frase):
#         print("La frase no debe conteneder numeros.")
#     else: 
#         break
    
# while True: 
#     vocal = input("Escriba una vocal: ")
#     vocal_replace = vocal.lower()

#     if vocal_replace in "aeiou":
#         nueva_frase = frase.replace(vocal_replace, vocal.upper())
#         print(f"Su frase es: {nueva_frase}")
#         break
#     else:
#         print("Por favor introduzca una vocal válida.")
        


# SI SE DA UNA LETRA QUE NO ES VOCAL, ESTA PIDE TODA LA FRASE DE NUEVO Y LA VOCAL.
# while True:
#     frase = input("introduce una frase: ")
#     vocal = input("Introduce una vocal: ")
#     vocal_replacee = vocal.lower()
#     if vocal.lower() in "aeiou":
#         nueva_frase = frase.replace(vocal_replacee, vocal.upper())
#         print(f"Su frase es {nueva_frase}")
#         break
#     else:
#         print("Por favor escriba una vocal.")
       






# # Pedir al usuario que introduzca una frase
# frase = input("Introduce una frase: ")

# # Pedir al usuario que introduzca una vocal
# vocal = input("Introduce una vocal: ")

# # Verificar que la entrada sea una vocal
# if vocal.lower() in 'aeiou':
#     # Reemplazar la vocal en la frase con su versión en mayúscula
#     nueva_frase = frase.replace(vocal, vocal.upper())

#     # Mostrar la nueva frase con la vocal en mayúscula
#     print("La nueva frase con la vocal en mayúscula es:", nueva_frase)
# else:
#     print("Por favor, introduce una vocal válida.")
