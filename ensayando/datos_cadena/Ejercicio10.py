# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
# muestre por pantalla cada uno de los productos en una línea distinta.

# Solicitar al usuario que ingrese los productos de la cesta de compra separados por comas
productos_cesta_compra = input("Por favor digita lo que compraste separando cada producto con una coma: ")

# Separar los productos utilizando la coma como separador y crear una lista de productos
separar = productos_cesta_compra.split(",")#->> basicamente dice que entre coma se separe, si no pongo esto, me da los
#->> resultados ejemplo pan,carne =                  
# p
# a
# n
# ,

# Iterar sobre la lista de productos
# for producto in separar:

# Iterar sobre la lista de productos con enumerate
for enumeracion, producto_que_escribio_el_usuario in enumerate (separar, 1):
    # Utilizar strip para eliminar posibles espacios en blanco alrededor del producto
    print(f"{enumeracion}. {producto_que_escribio_el_usuario.strip()}")
