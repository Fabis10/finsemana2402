# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
# el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan 
# con un solo carácter.

# Solicitar al usuario que digite su fecha de nacimiento en formato dd/mm/aaaa
fecha_nacimiento = input("Por favor digite su fecha de nacimiento de la siguiente manera: dd/mm/aaaa: ")

# Definir un diccionario de mapeo de número de mes a nombre de mes
nombres_meses = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

# Separar la fecha en día, mes y año
dia, mes, año = fecha_nacimiento.split("/")

# Asegurar que el día y el mes tengan dos dígitos
if len(dia) == 1:
    dia = "0" + dia
    
if len(mes) == 1:
    mes = "0" + mes

# Imprimir por pantalla el día, mes y año en un formato legible
print(f"Día: {dia}")
print(f"Mes: {int(mes)} {nombres_meses[mes]}")
print(f"Año: {año}")
