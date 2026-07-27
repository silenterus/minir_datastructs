from dataclasses import dataclass
from typing import Optional

from .tools_kind import ToolsKind


@dataclass(frozen=True)
class ToolsWindowParams:
    window_title: str
    content_text: str
    icon_path_str: Optional[str]
    assets_dir_str: str
    kind: ToolsKind
