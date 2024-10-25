from data.classes.copies.PieceCopy import PieceCopy

class KingCopy(PieceCopy):
    def __init__(self, pos, color, board_copy):
        super().__init__(pos, color, board_copy)
        self.notation = 'K'

    def get_possible_moves(self, board_copy):
        output = []
        moves = [
            (0,-1), # north
            (1, -1), # ne
            (1, 0), # east
            (1, 1), # se
            (0, 1), # south
            (-1, 1), # sw
            (-1, 0), # west
            (-1, -1), # nw
        ]
        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if (
                new_pos[0] < 8 and
                new_pos[0] >= 0 and 
                new_pos[1] < 8 and 
                new_pos[1] >= 0
            ):
                output.append([
                    board_copy.get_square_from_pos(
                        new_pos
                    )
                ])
        return output

    def can_castle(self, board_copy):
        if not self.has_moved:
            if self.color == 'white':
                queenside_rook = board_copy.get_piece_from_pos((0, 7))
                kingside_rook = board_copy.get_piece_from_pos((7, 7))
                if queenside_rook != None:
                    if not queenside_rook.has_moved:
                        if [
                            board_copy.get_piece_from_pos((i, 7)) for i in range(1, 4)
                        ] == [None, None, None]:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved:
                        if [
                            board_copy.get_piece_from_pos((i, 7)) for i in range(5, 7)
                        ] == [None, None]:
                            return 'kingside'
            elif self.color == 'black':
                queenside_rook = board_copy.get_piece_from_pos((0, 0))
                kingside_rook = board_copy.get_piece_from_pos((7, 0))
                if queenside_rook != None:
                    if not queenside_rook.has_moved:
                        if [
                            board_copy.get_piece_from_pos((i, 0)) for i in range(1, 4)
                        ] == [None, None, None]:
                            return 'queenside'
                if kingside_rook != None:
                    if not kingside_rook.has_moved:
                        if [
                            board_copy.get_piece_from_pos((i, 0)) for i in range(5, 7)
                        ] == [None, None]:
                            return 'kingside'

    def get_valid_moves(self, board_copy):
        output = []
        for square in self.get_moves(board_copy):
            if not board_copy.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        if self.can_castle(board_copy) == 'queenside':
            output.append(
                board_copy.get_square_from_pos((self.x - 2, self.y))
            )
        if self.can_castle(board_copy) == 'kingside':
            output.append(
                board_copy.get_square_from_pos((self.x + 2, self.y))
            )
        return output