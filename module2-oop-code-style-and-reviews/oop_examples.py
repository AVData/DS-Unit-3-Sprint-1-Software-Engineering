"""
Classes to represent games.
"""
# construcor, field, and method, they are vocab words to learn

from random import random

class Game:
    '''
    General representation of an abstract game.
    '''
    def __init__(self, player1 = 'Mathias', player2 = 'Daniel'):
        self.rounds = 2
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        '''
        Print game print_players
        '''
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        '''
        increment rounds by 1
        '''
        self.rounds += 1

    def winner(self):
        '''
        pick a winner!
        '''
        return self.player1 if random() > 0.5 else self.player2

game1 = Game()

class Tic(Game):
    '''
    Tictactoe subclass of game
    '''
    def __init__(self, rounds = 3, player1 = 'Mike', player2 = 'Emma'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing TIC TAC TOE with {}'.format(self.player1, self.player2))
