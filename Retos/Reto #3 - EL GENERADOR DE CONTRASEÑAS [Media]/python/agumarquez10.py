##Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
##Podrás configurar generar contraseñas con los siguientes parámetros:
##Longitud: Entre 8 y 16.
##Con o sin letras mayúsculas.
##Con o sin números.
##Con o sin símbolos.
##(Pudiendo combinar todos estos parámetros entre ellos)
 
import random

def randompassword(length=8, capital=False, numbers=False, symbols=False):
    
    characters = ["a", "b", "c", "d"]

    password = ""

    final_lenght = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_lenght:
        password += random.choice(characters)

    return password

print(randompassword(length=25))

