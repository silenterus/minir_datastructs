from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Set, Tuple, Dict, Any, Union
from types import MappingProxyType

_FrozenDict = MappingProxyType[str, Any]
_StrTuple = Tuple[str, ...]


@dataclass(frozen=True)
class Position:
    line: int
    column: int


@dataclass(frozen=True)
class MarkdownFileData:
    path: str
    content: Optional[str] = None
    metadata: _FrozenDict = field(default_factory=lambda: MappingProxyType({}))


@dataclass(frozen=True)
class ProcessedMarkdownData:
    source_name: str
    source_path_abs: str
    markdown_files: Tuple[MarkdownFileData, ...]


class MarkdownAlignment(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    NONE = "none"


class MarkdownElementKind(Enum):
    DOCUMENT = "Document Root"
    FRONTMATTER = "Frontmatter Block (e.g., YAML, TOML, JSON)"
    HEADING = "Heading"
    PARAGRAPH = "Paragraph"
    BLOCKQUOTE = "Blockquote"
    FENCED_CODE_BLOCK = "Fenced Code Block"
    INDENTED_CODE_BLOCK = "Indented Code Block"
    ORDERED_LIST = "Ordered List"
    UNORDERED_LIST = "Unordered List"
    LIST_ITEM = "List Item"
    TASK_LIST_ITEM = "Task List Item (GFM)"
    TABLE = "Table"
    TABLE_ROW = "Table Row"
    TABLE_CELL = "Table Cell"
    HORIZONTAL_RULE = "Horizontal Rule"
    HTML_BLOCK = "HTML Block"
    HTML_COMMENT = "HTML Comment"
    LINK_REFERENCE_DEFINITION = "Link Reference Definition"
    FOOTNOTE_DEFINITION = "Footnote Definition"
    DEFINITION_LIST = "Definition List"
    DEFINITION_TERM = "Definition Term"
    DEFINITION_DESCRIPTION = "Definition Description"
    TABLE_OF_CONTENTS_PLACEHOLDER = "Table of Contents Placeholder (e.g. [TOC])"

    TEXT = "Plain Text Segment"
    LINK = "Inline Link"
    AUTOLINK = "Autolink"
    IMAGE = "Inline Image"
    INLINE_CODE = "Inline Code Span"
    EMPHASIS = "Emphasis"
    STRONG_EMPHASIS = "Strong Emphasis"
    STRIKETHROUGH = "Strikethrough"
    HTML_INLINE = "Inline HTML Tag"
    FOOTNOTE_REFERENCE = "Footnote Reference"
    SOFT_LINE_BREAK = "Soft Line Break"
    HARD_LINE_BREAK = "Hard Line Break"

    UNKNOWN = "Unknown Markdown Construct"


class MarkdownTokenType(Enum):
    TEXT = auto()
    WHITESPACE = auto()
    NEWLINE = auto()
    EOF = auto()
    UNKNOWN = auto()

    HEADING_ATX_PREFIX = auto()
    ATX_HEADING_TEXT = auto()
    SETEXT_HEADING_TEXT = auto()
    SETEXT_UNDERLINE_L1 = auto()
    SETEXT_UNDERLINE_L2 = auto()

    LIST_MARKER_UNORDERED = auto()
    LIST_MARKER_ORDERED_DIGITS = auto()
    LIST_MARKER_ORDERED_DELIM = auto()
    TASK_LIST_MARKER_UNCHECKED = auto()
    TASK_LIST_MARKER_CHECKED = auto()

    BLOCKQUOTE_PREFIX = auto()

    CODE_FENCE_START = auto()
    CODE_FENCE_END = auto()
    CODE_FENCE_INFO_STRING = auto()
    CODE_BLOCK_INDENT = auto()
    INDENTED_CHUNK = auto()
    CODE_CONTENT_LINE = auto()

    HORIZONTAL_RULE_MARKER = auto()

    TABLE_PIPE = auto()
    TABLE_HEADER_SEPARATOR_LINE_CONTENT = auto()
    TABLE_HEADER_SEPARATOR_HYPHEN = auto()
    TABLE_HEADER_SEPARATOR_COLON = auto()
    TABLE_ROW_LINE_CONTENT = auto()

    HTML_TAG_OPEN = auto()
    HTML_TAG_CLOSE = auto()
    HTML_TAG_SLASH = auto()
    HTML_TAG_NAME = auto()
    HTML_ATTRIBUTE_NAME = auto()
    HTML_ATTRIBUTE_VALUE = auto()
    HTML_COMMENT_START_DELIMITER = auto()
    HTML_COMMENT_CONTENT = auto()
    HTML_COMMENT_END_DELIMITER = auto()
    HTML_DECLARATION_START_DELIMITER = auto()
    HTML_PROCESSING_INSTRUCTION_START_DELIMITER = auto()
    HTML_CDATA_START_DELIMITER = auto()
    HTML_CDATA_END_DELIMITER = auto()
    HTML_ENTITY = auto()

    FRONTMATTER_DELIMITER = auto()
    FRONTMATTER_CONTENT_LINE = auto()

    LINK_TEXT_START_BRACKET = auto()
    LINK_TEXT_END_BRACKET = auto()
    LINK_DEST_START_PAREN = auto()
    LINK_DEST_END_PAREN = auto()
    LINK_TITLE_DELIMITER = auto()
    LINK_REF_DEF_LABEL_START = auto()
    LINK_REF_DEF_LABEL_TEXT = auto()
    LINK_REF_DEF_COLON = auto()
    LINK_REF_DEF_DESTINATION = auto()
    LINK_REF_DEF_TITLE_START = auto()
    LINK_REF_DEF_TITLE_CONTENT = auto()
    LINK_REF_DEF_TITLE_END = auto()
    LINK_REF_LABEL_START_BRACKET = auto()
    LINK_REF_LABEL_END_BRACKET = auto()

    IMAGE_PREFIX_BANG = auto()

    INLINE_CODE_DELIMITER = auto()
    EMPHASIS_ASTERISK = auto()
    EMPHASIS_UNDERSCORE = auto()
    STRONG_EMPHASIS_ASTERISK = auto()
    STRONG_EMPHASIS_UNDERSCORE = auto()
    STRIKETHROUGH_TILDE = auto()

    FOOTNOTE_REF_START_DELIMITER = auto()
    FOOTNOTE_LABEL_TEXT = auto()
    FOOTNOTE_LABEL_END_BRACKET = auto()
    FOOTNOTE_DEF_COLON = auto()

    BACKSLASH_ESCAPE = auto()
    ESCAPED_CHAR = auto()

    ATTRIBUTE_BLOCK_START = auto()
    ATTRIBUTE_BLOCK_END = auto()
    ATTRIBUTE_ID_PREFIX = auto()
    ATTRIBUTE_CLASS_PREFIX = auto()
    ATTRIBUTE_KEY_VALUE_SEPARATOR = auto()
    ATTRIBUTE_TEXT = auto()

    COLON_SEPARATOR = auto()


class MarkdownCommentType(Enum):
    HTML_STANDARD_COMMENT = "Standard HTML Comment (e.g., <!-- ... -->)"
    PARSER_DIRECTIVE_COMMENT = "Parser Directive Comment (e.g. <!-- .element: class='foo' -->)"


class MarkdownParseState(Enum):
    DEFAULT_BLOCK_CONTEXT = auto()
    IN_ATX_HEADING = auto()
    IN_SETEXT_HEADING_LINE1 = auto()
    IN_PARAGRAPH = auto()
    IN_FENCED_CODE_BLOCK_HEADER = auto()
    IN_FENCED_CODE_BLOCK_BODY = auto()
    IN_INDENTED_CODE_BLOCK = auto()
    IN_HTML_BLOCK = auto()
    IN_HTML_COMMENT_BLOCK = auto()
    IN_FRONTMATTER_BLOCK = auto()
    IN_UNORDERED_LIST = auto()
    IN_ORDERED_LIST = auto()
    IN_LIST_ITEM_CONTENT = auto()
    IN_BLOCKQUOTE = auto()
    IN_TABLE_HEADER = auto()
    IN_TABLE_SEPARATOR = auto()
    IN_TABLE_BODY = auto()
    IN_LINK_TEXT = auto()
    IN_LINK_DESTINATION_OR_TITLE = auto()
    IN_LINK_REFERENCE_DEFINITION = auto()
    IN_FOOTNOTE_DEFINITION = auto()


@dataclass(frozen=True)
class MarkdownComment:
    content: str
    full_comment_text: str
    start_pos: Position
    end_pos: Position
    type: MarkdownCommentType
    markdown_document_path: str


@dataclass(frozen=True)
class MarkdownToken:
    type: MarkdownTokenType
    value: str
    full_text: str
    start_pos: Position
    end_pos: Position
    file_data: MarkdownFileData


@dataclass(frozen=True)
class MarkdownProcessingError:
    file_data: MarkdownFileData
    error_message: str
    start_pos: Optional[Position] = None
    end_pos: Optional[Position] = None
    context_snippet: Optional[str] = None


@dataclass(frozen=True)
class ExtractedMarkdownElement:
    kind: MarkdownElementKind
    file_data: MarkdownFileData
    start_pos: Position
    end_pos: Position
    id: str = field(default_factory=lambda: f"md_elem_{uuid.uuid4().hex}")

    raw_source_text: Optional[str] = None
    children: Tuple[ExtractedMarkdownElement, ...] = field(default_factory=tuple)
    parent_id: Optional[str] = None

    main_content_start_pos: Optional[Position] = None
    main_content_end_pos: Optional[Position] = None
    hierarchical_path_labels: _StrTuple = field(default_factory=tuple)
    associated_comment: Optional[MarkdownComment] = None

    heading_level: Optional[int] = None
    heading_auto_id: Optional[str] = None

    code_language_info: Optional[str] = None
    code_content: Optional[str] = None

    list_is_ordered: Optional[bool] = None
    list_start_number: Optional[int] = None
    list_marker_type: Optional[str] = None
    list_is_tight: Optional[bool] = None

    task_list_item_checked: Optional[bool] = None

    table_alignments: Optional[Tuple[Optional[MarkdownAlignment], ...]] = None
    table_has_header: Optional[bool] = None

    is_header_row: Optional[bool] = None
    is_header_cell: Optional[bool] = None

    target_url: Optional[str] = None
    link_or_image_title: Optional[str] = None
    image_alt_text: Optional[str] = None
    is_reference_style_link_or_image: Optional[bool] = None
    link_or_image_reference_label: Optional[str] = None

    text_content_value: Optional[str] = None

    link_ref_def_label: Optional[str] = None
    link_ref_def_url: Optional[str] = None
    link_ref_def_title: Optional[str] = None

    footnote_def_label: Optional[str] = None
    footnote_ref_label: Optional[str] = None

    frontmatter_language: Optional[str] = None
    frontmatter_raw_content: Optional[str] = None
    frontmatter_parsed_data: Optional[_FrozenDict] = None

    html_tag_name: Optional[str] = None
    html_attributes: Optional[_FrozenDict] = None
    html_content_raw: Optional[str] = None
    html_comment_content: Optional[str] = None

    custom_attributes: _FrozenDict = field(default_factory=lambda: MappingProxyType({}))


class MarkdownSyntax:
    MD_HORIZONTAL_SPACE_CHARS: Set[str] = {' ', '\t'}
    MD_EOL_CHARS: Set[str] = {'\n', '\r'}
    MD_ALL_WHITESPACE_CHARS: Set[str] = MD_HORIZONTAL_SPACE_CHARS | MD_EOL_CHARS | {'\x0b', '\x0c', '\f', '\v'} # \f and \v added for completeness based on general standards

    MD_HEADING_CHAR: str = '#'
    MD_ATX_HEADING_MARKER: str = '#'
    MD_SETEXT_HEADING_L1_MARKER: str = '='
    MD_SETEXT_HEADING_L2_MARKER: str = '-'

    MD_UNORDERED_LIST_MARKERS: Set[str] = {'*', '-', '+'}
    MD_ORDERED_LIST_DELIMITERS: Set[str] = {'.', ')'}

    MD_BLOCKQUOTE_CHAR: str = '>'

    MD_FENCE_BACKTICK_STRING: str = "```"
    MD_FENCE_TILDE_STRING: str = "~~~"
    MD_FENCE_CHARS: Set[str] = {'`', '~'}
    MD_FENCED_CODE_BLOCK_DELIMITERS: Set[str] = {MD_FENCE_BACKTICK_STRING, MD_FENCE_TILDE_STRING}


    MD_HR_CHARS: Set[str] = {'*', '-', '_'}
    MD_THEMATIC_BREAK_MIN_CHARS: int = 3

    MD_CODE_SPAN_CHAR: str = '`'
    MD_EMPHASIS_CHARS: Set[str] = {'*', '_'}
    MD_EMPHASIS_ASTERISK_CHAR: str = '*' # Retained from B1 for potential specific use
    MD_EMPHASIS_UNDERSCORE_CHAR: str = '_' # Retained from B1 for potential specific use
    MD_STRONG_EMPHASIS_ASTERISK_SEQUENCE: str = '**'
    MD_STRONG_EMPHASIS_UNDERSCORE_SEQUENCE: str = '__'
    MD_STRIKETHROUGH_TILDE_SEQUENCE: str = '~~'

    MD_LINK_TEXT_START: str = '['
    MD_LINK_TEXT_END: str = ']'
    MD_LINK_URL_START: str = '('
    MD_LINK_URL_END: str = ')'
    MD_IMAGE_PREFIX: str = '!'
    MD_LINK_REFERENCE_DEFINITION_COLON: str = ':'

    MD_TABLE_PIPE_CHAR: str = '|'
    MD_TABLE_HEADER_SEP_CHAR: str = '-'
    MD_TABLE_ALIGNMENT_COLON_CHAR: str = ':'

    MD_HTML_COMMENT_START: str = "<!--"
    MD_HTML_COMMENT_END: str = "-->"
    MD_FRONTMATTER_DELIMITER_YAML: str = "---"
    MD_FRONTMATTER_DELIMITER_TOML: str = "+++"

    GFM_TASK_LIST_UNCHECKED_MARKERS: Set[str] = {"[ ]", "[ ] "}
    GFM_TASK_LIST_CHECKED_MARKERS: Set[str] = {"[x]", "[X]", "[x] ", "[X] "}
    GFM_TASK_LIST_MARKER_UNCHECKED: str = "[ ]" # Retained from B1
    GFM_TASK_LIST_MARKER_CHECKED_LOWER: str = "[x]" # Retained from B1
    GFM_TASK_LIST_MARKER_CHECKED_UPPER: str = "[X]" # Retained from B1

    MD_ESCAPE_CHAR: str = '\\'
    MD_ESCAPABLE_ASCII_PUNCTUATION: Set[str] = {
        '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    }

    HTML_VOID_ELEMENTS: Set[str] = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"
    }

    POTENTIAL_INLINE_MARKERS_START_CHARS: Set[str] = {
        '*', '_', '`', '~', '[', '!', '<'
    }
    DEFAULT_TAB_WIDTH: int = 4

    @staticmethod
    def is_markdown_horizontal_space(char: str) -> bool:
        return char in MarkdownSyntax.MD_HORIZONTAL_SPACE_CHARS

    @staticmethod
    def is_newline(char: str) -> bool:
        return char in MarkdownSyntax.MD_EOL_CHARS

    @staticmethod
    def count_leading_spaces_and_tabs(line: str, tab_width: int = DEFAULT_TAB_WIDTH) -> int:
        count = 0
        for char_val in line:
            if char_val == ' ':
                count += 1
            elif char_val == '\t':
                count += tab_width - (count % tab_width)
            else:
                break
        return count

ELEMENTS_WITHOUT_EXPLICIT_NAME_CONTENT: Set[MarkdownElementKind] = {
    MarkdownElementKind.DOCUMENT,
    MarkdownElementKind.HORIZONTAL_RULE,
    MarkdownElementKind.HTML_COMMENT,
    MarkdownElementKind.FRONTMATTER,
    MarkdownElementKind.SOFT_LINE_BREAK,
    MarkdownElementKind.HARD_LINE_BREAK,
    MarkdownElementKind.ORDERED_LIST,
    MarkdownElementKind.UNORDERED_LIST,
    MarkdownElementKind.TABLE,
    MarkdownElementKind.TABLE_ROW,
    MarkdownElementKind.DEFINITION_LIST,
    MarkdownElementKind.UNKNOWN
}