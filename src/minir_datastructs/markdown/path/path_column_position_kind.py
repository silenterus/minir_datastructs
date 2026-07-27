import enum
import os
from dataclasses import dataclass


class PathColumnPositionKind(enum.Enum):
    START = "start"  # Path is at the start of the relevant text segment/line.
    END = "end"  # Path is at the end of the relevant text segment/line.
    MID = "mid"  # Path is in the middle of the relevant text segment/line.
    ONLY = "only"  # Path is the only content of the relevant text segment/line.
    UNKNOWN = "unknown" # Added for robustness if position cannot be determined


PATH_COLUMN_POSITION_PRIORITY = {
    PathColumnPositionKind.ONLY: 3,
    PathColumnPositionKind.START: 2,
    PathColumnPositionKind.END: 1,
    PathColumnPositionKind.MID: 0
}

