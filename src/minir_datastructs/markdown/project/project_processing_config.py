from dataclasses import dataclass, field
from typing import Set, Optional

from minir_datastructs.markdown.language.language_kind import ALL_EXTENSION_SET
from minir_datastructs.project.constants import STANDARD_GIT_IGNORE_PATTERNS

from .project_post_processing_config import ProjectPostProcessingConfig




@dataclass(frozen=True)
class ProjectProcessingConfig:
    """Configuration for processing a single project."""
    project_path_abs: str
    target_extensions: Set[str] = field(default_factory=lambda: set(ALL_EXTENSION_SET))
    standard_ignore_rules: Set[str] = field(default_factory=lambda: set(STANDARD_GIT_IGNORE_PATTERNS))
    index: int = 0
    post_processing: ProjectPostProcessingConfig = None
    project_name: Optional[str] = None