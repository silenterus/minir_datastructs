
from typing import Optional
from dataclasses import dataclass, field
from .pipe_handle import PipeHandle



@dataclass(frozen=True)
class PipeReaderState:
    """
    Represents the state of the pipe reader at a point in time.
    This dataclass is immutable (`frozen=True`). Operations that would modify
    state instead produce a new PipeReaderState instance. This is key to DOP.
    """
    pipe_handle: PipeHandle
    buffer: bytes = field(default_factory=lambda: bytes())
    expected_message_length: Optional[int] = None
