from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    line: int
    column: int

    def __repr__(self) -> str: return f"Position(line={self.line}, column={self.column})"

