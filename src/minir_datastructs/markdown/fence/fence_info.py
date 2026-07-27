from dataclasses import dataclass, field
from typing import Optional, Dict, Any

from minir_datastructs.markdown.language.language_kind import LanguageKind
from minir_datastructs.markdown.path.path_data import PathData


@dataclass
class FenceInfo:
    language: LanguageKind = LanguageKind.TEXT
    extracted_language_tag: Optional[str] = None
    extracted_rest: Optional[str] = None
    path_data: Optional[PathData] = None
    path_data_from_fence_attribute: Optional[PathData] = None # Path explicitly defined like file="path/to/file"
    attributes: Dict[str, Any] = field(default_factory=dict) # All parsed key-value attributes

    def __post_init__(self):
        if self.extracted_rest == "":
            self.extracted_rest = None

    def __str__(self) -> str:
        parts = [f"Language: LanguageKind.{self.language.name} ({self.language.value})"]
        if self.extracted_language_tag is not None:
            parts.append(f"Extracted Tag: '{self.extracted_language_tag}'")
        if self.attributes:
            parts.append(f"Attributes: {self.attributes}")
        if self.extracted_rest is not None:
            parts.append(f"Rest of Fence (unparsed): '{self.extracted_rest}'")
        if self.path_data_from_fence_attribute:
            parts.append(f"Path from Fence Attribute: {self.path_data_from_fence_attribute.content}")
        return "\n  ".join(parts)


