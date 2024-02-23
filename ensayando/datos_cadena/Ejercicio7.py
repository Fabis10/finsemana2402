# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

# Pedir al usuario que introduzca su correo electrónico
correo_usuario = input("Introduce tu correo electrónico: ")

#Dividir el correo electrónico en nombre_usuario y dominio, nombre queda con la primera parte de @ y dominio con la otra 
nombre_usuario, dominio = correo_usuario.split('@')

# Crear un nuevo correo electrónico con el mismo nombre de usuario y dominio "ceu.es"
nuevo_correo = f"{nombre_usuario}@ceu.es"

# Mostrar el nuevo correo electrónico
print(f"Tu nuevo correo electrónico es: {nuevo_correo}")






# correo = input("Por favor escriba su correo electronico: ")
# nombre_usuario, dominio = correo.split("@")


# nuevo_correo = f"{nombre_usuario}ceu.es"
# # nuevo_correo = f"{dominio}sadasdsadasd"
# print(f"Su correo electronico es: {nuevo_correo}")
