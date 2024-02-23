while True:  
    frase = input("Escriba una frase: ")
    
    if any(char.isdigit() for char in frase):
        print("La frase no debe contener números.")
    else: 
        break
    
while True: 
    vocal = input("Escriba una vocal: ")
    vocal_replace = vocal.lower()

    if vocal_replace in "aeiou":
        nueva_frase = frase.replace(vocal_replace, vocal.upper())
        print(f"Su frase es: {nueva_frase}")
        break
    else:
        print("Por favor introduzca una vocal válida.")
