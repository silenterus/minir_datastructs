from dataclasses import dataclass
from typing import Optional

from .main_window_kind import MainWindowKind


@dataclass(frozen=True)
class MainWindowParams:
    window_title: str
    content_text: str
    icon_path_str: Optional[str]
    assets_dir_str: str
    kind: MainWindowKind
