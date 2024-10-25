from data.classes.copies.PieceCopy import PieceCopy

class BishopCopy(PieceCopy):
    def __init__(self, pos, color, board_copy):
        super().__init__(pos, color, board_copy)
        self.notation = 'B'

    def get_possible_moves(self, board_copy):
        output = []
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board_copy.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board_copy.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board_copy.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board_copy.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)
        return output