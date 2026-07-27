from enum import Enum
from dataclasses import dataclass, field
from typing import Union, Tuple, Optional, Dict, cast

class CommentSymbolCategory(Enum):
    ONE_LINE = "one_line"
    MULTI_LINE = "multi_line"

class StandardCommentSymbolOneLine(Enum):
    NONE = ("none", 0, "")
    DOUBLE_SLASH = ("double_slash", 1, "//")
    HASH = ("hash", 2, "#")
    DOUBLE_HYPHEN = ("double_hyphen", 3, "--")
    SEMICOLON = ("semicolon", 4, ";")
    REM_KEYWORD = ("rem_keyword", 5, "REM")
    ASTERISK_COLUMN_SPECIFIC = ("asterisk_column_specific", 6, "*")
    PERCENT = ("percent", 7, "%")
    EXCLAMATION = ("exclamation", 8, "!")
    SINGLE_QUOTE_VB = ("single_quote_vb", 9, "'")
    APL_LAMP = ("apl_lamp", 10, "⍝")
    STAR_COLUMN1_FORTRAN_COBOL = ("star_column1_fortran_cobol", 11, "* ")
    C_COLUMN1_FORTRAN = ("c_column1_fortran", 12, "C ")
    TRIPLE_SLASH_DOC = ("triple_slash_doc", 13, "///")
    EXCLAMATION_RUST_DOC = ("exclamation_rust_doc", 14, "//!")
    DOUBLE_ASTERISK_JAVADOC_START = ("double_asterisk_javadoc_start", 15, "/**")
    AT_SIGN_BATCH = ("at_sign_batch", 16, "@")
    DOUBLE_SEMICOLON_WAT = ("double_semicolon_wat", 17, ";;")
    COLON_COLON_BATCH = ("colon_colon_batch", 18, "::")
    C_CHAR_COLUMN1_FORTRAN = ("c_char_column1_fortran", 19, "C")
    COBOL_FREE_FORM_LINE = ("cobol_free_form_line", 20, "*>")
    NIM_DOC_LINE = ("nim_doc_line", 21, "##")
    M4_DNL_LINE = ("m4_dnl_line", 23, "dnl")
    VIML_DOUBLE_QUOTE_LINE = ("viml_double_quote_line", 24, "\"")
    FORTH_BACKSLASH_EOL_LINE = ("forth_backslash_eol_line", 25, "\\ ")
    TLAPLUS_LINE = ("tlaplus_line", 26, "\\*")
    MERMAID_DOUBLE_PERCENT_LINE = ("mermaid_double_percent_line", 27, "%%")
    DOUBLE_AMPERSAND_XBASE = ("double_ampersand_xbase", 28, "&&")
    IDRIS_DOC_LINE = ("idris_doc_line", 29, "|||")
    RST_EXPLICIT_COMMENT_LINE = ("rst_explicit_comment_line", 30, ".. ")
    SLIM_SLASH_LINE = ("slim_slash_line", 31, "/")
    HAML_HYPHEN_HASH_LINE = ("haml_hyphen_hash_line", 32, "-#")
    VELOCITY_DOUBLE_HASH_LINE = ("velocity_double_hash_line", 33, "##")
    PUG_SLASH_SLASH_HYPHEN_LINE = ("pug_slash_slash_hyphen_line", 34, "//-")
    BLITZMAX_REM_LIKE_LOWER = ("blitzmax_rem_like_lower", 35, "rem")
    BLITZMAX_SINGLE_QUOTE = ("blitzmax_single_quote", 36, "'")
    ABAP_ASTERISK_LINE_START = ("abap_asterisk_line_start", 37, "*")
    ABAP_DOUBLE_QUOTE_NON_FIRST_COL = ("abap_double_quote_non_first_col", 38, "\"")
    SLASH_SLASH_SLASH_DOC = TRIPLE_SLASH_DOC
    NOTE_FOXPRO_LINE = ("note_foxpro_line", 40, "NOTE")
    NB_DOT_JLANG_LINE = ("nb_dot_jlang_line", 42, "NB.")
    JCL_DOUBLE_SLASH_STAR_LINE = ("jcl_double_slash_star_line", 43, "//*")
    DOT_BACKSLASH_DOUBLE_QUOTE_ROFF_LINE = ("dot_backslash_double_quote_roff_line", 44, ".\\\"")
    FAUST_TRIPLE_HYPHEN_DOC_LINE = ("faust_triple_hyphen_doc_line", 45, "---")
    CLARION_PIPE_LINE = ("clarion_pipe_line", 46, "|")
    HASH_SPACE_ORGMODE = ("hash_space_orgmode", 47, "# ")
    BACKSLASH_FORTH_SHEN = ("backslash_forth_shen", 48, "\\")
    EXCLAMATION_SMALLTALK_LINE = ("exclamation_smalltalk_line", 49, "!")
    BLITZMAX_REM_LIKE_TITLE = ("blitzmax_rem_like_title", 50, "Rem")

    @property
    def key_string(self) -> str:
        return cast(Tuple[str, int, str], self.value)[0]

    @property
    def unique_int_value(self) -> int:
        return cast(Tuple[str, int, str], self.value)[1]

    @property
    def symbol_string(self) -> str:
        return cast(Tuple[str, int, str], self.value)[2]

    @property
    def category(self) -> CommentSymbolCategory:
        return CommentSymbolCategory.ONE_LINE

