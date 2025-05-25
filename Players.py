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
        possible_moves = board.get_valid_moves()
        n = random.randint(0,len(possible_moves)-1)
        return possible_moves[n]

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
        """
        represent each board state as a string with 9 characters
        characters 0-2 are the first row, 3-5 second row, 6-8 third row
        """
        self.values = {"         ": 0.5}

    def get_move(self, board):
        """
        check all possible moves, get their values, or append new values to values dictionary
        """
        possible_moves = board.get_valid_moves()
        # iterate through all moves and get the move with the highest value
        best_move_val = 0
        best_move = (0,0)
        curr_board_string = board.convert_to_string()
        for r,c in possible_moves:
            move_idx = self.get_move_string_index(r,c)
            new_board_string = curr_board_string[:move_idx] + "X" + curr_board_string[move_idx+1:]
            # if board not in values dictionary yet
            if new_board_string not in self.values.keys():
                new_board_string_val = self.get_board_string_value(new_board_string)
                self.values[new_board_string] = new_board_string_val
            if self.values[new_board_string] >= best_move_val:
                best_move = (r,c)
        return best_move
    
    def get_board_string_value(self, board_str):
        # check if X won
        if board_str[0:3] == "XXX" or board_str[3:6] == "XXX" or board_str[6:] == "XXX":
            return 1
        for i in range(3):
            if board_str[0+i] == "X" and board_str[3+i] == "X" and board_str[6+i] == "X":
                return 1
        if board_str[0] == "X" and board_str[4] == "X" and board_str[8] == "X":
            return 1
        if board_str[2] == "X" and board_str[4] == "X" and board_str[6] == "X":
            return 1
        # check if O won
        if board_str[0:3] == "OOO" or board_str[3:6] == "OOO" or board_str[6:] == "OOO":
            return 0
        for i in range(3):
            if board_str[0+i] == "O" and board_str[3+i] == "O" and board_str[6+i] == "O":
                return 0
        if board_str[0] == "O" and board_str[4] == "O" and board_str[8] == "O":
            return 0
        if board_str[2] == "O" and board_str[4] == "O" and board_str[6] == "O":
            return 0
        # check if tie
        if " " not in board_str:
            return 0
        # no winner or tie
        return 0.5
    
    def get_move_string_index(self, row, col):
        return (3 * row) + col
