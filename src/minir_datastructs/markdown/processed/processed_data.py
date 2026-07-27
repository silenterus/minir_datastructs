from dataclasses import dataclass, field
from typing import Dict, Any, List, FrozenSet

from minir_datastructs.markdown.file.file_data import FileData
from minir_datastructs.markdown.language.language_kind import LanguageKind
from minir_datastructs.markdown.language.language_workspace_group_kind import LanguageWorkspaceGroupKind


@dataclass(frozen=True)
class ProcessedProjectData:
    """Represents all collected data for a single project."""
    project_name: str
    project_path_abs: str
    files: List[FileData]
    index: int = 0
    hash: str = ""  # Hash of the project data itself
    workspace_type: LanguageWorkspaceGroupKind = LanguageWorkspaceGroupKind.PYTHON
    languages: FrozenSet[LanguageKind] = field(default_factory=frozenset)

    def as_dict(self) -> Dict[str, Any]:
        """Converts ProcessedProjectData to a JSON-serializable dictionary."""
        return {
            "project_name": self.project_name,
            "project_path": self.project_path_abs,
            "files": [f.as_dict() for f in self.files],
            "index": self.index,
            "hash": self.hash,
            "workspace_type": self.workspace_type.value,
            "languages": sorted([lang.value for lang in self.languages]),
        }
