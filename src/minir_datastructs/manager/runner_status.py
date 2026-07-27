from enum import Enum, auto

class RunnerStatus(Enum):
    INITIALIZING = auto()
    CONNECTING = auto()
    WAITING_FOR_MANAGER = auto()
    READY = auto()
    BUSY = auto()
    SHUTTING_DOWN = auto()
    TERMINATED = auto()
    UNREACHABLE = auto()
