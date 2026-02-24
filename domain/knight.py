from domain.board import Board
from domain.move import Move
from domain.position import Position

knight_moves = [Move(2,-1), Move(2,1), Move(1,2), Move(-1,2), Move(-2,1), Move(-2,-1), Move(-1,-2), Move(1,-2)]

class Knight():
    pos: Position

    def __init__(self, pos) -> None:
        self.pos = pos

    def move(self, start_pos: Position, move: Move) -> Position:
        new_x = start_pos.x_pos + move.dx
        new_y = start_pos.y_pos + move.dy

        return Position(new_x, new_y, start_pos.size)
    
    def is_valid_move(self, start_pos: Position, move: Move) -> bool:
        new_pos = start_pos.add(move)
        return new_pos.is_valid()

    def find_valid_moves(self, pos: Position, board: Board) -> list[Move]:
        valid_moves: list[Move] = []
        for moves in knight_moves:
            if self.is_valid_move(pos, moves) and board.has_not_been_visited(pos.add(moves)):
                valid_moves.append(moves)
        return valid_moves