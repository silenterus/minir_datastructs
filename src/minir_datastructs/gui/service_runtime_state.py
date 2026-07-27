import threading
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ServiceRuntimeState:
    thread: Optional[threading.Thread] = None
    stop_event: threading.Event = field(default_factory=threading.Event)
    is_active: bool = False
