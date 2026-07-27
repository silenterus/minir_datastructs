from dataclasses import dataclass
from typing import Optional

from .settings_category import SettingsCategory


@dataclass(frozen=True)
class SettingsWindowParams:
    window_title: str
    content_text: str
    icon_path_str: Optional[str]
    assets_dir_str: str
    category: SettingsCategory
