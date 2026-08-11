
 #* Escribe un programa que reciba un texto y transforme lenguaje natural a
 #* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 #*  se caracteriza por sustituir caracteres alfanuméricos.
 #* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 #*   con el alfabeto y los números en "leet".
 #*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


def leet_speak(text):
    leet_dict = {
        'a': '4',
        'b': '8',
        'c': '<',
        'd': '|)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '#',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|_',
        'm': '|\/|',
        'n': '|\|',
        'o': '0',
        'p': '|*',
        'q': '(,)',
        'r': '|2',
        's': '$',
        't': "']['",
        'u': '|_|',
        'v': '|/',
        'w': '\^/',
        'x': '%',
        'y': '`/',
        'z': '~/_'
    }

    leet_text = ''
    for char in text:
        if char.lower() in leet_dict:
            leet_text += leet_dict[char.lower()]
        else:
            leet_text += char

    return leet_text