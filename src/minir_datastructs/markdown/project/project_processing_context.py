from dataclasses import dataclass
from typing import Set

import pathspec


@dataclass(frozen=True)
class ProjectProcessingContext:
    """Contextual information for processing a single project."""
    project_root_abs_path: str
    project_name: str
    ignore_spec: pathspec.PathSpec
    target_extensions: Set[str]
    index: int = 0