class StandardCommentSymbolMultiLine(Enum):
    NONE = ("none", 0, "", "")
    SLASH_ASTERISK = ("slash_asterisk", 1, "/*", "*/")
    HTML_XML_SGML = ("html_xml_sgml", 2, "<!--", "-->")
    PYTHON_TRIPLE_DOUBLE_QUOTE = ("python_triple_double_quote", 3, '"""', '"""')
    PYTHON_TRIPLE_SINGLE_QUOTE = ("python_triple_single_quote", 4, "'''", "'''")
    HASKELL_CURLY_HYPHEN = ("haskell_curly_hyphen", 5, "{-", "-}")
    PASCAL_OCAML_ML_CURLY_BRACE = ("pascal_ocaml_ml_curly_brace", 6, "{", "}")
    PASCAL_OCAML_ML_PAREN_ASTERISK = ("pascal_ocaml_ml_paren_asterisk", 7, "(*", "*)")
    LUA_DOUBLE_HYPHEN_BRACKET = ("lua_double_hyphen_bracket", 8, "--[[", "]]")
    SCHEME_RACKET_HASH_PIPE = ("scheme_racket_hash_pipe", 9, "#|", "|#")
    RUBY_BEGIN_END = ("ruby_begin_end", 10, "=begin", "=end")
    POWERSHELL_HASH_BRACKET = ("powershell_hash_bracket", 11, "<#", "#>")
    SMALLTALK_DOUBLE_QUOTE_BLOCK = ("smalltalk_double_quote_block", 13, '"', '"')
    JULIA_HASH_EQUALS = ("julia_hash_equals", 14, "#=", "=#")
    NIM_HASH_BRACKET_DISCARD = ("nim_hash_bracket_discard", 15, "#[", "]#")
    D_SLASH_PLUS_NESTABLE = ("d_slash_plus_nestable", 16, "/+", "+/")
    MATLAB_PERCENT_BRACE = ("matlab_percent_brace", 17, "%{", "%}")
    PERL_POD = ("perl_pod", 20, "=pod", "=cut")
    C_PREPROCESSOR_IF0 = ("c_preprocessor_if0", 21, "#if 0", "#endif")
    RUST_BLOCK_DOC_OUTER = ("rust_block_doc_outer", 25, "/**", "*/")
    RUST_BLOCK_DOC_INNER = ("rust_block_doc_inner", 26, "/*!", "*/")
    CFML_BLOCK = ("cfml_block", 27, "<!---", "--->")
    JSX_TSX_CURLY_SLASH_ASTERISK_BLOCK = ("jsx_tsx_curly_slash_asterisk_block", 28, "{/*", "*/}")
    ASCIIDOC_BLOCK = ("asciidoc_block", 29, "////", "////")
    TWIG_COMMENT_BLOCK = ("twig_comment_block", 30, "{#", "#}") # Also Jinja
    HANDLEBARS_EXCLAMATION_BLOCK = ("handlebars_exclamation_block", 31, "{{!", "}}") # Also Mustache
    HANDLEBARS_EXCLAMATION_DASH_BLOCK = ("handlebars_exclamation_dash_block", 32, "{{!--", "--}}")
    EJS_COMMENT_BLOCK = ("ejs_comment_block", 33, "<%#", "%>")
    CMAKE_BRACKET_BLOCK = ("cmake_bracket_block", 34, "#[[", "]]")
    MAKO_DOC_BLOCK = ("mako_doc_block", 35, "<%doc>", "</%doc>")
    SMARTY_COMMENT_BLOCK = ("smarty_comment_block", 36, "{*", "*}")
    WAT_PAREN_SEMICOLON_BLOCK = ("wat_paren_semicolon_block", 37, "(;", ";)")
    RAZOR_COMMENT_BLOCK = ("razor_comment_block", 38, "@*", "*@")
    COFFEESCRIPT_BLOCK = ("coffeescript_block", 39, "###", "###")
    FORTH_PAREN_BLOCK = ("forth_paren_block", 40, "(", ")") # For GCode as well
    SAS_ASTERISK_SEMICOLON_BLOCK = ("sas_asterisk_semicolon_block", 41, "*", ";")
    VELOCITY_HASH_ASTERISK_BLOCK = ("velocity_hash_asterisk_block", 42, "#*", "*#")
    JSP_COMMENT_BLOCK = ("jsp_comment_block", 43, "<%--", "--%>") # Also ASP
    XQUERY_COMMENT_BLOCK = ("xquery_comment_block", 44, "(:", ":)")
    AUTOIT_HASH_CS_CE_BLOCK = ("autoit_hash_cs_ce_block", 45, "#cs", "#ce")
    AUTOIT_HASH_COMMENTS_BLOCK = ("autoit_hash_comments_block", 46, "#comments-start", "#comments-end")
    FREEMARKER_COMMENT_BLOCK = ("freemarker_comment_block", 47, "<#--", "-->")
    GAMS_DOLLAR_ONOFF_TEXT_BLOCK = ("gams_dollar_onoff_text_block", 48, "$ontext", "$offtext")
    INFORM7_BRACKET_BLOCK = ("inform7_bracket_block", 50, "[", "]")
    LEAN_SLASH_HYPHEN_DOC_BLOCK = ("lean_slash_hyphen_doc_block", 51, "/--", "--/")
    LEAN_SLASH_HYPHEN_COMMENT_BLOCK = ("lean_slash_hyphen_comment_block", 52, "/-", "-/")
    LIQUID_COMMENT_BLOCK = ("liquid_comment_block", 53, "{% comment %}", "{% endcomment %}")
    OCTAVE_HASH_BRACE_BLOCK = ("octave_hash_brace_block", 54, "#{", "}")
    PAPYRUS_BRACE_BLOCK = ("papyrus_brace_block", 55, "{", "}")
    SIMULA_COMMENT_KEYWORD_BLOCK = ("simula_comment_keyword_block", 56, "COMMENT", ";")
    WENYAN_SHU_YUE_BLOCK = ("wenyan_shu_yue_block", 57, "疏曰。「", "」")
    RAKU_HASH_PAREN_BLOCK = ("raku_hash_paren_block", 58, "#(", ")")
    RAKU_EMBEDDED_DOC_BLOCK = ("raku_embedded_doc_block", 59, "=begin comment", "=end comment")
    NIM_HASH_DOUBLE_BRACKET_DOC_BLOCK = ("nim_hash_double_bracket_doc_block", 60, "#[[", "]]#")
    CEYLON_TRIPLE_QUOTE_DOC_BLOCK = ("ceylon_triple_quote_doc_block", 61, "\"\"\"", "\"\"\"")
    RPM_SPEC_CHANGELOG_BLOCK = ("rpm_spec_changelog_block", 62, "%changelog", "")
    FORTH_PAREN_SPACED_BLOCK = ("forth_paren_spaced_block", 63, "( ", " )")
    PLANTUML_SLASH_APOSTROPHE_BLOCK = ("plantuml_slash_apostrophe_block", 64, "/'", "'/")
    IDRIS_DOC_BLOCK = ("idris_doc_block", 65, "{-|", "|-}")
    DHALL_DOC_BLOCK = ("dhall_doc_block", 66, "{-!-", "-!}")
    REBOL_COMMENT_BLOCK_BRACE = ("rebol_comment_block_brace", 67, "comment {", "}")
    REBOL_COMMENT_BLOCK_BRACKET = ("rebol_comment_block_bracket", 68, "comment [", "]")

    @property
    def key_string(self) -> str:
        return cast(Tuple[str, int, str, str], self.value)[0]

    @property
    def unique_int_value(self) -> int:
        return cast(Tuple[str, int, str, str], self.value)[1]

    @property
    def start_symbol_string(self) -> str:
        return cast(Tuple[str, int, str, str], self.value)[2]

    @property
    def end_symbol_string(self) -> str:
        return cast(Tuple[str, int, str, str], self.value)[3]

    @property
    def category(self) -> CommentSymbolCategory:
        return CommentSymbolCategory.MULTI_LINE

CommentSymbol = Union[StandardCommentSymbolOneLine, StandardCommentSymbolMultiLine]

@dataclass(frozen=True)
class Position:
    line: int
    column: int

    def __repr__(self) -> str:
        return f"Position(line={self.line}, column={self.column})"

@dataclass(frozen=True)
class Range:
    start: Position
    end: Position

    def __repr__(self) -> str:
        return f"Range(start={self.start}, end={self.end})"

class CommentDefinitionType(Enum):
    SINGLE_LINE = "single_line"
    MULTI_LINE = "multi_line"

@dataclass(frozen=True)
class CommentSyntaxDefinition:
    key: str
    type: CommentDefinitionType
    start_delimiter: str
    end_delimiter: Optional[str] = None
    is_nestable: bool = False
    is_doc_comment: bool = False
    requires_line_start: bool = False
    column_specific_start: Optional[int] = None

    def __post_init__(self):
        if not self.start_delimiter:
            raise ValueError(f"start_delimiter for '{self.key}' cannot be empty.")
        if self.type == CommentDefinitionType.MULTI_LINE:
            if self.end_delimiter is None or (not self.end_delimiter and self.key != "rpm_spec_changelog_block_comment_def"):
                raise ValueError(
                    f"Multi-line comment definition '{self.key}' must have a non-empty end_delimiter "
                    "or be an allowed special case (e.g., rpm_spec_changelog_block_comment_def)."
                )
        if self.column_specific_start is not None and self.column_specific_start < 1:
            raise ValueError(f"column_specific_start for '{self.key}' must be 1-indexed and positive.")

@dataclass(frozen=True)
class ExtractedCommentInstance:
    comment_type: CommentSymbol
    location: Range
    content_location: Range

    def __repr__(self) -> str:
        return (f"ExtractedCommentInstance(comment_type={self.comment_type.name}, "
                f"location={self.location}, content_location={self.content_location})")

@dataclass(frozen=True)
class LanguageCommentProfile:
    language_id: str
    syntax_keys: Tuple[str, ...]
    parser_options: Dict[str, bool] = field(default_factory=lambda: {"handle_string_literals": True})

