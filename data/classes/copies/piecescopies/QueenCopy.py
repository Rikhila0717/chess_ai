from data.classes.copies.PieceCopy import PieceCopy

class QueenCopy(PieceCopy):
    def __init__(self, pos, color, board_copy):
        super().__init__(pos, color, board_copy)
        self.notation = 'Q'

    def get_possible_moves(self, board_copy):
        output = []
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board_copy.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_north)
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board_copy.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board_copy.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_east)
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board_copy.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board_copy.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_south)
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board_copy.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board_copy.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_west)
        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board_copy.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)
        return output