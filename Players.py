import random
from Board import *

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
    def get_board_string_value(self, board_str):
        if self.get_symbol() == "X":
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
        if self.get_symbol() == "O":
            # check if X won
            if board_str[0:3] == "XXX" or board_str[3:6] == "XXX" or board_str[6:] == "XXX":
                return 0
            for i in range(3):
                if board_str[0+i] == "X" and board_str[3+i] == "X" and board_str[6+i] == "X":
                    return 0
            if board_str[0] == "X" and board_str[4] == "X" and board_str[8] == "X":
                return 0
            if board_str[2] == "X" and board_str[4] == "X" and board_str[6] == "X":
                return 0
            # check if O won
            if board_str[0:3] == "OOO" or board_str[3:6] == "OOO" or board_str[6:] == "OOO":
                return 1
            for i in range(3):
                if board_str[0+i] == "O" and board_str[3+i] == "O" and board_str[6+i] == "O":
                    return 1
            if board_str[0] == "O" and board_str[4] == "O" and board_str[8] == "O":
                return 1
            if board_str[2] == "O" and board_str[4] == "O" and board_str[6] == "O":
                return 1
        # check if tie
        if " " not in board_str:
            return 0
        # no winner or tie
        return 0.5
    
    def get_move_string_index(self, row, col):
        return (3 * row) + col


class RandomPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def get_move(self, board):
        possible_moves = board.get_valid_moves()
        n = random.randint(0,len(possible_moves)-1)
        return possible_moves[n]
    

class NotRandomPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def get_move(self, board):
        possible_moves = board.get_valid_moves()
        if (0,0) in possible_moves:
            return (0,0)
        elif (0,1) in possible_moves:
            return (0,1)
        elif (0,2) in possible_moves:
            return (0,2)
        elif (1,0) in possible_moves:
            return (1,0)
        elif (1,1) in possible_moves:
            return (1,1)
        elif (1,2) in possible_moves:
            return (1,2)
        elif (2,0) in possible_moves:
            return (2,0)
        elif (2,1) in possible_moves:
            return (2,1)
        else:
            return (2,2)


class HeuristicPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def check_opp_win(self, board_str):
        if self.get_symbol() == "O":
            # check if opponent could win in next move
            if (board_str[0:3].count("X") == 2 and board_str[0:3].count(" ") == 1) or (board_str[3:5].count("X") == 2 and board_str[3:5].count(" ") == 1) or (board_str[6:].count("X") == 2 and board_str[6:].count(" ") == 1):
                return True
            for i in range(3):
                if (board_str[0+i] == "X" and board_str[3+i] == "X" and board_str[6+i] == " ") or (board_str[0+i] == "X" and board_str[3+i] == " " and board_str[6+i] == "X") or (board_str[0+i] == " " and board_str[3+i] == "X" and board_str[6+i] == "X"):
                    return True
            if (board_str[0] == "X" and board_str[4] == "X" and board_str[8] == " ") or (board_str[0] == "X" and board_str[4] == " " and board_str[8] == "X") or (board_str[0] == " " and board_str[4] == "X" and board_str[8] == "X"):
                return True
            if (board_str[2] == "X" and board_str[4] == "X" and board_str[6] == " ") or (board_str[2] == "X" and board_str[4] == " " and board_str[6] == "X") or (board_str[2] == " " and board_str[4] == "X" and board_str[6] == "X"):
                return True
        else:
            # check if opponent could win in next move
            if (board_str[0:3].count("O") == 2 and board_str[0:3].count(" ") == 1) or (board_str[3:5].count("O") == 2 and board_str[3:5].count(" ") == 1) or (board_str[6:].count("O") == 2 and board_str[6:].count(" ") == 1):
                return True
            for i in range(3):
                if (board_str[0+i] == "O" and board_str[3+i] == "O" and board_str[6+i] == " ") or (board_str[0+i] == "O" and board_str[3+i] == " " and board_str[6+i] == "O") or (board_str[0+i] == " " and board_str[3+i] == "O" and board_str[6+i] == "O"):
                    return True
            if (board_str[0] == "O" and board_str[4] == "O" and board_str[8] == " ") or (board_str[0] == "O" and board_str[4] == " " and board_str[8] == "O") or (board_str[0] == " " and board_str[4] == "O" and board_str[8] == "O"):
                return True
            if (board_str[2] == "O" and board_str[4] == "O" and board_str[6] == " ") or (board_str[2] == "O" and board_str[4] == " " and board_str[6] == "O") or (board_str[2] == " " and board_str[4] == "O" and board_str[6] == "O"):
                return True
        return False

    def get_move(self, board):
        possible_moves = board.get_valid_moves()
        # 20 % chance to choose random move -- ensure imperfect player
        if random.randint(0,5) == 0:
            return random.choice(possible_moves)
        # find best move
        non_losing_moves = []
        curr_board_string = board.convert_to_string()
        for r,c in possible_moves:
            move_idx = self.get_move_string_index(r,c)
            new_board_string = curr_board_string[:move_idx] + self.symbol + curr_board_string[move_idx+1:]
            curr_move_val = self.get_board_string_value(new_board_string)
            # if move results in win, play the move
            if curr_move_val == 0:
                return (r,c)
            # if opponenet wins, don't play that move
            if self.check_opp_win(new_board_string) == False:
                non_losing_moves.append((r,c))
        # play random non loosing move (prioritize middle if available)
        if len(non_losing_moves) > 0:
            if (1,1) in non_losing_moves:
                return (1,1)
            else:
                return random.choice(non_losing_moves)
        return random.choice(possible_moves)
    

class EpsilonGreedyPlayer(Player):
    """
    Use epsilon greedy approach to choose best move
    Use Q_k+1 = Q_k + 1/k (R_k - Q_k) as action values
    """
    def __init__(self, symbol):
        Player.__init__(self, symbol)
        """
        represent each board state as a string with 9 characters
        characters 0-2 are the first row, 3-5 second row, 6-8 third row
        """
        self.values = {}

    def get_move(self, board):
        """
        check all possible moves, get their values, or append new values to values dictionary
        """
        possible_moves = board.get_valid_moves()
        # select non greedy move epsilon% of the time currently epsilon = 0.01
        if random.randint(0,100) == 0: 
            return random.choice(possible_moves)
        best_move_val = 0
        best_moves = []
        # iterate through all possible moves to find the best one
        for r,c in possible_moves:
            move_idx = self.get_move_string_index(r,c)
            board_str = board.convert_to_string()
            new_board_string = board_str[:move_idx] + self.get_symbol() + board_str[move_idx+1:]
            # if board resulting from curr possible move in values dictionary
            if new_board_string in self.values.keys():
                if (self.values[new_board_string][0] / self.values[new_board_string][1]) > best_move_val:
                    best_moves = [(r,c)]
                    best_move_val = (self.values[new_board_string][0] / self.values[new_board_string][1])
                elif (self.values[new_board_string][0] / self.values[new_board_string][1]) == best_move_val:
                    best_moves.append((r,c)) 
        # if best_moves is empty chose random possible move, else randomly select move from the best_moves array
        if len(best_moves) == 0:
            return random.choice(possible_moves)
        else:
            best_move = random.choice(best_moves)
        return best_move
            
            
