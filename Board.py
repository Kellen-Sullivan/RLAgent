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
    
    
        