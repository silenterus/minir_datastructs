from dataclasses import dataclass
from typing import Optional

"""
flet.MainAxisAlignment
class MainAxisAlignment(Enum):
    START = "start"
    END = "end"
    CENTER = "center"
    SPACE_BETWEEN = "spaceBetween"
    SPACE_AROUND = "spaceAround"
    SPACE_EVENLY = "spaceEvenly"
flet.CrossAxisAlignment
class CrossAxisAlignment(Enum):
    START = "start"
    END = "end"
    CENTER = "center"
    STRETCH = "stretch"
    BASELINE = "baseline"
"""


@dataclass(frozen=True)
class FletPageStyleConfig:
    title: str
    vertical_alignment: str
    horizontal_alignment: str
    initial_content_text: Optional[str] = None
    icon_path_str: Optional[str] = None
    prevent_close: bool = False
    visible: bool = True
