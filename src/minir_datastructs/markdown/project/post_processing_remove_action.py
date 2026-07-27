from dataclasses import dataclass
from enum import Enum
from typing import List


class PostProcessingRemoveAction(Enum):
    COMMENT = "comment"
    DOCS = "docs"
