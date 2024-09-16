import random
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class CyclePlayer(Player):
    def __init__(self):
        self.Cycle_move_count = 0

    def move(self):
        if self.Cycle_move_count == 0:
            self.Cycle_move_count += 1
            return random.choice(moves)
        elif self.player2_move == 'rock':
            return 'paper'
        elif self.player2_move == 'paper':
            return 'scissors'
        elif self.player2_move == 'scissors':
            return 'rock'

    def learn(self, my_move, their_move):
        self.player2_move = my_move


class ReflectPlayer(Player):
    def __init__(self):
        self.Reflect_move_count = 0

    def move(self):
        if self.Reflect_move_count == 0:
            self.Reflect_move_count += 1
            return random.choice(moves)
        else:
            if self.player1_move == 'rock':
                return 'rock'
            elif self.player1_move == 'paper':
                return 'paper'
            elif self.player1_move == 'scissors':
                return 'scissors'

    def learn(self, my_move, their_move):
        self.player1_move = their_move


class HumanPlayer(Player):
    def move(self):
        while True:
            HumanMove = input("Rock, paper, scissors?" +
                              " or type 'quit' to quit >").lower()
            if (HumanMove == 'rock' or
                    HumanMove == 'paper' or
                    HumanMove == 'scissors'):
                return HumanMove
            elif HumanMove == 'quit':
                quit()
            else:
                print("Invalid input, please try again")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Old place of beats(one, two)

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.score(move1, move2)  # Call the score

    def play_game(self):
        while True:
            self.p1_score = 0
            self.p2_score = 0
            print("\033[1;37;40m ******** Game start! ********")
            for round in range(5):
                print(f"\033[1;37;40m* Round {round+1}:")
                self.play_round()
            print(f"""\033[1;33;40m
                            Final scores: Player one : {self.p1_score}
                                          Player two : {self.p2_score}
                      """)
            if self.p1_score > self.p2_score:
                print("""\033[1;32;40m
                         ************** You Win :) **************
                         """)
            elif self.p2_score > self.p1_score:
                print("""\033[1;31;40m
                         ************* You lose :( **************
                         """)
            else:
                print("""\033[1;35;40m
                         ***************** TIE ******************
                         """)
            print("""
                         ----------------------------------------
                     """)
            print("""
                         ----------------------------------------\n\n
                     """)

    def beats(self, one, two):
        if one == two:          # Handle the TIE
            return ('TIE')
        else:
            return ((one == 'rock' and two == 'scissors') or
                    (one == 'scissors' and two == 'paper') or
                    (one == 'paper' and two == 'rock'))

    def score(self, move1, move2):   # To keep the score
        if self.beats(move1, move2) == 'TIE':
            print("\033[1;35;40m** TIE **")
        elif self.beats(move1, move2):
            self.p1_score += 1
            print("\033[1;32;40m** PLAYER ONE WINS **")
        else:
            print("\033[1;31;40m** PLAYER TWO WINS **")
            self.p2_score += 1
        print(f"\033[1;34;40mScore: Player one {self.p1_score},",
              f"Player two {self.p2_score} \n")


if __name__ == '__main__':
    players_list = [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    game = Game(HumanPlayer(), random.choice(players_list))
    game.play_game()


def quit():
    print("Bye!")
