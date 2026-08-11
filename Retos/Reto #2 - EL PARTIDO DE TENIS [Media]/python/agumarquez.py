from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2


def tennis_match(points):

    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0

    for player in points:

        p1_points += 1 if player == Player.P1 else 0
        p2_points += 1 if player == Player.P2 else 0

        if p1_points >= 3 and p2_points >= 3:
            print("Deuce" if p1_points == p2_points else
                  "Ventaja P1" if p1_points > p2_points else "Ventaja P2")
        else:
            print(f"{game[p1_points]} - {game[p2_points]}")

tennis_match([Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P1])
