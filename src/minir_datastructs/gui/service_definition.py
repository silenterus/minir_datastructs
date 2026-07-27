import threading
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ServiceDefinition:
    name: str
    target_loop_func: Callable[[threading.Event], None]
