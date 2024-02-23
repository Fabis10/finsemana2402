# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por 
# pantalla el número de euros y el número de céntimos del precio introducido.




# precio = input("Introduce el precio del producto con dos decimales:  ")
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

# Solicitar al usuario que introduzca el precio del producto en euros con dos decimales
precio = input("Introduce el precio del producto en euros con dos decimales: ")

# Verificar que la entrada sea válida (contiene un punto decimal y es un número)
if '.' in precio and precio.replace('.', '').isdigit():
    # Dividir el precio en la parte de euros y la parte de centavos
    euros, centavos = precio.split('.')
    
    # Imprimir el precio en un formato legible
    print(f"{euros} euros con {centavos} centavos")
else:
    # Si la entrada no es válida, imprimir un mensaje de error
    print("Por favor, introduce un precio válido con dos decimales.")
