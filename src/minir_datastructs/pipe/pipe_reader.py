
from dataclasses import dataclass, field, replace

# --- Intra-Package Imports ---
from .pipe_read_config import PipeReadConfig
from .pipe_reader_state import PipeReaderState




@dataclass(frozen=True)
class PipeReader:
    """
    A composite data structure bundling the current state and configuration of the pipe reader.
    This is passed to functions that need both pieces of information.
    """
    state: PipeReaderState
    config: PipeReadConfig


   # You could also add more specific "updater" methods if you prefer:
    def update_state(self, new_state: PipeReaderState) -> 'PipeReader':
        """
        Creates a new PipeReader instance with an updated state.
        """
        return replace(self, state=new_state)

    def update_config(self, new_config: PipeReadConfig) -> 'PipeReader':
        """
        Creates a new PipeReader instance with an updated config.
        """
        return replace(self, config=new_config)