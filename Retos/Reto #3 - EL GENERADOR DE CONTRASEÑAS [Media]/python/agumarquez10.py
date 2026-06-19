##Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
##Podrás configurar generar contraseñas con los siguientes parámetros:
##Longitud: Entre 8 y 16.
##Con o sin letras mayúsculas.
##Con o sin números.
##Con o sin símbolos.
##(Pudiendo combinar todos estos parámetros entre ellos)
 
import random

def randompassword(length=8, capital=False, numbers=False, symbols=False):
    
    characters = list(range(97, 123))

    if capital:
        characters += list(range(65, 91))

    if numbers:
        characters += list(range(49, 58))

    if symbols:
        characters += list(range(33, 48)) + list(range(58,65)) + list(range(91, 97))

    password = ""

    final_lenght = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_lenght:
        password += chr(random.choice(characters))

    return password

print(randompassword())
print(randompassword(length=16))
print(randompassword(length=1))
print(randompassword(length=22))
print(randompassword(length=12, capital=True))
print(randompassword(length=12, capital=True, numbers=True))
print(randompassword(length=12, capital=True, numbers=True, symbols=True))
