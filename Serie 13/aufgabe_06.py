import random


class Game: #Oberklasse
    def __init__(self, player1, player2): #Namen werden hier gespeichert,Punktestand, winner=None
        self.player1 = player1
        self.player2 = player2
        self.score = {player1: 0, player2: 0}
        self.winner = None

    def announce_winner(self, player): #Gewinner setzen und ausgeben
        if self.winner is None:
            self.winner = player
            print(f"The winner is {player}!")
        else:
            raise Exception("Game already has a winner.")
        
    def update_score(self, player, points): #erhoht punktestand des spielers
        if player in self.score:
            self.score[player] += points
        else:
            raise Exception("Player not found in the game.")
        

class Cointoss(Game): #Cointoss erbt von game, bekommt automatisch player1, player2, score, winner, announce_winner, update_score

    """Ein Zug = Münzwurf.
    Kopf -> Spieler 1 bekommt 1 Punkt
    Zahl -> Spieler 2 bekommt 1 Punkt
    Wer zuerst 3 Punkte hat, gewinnt.
    """

    def play_round(self):
        if self.winner is not None:
            raise Exception("Game already has a winner.")
        
        toss = random.choice(["Kopf", "Zahl"])
        print(f"Münzwurf: {toss}")

        if toss == "Kopf":
            self.update_score(self.player1, 1)
        else:
            self.update_score(self.player2, 1)

        print(f"Punktestand: {self.player1}={self.score[self.player1]}, {self.player2}={self.score[self.player2]}")

        # Gewinner prüfen
        if self.score[self.player1] >= 3:
            self.announce_winner(self.player1)
        elif self.score[self.player2] >= 3:
            self.announce_winner(self.player2)


class Battleship1d(Game):
    """
    Jeder Spieler hat 1 Schiff auf einem Feld von 0..9 (zufällig).
    Ein Spielzug play_round() liest von beiden Spielern je ein Feld (Tastatur).
    Wer zuerst das Schiff des Gegners findet, gewinnt.
    Spieler 1 beginnt immer.
    """

    def __init__(self, player1, player2): #ruft den konstuktor von game auf, initialisiert spieler, score, winner
        super().__init__(player1, player2)
        self.ship_pos = {
            player1: random.randint(0, 9),
            player2: random.randint(0, 9), #Jeder Spieler bekommt ein Schiff, position zahl von 0 bis 9
        }
        self.turn = player1  # Spieler 1 beginnt

    def play_round(self):
        if self.winner is not None:
            raise Exception("Game already has a winner.")

        attacker = self.turn
        defender = self.player2 if attacker == self.player1 else self.player1

        # Eingabe validieren
        guess_str = input(f"{attacker}, wähle ein Feld (0-9), um {defender} anzugreifen: ")
        try:
            guess = int(guess_str)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben!")
            return

        if guess < 0 or guess > 9:
            print("Ungültig: Feld muss zwischen 0 und 9 liegen.")
            return

        # Treffer prüfen
        if guess == self.ship_pos[defender]:
            print("TREFFER! Schiff gefunden.")
            self.announce_winner(attacker)
        else:
            print("Wasser. Kein Treffer.")

        # Zug wechseln (nur wenn noch kein Gewinner)
        if self.winner is None:
            self.turn = defender


game = Cointoss("Alice", "Bob")

while game.winner is None:
    game.play_round()


game = Battleship1d("Alice", "Bob")

while game.winner is None:
    game.play_round()
