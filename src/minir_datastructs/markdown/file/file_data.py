import os
from dataclasses import dataclass
from typing import Dict, Any

from minir_datastructs.markdown.language.language_kind import LanguageKind


@dataclass(frozen=True)
class FileData:
    full_path: str
    relative_path_posix: str
    content: str
    index: int = 0
    language: LanguageKind = LanguageKind.TEXT
    extension: str = "txt"  # Extension without leading dot, e.g., "txt", "py"
    stem: str = ""  # Optional
    hash: str = ""  # Optional content hash (e.g., sha256 of content)

    def as_dict(self) -> Dict[str, Any]:
        """Converts FileData to a JSON-serializable dictionary."""
        return {
            "full_path": self.full_path,
            "relative_path": self.relative_path_posix.replace('/', os.sep),  # For output, use OS sep
            "content": self.content,
            "index": self.index,
            "language": self.language.value,
            "extension": self.extension,
            "stem": self.stem,
            "hash": self.hash,
        }



