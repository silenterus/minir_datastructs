from typing import NamedTuple, Optional

from .redirection_operator import RedirectionOperator






class ProcessedContent(NamedTuple):
    """Structure holding the result of the transformation."""
    cleaned_source: str
    operation: Optional[RedirectionOperator]
    data: Optional[str]

    def __repr__(self) -> str:
        op_repr = f'{self.operation}' if self.operation else 'None'
        data_repr = f'{self.data!r}' if self.data is not None else 'None'
        return f'ProcessedContent(cleaned_source={self.cleaned_source!r}, operation={op_repr}, data={data_repr})'
