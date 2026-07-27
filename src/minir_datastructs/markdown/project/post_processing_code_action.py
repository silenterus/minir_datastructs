from dataclasses import dataclass
from enum import Enum
from typing import List




class PostProcessingCodeAction(Enum):
    DECOUPLE = "decouple"
    PACK = "pack"
    UNPACK = "unpack"