class Board:
    def __init__(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display(self):
        for i in range(3):
            print(self.grid[i][0], " |", self.grid[i][1], "| ", self.grid[i][2])
            if i < 2:
                print("===========")

    def get_cell(self, col, row):
        if not self.is_in_bounds(col,row):
            return None
        else:
            return self.grid[col][row]
        
    def set_cell(self, col, row):
        if not self.is_in_bounds(col, row):
            return None
        else:
            self.grid[col][row]

    def is_in_bounds(self, col, row):
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            return True
        else:
            return False
    
    def is_cell_empty(self, col, row):
        if self.grid[col][row] == " ":
            return True
        else:
            return False
        