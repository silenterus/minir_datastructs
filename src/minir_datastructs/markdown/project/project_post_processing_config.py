from dataclasses import dataclass
from enum import Enum
from typing import List
from .post_processing_code_config import PostProcessingCodeConfig


@dataclass(frozen=True)
class ProjectPostProcessingConfig:
    active: bool = False
    code_processing: List[PostProcessingCodeConfig] = None
    compact: bool = True

