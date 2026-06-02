'''
* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
* El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
* gane cada punto del juego.
*
* - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
* - Ante la secuencia[P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
'''

def marcadore_tenis (secuencia):
    p1 = 0
    p2 = 0


    puntos = {
        0: "Love",
        1: "15",
        2: "30",
        3: "40"
    }

    for punto in secuencia:
        if punto == "P1":
            p1 += 1
        else:
            p2 += 1
        

        if p1 >= 4 and p1 - p2 >= 2:
            print("Ganador P1")
            break
        if p2 >= 4 and p2 - p1 >= 2:
            print("Ganador P2")
            break

        if p1 >= 3 and p2 >= 3 and abs(p1 - p2) == 1:
            if p1 > p2:
                print ("Ventaja P1")
            else:
                print("Ventaja P2")
            continue


        if p1 >= 3 and p2 >= 3 and p1 == p2:
            print("Deuce")
            continue
        print(puntos[p1], "-", puntos[p2])


marcadore_tenis(["P1","P1","P2","P2","P1","P2","P1","P1"])