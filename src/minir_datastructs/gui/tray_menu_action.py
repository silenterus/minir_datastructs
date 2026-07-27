from dataclasses import dataclass
from typing import Callable, Optional


@dataclass(frozen=True)
class TrayMenuAction:
    text_provider: Callable[[], str]
    action_handler: Callable[[], None]
    is_default: bool = False
    is_visible_provider: Optional[Callable[[], bool]] = None
    is_enabled_provider: Optional[Callable[[], bool]] = None
    is_checked_provider: Optional[Callable[[], bool]] = None
