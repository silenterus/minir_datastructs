
from dataclasses import dataclass
from dataclasses import field
from typing import List

from .extracted_data_block import ExtractedDataBlock
from minir_datastructs.markdown.path.path_data import PathData


@dataclass
class ExtractedBlock:
    data: ExtractedDataBlock
    paths: List[PathData] = field(default_factory=list)
    found_paths: List[str] = field(default_factory=list)
    is_valid:bool = True









