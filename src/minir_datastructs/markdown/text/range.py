from dataclasses import dataclass

from .position import Position


@dataclass(frozen=True)
class Range:
    start: Position
    end: Position

    def __repr__(self) -> str: return f"Range(start={self.start}, end={self.end})"


