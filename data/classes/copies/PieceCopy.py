from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from data.classes.copies.BoardCopy import BoardCopy
    from data.classes.copies.SquareCopy import SquareCopy


class PieceCopy:
    def __init__(self,pos: tuple[int,int],color:Literal['white','black'],
                 board_copy: 'BoardCopy'):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.notation = ' '
        self.has_moved: bool = False

    def get_possible_moves(self) -> list[list['SquareCopy']]:
        assert(False)

    def get_moves(self,board_copy: 'BoardCopy') -> list['SquareCopy']:
        output: list[SquareCopy] = []
        for direction in self.get_possible_moves(board_copy):
            direction: list[SquareCopy]
            for square in direction:
                square: SquareCopy
                if square.occupying_piece is not None:
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square)
                        break
                else:
                    output.append(square)
        return output
    
    def get_valid_moves(self, board_copy: 'BoardCopy') -> list['SquareCopy']:
        output: list[SquareCopy] = []
        for square in self.get_moves(board_copy):
            if not board_copy.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        return output

    def move(self, board_copy: 'BoardCopy', square:'SquareCopy', force: bool=False) -> bool:
        if (square is None):
            return False
        if square in self.get_valid_moves(board_copy) or force:
            prev_square = board_copy.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board_copy.selected_square = None
            self.has_moved = True

            # Pawn promotion
            if self.notation == 'P':
                if self.y == 0 or self.y == 7:
                    from data.classes.copies.piecescopies.QueenCopy import QueenCopy
                    square.occupying_piece = QueenCopy(
                        (self.x, self.y),
                        self.color,
                        board_copy
                    )
            # Move rook if king castles
            if self.notation == 'K':
                if prev_square.x - self.x == 2:
                    rook = board_copy.get_piece_from_pos((0, self.y))
                    rook.move(board_copy, board_copy.get_square_from_pos((3, self.y)), force=True)
                elif prev_square.x - self.x == -2:
                    rook = board_copy.get_piece_from_pos((7, self.y))
                    rook.move(board_copy, board_copy.get_square_from_pos((5, self.y)), force=True)
            return True
        else:
            board_copy.selected_square = None
            return False

    # True for all pieces except pawn
    def attacking_squares(self, board_copy: 'BoardCopy') -> bool:
        return self.get_moves(board_copy)