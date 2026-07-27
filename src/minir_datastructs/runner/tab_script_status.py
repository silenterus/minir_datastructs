from enum import Enum

class TabScriptStatus(Enum):
    NOT_LOADED = 0
    SITE_LOADED = 1
    NEW_CHAT_CLICKED = 2
    TEXT_SUBMITTED = 3
    WAITING_FOR_TEXT = 4
    FINISHED = 5
    IDLE = 6
    ERROR = 9