_DEFAULT_SYNTAX_DEFINITIONS: Dict[str, CommentSyntaxDefinition] = {}
_SYNTAX_DEF_TO_COMMENT_SYMBOL_MAP: Dict[str, CommentSymbol] = {}
LANGUAGE_PROFILES_REGISTRY: Dict[str, LanguageCommentProfile] = {}

def _find_comment_symbol_for_syntax_def(syntax_def: CommentSyntaxDefinition) -> CommentSymbol:
    if syntax_def.type == CommentDefinitionType.SINGLE_LINE:
        for member in StandardCommentSymbolOneLine:
            if member.symbol_string == syntax_def.start_delimiter:
                return member
    elif syntax_def.type == CommentDefinitionType.MULTI_LINE:
        for member in StandardCommentSymbolMultiLine:
            if member.start_symbol_string == syntax_def.start_delimiter and \
               member.end_symbol_string == syntax_def.end_delimiter:
                return member
    raise ValueError(
        f"Could not find a matching CommentSymbol for syntax definition: "
        f"key='{syntax_def.key}', type='{syntax_def.type.value}', "
        f"start_delimiter='{syntax_def.start_delimiter}', end_delimiter='{syntax_def.end_delimiter or ''}'"
    )

def _initialize_comment_configurations() -> None:
    global _DEFAULT_SYNTAX_DEFINITIONS, _SYNTAX_DEF_TO_COMMENT_SYMBOL_MAP
    if _DEFAULT_SYNTAX_DEFINITIONS:
        return

    definitions_data: Dict[str, CommentSyntaxDefinition] = {
        "c_line_comment_def": CommentSyntaxDefinition(key="c_line_comment_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//"),
        "c_block_comment_def": CommentSyntaxDefinition(key="c_block_comment_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/*", end_delimiter="*/"),
        "c_block_comment_nestable_def": CommentSyntaxDefinition(key="c_block_comment_nestable_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/*", end_delimiter="*/", is_nestable=True),
        "doc_line_triple_slash_def": CommentSyntaxDefinition(key="doc_line_triple_slash_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="///", is_doc_comment=True),
        "doc_line_double_slash_bang_def": CommentSyntaxDefinition(key="doc_line_double_slash_bang_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//!", is_doc_comment=True),
        "doc_block_slash_double_asterisk_def": CommentSyntaxDefinition(key="doc_block_slash_double_asterisk_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/**", end_delimiter="*/", is_doc_comment=True),
        "doc_block_slash_asterisk_bang_def": CommentSyntaxDefinition(key="doc_block_slash_asterisk_bang_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/*!", end_delimiter="*/", is_doc_comment=True, is_nestable=True),
        "c_preprocessor_if0_block_def": CommentSyntaxDefinition(key="c_preprocessor_if0_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#if 0", end_delimiter="#endif", requires_line_start=True),
        "python_hash_line_def": CommentSyntaxDefinition(key="python_hash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="#"),
        "python_triple_double_quote_block_def": CommentSyntaxDefinition(key="python_triple_double_quote_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter='"""', end_delimiter='"""', is_doc_comment=True),
        "python_triple_single_quote_block_def": CommentSyntaxDefinition(key="python_triple_single_quote_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="'''", end_delimiter="'''", is_doc_comment=True),
        "hash_line_def": CommentSyntaxDefinition(key="hash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="#"),
        "double_hyphen_line_def": CommentSyntaxDefinition(key="double_hyphen_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="--"),
        "semicolon_line_def": CommentSyntaxDefinition(key="semicolon_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter=";"),
        "semicolon_line_requires_start_def": CommentSyntaxDefinition(key="semicolon_line_requires_start_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter=";", requires_line_start=True),
        "wat_double_semicolon_line_def": CommentSyntaxDefinition(key="wat_double_semicolon_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter=";;"),
        "rem_keyword_line_def": CommentSyntaxDefinition(key="rem_keyword_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="REM", requires_line_start=True),
        "rem_blitz_max_line_lower_def": CommentSyntaxDefinition(key="rem_blitz_max_line_lower_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="rem", requires_line_start=True),
        "rem_blitz_max_line_title_def": CommentSyntaxDefinition(key="rem_blitz_max_line_title_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="Rem", requires_line_start=True),
        "at_sign_batch_line_def": CommentSyntaxDefinition(key="at_sign_batch_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="@", requires_line_start=True),
        "batch_double_colon_line_def": CommentSyntaxDefinition(key="batch_double_colon_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="::"),
        "fortran_exclamation_line_def": CommentSyntaxDefinition(key="fortran_exclamation_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="!"),
        "fortran_fixed_c_col1_line_def": CommentSyntaxDefinition(key="fortran_fixed_c_col1_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="C", column_specific_start=1),
        "fortran_fixed_star_col1_line_def": CommentSyntaxDefinition(key="fortran_fixed_star_col1_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="*", column_specific_start=1),
        "fortran_fixed_star_spaced_line_def": CommentSyntaxDefinition(key="fortran_fixed_star_spaced_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="* ", column_specific_start=1),
        "fortran_fixed_alt_c_col1_line_def": CommentSyntaxDefinition(key="fortran_fixed_alt_c_col1_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="c", column_specific_start=1),
        "cobol_fixed_star_col7_line_def": CommentSyntaxDefinition(key="cobol_fixed_star_col7_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="*", column_specific_start=7),
        "cobol_free_form_line_def": CommentSyntaxDefinition(key="cobol_free_form_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="*>"),
        "percent_line_def": CommentSyntaxDefinition(key="percent_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="%"),
        "matlab_percent_brace_block_def": CommentSyntaxDefinition(key="matlab_percent_brace_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="%{", end_delimiter="%}", is_nestable=True),
        "vb_single_quote_line_def": CommentSyntaxDefinition(key="vb_single_quote_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="'"),
        "blitz_max_single_quote_line_def": CommentSyntaxDefinition(key="blitz_max_single_quote_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="'"),
        "apl_lamp_line_def": CommentSyntaxDefinition(key="apl_lamp_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="⍝"),
        "html_xml_block_def": CommentSyntaxDefinition(key="html_xml_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<!--", end_delimiter="-->"),
        "haskell_curly_hyphen_block_def": CommentSyntaxDefinition(key="haskell_curly_hyphen_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{-", end_delimiter="-}", is_nestable=True),
        "pascal_curly_brace_block_def": CommentSyntaxDefinition(key="pascal_curly_brace_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{", end_delimiter="}"),
        "pascal_paren_asterisk_block_def": CommentSyntaxDefinition(key="pascal_paren_asterisk_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="(*", end_delimiter="*)", is_nestable=True),
        "lua_long_bracket_block_def": CommentSyntaxDefinition(key="lua_long_bracket_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="--[[", end_delimiter="]]"),
        "scheme_hash_pipe_block_def": CommentSyntaxDefinition(key="scheme_hash_pipe_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#|", end_delimiter="|#", is_nestable=True),
        "ruby_begin_end_block_def": CommentSyntaxDefinition(key="ruby_begin_end_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="=begin", end_delimiter="=end", requires_line_start=True),
        "powershell_hash_bracket_block_def": CommentSyntaxDefinition(key="powershell_hash_bracket_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<#", end_delimiter="#>", is_nestable=True),
        "smalltalk_double_quote_block_def": CommentSyntaxDefinition(key="smalltalk_double_quote_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter='"', end_delimiter='"'),
        "julia_hash_equals_block_def": CommentSyntaxDefinition(key="julia_hash_equals_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#=", end_delimiter="=#", is_nestable=True),
        "nim_hash_line_def": CommentSyntaxDefinition(key="nim_hash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="#"),
        "nim_doc_line_def": CommentSyntaxDefinition(key="nim_doc_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="##", is_doc_comment=True),
        "nim_hash_bracket_discard_block_def": CommentSyntaxDefinition(key="nim_hash_bracket_discard_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#[", end_delimiter="]#", is_nestable=True),
        "nim_hash_double_bracket_doc_block_def": CommentSyntaxDefinition(key="nim_hash_double_bracket_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#[[", end_delimiter="]]#", is_nestable=True, is_doc_comment=True),
        "d_slash_plus_nestable_block_def": CommentSyntaxDefinition(key="d_slash_plus_nestable_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/+", end_delimiter="+/", is_nestable=True),
        "perl_pod_block_def": CommentSyntaxDefinition(key="perl_pod_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="=pod", end_delimiter="=cut", requires_line_start=True, is_doc_comment=True),
        "asciidoc_line_def": CommentSyntaxDefinition(key="asciidoc_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//"),
        "asciidoc_block_def": CommentSyntaxDefinition(key="asciidoc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="////", end_delimiter="////", requires_line_start=True),
        "rst_dot_dot_space_line_def": CommentSyntaxDefinition(key="rst_dot_dot_space_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter=".. ", requires_line_start=True),
        "wat_paren_semicolon_block_def": CommentSyntaxDefinition(key="wat_paren_semicolon_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="(;", end_delimiter=";)", is_nestable=True),
        "coffeescript_block_def": CommentSyntaxDefinition(key="coffeescript_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="###", end_delimiter="###", is_doc_comment=True),
        "cfml_block_def": CommentSyntaxDefinition(key="cfml_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<!---", end_delimiter="--->"),
        "forth_backslash_space_line_def": CommentSyntaxDefinition(key="forth_backslash_space_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="\\ "),
        "forth_paren_spaced_block_def": CommentSyntaxDefinition(key="forth_paren_spaced_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="( ", end_delimiter=" )"),
        "tlaplus_line_def": CommentSyntaxDefinition(key="tlaplus_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="\\*"),
        "xquery_block_def": CommentSyntaxDefinition(key="xquery_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="(:", end_delimiter=":)", is_nestable=True),
        "plantuml_single_quote_line_def": CommentSyntaxDefinition(key="plantuml_single_quote_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="'"),
        "plantuml_slash_apostrophe_block_def": CommentSyntaxDefinition(key="plantuml_slash_apostrophe_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/'", end_delimiter="'/"),
        "idris_doc_line_def": CommentSyntaxDefinition(key="idris_doc_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="|||", is_doc_comment=True),
        "idris_doc_block_def": CommentSyntaxDefinition(key="idris_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{-|", end_delimiter="|-}", is_nestable=True, is_doc_comment=True),
        "dhall_doc_block_def": CommentSyntaxDefinition(key="dhall_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{-!-", end_delimiter="-!}", is_nestable=True, is_doc_comment=True),
        "cmake_bracket_block_def": CommentSyntaxDefinition(key="cmake_bracket_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#[[", end_delimiter="]]"),
        "jsp_block_def": CommentSyntaxDefinition(key="jsp_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<%--", end_delimiter="--%>"),
        "razor_block_def": CommentSyntaxDefinition(key="razor_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="@*", end_delimiter="*@"),
        "smarty_block_def": CommentSyntaxDefinition(key="smarty_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{*", end_delimiter="*}"),
        "twig_block_def": CommentSyntaxDefinition(key="twig_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{#", end_delimiter="#}"),
        "freemarker_block_def": CommentSyntaxDefinition(key="freemarker_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<#--", end_delimiter="-->"),
        "velocity_double_hash_line_def": CommentSyntaxDefinition(key="velocity_double_hash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="##"),
        "velocity_hash_asterisk_block_def": CommentSyntaxDefinition(key="velocity_hash_asterisk_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#*", end_delimiter="*#"),
        "mako_doc_block_def": CommentSyntaxDefinition(key="mako_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<%doc>", end_delimiter="</%doc>", is_doc_comment=True),
        "liquid_comment_block_def": CommentSyntaxDefinition(key="liquid_comment_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{% comment %}", end_delimiter="{% endcomment %}"),
        "handlebars_comment_block_def": CommentSyntaxDefinition(key="handlebars_comment_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{{!--", end_delimiter="--}}"),
        "mustache_comment_block_def": CommentSyntaxDefinition(key="mustache_comment_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{{!", end_delimiter="}}"),
        "m4_dnl_line_def": CommentSyntaxDefinition(key="m4_dnl_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="dnl", requires_line_start=True),
        "viml_double_quote_line_def": CommentSyntaxDefinition(key="viml_double_quote_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter='"', requires_line_start=True),
        "mermaid_double_percent_line_def": CommentSyntaxDefinition(key="mermaid_double_percent_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="%%"),
        "slim_slash_line_def": CommentSyntaxDefinition(key="slim_slash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="/", requires_line_start=True),
        "haml_hyphen_hash_line_def": CommentSyntaxDefinition(key="haml_hyphen_hash_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="-#", requires_line_start=True),
        "pug_unbuffered_line_def": CommentSyntaxDefinition(key="pug_unbuffered_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//"),
        "pug_silent_block_starter_line_def": CommentSyntaxDefinition(key="pug_silent_block_starter_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//-"),
        "sas_asterisk_semicolon_block_def": CommentSyntaxDefinition(key="sas_asterisk_semicolon_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="*", end_delimiter=";", requires_line_start=True), # requires_line_start added
        "rebol_comment_brace_block_def": CommentSyntaxDefinition(key="rebol_comment_brace_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="comment {", end_delimiter="}"),
        "rebol_comment_bracket_block_def": CommentSyntaxDefinition(key="rebol_comment_bracket_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="comment [", end_delimiter="]"),
        "abap_asterisk_line_def": CommentSyntaxDefinition(key="abap_asterisk_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="*", requires_line_start=True),
        "abap_double_quote_line_non_col1_def": CommentSyntaxDefinition(key="abap_double_quote_line_non_col1_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter='"'),
        "rpm_spec_changelog_block_comment_def": CommentSyntaxDefinition(key="rpm_spec_changelog_block_comment_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="%changelog", end_delimiter="", requires_line_start=True),
        "jsx_tsx_curly_slash_asterisk_def": CommentSyntaxDefinition(key="jsx_tsx_curly_slash_asterisk_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{/*", end_delimiter="*/}"),
        "autoit_hash_cs_ce_block_def": CommentSyntaxDefinition(key="autoit_hash_cs_ce_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#cs", end_delimiter="#ce"),
        "autoit_hash_comments_block_def": CommentSyntaxDefinition(key="autoit_hash_comments_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#comments-start", end_delimiter="#comments-end"),
        "gams_dollar_onoff_text_block_def": CommentSyntaxDefinition(key="gams_dollar_onoff_text_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="$ontext", end_delimiter="$offtext", requires_line_start=True),
        "gcode_paren_block_def": CommentSyntaxDefinition(key="gcode_paren_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="(", end_delimiter=")"),
        "inform7_bracket_block_def": CommentSyntaxDefinition(key="inform7_bracket_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="[", end_delimiter="]", is_doc_comment=True),
        "lean_slash_hyphen_doc_block_def": CommentSyntaxDefinition(key="lean_slash_hyphen_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/--", end_delimiter="--/", is_doc_comment=True, is_nestable=True),
        "lean_slash_hyphen_comment_block_def": CommentSyntaxDefinition(key="lean_slash_hyphen_comment_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="/-", end_delimiter="-/", is_nestable=True),
        "octave_hash_brace_block_def": CommentSyntaxDefinition(key="octave_hash_brace_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#{", end_delimiter="}", is_nestable=True),
        "papyrus_brace_block_def": CommentSyntaxDefinition(key="papyrus_brace_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="{", end_delimiter="}", requires_line_start=True),
        "simula_comment_keyword_block_def": CommentSyntaxDefinition(key="simula_comment_keyword_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="COMMENT", end_delimiter=";"),
        "wenyan_shu_yue_block_def": CommentSyntaxDefinition(key="wenyan_shu_yue_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="疏曰。「", end_delimiter="」", is_doc_comment=True),
        "raku_hash_paren_block_def": CommentSyntaxDefinition(key="raku_hash_paren_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="#(", end_delimiter=")"),
        "raku_embedded_doc_block_def": CommentSyntaxDefinition(key="raku_embedded_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="=begin comment", end_delimiter="=end comment", requires_line_start=True, is_doc_comment=True),
        "ceylon_triple_quote_doc_block_def": CommentSyntaxDefinition(key="ceylon_triple_quote_doc_block_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="\"\"\"", end_delimiter="\"\"\"", is_doc_comment=True),
        "note_foxpro_line_def": CommentSyntaxDefinition(key="note_foxpro_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="NOTE", requires_line_start=True),
        "double_ampersand_xbase_line_def": CommentSyntaxDefinition(key="double_ampersand_xbase_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="&&"),
        "nb_dot_jlang_line_def": CommentSyntaxDefinition(key="nb_dot_jlang_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="NB."),
        "jcl_double_slash_star_line_def": CommentSyntaxDefinition(key="jcl_double_slash_star_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//*", requires_line_start=True),
        "dot_backslash_double_quote_roff_line_def": CommentSyntaxDefinition(key="dot_backslash_double_quote_roff_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter=".\\\"", requires_line_start=True),
        "faust_triple_hyphen_doc_line_def": CommentSyntaxDefinition(key="faust_triple_hyphen_doc_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="---", is_doc_comment=True),
        "clarion_pipe_line_def": CommentSyntaxDefinition(key="clarion_pipe_line_def", type=CommentDefinitionType.SINGLE_LINE, start_delimiter="|", requires_line_start=True),
        "ejs_block_comment_def": CommentSyntaxDefinition(key="ejs_block_comment_def", type=CommentDefinitionType.MULTI_LINE, start_delimiter="<%#", end_delimiter="%>")
    }
    _DEFAULT_SYNTAX_DEFINITIONS = definitions_data

    temp_map: Dict[str, CommentSymbol] = {}
    for syntax_def_val in _DEFAULT_SYNTAX_DEFINITIONS.values():
        try:
            temp_map[syntax_def_val.key] = _find_comment_symbol_for_syntax_def(syntax_def_val)
        except ValueError as e:
            raise RuntimeError(f"Initialization Error: Failed to map syntax definitions. {e}") from e
    _SYNTAX_DEF_TO_COMMENT_SYMBOL_MAP = temp_map

def _populate_language_profiles_registry() -> None:
    global LANGUAGE_PROFILES_REGISTRY
    if LANGUAGE_PROFILES_REGISTRY:
        return

    def create_profile(lang_id: str, syntax_keys: Tuple[str, ...], handle_strings: bool = True):
        options = {"handle_string_literals": handle_strings}
        return LanguageCommentProfile(language_id=lang_id, syntax_keys=syntax_keys, parser_options=options)

    c_style_base_defs = ("c_line_comment_def", "c_block_comment_def")
    c_style_doc_defs = c_style_base_defs + ("doc_block_slash_double_asterisk_def", "doc_line_triple_slash_def")
    c_style_nestable_block_defs = ("c_line_comment_def", "c_block_comment_nestable_def")
    rust_style_full_defs = ("c_line_comment_def", "c_block_comment_nestable_def", "doc_line_triple_slash_def", "doc_line_double_slash_bang_def", "doc_block_slash_double_asterisk_def", "doc_block_slash_asterisk_bang_def")

    profiles = [
        create_profile("python", ("python_hash_line_def", "python_triple_double_quote_block_def", "python_triple_single_quote_block_def")),
        create_profile("csharp", c_style_doc_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("c", c_style_base_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("cpp", c_style_doc_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("java", c_style_doc_defs),
        create_profile("javascript", c_style_doc_defs),
        create_profile("typescript", c_style_doc_defs),
        create_profile("jsx", c_style_doc_defs + ("jsx_tsx_curly_slash_asterisk_def",)),
        create_profile("tsx", c_style_doc_defs + ("jsx_tsx_curly_slash_asterisk_def",)),
        create_profile("go", c_style_base_defs),
        create_profile("rust", rust_style_full_defs),
        create_profile("swift", ("c_line_comment_def", "c_block_comment_nestable_def", "doc_line_triple_slash_def")),
        create_profile("kotlin", c_style_doc_defs),
        create_profile("scala", c_style_doc_defs),
        create_profile("php", ("c_line_comment_def", "hash_line_def", "c_block_comment_def", "doc_block_slash_double_asterisk_def")),
        create_profile("html", ("html_xml_block_def",), handle_strings=False),
        create_profile("xml", ("html_xml_block_def",), handle_strings=False),
        create_profile("svg", ("html_xml_block_def",), handle_strings=False),
        create_profile("css", ("c_block_comment_def",), handle_strings=True),
        create_profile("less", ("c_line_comment_def", "c_block_comment_def"), handle_strings=True),
        create_profile("sass", ("c_line_comment_def", "c_block_comment_nestable_def"), handle_strings=True),
        create_profile("stylus", ("c_line_comment_def", "c_block_comment_nestable_def"), handle_strings=True),
        create_profile("sql", ("double_hyphen_line_def", "c_block_comment_def")),
        create_profile("plsql", ("double_hyphen_line_def", "c_block_comment_def")),
        create_profile("tsql", ("double_hyphen_line_def", "c_block_comment_def")),
        create_profile("yaml", ("hash_line_def",), handle_strings=False),
        create_profile("json", ("c_line_comment_def", "c_block_comment_def"), handle_strings=False),
        create_profile("json5", ("c_line_comment_def", "c_block_comment_def"), handle_strings=True),
        create_profile("toml", ("hash_line_def",), handle_strings=False),
        create_profile("ini", ("semicolon_line_requires_start_def", "hash_line_def"), handle_strings=False),
        create_profile("unreal_config_ini", ("semicolon_line_requires_start_def",), handle_strings=False),
        create_profile("editorconfig", ("hash_line_def", "semicolon_line_requires_start_def"), handle_strings=False),
        create_profile("dotenv", ("hash_line_def",), handle_strings=False),
        create_profile("properties", ("hash_line_def", "fortran_exclamation_line_def"), handle_strings=False),
        create_profile("git_ignore", ("hash_line_def",), handle_strings=False),
        create_profile("assembly", ("semicolon_line_def", "hash_line_def", "c_block_comment_def")),
        create_profile("bash", ("hash_line_def",)),
        create_profile("shell", ("hash_line_def",)),
        create_profile("zsh", ("hash_line_def",)),
        create_profile("dockerfile", ("hash_line_def",), handle_strings=False),
        create_profile("makefile", ("hash_line_def",), handle_strings=False),
        create_profile("cmake", ("hash_line_def", "cmake_bracket_block_def")),
        create_profile("terraform", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("ada", ("double_hyphen_line_def",)),
        create_profile("cobol", ("cobol_fixed_star_col7_line_def", "cobol_free_form_line_def")),
        create_profile("fortran", ("fortran_exclamation_line_def", "fortran_fixed_c_col1_line_def", "fortran_fixed_star_col1_line_def", "fortran_fixed_alt_c_col1_line_def", "fortran_fixed_star_spaced_line_def")),
        create_profile("pascal", ("c_line_comment_def", "pascal_curly_brace_block_def", "pascal_paren_asterisk_block_def")),
        create_profile("delphi", ("c_line_comment_def", "pascal_curly_brace_block_def", "pascal_paren_asterisk_block_def")),
        create_profile("object_pascal", ("c_line_comment_def", "pascal_curly_brace_block_def", "pascal_paren_asterisk_block_def")),
        create_profile("lua", ("double_hyphen_line_def", "lua_long_bracket_block_def")),
        create_profile("perl", ("hash_line_def", "perl_pod_block_def")),
        create_profile("powershell", ("hash_line_def", "powershell_hash_bracket_block_def")),
        create_profile("r", ("hash_line_def",)),
        create_profile("ruby", ("hash_line_def", "ruby_begin_end_block_def")),
        create_profile("dart", ("c_line_comment_def", "c_block_comment_def", "doc_line_triple_slash_def", "doc_block_slash_double_asterisk_def")),
        create_profile("groovy", ("c_line_comment_def", "c_block_comment_def", "doc_block_slash_double_asterisk_def")),
        create_profile("haskell", ("double_hyphen_line_def", "haskell_curly_hyphen_block_def")),
        create_profile("clojure", ("semicolon_line_def",)),
        create_profile("common_lisp", ("semicolon_line_def", "scheme_hash_pipe_block_def")),
        create_profile("scheme", ("semicolon_line_def", "scheme_hash_pipe_block_def")),
        create_profile("racket", ("semicolon_line_def", "scheme_hash_pipe_block_def")),
        create_profile("emacs_lisp", ("semicolon_line_def", "scheme_hash_pipe_block_def")),
        create_profile("elixir", ("hash_line_def",)),
        create_profile("erlang", ("percent_line_def",)),
        create_profile("julia", ("hash_line_def", "julia_hash_equals_block_def")),
        create_profile("nim", ("nim_hash_line_def", "nim_doc_line_def", "nim_hash_bracket_discard_block_def", "nim_hash_double_bracket_doc_block_def")),
        create_profile("ocaml", ("pascal_paren_asterisk_block_def",)),
        create_profile("fsharp", ("c_line_comment_def", "pascal_paren_asterisk_block_def", "doc_line_triple_slash_def")),
        create_profile("matlab", ("percent_line_def", "matlab_percent_brace_block_def")),
        create_profile("octave", ("percent_line_def", "hash_line_def", "matlab_percent_brace_block_def", "octave_hash_brace_block_def")),
        create_profile("latex", ("percent_line_def",), handle_strings=False),
        create_profile("tex_plain", ("percent_line_def",), handle_strings=False),
        create_profile("bibtex", ("percent_line_def",), handle_strings=False),
        create_profile("prolog", ("percent_line_def", "c_block_comment_def")),
        create_profile("objectivec", c_style_doc_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("markdown", ("html_xml_block_def",), handle_strings=False),
        create_profile("restructuredtext", ("rst_dot_dot_space_line_def",), handle_strings=False),
        create_profile("asciidoc", ("asciidoc_line_def", "asciidoc_block_def"), handle_strings=False),
        create_profile("orgmode", ("hash_line_def",), handle_strings=False),
        create_profile("bat", ("rem_keyword_line_def", "batch_double_colon_line_def", "at_sign_batch_line_def", "rem_blitz_max_line_lower_def"), handle_strings=False), # Added rem_blitz_max_line_lower_def for `rem`
        create_profile("viml", ("viml_double_quote_line_def",)),
        create_profile("m4", ("hash_line_def", "m4_dnl_line_def")),
        create_profile("coffeescript", ("hash_line_def", "coffeescript_block_def")),
        create_profile("cfml", ("cfml_block_def",)),
        create_profile("forth", ("forth_backslash_space_line_def", "forth_paren_spaced_block_def"), handle_strings=False),
        create_profile("twig", ("twig_block_def",), handle_strings=True),
        create_profile("jinja", ("twig_block_def",), handle_strings=True),
        create_profile("liquid_tpl", ("liquid_comment_block_def",), handle_strings=True),
        create_profile("handlebars", ("handlebars_comment_block_def", "mustache_comment_block_def"), handle_strings=True),
        create_profile("mustache", ("mustache_comment_block_def",), handle_strings=True),
        create_profile("ejs", ("ejs_block_comment_def",), handle_strings=True),
        create_profile("xquery", ("xquery_block_def",)),
        create_profile("asp_classic", ("vb_single_quote_line_def", "jsp_block_def"), handle_strings=True),
        create_profile("jsp", ("jsp_block_def",), handle_strings=True),
        create_profile("aspx", ("jsp_block_def", "html_xml_block_def"), handle_strings=True),
        create_profile("unreal_build_script_cs", c_style_doc_defs),
        create_profile("unreal_shader_file", c_style_base_defs),
        create_profile("unreal_shader_header", c_style_base_defs),
        create_profile("unreal_project", c_style_base_defs, handle_strings=True),
        create_profile("unreal_plugin_descriptor", c_style_base_defs, handle_strings=True),
        create_profile("verse", ("hash_line_def", "powershell_hash_bracket_block_def")),
        create_profile("text", (), handle_strings=False),
        create_profile("unknown", (), handle_strings=False),
        create_profile("diff", (), handle_strings=False),
        create_profile("csv", ("hash_line_def",), handle_strings=False),
        create_profile("tsv", ("hash_line_def",), handle_strings=False),
        create_profile("d", ("c_line_comment_def", "c_block_comment_nestable_def", "d_slash_plus_nestable_block_def", "doc_line_triple_slash_def", "doc_block_slash_double_asterisk_def", "doc_block_slash_asterisk_bang_def")),
        create_profile("hocon", ("c_line_comment_def", "hash_line_def")),
        create_profile("cypher", ("c_line_comment_def",)),
        create_profile("sparql", ("hash_line_def",)),
        create_profile("glsl", c_style_base_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("hlsl", c_style_base_defs + ("c_preprocessor_if0_block_def",)),
        create_profile("gradle", c_style_base_defs),
        create_profile("protobuf", c_style_base_defs),
        create_profile("textproto", ("hash_line_def",)),
        create_profile("kconfig", ("hash_line_def",), handle_strings=False),
        create_profile("rpm_spec", ("hash_line_def", "rpm_spec_changelog_block_comment_def"), handle_strings=False),
        create_profile("solidarity", c_style_doc_defs),
        create_profile("zig", ("c_line_comment_def",)),
        create_profile("crystal", ("hash_line_def",)),
        create_profile("haxe", c_style_doc_defs),
        create_profile("pug", ("pug_unbuffered_line_def", "pug_silent_block_starter_line_def"), handle_strings=False),
        create_profile("slim_tpl", ("slim_slash_line_def", "html_xml_block_def"), handle_strings=False),
        create_profile("haml", ("haml_hyphen_hash_line_def",), handle_strings=False),
        create_profile("mako", ("velocity_double_hash_line_def", "mako_doc_block_def"), handle_strings=True),
        create_profile("smarty_tpl", ("smarty_block_def",), handle_strings=True),
        create_profile("freemarker_tpl", ("freemarker_block_def",), handle_strings=True),
        create_profile("velocity_tpl", ("velocity_double_hash_line_def", "velocity_hash_asterisk_block_def"), handle_strings=True),
        create_profile("wren", c_style_base_defs),
        create_profile("stan", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("thrift", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("edgeql", ("hash_line_def",)),
        create_profile("rego", ("hash_line_def",)),
        create_profile("caddyfile", ("hash_line_def",), handle_strings=False),
        create_profile("webassembly_text", ("wat_double_semicolon_line_def", "wat_paren_semicolon_block_def")),
        create_profile("jenkinsfile", c_style_base_defs),
        create_profile("robot", ("hash_line_def",), handle_strings=False),
        create_profile("idris", ("double_hyphen_line_def", "idris_doc_line_def", "haskell_curly_hyphen_block_def", "idris_doc_block_def")),
        create_profile("purescript", ("double_hyphen_line_def", "haskell_curly_hyphen_block_def")),
        create_profile("elm", ("double_hyphen_line_def", "haskell_curly_hyphen_block_def")),
        create_profile("dhall", ("double_hyphen_line_def", "haskell_curly_hyphen_block_def", "dhall_doc_block_def")),
        create_profile("openscad", c_style_base_defs),
        create_profile("ant", ("html_xml_block_def",), handle_strings=False),
        create_profile("maven_pom", ("html_xml_block_def",), handle_strings=False),
        create_profile("windows_registry", ("semicolon_line_requires_start_def",), handle_strings=False),
        create_profile("jsonnet", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("gemfile", ("hash_line_def",)),
        create_profile("tcl", ("hash_line_def",)),
        create_profile("awk", ("hash_line_def",)),
        create_profile("autohotkey", ("semicolon_line_requires_start_def", "c_block_comment_def", "autoit_hash_cs_ce_block_def", "autoit_hash_comments_block_def")),
        create_profile("applescript", ("double_hyphen_line_def", "pascal_paren_asterisk_block_def")),
        create_profile("apex", c_style_doc_defs),
        create_profile("coq", ("pascal_paren_asterisk_block_def",)),
        create_profile("gamemaker_language", c_style_doc_defs),
        create_profile("hacklang", ("c_line_comment_def", "hash_line_def", "c_block_comment_def")),
        create_profile("livescript", ("hash_line_def", "c_block_comment_def")),
        create_profile("lookml", ("hash_line_def",), handle_strings=False),
        create_profile("meson", ("hash_line_def",), handle_strings=False),
        create_profile("modula2", ("pascal_paren_asterisk_block_def",)),
        create_profile("moonscript", ("double_hyphen_line_def", "lua_long_bracket_block_def")),
        create_profile("nsis", ("semicolon_line_def", "hash_line_def", "c_block_comment_def")),
        create_profile("openedge_abl", ("c_block_comment_def",)),
        create_profile("postscript", ("percent_line_def",), handle_strings=False),
        create_profile("povray_sdl", c_style_base_defs),
        create_profile("processing", c_style_doc_defs),
        create_profile("qml", c_style_base_defs),
        create_profile("raml", ("hash_line_def",), handle_strings=False),
        create_profile("reasonml", c_style_doc_defs),
        create_profile("red_lang", ("semicolon_line_def", "rebol_comment_brace_block_def", "rebol_comment_bracket_block_def")),
        create_profile("rebol", ("semicolon_line_def", "rebol_comment_brace_block_def", "rebol_comment_bracket_block_def")),
        create_profile("renpy", ("hash_line_def",)),
        create_profile("sas_lang", ("fortran_fixed_star_col1_line_def", "sas_asterisk_semicolon_block_def", "c_block_comment_def")),
        create_profile("scilab", ("c_line_comment_def",)),
        create_profile("sourcepawn", c_style_base_defs),
        create_profile("sqf", c_style_base_defs),
        create_profile("sml", ("pascal_paren_asterisk_block_def",)),
        create_profile("stata", ("fortran_fixed_star_col1_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("tla_plus", ("tlaplus_line_def", "pascal_paren_asterisk_block_def")),
        create_profile("unrealscript", c_style_doc_defs),
        create_profile("vala", c_style_doc_defs),
        create_profile("vcl", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("vbscript", ("vb_single_quote_line_def", "rem_keyword_line_def")),
        create_profile("webidl", c_style_base_defs),
        create_profile("wdl", ("hash_line_def",)),
        create_profile("yang", c_style_base_defs),
        create_profile("csound", ("semicolon_line_def", "c_block_comment_def")),
        create_profile("supercollider", c_style_doc_defs),
        create_profile("chuck", c_style_base_defs),
        create_profile("faust", ("c_line_comment_def", "faust_triple_hyphen_doc_line_def", "c_block_comment_def")),
        create_profile("blitzmax", ("blitz_max_single_quote_line_def", "rem_blitz_max_line_lower_def", "rem_blitz_max_line_title_def")),
        create_profile("boo", ("hash_line_def", "c_block_comment_def")),
        create_profile("abap", ("abap_asterisk_line_def", "abap_double_quote_line_non_col1_def")),
        create_profile("agda", ("double_hyphen_line_def", "haskell_curly_hyphen_block_def")),
        create_profile("autoit", ("semicolon_line_requires_start_def", "autoit_hash_cs_ce_block_def", "autoit_hash_comments_block_def")),
        create_profile("smalltalk", ("smalltalk_double_quote_block_def",)),
        create_profile("cabal", ("double_hyphen_line_def",), handle_strings=False),
        create_profile("clojurescript", ("semicolon_line_def",)),
        create_profile("cuda", c_style_doc_defs),
        create_profile("graphviz", ("c_line_comment_def", "c_block_comment_def", "hash_line_def")),
        create_profile("nginx", ("hash_line_def",), handle_strings=False),
        create_profile("apacheconf", ("hash_line_def",), handle_strings=False),
        create_profile("xslt_lang", ("html_xml_block_def",), handle_strings=False),
        create_profile("xsl", ("html_xml_block_def",), handle_strings=False),
        create_profile("actionscript", c_style_doc_defs),
        create_profile("ags_script", c_style_base_defs),
        create_profile("alloy", ("c_line_comment_def", "double_hyphen_line_def")),
        create_profile("angelscript", c_style_base_defs),
        create_profile("antlr", c_style_doc_defs),
        create_profile("api_blueprint", ("html_xml_block_def",), handle_strings=False),
        create_profile("asn1", ("double_hyphen_line_def",)),
        create_profile("asp", ("vb_single_quote_line_def", "jsp_block_def")),
        create_profile("aspectj", c_style_doc_defs),
        create_profile("ats", ("c_line_comment_def", "pascal_paren_asterisk_block_def")),
        create_profile("augeas", (), handle_strings=False),
        create_profile("avro_idl", c_style_base_defs),
        create_profile("ballerina", ("c_line_comment_def",)),
        create_profile("bicep", c_style_base_defs),
        create_profile("bitbake", ("hash_line_def",)),
        create_profile("blitzbasic", ("rem_blitz_max_line_lower_def", "semicolon_line_def")),
        create_profile("brightscript", ("vb_single_quote_line_def", "rem_keyword_line_def")),
        create_profile("bsv", c_style_base_defs),
        create_profile("cadence", c_style_base_defs),
        create_profile("ceylon", ("c_line_comment_def", "c_block_comment_def", "doc_block_slash_double_asterisk_def", "ceylon_triple_quote_doc_block_def")),
        create_profile("chapel", c_style_base_defs),
        create_profile("cil", c_style_base_defs),
        create_profile("clarion", ("fortran_exclamation_line_def", "clarion_pipe_line_def")),
        create_profile("clean", c_style_base_defs),
        create_profile("clipper", ("c_line_comment_def", "c_block_comment_def", "abap_asterisk_line_def", "double_ampersand_xbase_line_def")),
        create_profile("component_pascal", ("pascal_paren_asterisk_block_def",)),
        create_profile("cool", ("double_hyphen_line_def", "pascal_paren_asterisk_block_def")),
        create_profile("cue_lang", c_style_base_defs),
        create_profile("cython", ("python_hash_line_def", "python_triple_double_quote_block_def", "python_triple_single_quote_block_def")),
        create_profile("dafny", c_style_base_defs),
        create_profile("dylan", c_style_base_defs),
        create_profile("ecl", c_style_base_defs),
        create_profile("eiffel", ("double_hyphen_line_def",)),
        create_profile("factor", ("hash_line_def", "fortran_exclamation_line_def")),
        create_profile("fantom", c_style_base_defs),
        create_profile("fstar", ("c_line_comment_def", "pascal_paren_asterisk_block_def")),
        create_profile("gams", ("abap_asterisk_line_def", "gams_dollar_onoff_text_block_def")),
        create_profile("gcode", ("semicolon_line_def", "gcode_paren_block_def")),
        create_profile("gherkin", ("hash_line_def",), handle_strings=False),
        create_profile("gnuplot", ("hash_line_def",)),
        create_profile("gosu", c_style_base_defs),
        create_profile("harbour", ("c_line_comment_def", "c_block_comment_def", "abap_asterisk_line_def", "double_ampersand_xbase_line_def")),
        create_profile("idl", ("semicolon_line_def",)),
        create_profile("inform", ("fortran_exclamation_line_def", "inform7_bracket_block_def")),
        create_profile("io_lang", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("isabelle", ("pascal_paren_asterisk_block_def",)),
        create_profile("j_lang", ("nb_dot_jlang_line_def",)),
        create_profile("jcl", ("jcl_double_slash_star_line_def",)),
        create_profile("jolie", c_style_base_defs),
        create_profile("jsoniq", ("xquery_block_def",)),
        create_profile("kusto_kql", ("c_line_comment_def",)),
        create_profile("lasso", c_style_base_defs),
        create_profile("lean", ("double_hyphen_line_def", "lean_slash_hyphen_doc_block_def", "lean_slash_hyphen_comment_block_def")),
        create_profile("ligo", ("c_line_comment_def", "pascal_paren_asterisk_block_def")),
        create_profile("llvm_ir", ("semicolon_line_def",)),
        create_profile("logo", ("semicolon_line_def",)),
        create_profile("logtalk", ("percent_line_def", "c_block_comment_def")),
        create_profile("lsl", ("c_line_comment_def",)),
        create_profile("maple", ("hash_line_def",)),
        create_profile("mathematica", ("pascal_paren_asterisk_block_def",)),
        create_profile("wolfram", ("pascal_paren_asterisk_block_def",)),
        create_profile("maxscript", ("double_hyphen_line_def", "c_block_comment_def")),
        create_profile("mercury", ("percent_line_def", "c_block_comment_def")),
        create_profile("metal", c_style_base_defs),
        create_profile("modelica", c_style_base_defs),
        create_profile("modula3", ("pascal_paren_asterisk_block_def",)),
        create_profile("monkey_c", c_style_base_defs),
        create_profile("monkeyx", ("blitz_max_single_quote_line_def",)),
        create_profile("move_lang", c_style_base_defs),
        create_profile("mql", ("c_line_comment_def", "c_block_comment_def", "hash_line_def")),
        create_profile("myrddin", ("hash_line_def",)),
        create_profile("netlogo", ("semicolon_line_def",)),
        create_profile("newlisp", ("semicolon_line_def", "hash_line_def", "scheme_hash_pipe_block_def")),
        create_profile("nextflow", c_style_base_defs),
        create_profile("nu", ("semicolon_line_def", "c_block_comment_def")),
        create_profile("nunjucks_tpl", ("twig_block_def",), handle_strings=True),
        create_profile("nwscript", c_style_base_defs),
        create_profile("objectivej", c_style_base_defs),
        create_profile("odin", c_style_base_defs),
        create_profile("openclc", c_style_base_defs),
        create_profile("openqasm", ("c_line_comment_def",)),
        create_profile("oz", ("percent_line_def",)),
        create_profile("p4_lang", c_style_base_defs),
        create_profile("papyrus_script", ("semicolon_line_def", "papyrus_brace_block_def")),
        create_profile("parasail", c_style_base_defs),
        create_profile("pawn", c_style_base_defs),
        create_profile("picat", ("percent_line_def",)),
        create_profile("pico_lisp", ("hash_line_def",)),
        create_profile("pike", c_style_base_defs),
        create_profile("plantuml", ("plantuml_single_quote_line_def", "plantuml_slash_apostrophe_block_def")),
        create_profile("pony", c_style_base_defs),
        create_profile("powerbuilder", c_style_base_defs),
        create_profile("powerfx", c_style_base_defs),
        create_profile("promela", c_style_base_defs),
        create_profile("purebasic", ("semicolon_line_def",)),
        create_profile("puppet", ("hash_line_def", "c_block_comment_def")),
        create_profile("qsharp", ("c_line_comment_def", "doc_line_triple_slash_def")),
        create_profile("rexx", ("c_block_comment_def",)),
        create_profile("ring", ("hash_line_def", "c_line_comment_def", "c_block_comment_def")),
        create_profile("roff", ("dot_backslash_double_quote_roff_line_def", "hash_line_def")),
        create_profile("rpg", c_style_base_defs),
        create_profile("sas", ("abap_asterisk_line_def", "sas_asterisk_semicolon_block_def", "c_block_comment_def")),
        create_profile("seed7", ("hash_line_def", "pascal_paren_asterisk_block_def")),
        create_profile("self_lang", ("smalltalk_double_quote_block_def",)),
        create_profile("shen", ("forth_backslash_space_line_def", "pascal_paren_asterisk_block_def")),
        create_profile("simula", ("simula_comment_keyword_block_def",)),
        create_profile("smali", ("hash_line_def",)),
        create_profile("snakemake", ("hash_line_def",)),
        create_profile("snobol", ("abap_asterisk_line_def",)),
        create_profile("squirrel", c_style_base_defs),
        create_profile("starlark", ("hash_line_def",)),
        create_profile("swig", ("c_line_comment_def", "c_block_comment_def", "hash_line_def")),
        create_profile("systemverilog", c_style_base_defs),
        create_profile("tads", c_style_base_defs),
        create_profile("textile", ("html_xml_block_def",), handle_strings=False),
        create_profile("turing", ("percent_line_def",)),
        create_profile("unicon", ("hash_line_def",)),
        create_profile("urweb", ("pascal_paren_asterisk_block_def",)),
        create_profile("v", c_style_base_defs),
        create_profile("verilog", c_style_base_defs),
        create_profile("vhdl", ("double_hyphen_line_def",)),
        create_profile("visual_foxpro", ("abap_asterisk_line_def", "double_ampersand_xbase_line_def", "note_foxpro_line_def")),
        create_profile("vyper", ("hash_line_def",)),
        create_profile("wenyan", ("hash_line_def", "python_triple_single_quote_block_def", "wenyan_shu_yue_block_def")),
        create_profile("wgsl", c_style_base_defs),
        create_profile("whiley", ("c_line_comment_def",)),
        create_profile("wikitext", ("html_xml_block_def",), handle_strings=False),
        create_profile("x10", c_style_base_defs),
        create_profile("xojo", ("vb_single_quote_line_def", "c_line_comment_def", "rem_keyword_line_def")),
        create_profile("xtend", c_style_doc_defs),
        create_profile("zeek", ("hash_line_def",)),
        create_profile("zephir", c_style_base_defs),
        create_profile("zimpl", ("hash_line_def",)),
    ]

    for profile in profiles:
        LANGUAGE_PROFILES_REGISTRY[profile.language_id] = profile

    if "none" not in LANGUAGE_PROFILES_REGISTRY:
        LANGUAGE_PROFILES_REGISTRY["none"] = create_profile("none", (), handle_strings=False)

# _initialize_comment_configurations()
# _populate_language_profiles_registry()