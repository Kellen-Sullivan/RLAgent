import copy

class Board:
    def __init__(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display(self):
        for i in range(3):
            print(self.grid[i][0], " |", self.grid[i][1], "| ", self.grid[i][2])
            if i < 2:
                print("===========")

    def clear_board(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def get_cell(self, row, col):
        if not self.is_in_bounds(row, col):
            return None
        else:
            return self.grid[row][col]
        
    def is_in_bounds(self, row, col):
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            return True
        else:
            return False

    def is_cell_empty(self, row, col):
        if self.grid[row][col] == " ":
            return True
        else:
            return False

    def is_valid_move(self, row, col):
        if col >= 0 and col < 3 and row >= 0 and row < 3 and self.is_cell_empty(row, col):
            return True
        else:
            return False
        
    def get_valid_moves(self):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if self.is_cell_empty(i, j):
                    valid_moves.append((i,j))
        return valid_moves
        
    def convert_to_string(self):
        board_str = ""
        for i in range(3):
            for j in range(3):
                board_str += self.grid[i][j]
        return board_str        

    def play_move(self, row, col, symbol):
        if not self.is_valid_move(row, col):
            return None
        else:
            self.grid[row][col] = symbol
        
    def check_win(self, symbol):
        # check rows
        for i in range(3):
            if self.grid[i][0] == symbol and self.grid[i][1] == symbol and self.grid[i][2] == symbol:
                return True
        # check cols
        for i in range(3):
            if self.grid[0][i] == symbol and self.grid[1][i] == symbol and self.grid[2][i] == symbol:
                return True
        # check diagonals
        if self.grid[0][0] == symbol and self.grid[1][1] == symbol and self.grid[2][2] == symbol:
            return True
        if self.grid[2][0] == symbol and self.grid[1][1] == symbol and self.grid[0][2] == symbol:
            return True
        # player is not winner
        return False
    
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == " ":
                    return False
        return True

    def get_symmetric_boards(self, board):
        symmetric_boards = [board]
        # rotate board 90, 180, and 270 degrees
        one_rotation = self.rotate_board(board)
        two_rotation = self.rotate_board(one_rotation)
        three_rotation = self.rotate_board(two_rotation)
        # reflect board
        reflect_vert = self.reflect_board_vertical(board)
        reflect_horizontal = self.reflect_board_horizontal(board)
        reflect_pos_diag = self.reflect_board_pos_diagonal(board)
        reflect_neg_diag = self.reflect_board_neg_diagonal(board)
        # add symmetric boards to array
        symmetric_boards.append(one_rotation)
        symmetric_boards.append(two_rotation)
        symmetric_boards.append(three_rotation)
        symmetric_boards.append(reflect_vert)
        symmetric_boards.append(reflect_horizontal)
        symmetric_boards.append(reflect_pos_diag)
        symmetric_boards.append(reflect_neg_diag)
        return symmetric_boards
    
    def display_symmetric_boards(self, sym_boards):
        print("Symmetric boards: ")
        print("**************************")
        for board in sym_boards:
            for i in range(3):
                print(board[i][0], " |", board[i][1], "| ", board[i][2])
                if i < 2:
                    print("===========")
            print("**************************")
        print("Done with symmetric boards")

    def convert_symmetric_boards_to_str(self, sym_boards):
        symmetric_board_strings = []
        for board in sym_boards:
            board_str = ""
            for i in range(3):
                for j in range(3):
                    board_str += board[i][j]
            symmetric_board_strings.append(board_str)
        return symmetric_board_strings

    def rotate_board(self, grid):
        # rotate board 90 degrees clockwise
        rotated_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # top row 
        rotated_array[0][0] = grid[0][2]
        rotated_array[0][1] = grid[1][2]
        rotated_array[0][2] = grid[2][2]
        # left mid 
        rotated_array[1][0] = grid[0][1]
        # bottom row
        rotated_array[2][0] = grid[0][0]
        rotated_array[2][1] = grid[1][0]
        rotated_array[2][2] = grid[2][0]
        # right mid
        rotated_array[1][2] = grid[2][1]
        # middle
        rotated_array[1][1] = grid[1][1]
        return rotated_array
    
    def reflect_board_pos_diagonal(self, grid):
        # reflect board across pos diagonal
        reflected_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # top left corner
        reflected_array[0][0] = grid[2][2]
        reflected_array[0][1] = grid[1][2]
        reflected_array[1][0] = grid[2][1]
        # bottom right corner
        reflected_array[2][2] = grid[0][0]
        reflected_array[2][1] = grid[1][0]
        reflected_array[1][2] = grid[0][1]
        # pos diagonal
        reflected_array[0][2] = grid[0][2]
        reflected_array[1][1] = grid[1][1]
        reflected_array[2][0] = grid[2][0]
        
        return reflected_array

    def reflect_board_neg_diagonal(self, grid):
        # reflect board across pos diagonal
        reflected_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # top right corner
        reflected_array[0][2] = grid[2][0]
        reflected_array[0][1] = grid[1][0]
        reflected_array[1][2] = grid[2][1]
        # bottom left corner
        reflected_array[2][0] = grid[0][2]
        reflected_array[1][0] = grid[0][1]
        reflected_array[2][1] = grid[1][2]
        # neg diagonal
        reflected_array[0][0] = grid[0][0]
        reflected_array[1][1] = grid[1][1]
        reflected_array[2][2] = grid[2][2]
        
        return reflected_array

    def reflect_board_horizontal(self, grid):
         # reflect board across horizontal axis (across middle row)
        reflected_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # top row
        reflected_array[0][0] = grid[2][0]
        reflected_array[0][1] = grid[2][1]
        reflected_array[0][2] = grid[2][2]
        # bottom row
        reflected_array[2][0] = grid[0][0]
        reflected_array[2][1] = grid[0][1]
        reflected_array[2][2] = grid[0][2]
        # middle row
        reflected_array[1][0] = grid[1][0]
        reflected_array[1][1] = grid[1][1]
        reflected_array[1][2] = grid[1][2]
        
        return reflected_array

    def reflect_board_vertical(self, grid):
        # reflect board across vertical axis (around middle column)
        reflected_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # left col
        reflected_array[0][0] = grid[0][2]
        reflected_array[1][0] = grid[1][2]
        reflected_array[2][0] = grid[2][2]
        # right col
        reflected_array[0][2] = grid[0][0]
        reflected_array[1][2] = grid[1][0]
        reflected_array[2][2] = grid[2][0]
        # middle col
        reflected_array[0][1] = grid[0][1]
        reflected_array[1][1] = grid[1][1]
        reflected_array[2][1] = grid[2][1]
        
        return reflected_array
    
    
        