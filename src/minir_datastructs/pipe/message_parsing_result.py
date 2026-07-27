
from typing import Any, List, Optional
from dataclasses import dataclass, field



@dataclass(frozen=True)
class MessageParsingResult:
    """
    Holds the results of attempting to parse messages from a buffer.
    This is an immutable data structure representing the outcome of a pure function.
    """
    messages: List[Any] = field(default_factory=list)
    remaining_buffer: bytes = field(default_factory=lambda: bytes())
    new_expected_length: Optional[int] = None
    deserialization_errors: List[Exception] = field(default_factory=list)
