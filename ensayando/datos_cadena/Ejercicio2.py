# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
# nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
# otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
# combinando mayúsculas y minúsculas como quiera.


# Iniciar un bucle infinito para solicitar el nombre del usuario
while True:
    # Pedir al usuario que escriba su nombre completo
    nombre = input("Por favor, escribe tu nombre completo: ")

    # Verificar si el nombre contiene algún dígito (número)
    if not any(char.isdigit() for char in nombre):
        # Si el nombre no contiene dígitos, imprimir varias formas de representar el nombre
        print(f"Su nombre completo en minúsculas es {nombre.lower()}")
        print(f"Su nombre completo en mayúsculas es {nombre.upper()}")
        print(f"Su nombre completo con las primeras letras en mayúsculas es {nombre.title()}")
        
        # Salir del bucle
        break
    else:
        # Si el nombre contiene dígitos, imprimir un mensaje de error y volver a solicitar el nombre
        print("Weon, escribe un nombre sin números. ¡No jodas!")





# nombre = input("Por favor digite su nombre completo: ")
# print(f"Su nombre completo en minusculas es: {nombre.lower()}")
# print(f"Su nombre completo en mayusculases es: {nombre.upper()}")
# print(f"Su nombre con la primera letra en mayuscula es: {nombre.title()}")


# intentos_maximos = 5
# intentos = 0

# while intentos < intentos_maximos:
#     nombre = input("Por favor, digite su nombre completo: ")
    
#     # Verificar si hay algún número en el nombre
#     if not any(char.isdigit() for char in nombre): #if not any -> si es verdadeor lo vuelve negativo y viceversa 
#         print(f"Su nombre completo en minúsculas es: {nombre.lower()}")
#         print(f"Su nombre completo en mayúsculas es: {nombre.upper()}")
#         print(f"Su nombre con la primera letra en mayúscula es: {nombre.title()}")
#         break
#     else: # -> si no 
#         intentos += 1
#         print("Por favor, ingrese un nombre sin números.") # -> si es verdadera
        

# Mostrar el nombre en diferentes formas    


#ejemplo de lista 
# mi_lista = [False, False, False, False]
# resultado = any(mi_lista)
# print(resultado)  # Salida: True (ya que al menos un elemento es True)






# nombre_completo = input("Por favor, introduce tu nombre completo: ")

# # Mostrar el nombre completo en diferentes formas
# print("1. Nombre completo en minúsculas:", nombre_completo.lower())
# print("2. Nombre completo en mayúsculas:", nombre_completo.upper())

# # Dividir el nombre en partes (nombre, apellido1, apellido2, ...)
# partes_nombre = nombre_completo.split()

# # Formatear y mostrar el nombre con la primera letra en mayúscula de cada parte
# nombre_formateado = ' '.join([parte.capitalize() for parte in partes_nombre])
# print("3. Nombre con la primera letra en mayúscula de cada parte:", nombre_formateado)





