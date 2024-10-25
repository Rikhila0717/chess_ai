from data.classes.copies.PieceCopy import PieceCopy

class RookCopy(PieceCopy):
    def __init__(self, pos, color, board_copy):
        super().__init__(pos, color, board_copy)
        self.notation = 'R'

    def get_possible_moves(self, board_copy):
        output = []
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board_copy.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_north)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board_copy.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_east)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board_copy.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_south)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board_copy.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_west)
        return output