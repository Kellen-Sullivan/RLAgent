from Players import *
import sys
from Board import *
import matplotlib.pyplot as plt

class GameDriver:
    def __init__(self, p2type="random", num_of_games=100, display=True): # maybe add more inputs here
        
        # set player 1 to be Epsilon Greedy
        self.p1 = EpsilonGreedyPlayer("X")
    
        # set player 2
        if p2type == "random":
            self.p2 = RandomPlayer("O")
        elif p2type == "heuristic":
            self.p2 = HeuristicPlayer("O")
        elif p2type == "notrandom":
            self.p2 = NotRandomPlayer("O")
        else:
            print("Invalid player 2 type")
            exit(-1)

        # display the board after each move
        if display == "True":
            self.display = True
        else:
            self.display = False

        self.board = Board()
        self.num_of_games = int(num_of_games)
        self.boards_visited = []

    def process_move(self, curr_player):
        invalid_move = True
        while(invalid_move):
            (row, col) = curr_player.get_move(self.board)
            if (not self.board.is_valid_move(row, col)):
                if self.display:
                    print("Invalid move")
            else:
                if self.display:
                    print("Move:", [row, col], "\n")
                self.board.play_move(row,col,curr_player.symbol)
                return

    def run(self):
        self.board.clear_board()
        self.boards_visited.append(self.board)
        toggle = 0
        curr_player = self.p1 # player 1 starts the game
        if self.display:
            self.board.display()
        while(True):
            self.process_move(curr_player)
            self.boards_visited.append(self.board)
            if self.display: 
                self.board.display()
            # check winner or tie
            if self.board.check_win(curr_player.get_symbol()):
                if self.display: 
                    print("Player ", curr_player.get_symbol(), " wins!")
                return 1 if curr_player.get_symbol() == "X" else -1
            if self.board.check_tie():
                if self.display:
                    print("Game ends in a tie!")
                return 0
            # toggle the current player
            toggle += 1
            if toggle % 2 == 0:
                curr_player = self.p1
            else:
                curr_player = self.p2

def make_plots(games_played, win_percentages):
    # win percentage
    plt.plot(games_played, win_percentages)
    plt.xlabel("Games Played")
    plt.ylabel("Win Percentage")
    plt.title("Epsilon Win Percentage Over Time")
    plt.show()


def epsilon_greedy_update_values(winner, game):
    games_won_at_board = 0
    if winner == 1:
        games_won_at_board = 1
    else:
        games_won_at_board = 0
    # update board values 
    for board in game.boards_visited:
        board_str = board.convert_to_string()
        if board_str not in game.p1.values.keys() :
            game.p1.values[board_str] = (games_won_at_board,1)
        else:
            game.p1.values[board_str] = (games_won_at_board + game.p1.values[board_str][0],1+game.p1.values[board_str][1])

def main():
    game = GameDriver(sys.argv[1], sys.argv[2], sys.argv[3])
    player_X_wins, player_O_wins = 0, 0
    games_played, win_percentages = [], []
    for i in range(game.num_of_games):
        winner = game.run()
        if winner == 1:
            player_X_wins += 1
        elif winner == -1:
            player_O_wins += 1
        if i % (game.num_of_games // 10) == 0 and i != 0:
            games_played.append(i)
            win_percentages.append(((player_X_wins / (i+1)) * 100))
        epsilon_greedy_update_values(winner, game)
            
    # print simulation results
    print(f"player X won {player_X_wins}/{game.num_of_games} games ({((player_X_wins / game.num_of_games) * 100):.2f}%)")
    print(f"player O won {player_O_wins}/{game.num_of_games} games ({((player_O_wins / game.num_of_games) * 100):.2f}%)")
    print(f"There were {game.num_of_games - player_X_wins - player_O_wins} ties!")  
    print(game.p1.values)
    make_plots(games_played, win_percentages)
  
main()