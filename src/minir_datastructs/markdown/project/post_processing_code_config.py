from dataclasses import dataclass
from enum import Enum
from typing import List

from .post_processing_code_action import PostProcessingCodeAction
from .post_processing_remove_action import PostProcessingRemoveAction


@dataclass(frozen=True)
class PostProcessingCodeConfig:
    action: PostProcessingCodeAction
    remove: List[PostProcessingRemoveAction]
