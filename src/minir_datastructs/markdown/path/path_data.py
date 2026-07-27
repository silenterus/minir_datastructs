from dataclasses import dataclass

from .path_column_position_kind import PathColumnPositionKind
from minir_datastructs.markdown.path.path_position_kind import PathPositionKind


@dataclass
class PathData:
    content: str
    position: PathPositionKind
    column_position: PathColumnPositionKind

    def __repr__(self) -> str:
        return f"PathData(content='{self.content}', position={self.position.name}, column_position={self.column_position.name})"



