# File: your_package/tray_menu_item_data.py
from dataclasses import dataclass
from typing import Callable, Optional

# No direct import of TraySubMenuData here at the top level

@dataclass(frozen=True)
class TrayMenuItemData:
    text_provider: Callable[[], str]
    action_handler: Optional[Callable[[], None]] = None
    submenu_data: Optional['TraySubMenuData'] = None  # Use string literal
    is_default: bool = False
    is_checked_provider: Optional[Callable[[], bool]] = None