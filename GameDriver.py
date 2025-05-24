from Players import *
import sys
from Board import *

class GameDriver:
    def __init__(self, p1type="human", p2type="human"): # maybe add more inputs here
        if p1type == "human":
            self.p1 = HumanPlayer("X")
        elif p1type == "agent":
            self.p2 = AgentPlayer("X")
        else:
            print("Invalid player 1 type")
            exit(-1)

        if p2type == "human":
            self.p2 = HumanPlayer("O")
        elif p2type == "agent":
            self.p2 = AgentPlayer("O")
        else:
            print("Invalid player 2 type")
            exit(-1)

        self.board = Board()

    def process_move(self, curr_player, opponent):
        invalid_move = True
        while(invalid_move):
            (col, row) = curr_player.get_move(self.board)
            print("Move:", [col,row], "\n")
            if (not self.board.is_in_bounds(col, row, curr_player.symbol)):
                print("Invalid move")
            else:
                print("Move:", [col,row], "\n")
                self.board.play_move(col,row,curr_player.symbol)
                return

    def run(self):
        self.board.display()
        # TODO: IMPLEMENT THIS FUNCTION

def main():
    game = GameDriver(sys.argv[1], sys.argv[2])
    game.run()

main()