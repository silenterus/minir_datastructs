from enum import Enum, auto


class RedirectionOperator(Enum):
    """Enumeration of supported redirection and pipe operators."""
    NONE = auto()
    INPUT = auto()
    APPEND_INPUT = auto()
    OUTPUT = auto()
    APPEND_OUTPUT = auto()
    PIPE = auto()
    PARALLEL_PIPE = auto()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}.{self.name}'
