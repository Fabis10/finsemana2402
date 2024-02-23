peso = float(input("Digite su peso en kg: "))
estatura = float(input("Digite su estatura en metros: "))
masa_corporal = round(peso / estatura **2) #round para que me redondee el resultado y no me diga 0.12323 si no 0
print("Su masa corporal es de ", masa_corporal)

# peso = input("¿Cuál es tu peso en kg? ")
# estatura = input("¿Cuál es tu estatura en metros?")
# imc = round(float(peso)/float(estatura)**2,2)
# print("Tu índice de masa corporal es " + str(imc))