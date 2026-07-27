from dataclasses import dataclass, field
from typing import Tuple, Union, Literal, Optional, Dict, List

from minir_datastructs.enum.enum_string_description import EnumStringDescription
from minir_datastructs.enum.enum_string_aliases_description import EnumStringAliasesDescription







class CommentSymbolOneLine(EnumStringDescription):
    # MEMBER_NAME = (key_string, unique_int_value, symbol_string)
    NONE =                      ("none",                          0, "")
    DOUBLE_SLASH =              ("double_slash",                  1, "//")       # C, C++, Java, C#, JS, TS, Go, Rust, Swift, Scala, Kotlin, PHP
    HASH =                      ("hash",                          2, "#")        # Python, Ruby, Perl, Shell (sh, bash, zsh), YAML, R, PowerShell, Nim, Julia
    DOUBLE_HYPHEN =             ("double_hyphen",                 3, "--")       # SQL, Ada, Haskell, Lua (prefix for block comment too)
    SEMICOLON =                 ("semicolon",                     4, ";")        # Lisp (Scheme, Common Lisp), Assembly (many), INI files, AutoHotkey, Clojure
    REM =                       ("rem_keyword",                   5, "REM")      # Batch files (DOS/Windows), BASIC (older versions)
    ASTERISK_COLUMN_SPECIFIC =  ("asterisk_column_specific",      6, "*")        # COBOL (column 7), FORTRAN (fixed-form, column 1)
    PERCENT =                   ("percent",                       7, "%")        # MATLAB, LaTeX, Prolog, Erlang
    EXCLAMATION =               ("exclamation",                   8, "!")        # FORTRAN (modern free-form)
    SINGLE_QUOTE =              ("single_quote_vb",               9, "'")        # VB/VBA (Visual Basic / Visual Basic for Applications)
    APL_LAMP =                  ("apl_lamp",                     10, "⍝")       # APL
    STAR_COLUMN1 =              ("star_column1_fortran_cobol",   11, "* ")      # FORTRAN (col 1), COBOL (col 7 + space often) - more specific
    C_COLUMN1 =                 ("c_column1_fortran",            12, "C ")      # FORTRAN (col 1) - more specific
    SLASH_SLASH_SLASH =         ("triple_slash_doc",             13, "///")     # C# (XML Doc Comments), Rust (outer line doc comment)
    EXCLAMATION_RUST_DOC =      ("exclamation_rust_doc",         14, "//!")     # Rust (inner line doc comment)
    DOUBLE_ASTERISK_JAVADOC =   ("double_asterisk_javadoc_start",15, "/**")    # JavaDoc/JSDoc/PHPDoc, etc. (often start of a multi-line, but used as prefix)
    AT_SIGN =                   ("at_sign_batch",                16, "@")       # Batch files (often with ECHO OFF)
    SLASH_ASTERISK_DELPHI =     ("slash_asterisk_delphi",        17, "//")      # Delphi uses // as well




class CommentSymbolMultiLine(EnumStringAliasesDescription):
    # MEMBER_NAME = (key_string, unique_int_value, start_symbol_string, end_symbol_string)
    NONE =                          ("none",                             0, "", "")
    SLASH_ASTERISK =                ("slash_asterisk",                   1, "/*", "*/")          # C, C++, Java, C#, JS, TS, Go, Rust, Swift, Scala, Kotlin, CSS, SQL (some), PHP, PL/I
    HTML_XML_SGML =                 ("html_xml_sgml",                    2, "<!--", "-->")       # HTML, XML, SGML
    PYTHON_TRIPLE_DOUBLE_QUOTE =    ("python_triple_double_quote",       3, '"""', '"""')       # Python (docstrings, used as block comments)
    PYTHON_TRIPLE_SINGLE_QUOTE =    ("python_triple_single_quote",       4, "'''", "'''")       # Python (docstrings, used as block comments)
    HASKELL_CURLY_HYPHEN =          ("haskell_curly_hyphen",             5, "{-", "-}")          # Haskell
    PASCAL_OCAML_ML_CURLY_ASTERISK =("pascal_ocaml_ml_curly_asterisk",   6, "{", "}")            # Pascal (original), Modula-2 (some dialects use this over paren-asterisk)
    PASCAL_OCAML_ML_PAREN_ASTERISK =("pascal_ocaml_ml_paren_asterisk",   7, "(*", "*)")          # Pascal (most common), Delphi, Modula-2, OCaml, Standard ML, F#
    LUA_DOUBLE_HYPHEN_BRACKET =     ("lua_double_hyphen_bracket",        8, "--[[", "]]")        # Lua (can also be `--[=[ ... ]=]`, etc.)
    SCHEME_RACKET_HASH_PIPE =       ("scheme_racket_hash_pipe",          9, "#|", "|#")          # Scheme, Racket
    RUBY_BEGIN_END =                ("ruby_begin_end",                  10, "=begin", "=end")    # Ruby (must be at start of line)
    POWERSHELL_HASH_BRACKET =       ("powershell_hash_bracket",         11, "<#", "#>")          # PowerShell
    ELIXIR_PERCENT_CURLY_DOC =      ("elixir_percent_curly_doc",        12, "%{", "}%")          # Elixir (often for module docs, can act as block comments)
    SMALLTALK_DOUBLE_QUOTE =        ("smalltalk_double_quote",          13, '"', '"')           # Smalltalk
    JULIA_HASH_EQUALS =             ("julia_hash_equals",               14, "#=", "=#")          # Julia
    NIM_HASH_BRACKET_DISCARD =      ("nim_hash_bracket_discard",        15, "#[", "]#")          # Nim (also `##[` for raw string literals that can be used as comments)
    D_SLASH_PLUS_NESTABLE =         ("d_slash_plus_nestable",           16, "/+", "+/")          # D (nestable block comments)
    MATLAB_PERCENT_BRACE =          ("matlab_percent_brace",            17, "%{", "%}")          # MATLAB
    SQL_SLASH_ASTERISK =            ("sql_slash_asterisk",              18, "/*", "*/")          # Redundant with SLASH_ASTERISK but explicit for SQL context if needed
    R_ROXYGEN_TAG =                 ("r_roxygen_tag",                   19, "#'", "")            # R (Roxygen comments, technically single-line but used for blocks)
    PERL_POD =                      ("perl_pod",                        20, "=pod", "=cut")      # Perl (Plain Old Documentation)
    C_PREPROCESSOR_IF0 =            ("c_preprocessor_if0",              21, "#if 0", "#endif")   # C/C++ (conditional compilation used for commenting out blocks)
    FORTRAN_NO_STANDARD_BLOCK =     ("fortran_no_standard_block",       22, "!<block>", "!</block>") # Placeholder, no true standard block, often line-by-line `!`
    COBOL_NO_STANDARD_BLOCK =       ("cobol_no_standard_block",         23, "*>", "<*")          # Placeholder, no true standard block, often line-by-line `*` in col 7
    LISP_HASH_SEMICOLON_BLOCK =     ("lisp_hash_semicolon_block",       24, "#;", "")            # Common Lisp (comments out the S-expression that follows) - acts like block for one form
    RUST_BLOCK_DOC_OUTER =          ("rust_block_doc_outer",            25, "/**", "*/")         # Rust outer block doc comments (like Javadoc)
    RUST_BLOCK_DOC_INNER =          ("rust_block_doc_inner",            26, "/*!", "*/")         # Rust inner block doc comments
    POSTSCRIPT_DSC =                ("postscript_dsc",                  27, "%%BeginResource", "%%EndResource") # PostScript Document Structuring Conventions (example)
    PLAINTEXT_HERE_DOC_LIKE =       ("plaintext_here_doc_like",         28, "<<COMMENT", "COMMENT") # Generic pattern for here-docs used as comments





