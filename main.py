
import time
from domain.board import Board
from domain.knight import Knight
from domain.position import Position
from domain.move import Move

def solve(board: Board, knight: Knight):
    start_pos: Position = knight.pos
    pos: Position = knight.pos
    performed_moves: list[Move] = []
    try_move: Move = None
    while board.has_been_solved() != True:
        try_make_move(knight, board)


def try_make_move(knight: Knight, board: Board) -> bool:
    if board.has_been_solved():
        return True

    valid_moves = knight.find_valid_moves(knight.pos, board)
    if len(valid_moves) == 0:
        return False
    
    for move in valid_moves:
        new_pos = knight.pos.add(move)
        new_knight = Knight(knight.pos.add(move))
        board.visit(new_knight.pos)
        board.visualize()
        time.sleep(0.05)
        if try_make_move(new_knight, board):
            return True
        
        board.unvisit(new_pos)

    return False


if __name__ == '__main__':
    n = 6
    start_pos = Position(0,0,n)
    chessboard = Board(n, start_pos)
    knight: Knight = Knight(start_pos)
    chessboard
    print("starting solve")
    solve(chessboard, knight)
    print("Solved")
    