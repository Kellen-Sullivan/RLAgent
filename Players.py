class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)
    
    def get_move(self, board):
        col = int(input("Enter col: "))
        row = int(input("Enter row: "))
        return (row, col)
    
# TODO: Implement 
class AgentPlayer(Player):
    pass
