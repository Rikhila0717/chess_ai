import argparse

from data.classes.ChessMatch import chess_match
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.agents.MinimaxPlayer import MinimaxPlayer
from data.classes.agents.RandomPlayer import RandomPlayer
from data.classes.agents.HumanPlayer import HumanPlayer

def main():
    # parser = argparse.ArgumentParser(description="Initialize players for the game.")
    # parser.add_argument('white', type=str, help="Type of the white player")
    # parser.add_argument('black', type=str, help="type of the black player")
    # args = parser.parse_args()
    # if args.white not in globals().keys():
    #     print(f'White player {args.white} not found!')
    #     return
    # if args.black not in globals().keys():
    #     print(f'Black player {args.black} not found!')
    #     return
    # white_player: ChessAgent = globals()[args.white]('white')
    # black_player: ChessAgent = globals()[args.black]('black')
    # black_player = MinimaxPlayer('black',depth=3)
    # white_player = HumanPlayer('white')
    # black_player = RandomPlayer('black')
    # chess_match(white_player, black_player)

    # chess_match(MinimaxPlayer('white'),MinimaxPlayer('black'))
    chess_match(RandomPlayer('white'),MinimaxPlayer('black'))

if __name__ == '__main__':
    main() 