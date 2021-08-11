import math
import random

class Player:
    def _init_(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandmCompPlayer(Player):
    def _init_(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_swaure = True
            except ValueError:
                print('Invalid option, try again')
        return val