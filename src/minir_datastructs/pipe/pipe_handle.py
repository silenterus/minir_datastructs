from dataclasses import dataclass
from typing import TYPE_CHECKING

# Define a type alias
if TYPE_CHECKING:
    import pywintypes
    WindowsHandle = pywintypes.HANDLE
else:
    WindowsHandle = int

@dataclass(frozen=True)
class PipeHandle:
    """
    A wrapper for the pipe handle to provide type clarity and immutability.
    The 'value' is a Windows HANDLE.
    """
    value: WindowsHandle