CommentSymbol = Union[CommentSymbolOneLine, CommentSymbolMultiLine]


# Your existing Position and Range are good
@dataclass(frozen=True)
class Position:
    line: int  # 0-indexed or 1-indexed? Be consistent. Let's assume 1-indexed for user display.
    column: int # 0-indexed or 1-indexed? Let's assume 1-indexed.

@dataclass(frozen=True)
class Range:
    start: Position
    end: Position


@dataclass(frozen=True)
class CommentSyntaxDefinition:
    """
    Defines the properties of a specific comment syntax.
    Instances of this class are typically pre-defined and registered.
    """
    key: str  # Unique key, e.g., "double_slash", "python_triple_double_quote"
    type: Literal["single_line", "multi_line"]
    start_delimiter: str
    end_delimiter: Optional[str] = None  # None for single-line (implicitly newline)

    # Parsing/Extraction hints:
    is_nestable: bool = False  # e.g., /* /* */ */ or D's /+ +/
    requires_line_start: bool = False  # e.g., Ruby's =begin, Perl's =pod
    column_specific_start: Optional[int] = None  # e.g., COBOL col 7, FORTRAN col 1 or 7
    is_doc_comment: bool = False  # Is it typically used for documentation (/**, """, ///)?
    # If true, content extraction might be smarter (e.g., stripping leading asterisks)

    # Original enum member, for traceability or specific logic if needed
    source_enum_member: Optional[CommentSymbol] = None

    def __post_init__(self):
        if self.type == "single_line" and self.end_delimiter is not None:
            # Or raise warning, or auto-set to None.
            # For now, assume single_line implies end_delimiter is effectively newline
            pass
        if self.type == "multi_line" and self.end_delimiter is None:
            raise ValueError(f"Multi-line comment syntax '{self.key}' must have an end_delimiter.")



@dataclass(frozen=True)
class LanguageCommentProfile:
    language_id: str  # e.g., "python", "java", "csharp"
    file_extensions: Tuple[str, ...] # e.g., (".py", ".pyw")
    # List of keys for CommentSyntaxDefinition in the registry
    # Order might matter for parsing priority (e.g., "///" before "//")
    syntax_keys: Tuple[str, ...]

    # Optional: language-specific parsing options
    # e.g., whether triple quotes are primarily strings or comments in Python
    parser_options: Dict[str, bool] = field(default_factory=dict)




@dataclass
class ExtractedComment:
    text: str
    location: Range
    location_with_delimiter: Range
    comment_type: CommentSymbol


@dataclass
class ExtractedCommentInstance:
    """
    Represents a single extracted comment from the source code.
    """
    text_content: str  # The actual comment text, *without* delimiters.
    # For doc comments, this might be "cleaned" (e.g., leading * removed).
    raw_content: str  # The comment text, *without* delimiters, but *as it appeared* in the source.
    full_text_with_delimiters: str  # The entire comment string, *including* start and end delimiters.

    location: Range  # The Range in the source document for full_text_with_delimiters.
    content_location: Range  # The Range in the source document for just the raw_content.

    syntax_key: str  # Key of the CommentSyntaxDefinition used to find this comment.
    language_id: Optional[str] = None  # Which LanguageCommentProfile was active, if known.





