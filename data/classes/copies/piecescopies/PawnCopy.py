from data.classes.copies.PieceCopy import PieceCopy

class PawnCopy(PieceCopy):
    def __init__(self, pos, color, board_copy):
        super().__init__(pos, color, board_copy)
        self.notation = 'P'

    def get_possible_moves(self, board_copy):
        output = []
        moves = []
        # move forward
        if self.color == 'white':
            moves.append((0, -1))
            if not self.has_moved:
                moves.append((0, -2))
        elif self.color == 'black':
            moves.append((0, 1))
            if not self.has_moved:
                moves.append((0, 2))
        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0:
                output.append(
                    board_copy.get_square_from_pos(new_pos)
                )
        return output
    
    def get_moves(self, board_copy):
        output = []
        for square in self.get_possible_moves(board_copy):
            if square.occupying_piece != None:
                break
            else:
                output.append(square)
        if self.color == 'white':
            if self.x + 1 < 8 and self.y - 1 >= 0:
                square = board_copy.get_square_from_pos(
                    (self.x + 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                square = board_copy.get_square_from_pos(
                    (self.x - 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
        elif self.color == 'black':
            if self.x + 1 < 8 and self.y + 1 < 8:
                square = board_copy.get_square_from_pos(
                    (self.x + 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
            if self.x - 1 >= 0 and self.y + 1 < 8:
                square = board_copy.get_square_from_pos(
                    (self.x - 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        output.append(square)
        return output
    
    def attacking_squares(self, board_copy):
        moves = self.get_moves(board_copy)
        # return the diagonal moves 
        return [i for i in moves if i.x != self.x]