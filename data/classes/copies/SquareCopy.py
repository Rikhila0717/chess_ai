from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.classes.copies.PieceCopy import PieceCopy

class SquareCopy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y  = y
        self.pos = (x, y)
        self.init_piece()
    def init_piece(self):
        self.occupying_piece: PieceCopy = None