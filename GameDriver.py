from Players import *
import sys
from Board import *

class GameDriver:
    def __init__(self, p1type="agent", p2type="random"): # maybe add more inputs here
        if p1type == "learning":
            self.p1 = LearningPlayer("X")
        elif p1type == "random":
            self.p1 = RandomPlayer("X")
        elif p1type == "human":
            self.p1 = HumanPlayer("X")
        else:
            print("Invalid player 1 type")
            exit(-1)

        if p2type == "human":
            self.p2 = HumanPlayer("O")
        elif p2type == "random":
            self.p2 = RandomPlayer("O")
        else:
            print("Invalid player 2 type")
            exit(-1)

        self.board = Board()

    def process_move(self, curr_player):
        invalid_move = True
        while(invalid_move):
            (row, col) = curr_player.get_move(self.board)
            if (not self.board.is_valid_move(row, col)):
                print("Invalid move")
            else:
                print("Move:", [row, col], "\n")
                self.board.play_move(row,col,curr_player.symbol)
                return

    def run(self):
        toggle = 0
        curr_player = self.p1 # player 1 starts the game
        self.board.display()
        while(True):
            self.process_move(curr_player)
            self.board.display()
            # check winner or tie
            if self.board.check_win(curr_player.get_symbol()):
                print("Player ", curr_player.get_symbol(), " wins!")
                return
            if self.board.check_tie():
                print("Game ends in a tie!")
                return
            # toggle the current player
            toggle += 1
            if toggle % 2 == 0:
                curr_player = self.p1
            else:
                curr_player = self.p2

def main():
    game = GameDriver(sys.argv[1], sys.argv[2])
    game.run()

main()