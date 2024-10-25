from typing import Literal
from data.classes.Board import Board
from data.classes.copies.SquareCopy import SquareCopy
from data.classes.copies.piecescopies.PawnCopy import PawnCopy
from data.classes.copies.piecescopies.KingCopy import KingCopy
from data.classes.copies.piecescopies.KnightCopy import KnightCopy
from data.classes.copies.piecescopies.RookCopy import RookCopy
from data.classes.copies.piecescopies.QueenCopy import QueenCopy
from data.classes.copies.piecescopies.BishopCopy import BishopCopy



class BoardCopy:
    def __init__(self):
        self.selected_square: SquareCopy = None
        self.turn: Literal['white', 'black'] = 'white'
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.squares: list[SquareCopy] = self.generate_squares()
        self.setup_board()

    def copy_board(self, board: Board):

        self.selected_square = board.selected_square 
        self.turn = board.turn
        self.squares.clear()

        for square in board.squares:
            square_copy = SquareCopy(square.x, square.y)
            if square.occupying_piece:
                notation = square.occupying_piece.notation
                color = square.occupying_piece.color
                
                if notation == 'K':
                        square_copy.occupying_piece = KingCopy((square.x,square.y), color,self)
                elif notation == 'Q':
                        square_copy.occupying_piece = QueenCopy((square.x,square.y), color,self)
                elif notation == 'B':
                        square_copy.occupying_piece = BishopCopy((square.x,square.y), color,self)
                elif notation == 'N':
                        square_copy.occupying_piece = KnightCopy((square.x,square.y), color,self)
                elif notation == 'R':
                        square_copy.occupying_piece = RookCopy((square.x,square.y), color,self)
                elif notation == 'P':
                        square_copy.occupying_piece = PawnCopy((square.x,square.y), color,self)
            self.squares.append(square_copy)

    def generate_squares(self) -> list[SquareCopy]:
        output: list[SquareCopy] = []
        for y in range(8):
            for x in range(8):
                output.append(
                    SquareCopy(x,  y)
                )
        return output
    
    def get_square_from_pos(self, pos: tuple[float, float]) -> SquareCopy:
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_piece_from_pos(self, pos: tuple[float, float]):
        return self.get_square_from_pos(pos).occupying_piece

    def select_square(self, square: SquareCopy):
        self.selected_square = square

    def setup_board(self) -> None:
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece[1] == 'R':
                        square.occupying_piece = RookCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece[1] == 'N':
                        square.occupying_piece = KnightCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = BishopCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = QueenCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = KingCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = PawnCopy(
                            (x, y), 'white' if piece[0] == 'w' else 'black',self
                        )

    def handle_move(self, from_square: SquareCopy, to_square: SquareCopy) -> bool:
        if from_square is not None and from_square.occupying_piece is not None and from_square.occupying_piece.move(self, to_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
            return True
        else:
            return False
    
    def is_in_check(self, color: Literal['white', 'black'],
                    board_change: tuple[tuple[int, int],
                                        tuple[int, int]]=None) -> bool:
        # board_change = [(x1, y1), (x2, y2)]
        from data.classes.copies.PieceCopy import PieceCopy
        output = False
        king_pos: tuple[int, int] = None
        changing_piece: PieceCopy = None
        old_square: SquareCopy = None
        new_square: SquareCopy = None
        new_square_old_piece: PieceCopy = None
        if board_change is not None:
            for square in self.squares:
                if square.pos == board_change[0]:
                    changing_piece = square.occupying_piece
                    old_square = square
                    old_square.occupying_piece = None
            for square in self.squares:
                if square.pos == board_change[1]:
                    new_square = square
                    new_square_old_piece = new_square.occupying_piece
                    new_square.occupying_piece = changing_piece
        pieces = [
            i.occupying_piece for i in self.squares if i.occupying_piece is not None
        ]
        if changing_piece is not None:
            if changing_piece.notation == 'K':
                king_pos = new_square.pos
        if king_pos == None:
            for piece in pieces:
                if piece.notation == 'K' and piece.color == color:
                        king_pos = piece.pos
        for piece in pieces:
            if piece.color != color:
                for square in piece.attacking_squares(self):
                    if square.pos == king_pos:
                        output = True
        if board_change is not None:
            old_square.occupying_piece = changing_piece
            new_square.occupying_piece = new_square_old_piece
        return output

    # checkmate state checker
    def is_in_checkmate(self, color: Literal['white', 'black']):
        if not self.is_in_check(color):
            return False
        for piece in [i.occupying_piece for i in self.squares]:
            if piece != None and piece.color == color \
                and len(piece.get_valid_moves(self)) > 0:
                return False
        return True
