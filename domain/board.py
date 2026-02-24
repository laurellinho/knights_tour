
from domain.position import Position


class Board():
    board: list[list[str]]
    
    def __init__(self, size: int, start_pos: Position) -> None:
        self.board = [['[ ]'] * size for _ in range(size)] 
        self.board[start_pos.y_pos][start_pos.x_pos] = '[X]'

    def visit(self, pos: Position) -> "Board":
        self.board[pos.y_pos][pos.x_pos] = '[X]'
        return self
    
    def unvisit(self, pos: Position) -> "Board":
        self.board[pos.y_pos][pos.x_pos] = '[ ]'
        return self
    
    def has_not_been_visited(self, pos: Position) -> bool:
        if self.board[pos.y_pos][pos.x_pos] == '[ ]':
            return True
        return False

    def has_been_solved(self) -> bool:
        for rows in self.board:
            for cols in rows:
                if cols == '[X]':
                    continue
                return False
        print('Solved')
        return True
    
    def visualize(self):
        print('_______________________________')
        for rows in self.board:
            for cols in rows:
                print(cols, end="")
            print('\n')
        print('_______________________________')