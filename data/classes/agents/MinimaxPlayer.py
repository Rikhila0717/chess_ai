# /* MinimaxAgent.py

from typing import Literal
from data.classes.Square import Square
from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.copies.SquareCopy import SquareCopy
from data.classes.copies.BoardCopy import BoardCopy
import random

class MinimaxPlayer(ChessAgent):
    def __init__(self, color: Literal['white', 'black'], depth: int = 4):
        super().__init__(color)
        self.depth = depth

    def choose_action(self, board):
        best_move = None

        best_eval = -float('inf') if self.color == 'white' else float('inf')
        board_copy = BoardCopy()
        board_copy.copy_board(board)
        # print("In choose action: Printing board copy before starting minimax\n")
        self.print_board(board_copy)
        possible_moves = self.get_all_possible_moves(board_copy,self.color)
    
        for move in possible_moves:
            from_square, to_square= move
            current_piece = from_square.occupying_piece
            if current_piece is not None:
                if board_copy.handle_move(from_square, to_square):
                    eval = self.minimax(board_copy, self.depth, -float('inf'), float('inf'), self.color=='black')
                    if (self.color=='white' and eval>best_eval) or (self.color=='black' and eval<best_eval):
                        best_eval = eval
                        best_move = move
                    # else:
                    #     eval = self.minimax(board_copy, self.depth, -float('inf'), float('inf'), False)
                        # if eval < best_eval:
                        #     best_eval = eval
                        #     best_move = move
        # print(best_move)
        # print("After minimax completion: printing board")
        # self.print_board(board_copy)
        if not best_move:
            return False
        
        best_move_from_square = self.convert_square_copy_to_square(best_move[0],board)
        best_move_to_square = self.convert_square_copy_to_square(best_move[1],board)
        return (best_move_from_square,best_move_to_square)
    

    def convert_square_copy_to_square(self,square_copy: SquareCopy, board: Board) -> Square:
        position = square_copy.pos
        return board.get_square_from_pos(position)
    

    def minimax(self, board: BoardCopy, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_in_checkmate('white') or board.is_in_checkmate('black'):
            return self.evaluate_board(board)
        
        if maximizing_player:
            max_eval = -float('inf')
            possible_moves = self.get_all_possible_moves(board,self.color)
            if possible_moves is None:
                return None
            random.shuffle(possible_moves)
            for move in possible_moves:
                from_square, to_square= move
                current_piece = from_square.occupying_piece
                if current_piece is not None:
                    board_copy = BoardCopy()
                    board_copy.copy_board(board)
                    if board_copy.handle_move(from_square,to_square):
                        eval = self.minimax(board_copy, depth - 1, alpha, beta, False)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            opponent_color = 'white' if self.color == 'black' else 'black'
            possible_moves = self.get_all_possible_moves(board,opponent_color)
            if possible_moves is None:
                return None
            random.shuffle(possible_moves)
            for move in possible_moves:
                from_square,to_square=move
                current_piece = from_square.occupying_piece
                if current_piece is not  None:
                    board_copy = BoardCopy()
                    board_copy.copy_board(board)
                    if board.handle_move(from_square, to_square):
                        eval = self.minimax(board, depth - 1, alpha, beta, True)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def get_all_possible_moves(self, board: BoardCopy, color: Literal['white', 'black']):
        possible_moves: list[tuple[Square, Square]] = []
        for square in board.squares:
            if square.occupying_piece != None \
               and square.occupying_piece.color == color:
                for target in square.occupying_piece.get_valid_moves(board):
                    possible_moves.append((square, target))
        # print("line 121: possible_moves", possible_moves)
        return possible_moves

    def evaluate_board(self, board: BoardCopy):
        # Simple evaluation: sum of piece values
        piece_values = {
            'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0
        }
        
        value = 0
        for square in board.squares:
            if square.occupying_piece is not None:
                piece_notation = square.occupying_piece.notation.upper()
                if piece_notation in piece_values:
                    if square.occupying_piece.color == self.color:
                        value += piece_values[piece_notation]
                    else:
                        value -= piece_values[piece_notation]
        return value
    
    def print_board(self, board: BoardCopy):
    # Assuming board.squares is a flat list of Square objects
        size = int(len(board.squares) ** 0.5)  # Assuming a square board (e.g., 8x8)
        for i in range(size):
            for j in range(size):
                square = board.squares[i * size + j]  # Access the square by index
                if square.occupying_piece is not None:
                    print(square.occupying_piece.notation, end=' ')
                else:
                    print('-', end=' ')
            print()  # New line after each row
        print()  # Extra line for better readability