from Players import *
import sys
from Board import *
import matplotlib.pyplot as plt

class GameDriver:
    def __init__(self, p1type="random", p2type="random", num_of_games=100, learning_rate=1, display=True): # maybe add more inputs here
        if p1type == "learning":
            self.p1 = LearningPlayer("X")
        elif p1type == "random":
            self.p1 = RandomPlayer("X")
        elif p1type == "human":
            self.p1 = HumanPlayer("X")
        elif p1type == "heuristic":
            self.p1 = HeuristicPlayer("X")
        elif p1type == "mcts":
            self.p1 = MctsPlayer("X")
        else:
            print("Invalid player 1 type")
            exit(-1)
        if p2type == "learning":
            self.p2 = LearningPlayer("O")
        elif p2type == "human":
            self.p2 = HumanPlayer("O")
        elif p2type == "random":
            self.p2 = RandomPlayer("O")
        elif p2type == "heuristic":
            self.p2 = HeuristicPlayer("O")
        elif p2type == "mcts":
            self.p2 = MctsPlayer("O")
        else:
            print("Invalid player 2 type")
            exit(-1)

        if display == "True":
            self.display = True
        else:
            self.display = False

        self.board = Board()
        self.num_of_games = int(num_of_games)
        self.learning_rate = float(learning_rate)
        self.boards_visited = []

    def process_move(self, curr_player):
        invalid_move = True
        while(invalid_move):
            (row, col) = curr_player.get_move(self.board, self.learning_rate)
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
        self.boards_visited.append(self.board.grid)
        toggle = 0
        curr_player = self.p1 # player 1 starts the game
        if self.display:
            self.board.display()
        while(True):
            self.process_move(curr_player)
            self.boards_visited.append(self.board.grid)
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

def make_plots(games_played, win_percentages, boards_searched, learn):
    # win percentage
    plt.plot(games_played, win_percentages)
    plt.xlabel("Games Played")
    plt.ylabel("Win Percentage")
    plt.title("Player 1 Win Percentage Over Time")
    plt.show()
    
    if learn:
        # boards searched
        plt.plot(games_played, boards_searched)
        plt.xlabel("Games Played")
        plt.ylabel("Boards Searched")
        plt.title("Player 1 Boards Searched Over Time")
        plt.show()


def mcts_update_values(winner, game):
    games_won_at_board = 0
    if winner == 1:
        games_won_at_board = 1
    else:
        games_won_at_board = 0
    # update board values 
    for board in game.boards_visited:
        symmetric_boards = game.board.get_symmetric_boards(board)
        symmetric_boards_strs = game.board.convert_symmetric_boards_to_str(symmetric_boards)
        board_not_in_values = True
        active_board = ""
        for b in symmetric_boards_strs:
            if b in game.p1.values.keys():
                board_not_in_values = False
                active_board = b
        if board_not_in_values :
            game.p1.values[symmetric_boards_strs[0]] = (games_won_at_board,1)
        else:
            game.p1.values[active_board] = (games_won_at_board + game.p1.values[active_board][0],1+game.p1.values[active_board][1])

def main():
    game = GameDriver(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    learn = sys.argv[1] == "learning"
    mcts = sys.argv[1] == "mcts"
    player_X_wins, player_O_wins = 0, 0
    games_played, win_percentages, boards_searched = [], [], []
    for i in range(game.num_of_games):
        winner = game.run()
        if winner == 1:
            player_X_wins += 1
        elif winner == -1:
            player_O_wins += 1
        if i % (game.num_of_games // 10) == 0 and i != 0:
            game.learning_rate = game.learning_rate * 0.85
            games_played.append(i)
            win_percentages.append(((player_X_wins / i) * 100))
            if learn:
                boards_searched.append(len(game.p1.values.keys()))
        if mcts:
            # print(f"After game {i}")
            # print(game.p1.values)
            # print("=========================")
            # print(len(game.boards_visited))
            # print("=========================")
            mcts_update_values(winner, game)
            
    # print simulation results
    print(f"player X won {player_X_wins}/{game.num_of_games} games ({((player_X_wins / game.num_of_games) * 100):.2f}%)")
    print(f"player O won {player_O_wins}/{game.num_of_games} games ({((player_O_wins / game.num_of_games) * 100):.2f}%)")
    print(f"There were {game.num_of_games - player_X_wins - player_O_wins} ties!")  
    print(game.p1.values)
    if learn:
        print(f"boards searched: {len(game.p1.values.keys())}")
    make_plots(games_played, win_percentages, boards_searched, learn)
  
main()