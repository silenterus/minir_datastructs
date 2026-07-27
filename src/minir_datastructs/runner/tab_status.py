from enum import Enum

class TabStatus(Enum):
    IDLE = 1
    STARTING = 2
    RUNNING = 3
    FAILED = 4
    ABORTING = 5
    COMPLETED = 6
    CLOSED = 7
