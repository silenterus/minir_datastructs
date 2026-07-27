import re
from typing import Pattern

VALID_PATH_CHARS_REVERSE_PATTERN_OLD: Pattern[str] = re.compile(r"[\w\-\.\/\\]|[~$:\{\}]")




CODE_BLOCK_RE_OLD: Pattern[str] = re.compile(
    r"^(?P<indent> *)(?P<fence_start>(?P<fence_char>[`~])(?P=fence_char){1,})"
    r"[ \t]*(?P<attributes>[^\n]*?)[ \t]*\n"
    r"(?P<content>(?:.|\n)*?)"
    r"\n(?P=indent)(?P=fence_start)[ \t]*$",
    flags=re.MULTILINE  | re.UNICODE
)




# --- Consolidated Helper Regexes ---
RE_LINE_HIGHLIGHTS_OLD = re.compile(r"^\s*(\{[\d\s,-]+\})(.*)")
RE_VALID_HIGHLIGHT_CONTENT_OLD = re.compile(r"^[\d\s,-]+$")
RE_PANDOC_BLOCK_OLD = re.compile(r"^\s*(\{.*?\})(.*)")




RE_LANGUAGE_TOKEN_OLD: Pattern[str] = re.compile(r"^([\w+\-#\.]+)(.*)", re.UNICODE) # \w includes numbers and underscore

RE_MDX_PROP_PARSER_OLD: Pattern[str] = re.compile(
    r"""
    (?P<key>[\w.-]+) # Simpler key: word chars, dots, hyphens
    (?:
        \s*=\s*
        (?P<value>
            "(?:[^"\\]|\\.)*" |  # Double-quoted string
            '(?:[^'\\]|\\.)*' |  # Single-quoted string
            (?:true|false)     |  # Booleans (lowercase only)
            [+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)? | # Numbers
            \{[^}]*} |          # JSX-like expressions e.g. {value} - simplified
            [^\s"'=<>{}`]+       # Unquoted value (cannot contain spaces etc.)
        )
    )?
    """,
    re.VERBOSE | re.UNICODE
)



# Regexes and Mappings
RE_POTENTIAL_PATH_STR = r"""
    (?:[a-zA-Z0-9_~\-\.\$\{\}\:\%\+\@]*[\/\\][a-zA-Z0-9_~\-\.\$\{\}\:\%\+\@\/\\]*) # Path with slashes (added %,+,@)
    |
    (?:[a-zA-Z0-9_~\-\$\{\}\:\%\+\@]+\.[a-zA-Z0-9_]+) # file.extension (added %,+,@)
    |
    (?:(?:~\/)?[a-zA-Z0-9_~\-\$\{\}\:\%\+\@]+) # Simple path-like word (added %,+,@)
"""
RE_POTENTIAL_PATH: Pattern[str] = re.compile(RE_POTENTIAL_PATH_STR, re.VERBOSE | re.UNICODE)





VALID_PATH_CHARS_REVERSE_PATTERN: Pattern[str] = re.compile(
    r"[\w\-\.\/\\~$:\{\}]"  # Simplified from original "[\w\-\.\/\\]|[~$:\{\}]"
)

CODE_BLOCK_RE: Pattern[str] = re.compile(
    r"^(?P<indent> *)(?P<fence_start>(?P<fence_char>[`~])(?P=fence_char){2,})" # Changed {1,} to {2,} for standard Markdown (at least 3 fence chars)
    r"[ \t]*(?P<attributes>[^\n]*?)[ \t]*\n"
    r"(?P<content>(?:.|\n)*?)"
    r"\n(?P=indent)(?P=fence_start)[ \t]*$",
    flags=re.MULTILINE
)

RE_LANGUAGE_TOKEN: Pattern[str] = re.compile(r"^([a-zA-Z0-9_+\-#\.]+)(.*)")
RE_LINE_HIGHLIGHTS: Pattern[str] = re.compile(r"^\s*(\{[\d\s,-]+\})(.*)")
RE_VALID_HIGHLIGHT_CONTENT: Pattern[str] = re.compile(r"^[\d\s,-]+$")
RE_PANDOC_BLOCK: Pattern[str] = re.compile(r"^\s*(\{.*?\})(.*)")
RE_MDX_PROP_PARSER: Pattern[str] = re.compile(
    r"""
    (?P<key>[a-zA-Z_][\w.-]*)    # Key: starts with letter/underscore, then word chars, dots, hyphens
    (?: \s*=\s*                  # Optional equals sign surrounded by optional whitespace
        (?P<value>               # Value group
            "(?:[^"\\]|\\.)*" |  # Double-quoted string with escape sequences
            '(?:[^'\\]|\\.)*' |  # Single-quoted string with escape sequences
            (?:true|false)    |  # Boolean true/false
            [+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)? |  # Integer or floating point number
            [^\s"'=<>{}`]+       # Unquoted value (anything not space or certain delimiters)
        )
    )?                           # The entire value part is optional (for boolean-like attributes)
    """,
    re.VERBOSE | re.UNICODE
)