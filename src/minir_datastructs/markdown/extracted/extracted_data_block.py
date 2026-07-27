from dataclasses import dataclass
from typing import Tuple, Optional

from minir_datastructs.markdown.fence.fence_info import FenceInfo
from minir_datastructs.markdown.path.path_data import PathData


@dataclass
class ExtractedDataBlock:
    content: str
    line_range: Tuple[int, int]
    preceding_content: Optional[str]
    fence_line: Optional[str]
    fence_info: FenceInfo  = None
    primary_path: Optional[PathData] = None
