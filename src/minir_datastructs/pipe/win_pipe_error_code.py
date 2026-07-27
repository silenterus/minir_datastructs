
from typing import Optional
from enum import Enum



class WinPipeErrorCode(Enum):
    """
    Enumeration of relevant Windows error codes for pipe operations.
    Using an Enum enhances type safety and readability when handling these codes.
    """
    ERROR_SUCCESS = 0
    ERROR_BROKEN_PIPE = 109
    ERROR_MORE_DATA = 234
    ERROR_NO_DATA = 232
    ERROR_PIPE_NOT_CONNECTED = 233

    @classmethod
    def from_winerror(cls, winerror_code: int) -> Optional['WinPipeErrorCode']:
        """Attempts to convert a windows error code integer to an enum member."""
        try:
            return cls(winerror_code)
        except ValueError:
            return None
