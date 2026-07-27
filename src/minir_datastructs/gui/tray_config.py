from dataclasses import dataclass
from typing import Callable, List, Optional

from .constants import TrayItem


@dataclass(frozen=True)
class TrayConfig:
    app_name: str
    icon_image_path_str: Optional[str]
    menu_items_data: List[TrayItem]
    on_exit_callback: Callable[[], None]
