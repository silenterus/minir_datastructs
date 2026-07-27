
from dataclasses import dataclass, field
import struct

from minir_datastructs.manager.constants import HEADER_FORMAT, HEADER_SIZE


@dataclass(frozen=True)
class PipeReadConfig:
    """
    Configuration for reading from the pipe, specifically for message framing.
    This dataclass represents immutable configuration data.
    `frozen=True` ensures instances are immutable, aligning with DOP principles.
    """
    header_format: str = HEADER_FORMAT
    max_chunk_read_size: int = HEADER_SIZE

    @property
    def header_size(self) -> int:
        """Calculates header size based on the header_format. Purely derived data."""
        return struct.calcsize(self.header_format)
