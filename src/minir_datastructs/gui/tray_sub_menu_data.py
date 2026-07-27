# File: your_package/tray_sub_menu_data.py
from dataclasses import dataclass
from typing import List, Union

# No direct import of TrayMenuItemData here at the top level
from .tray_menu_separator_data import TrayMenuSeparatorData # Assuming this is not part of the cycle

@dataclass(frozen=True)
class TraySubMenuData:
    title: str
    # Use string literals for types that would cause a circular import
    items: List[Union['TrayMenuItemData', 'TrayMenuSeparatorData']]