from domain.move import Move

class Position:
    x_pos: int
    y_pos: int
    size: int

    def __init__(self, x, y, size) -> None:
        self.x_pos = x
        self.y_pos = y
        self.size = size


    def add(self, move: Move) -> "Position":
        return Position(self.x_pos + move.dx, self.y_pos + move.dy, self.size)
    
    def is_valid(self) -> bool:
        if self.x_pos >= 0 and self.x_pos < self.size:
            if self.y_pos >= 0 and self.y_pos < self.size:
                return True
        return False
    
    def __eq__(self, other_pos: "Position") -> bool:
        if self.x_pos == other_pos.x_pos:
            if self.y_pos == other_pos.y_pos:
                return True
        return False