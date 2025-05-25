from Players import *
import sys
from Board import *

class GameDriver:
    def __init__(self, p1type="agent", p2type="random", num_of_games=100, learning_rate=1): # maybe add more inputs here
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
        self.num_of_games = int(num_of_games)
        self.learning_rate = int(learning_rate)

    def process_move(self, curr_player):
        invalid_move = True
        while(invalid_move):
            (row, col) = curr_player.get_move(self.board)
            if (not self.board.is_valid_move(row, col)):
                print("Invalid move")
                return 1 # TEMP TEST
            else:
                print("Move:", [row, col], "\n")
                self.board.play_move(row,col,curr_player.symbol)
                return 0 # TEMP TEST

    def run(self):
        self.board.clear_board()
        toggle = 0
        curr_player = self.p1 # player 1 starts the game
        self.board.display()
        while(True):
            if self.process_move(curr_player) == 1: # TEMP TEST
                print("ERROR") # TEMP TEST
                return
            self.board.display()
            # check winner or tie
            if self.board.check_win(curr_player.get_symbol()):
                print("Player ", curr_player.get_symbol(), " wins!")
                return 1 if curr_player.get_symbol() == "X" else -1
            if self.board.check_tie():
                print("Game ends in a tie!")
                return 0
            # toggle the current player
            toggle += 1
            if toggle % 2 == 0:
                curr_player = self.p1
            else:
                curr_player = self.p2

def main():
    game = GameDriver(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    player_X_wins, player_O_wins = 0, 0
    for i in range(game.num_of_games):
        winner = game.run()
        if winner == 1:
            player_X_wins += 1
        elif winner == -1:
            player_O_wins += 1
    print(f"player X won {player_X_wins}/{game.num_of_games} games ({((player_X_wins / game.num_of_games) * 100):.2f}%)")
    print(f"player O won {player_O_wins}/{game.num_of_games} games ({((player_O_wins / game.num_of_games) * 100):.2f}%)")
    print(f"There were {game.num_of_games - player_X_wins - player_O_wins} ties!")  
  
main()