from typing import Dict, Final, List, Tuple
from .redirection_operator import RedirectionOperator

PATTERN_MARKER: Final[str] = '@@@'
MARKER_LEN: Final[int] = len(PATTERN_MARKER)
OPERATORS_ORDERED: Final[List[Tuple[str, RedirectionOperator]]] = [('<<', RedirectionOperator.APPEND_INPUT), ('>>', RedirectionOperator.APPEND_OUTPUT), ('||', RedirectionOperator.PARALLEL_PIPE), ('<', RedirectionOperator.INPUT), ('>', RedirectionOperator.OUTPUT), ('|', RedirectionOperator.PIPE)]
OPERATOR_MAP: Final[Dict[str, RedirectionOperator]] = dict(OPERATORS_ORDERED)
COMMENT_BLOCKS: Final[Dict[str, str]] = {
    '<!--': '-->',
    '/*': '*/',
}
COMMENT_SINGLE_LINE: Final[Tuple[str, ...]] = ('//', '#')
COMMENT_PREFIXES: Final[Tuple[str, ...]] = tuple(COMMENT_BLOCKS.keys()) + COMMENT_SINGLE_LINE
