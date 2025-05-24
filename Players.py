import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)
    
    def get_move(self, board):
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        return (row, col)

class RandomPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def get_move(self, board):
        col = random.randint(0,3)
        row = random.randint(0,3)
        return (row, col)

class LearningPlayer(Player):
    """
    TODO: Implement reinforcement learning 
    Assume this agent always plays X's
    Need to create a table of win probabilites for the agent
    All states with 3 X's in a row have a win prob of 1,
    All states with 3 O's in a row have a win prob of 0,
    Initially set all other states to 0.5
    """
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def get_move(self, board):
        col = random.randint(0,3)
        row = random.randint(0,3)
        return (row, col)
