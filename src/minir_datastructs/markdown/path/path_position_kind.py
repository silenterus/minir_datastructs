import enum


class PathPositionKind(enum.Enum):
    FENCE_LINE = "fence_line"  # Path is on the code block's fence line itself.
    CONTENT_FIRST_LINE = "content_first_line"  # Path is on the first line of the code block's content.
    CONTENT_LAST_LINE = "content_last_line"  # Path is on the last line of the code block's content.
    CONTENT = "content"  # Path is within the code block's content (not first or last line).
    PRECEDING_FIRST_LINE = "preceding_first_line"  # Path is in the first line of prose immediately preceding the code block.
    PRECEDING_LAST_LINE = "preceding_last_line"  # Path is in the last line of prose immediately preceding the code block.
    PRECEDING = "preceding"  # Path is in any line of prose (not first/last) immediately preceding the code block.





PATH_POSITION_PRIORITY = {
    PathPositionKind.FENCE_LINE: 6,
    PathPositionKind.CONTENT_FIRST_LINE: 5,
    PathPositionKind.PRECEDING_LAST_LINE: 4,
    PathPositionKind.CONTENT_LAST_LINE: 3,
    # PathPositionKind.PRECEDING_FIRST_LINE: 2,
    # PathPositionKind.CONTENT: 1,
    # PathPositionKind.PRECEDING: 0
}