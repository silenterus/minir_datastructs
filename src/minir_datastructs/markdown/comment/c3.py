from enum import Enum
from typing import Tuple, cast, Union, Optional, Dict, List
from dataclasses import dataclass, field

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
    COBOL_FREE_FORM_LINE = ("cobol_free_form_line", 17, "*>")
    NIM_DOC_LINE = ("nim_doc_line", 18, "##")
    WAT_DOUBLE_SEMICOLON_LINE = ("wat_double_semicolon_line", 19, ";;")
    M4_DNL_LINE = ("m4_dnl_line", 20, "dnl")
    VIML_DOUBLE_QUOTE_LINE = ("viml_double_quote_line", 21, "\"")
    FORTH_BACKSLASH_EOL_LINE = ("forth_backslash_eol_line", 22, "\\ ")
    TLAPLUS_LINE = ("tlaplus_line", 23, "\\*")
    MERMAID_DOUBLE_PERCENT_LINE = ("mermaid_double_percent_line", 24, "%%")
    IDRIS_DOC_LINE = ("idris_doc_line", 25, "|||")
    RST_EXPLICIT_COMMENT_LINE = ("rst_explicit_comment_line", 26, ".. ")
    SLIM_SLASH_LINE = ("slim_slash_line", 27, "/")
    HAML_HYPHEN_HASH_LINE = ("haml_hyphen_hash_line", 28, "-#")
    VELOCITY_DOUBLE_HASH_LINE = ("velocity_double_hash_line", 29, "##")
    PUG_SLASH_SLASH_HYPHEN_LINE = ("pug_slash_slash_hyphen_line", 30, "//-")
    BLITZMAX_REM_LIKE = ("blitzmax_rem_like", 31, "rem")
    BLITZMAX_SINGLE_QUOTE = ("blitzmax_single_quote", 32, "'")
    ABAP_ASTERISK_LINE_START = ("abap_asterisk_line_start", 33, "*")
    ABAP_DOUBLE_QUOTE_NON_FIRST_COL = ("abap_double_quote_non_first_col", 34, "\"")
    BATCH_DOUBLE_COLON_LINE = ("batch_double_colon_line", 35, "::")
    NOTE_FOXPRO_LINE = ("note_foxpro_line", 36, "NOTE")
    DOUBLE_AMPERSAND_XBASE_LINE = ("double_ampersand_xbase_line", 37, "&&")
    NB_DOT_JLANG_LINE = ("nb_dot_jlang_line", 38, "NB.")
    JCL_DOUBLE_SLASH_STAR_LINE = ("jcl_double_slash_star_line", 39, "//*")
    DOT_BACKSLASH_DOUBLE_QUOTE_ROFF_LINE = ("dot_backslash_double_quote_roff_line", 40, ".\\\"")
    FAUST_TRIPLE_HYPHEN_DOC_LINE = ("faust_triple_hyphen_doc_line", 41, "---")
    CLARION_PIPE_LINE = ("clarion_pipe_line", 42, "|")
    C_CHAR_COLUMN1_FORTRAN = ("c_char_column1_fortran", 43, "C")
    HASH_SPACE_ORGMODE = ("hash_space_orgmode", 44, "# ")
    BACKSLASH_FORTH_SHEN = ("backslash_forth_shen", 45, "\\")
    EXCLAMATION_SMALLTALK_LINE = ("exclamation_smalltalk_line", 46, "!")
    REM_BLITZ_MAX_UPPERCASE = ("rem_blitz_max_uppercase", 47, "Rem")
    SLASH_SLASH_SLASH_DOC = TRIPLE_SLASH_DOC

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
    PASCAL_OCAML_ML_CURLY_ASTERISK = ("pascal_ocaml_ml_curly_asterisk", 6, "{", "}") # Used by Pascal, OCaml, ML for block comments.
    PASCAL_OCAML_ML_PAREN_ASTERISK = ("pascal_ocaml_ml_paren_asterisk", 7, "(*", "*)") # Used by Pascal, OCaml, ML for block comments.
    LUA_DOUBLE_HYPHEN_BRACKET = ("lua_double_hyphen_bracket", 8, "--[[", "]]")
    SCHEME_RACKET_HASH_PIPE = ("scheme_racket_hash_pipe", 9, "#|", "|#")
    RUBY_BEGIN_END = ("ruby_begin_end", 10, "=begin", "=end")
    POWERSHELL_HASH_BRACKET = ("powershell_hash_bracket", 11, "<#", "#>")
    SMALLTALK_DOUBLE_QUOTE = ("smalltalk_double_quote", 12, '"', '"')
    JULIA_HASH_EQUALS = ("julia_hash_equals", 13, "#=", "=#")
    NIM_HASH_BRACKET_DISCARD = ("nim_hash_bracket_discard", 14, "#[", "]#")
    D_SLASH_PLUS_NESTABLE = ("d_slash_plus_nestable", 15, "/+", "+/")
    MATLAB_PERCENT_BRACE = ("matlab_percent_brace", 16, "%{", "%}")
    PERL_POD = ("perl_pod", 17, "=pod", "=cut")
    C_PREPROCESSOR_IF0 = ("c_preprocessor_if0", 18, "#if 0", "#endif")
    RUST_BLOCK_DOC_OUTER = ("rust_block_doc_outer", 19, "/**", "*/")
    RUST_BLOCK_DOC_INNER = ("rust_block_doc_inner", 20, "/*!", "*/")
    ASCIIDOC_BLOCK = ("asciidoc_block", 21, "////", "////")
    WAT_PAREN_SEMICOLON_BLOCK = ("wat_paren_semicolon_block", 22, "(;", ";)")
    COFFEESCRIPT_BLOCK = ("coffeescript_block", 23, "###", "###")
    CFML_BLOCK = ("cfml_block", 24, "<!---", "--->")
    FORTH_PAREN_BLOCK_SPACED = ("forth_paren_block_spaced", 25, "( ", " )")
    XQUERY_COMMENT_BLOCK = ("xquery_comment_block", 26, "(:", ":)")
    PLANTUML_SLASH_APOSTROPHE_BLOCK = ("plantuml_slash_apostrophe_block", 27, "/'", "'/")
    IDRIS_DOC_BLOCK = ("idris_doc_block", 28, "{-|", "|-}")
    DHALL_DOC_BLOCK = ("dhall_doc_block", 29, "{-!-", "-!}")
    CMAKE_BRACKET_BLOCK = ("cmake_bracket_block", 30, "#[[", "]]")
    JSP_COMMENT_BLOCK = ("jsp_comment_block", 31, "<%--", "--%>")
    RAZOR_COMMENT_BLOCK = ("razor_comment_block", 32, "@*", "*@")
    SMARTY_COMMENT_BLOCK = ("smarty_comment_block", 33, "{*", "*}")
    TWIG_COMMENT_BLOCK = ("twig_comment_block", 34, "{#", "#}")
    FREEMARKER_COMMENT_BLOCK = ("freemarker_comment_block", 35, "<#--", "-->")
    VELOCITY_HASH_ASTERISK_BLOCK = ("velocity_hash_asterisk_block", 36, "#*", "*#")
    MAKO_DOC_BLOCK = ("mako_doc_block", 37, "<%doc>", "</%doc>")
    SAS_ASTERISK_SEMICOLON_BLOCK = ("sas_asterisk_semicolon_block", 38, "*", ";")
    REBOL_COMMENT_BLOCK_BRACE = ("rebol_comment_block_brace", 39, "comment {", "}")
    REBOL_COMMENT_BLOCK_BRACKET = ("rebol_comment_block_bracket", 40, "comment [", "]")
    LIQUID_COMMENT_BLOCK = ("liquid_comment_block", 41, "{% comment %}", "{% endcomment %}")
    HANDLEBARS_EXCLAMATION_DASH_BLOCK = ("handlebars_exclamation_dash_block", 42, "{{!--", "--}}")
    HANDLEBARS_EXCLAMATION_BLOCK = ("handlebars_exclamation_block", 43, "{{!", "}}")
    RPM_SPEC_CHANGELOG_BLOCK = ("rpm_spec_changelog_block", 44, "%changelog", "")
    NIM_HASH_DOUBLE_BRACKET_DOC_BLOCK = ("nim_hash_double_bracket_doc_block", 45, "#[[", "]]#")
    JSX_TSX_CURLY_SLASH_ASTERISK_BLOCK = ("jsx_tsx_curly_slash_asterisk_block", 46, "{/*", "*/}")
    AUTOIT_HASH_CS_CE_BLOCK = ("autoit_hash_cs_ce_block", 47, "#cs", "#ce")
    AUTOIT_HASH_COMMENTS_BLOCK = ("autoit_hash_comments_block", 48, "#comments-start", "#comments-end")
    GAMS_DOLLAR_ONOFF_TEXT_BLOCK = ("gams_dollar_onoff_text_block", 49, "$ontext", "$offtext")
    GCODE_PAREN_BLOCK = ("gcode_paren_block", 50, "(", ")")
    INFORM7_BRACKET_BLOCK = ("inform7_bracket_block", 51, "[", "]")
    LEAN_SLASH_HYPHEN_DOC_BLOCK = ("lean_slash_hyphen_doc_block", 52, "/--", "--/")
    LEAN_SLASH_HYPHEN_COMMENT_BLOCK = ("lean_slash_hyphen_comment_block", 53, "/-", "-/")
    OCTAVE_HASH_BRACE_BLOCK = ("octave_hash_brace_block", 54, "#{", "}")
    PAPYRUS_BRACE_BLOCK = ("papyrus_brace_block", 55, "{", "}")
    SIMULA_COMMENT_KEYWORD_BLOCK = ("simula_comment_keyword_block", 56, "COMMENT", ";")
    WENYAN_SHU_YUE_BLOCK = ("wenyan_shu_yue_block", 57, "疏曰。「", "」")
    RAKU_HASH_PAREN_BLOCK = ("raku_hash_paren_block", 58, "#(", ")")
    RAKU_EMBEDDED_DOC_BLOCK = ("raku_embedded_doc_block", 59, "=begin comment", "=end comment")
    CEYLON_TRIPLE_QUOTE_DOC_BLOCK = ("ceylon_triple_quote_doc_block", 60, "\"\"\"", "\"\"\"")
    EJS_PERCENT_HASH_BLOCK = ("ejs_percent_hash_block", 61, "<%#", "%>")
    FORTH_PAREN_BLOCK_UNSPACED = ("forth_paren_block_unspaced", 62, "(", ")")


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

    def __repr__(self) -> str: return f"Position(line={self.line}, column={self.column})"


@dataclass(frozen=True)
class Range:
    start: Position
    end: Position

    def __repr__(self) -> str: return f"Range(start={self.start}, end={self.end})"


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
        if not self.start_delimiter: raise ValueError(f"start_delimiter for '{self.key}' cannot be empty.")
        if self.type == CommentDefinitionType.MULTI_LINE:
            if self.end_delimiter is None or not self.end_delimiter:
                if self.key != "rpm_spec_changelog_block_comment":
                    raise ValueError(
                        f"Multi-line comment definition '{self.key}' must have a non-empty end_delimiter or be an allowed special case.")
        if self.column_specific_start is not None and self.column_specific_start < 1:
            raise ValueError(f"column_specific_start for '{self.key}' must be 1-indexed and positive.")


@dataclass(frozen=True)
class ExtractedCommentInstance:
    comment_type: CommentSymbol
    location: Range
    content_location: Range

    def __repr__(
            self) -> str: return f"ExtractedCommentInstance(comment_type={self.comment_type.name}, location={self.location}, content_location={self.content_location})"


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
            if member.symbol_string == syntax_def.start_delimiter: return member
    elif syntax_def.type == CommentDefinitionType.MULTI_LINE:
        for member in StandardCommentSymbolMultiLine:
            if member.start_symbol_string == syntax_def.start_delimiter and \
                    member.end_symbol_string == syntax_def.end_delimiter: return member
    raise ValueError(
        f"Could not find a matching CommentSymbol for syntax definition: "
        f"key='{syntax_def.key}', type='{syntax_def.type.value}', "
        f"start_delimiter='{syntax_def.start_delimiter}', end_delimiter='{syntax_def.end_delimiter or ''}'"
    )


def _initialize_comment_configurations() -> None:
    global _DEFAULT_SYNTAX_DEFINITIONS, _SYNTAX_DEF_TO_COMMENT_SYMBOL_MAP
    if _DEFAULT_SYNTAX_DEFINITIONS: return

    definitions_data: Dict[str, CommentSyntaxDefinition] = {
        "c_line_comment": CommentSyntaxDefinition(key="c_line_comment", type=CommentDefinitionType.SINGLE_LINE,
                                                  start_delimiter="//"),
        "c_block_comment": CommentSyntaxDefinition(key="c_block_comment", type=CommentDefinitionType.MULTI_LINE,
                                                   start_delimiter="/*", end_delimiter="*/"),
        "c_block_comment_nestable": CommentSyntaxDefinition(key="c_block_comment_nestable",
                                                            type=CommentDefinitionType.MULTI_LINE, start_delimiter="/*",
                                                            end_delimiter="*/", is_nestable=True),
        "csharp_doc_line": CommentSyntaxDefinition(key="csharp_doc_line", type=CommentDefinitionType.SINGLE_LINE,
                                                   start_delimiter="///", is_doc_comment=True),
        "javadoc_block_comment": CommentSyntaxDefinition(key="javadoc_block_comment",
                                                         type=CommentDefinitionType.MULTI_LINE, start_delimiter="/**",
                                                         end_delimiter="*/", is_doc_comment=True),
        "rust_inner_doc_line": CommentSyntaxDefinition(key="rust_inner_doc_line",
                                                       type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//!",
                                                       is_doc_comment=True),
        "rust_inner_doc_block": CommentSyntaxDefinition(key="rust_inner_doc_block",
                                                        type=CommentDefinitionType.MULTI_LINE, start_delimiter="/*!",
                                                        end_delimiter="*/", is_doc_comment=True, is_nestable=True),
        "c_preprocessor_block": CommentSyntaxDefinition(key="c_preprocessor_block",
                                                        type=CommentDefinitionType.MULTI_LINE, start_delimiter="#if 0",
                                                        end_delimiter="#endif", requires_line_start=True),
        "python_hash_line": CommentSyntaxDefinition(key="python_hash_line", type=CommentDefinitionType.SINGLE_LINE,
                                                    start_delimiter="#"),
        "python_triple_double_quote_block": CommentSyntaxDefinition(key="python_triple_double_quote_block",
                                                                    type=CommentDefinitionType.MULTI_LINE,
                                                                    start_delimiter='"""', end_delimiter='"""',
                                                                    is_doc_comment=True),
        "python_triple_single_quote_block": CommentSyntaxDefinition(key="python_triple_single_quote_block",
                                                                    type=CommentDefinitionType.MULTI_LINE,
                                                                    start_delimiter="'''", end_delimiter="'''",
                                                                    is_doc_comment=True),
        "hash_line": CommentSyntaxDefinition(key="hash_line", type=CommentDefinitionType.SINGLE_LINE,
                                             start_delimiter="#"),
        "hash_space_line": CommentSyntaxDefinition(key="hash_space_line", type=CommentDefinitionType.SINGLE_LINE,
                                             start_delimiter="# "),
        "double_hyphen_line": CommentSyntaxDefinition(key="double_hyphen_line", type=CommentDefinitionType.SINGLE_LINE,
                                                      start_delimiter="--"),
        "semicolon_line": CommentSyntaxDefinition(key="semicolon_line", type=CommentDefinitionType.SINGLE_LINE,
                                                  start_delimiter=";"),
        "semicolon_line_requires_start": CommentSyntaxDefinition(key="semicolon_line_requires_start",
                                                                 type=CommentDefinitionType.SINGLE_LINE,
                                                                 start_delimiter=";", requires_line_start=True),
        "wat_double_semicolon_line": CommentSyntaxDefinition(key="wat_double_semicolon_line",
                                                             type=CommentDefinitionType.SINGLE_LINE,
                                                             start_delimiter=";;"),
        "rem_keyword_line": CommentSyntaxDefinition(key="rem_keyword_line", type=CommentDefinitionType.SINGLE_LINE,
                                                    start_delimiter="REM", requires_line_start=True),
        "rem_lowercase_line": CommentSyntaxDefinition(key="rem_lowercase_line",
                                                      type=CommentDefinitionType.SINGLE_LINE,
                                                      start_delimiter="rem", requires_line_start=True),
        "rem_capitalized_line": CommentSyntaxDefinition(key="rem_capitalized_line",
                                                        type=CommentDefinitionType.SINGLE_LINE,
                                                        start_delimiter="Rem", requires_line_start=True),
        "at_sign_batch_line": CommentSyntaxDefinition(key="at_sign_batch_line", type=CommentDefinitionType.SINGLE_LINE,
                                                      start_delimiter="@", requires_line_start=True),
        "batch_double_colon_line": CommentSyntaxDefinition(key="batch_double_colon_line",
                                                                   type=CommentDefinitionType.SINGLE_LINE,
                                                                   start_delimiter="::"),
        "fortran_exclamation_line": CommentSyntaxDefinition(key="fortran_exclamation_line",
                                                            type=CommentDefinitionType.SINGLE_LINE,
                                                            start_delimiter="!"),
        "fortran_fixed_c_col1_line": CommentSyntaxDefinition(key="fortran_fixed_c_col1_line",
                                                             type=CommentDefinitionType.SINGLE_LINE,
                                                             start_delimiter="C", column_specific_start=1),
        "fortran_fixed_c_space_col1_line": CommentSyntaxDefinition(key="fortran_fixed_c_space_col1_line",
                                                                  type=CommentDefinitionType.SINGLE_LINE,
                                                                  start_delimiter="C ", column_specific_start=1),
        "fortran_fixed_star_col1_line": CommentSyntaxDefinition(key="fortran_fixed_star_col1_line",
                                                                type=CommentDefinitionType.SINGLE_LINE,
                                                                start_delimiter="*", column_specific_start=1),
        "fortran_fixed_star_spaced_line_comment": CommentSyntaxDefinition(key="fortran_fixed_star_spaced_line_comment",
                                                                          type=CommentDefinitionType.SINGLE_LINE,
                                                                          start_delimiter="* ",
                                                                          column_specific_start=1),
        "fortran_fixed_alt_c_col1_line": CommentSyntaxDefinition(key="fortran_fixed_alt_c_col1_line",
                                                                 type=CommentDefinitionType.SINGLE_LINE,
                                                                 start_delimiter="c", column_specific_start=1),
        "cobol_fixed_star_col7_line": CommentSyntaxDefinition(key="cobol_fixed_star_col7_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="*", column_specific_start=7),
        "cobol_free_form_line": CommentSyntaxDefinition(key="cobol_free_form_line",
                                                        type=CommentDefinitionType.SINGLE_LINE, start_delimiter="*>"),
        "percent_line": CommentSyntaxDefinition(key="percent_line", type=CommentDefinitionType.SINGLE_LINE,
                                                start_delimiter="%"),
        "matlab_percent_brace_block": CommentSyntaxDefinition(key="matlab_percent_brace_block",
                                                              type=CommentDefinitionType.MULTI_LINE,
                                                              start_delimiter="%{", end_delimiter="%}",
                                                              is_nestable=True),
        "vb_single_quote_line": CommentSyntaxDefinition(key="vb_single_quote_line",
                                                        type=CommentDefinitionType.SINGLE_LINE, start_delimiter="'"),
        "blitzmax_single_quote_line": CommentSyntaxDefinition(key="blitzmax_single_quote_line",
                                                                       type=CommentDefinitionType.SINGLE_LINE,
                                                                       start_delimiter="'"),
        "apl_lamp_line": CommentSyntaxDefinition(key="apl_lamp_line", type=CommentDefinitionType.SINGLE_LINE,
                                                 start_delimiter="⍝"),
        "html_xml_block": CommentSyntaxDefinition(key="html_xml_block", type=CommentDefinitionType.MULTI_LINE,
                                                  start_delimiter="<!--", end_delimiter="-->"),
        "haskell_curly_hyphen_block": CommentSyntaxDefinition(key="haskell_curly_hyphen_block",
                                                              type=CommentDefinitionType.MULTI_LINE,
                                                              start_delimiter="{-", end_delimiter="-}",
                                                              is_nestable=True),
        "pascal_curly_brace_block": CommentSyntaxDefinition(key="pascal_curly_brace_block",
                                                            type=CommentDefinitionType.MULTI_LINE, start_delimiter="{",
                                                            end_delimiter="}"),
        "pascal_paren_asterisk_block": CommentSyntaxDefinition(key="pascal_paren_asterisk_block",
                                                               type=CommentDefinitionType.MULTI_LINE,
                                                               start_delimiter="(*", end_delimiter="*)",
                                                               is_nestable=True),
        "lua_long_bracket_block": CommentSyntaxDefinition(key="lua_long_bracket_block",
                                                          type=CommentDefinitionType.MULTI_LINE, start_delimiter="--[[",
                                                          end_delimiter="]]"),
        "scheme_hash_pipe_block": CommentSyntaxDefinition(key="scheme_hash_pipe_block",
                                                          type=CommentDefinitionType.MULTI_LINE, start_delimiter="#|",
                                                          end_delimiter="|#", is_nestable=True),
        "ruby_begin_end_block": CommentSyntaxDefinition(key="ruby_begin_end_block",
                                                        type=CommentDefinitionType.MULTI_LINE, start_delimiter="=begin",
                                                        end_delimiter="=end", requires_line_start=True),
        "powershell_hash_bracket_block": CommentSyntaxDefinition(key="powershell_hash_bracket_block",
                                                                 type=CommentDefinitionType.MULTI_LINE,
                                                                 start_delimiter="<#", end_delimiter="#>",
                                                                 is_nestable=True),
        "smalltalk_double_quote_block": CommentSyntaxDefinition(key="smalltalk_double_quote_block",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter='"', end_delimiter='"'),
        "smalltalk_exclamation_line": CommentSyntaxDefinition(key="smalltalk_exclamation_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="!"),
        "julia_hash_equals_block": CommentSyntaxDefinition(key="julia_hash_equals_block",
                                                           type=CommentDefinitionType.MULTI_LINE, start_delimiter="#=",
                                                           end_delimiter="=#", is_nestable=True),
        "nim_hash_line": CommentSyntaxDefinition(key="nim_hash_line", type=CommentDefinitionType.SINGLE_LINE,
                                                 start_delimiter="#"),
        "nim_doc_line": CommentSyntaxDefinition(key="nim_doc_line", type=CommentDefinitionType.SINGLE_LINE,
                                                start_delimiter="##", is_doc_comment=True),
        "nim_hash_bracket_discard_block": CommentSyntaxDefinition(key="nim_hash_bracket_discard_block",
                                                                  type=CommentDefinitionType.MULTI_LINE,
                                                                  start_delimiter="#[", end_delimiter="]#",
                                                                  is_nestable=True),
        "nim_hash_double_bracket_doc_block": CommentSyntaxDefinition(key="nim_hash_double_bracket_doc_block",
                                                                     type=CommentDefinitionType.MULTI_LINE,
                                                                     start_delimiter="#[[", end_delimiter="]]#",
                                                                     is_nestable=True, is_doc_comment=True),
        "d_slash_plus_nestable_block": CommentSyntaxDefinition(key="d_slash_plus_nestable_block",
                                                               type=CommentDefinitionType.MULTI_LINE,
                                                               start_delimiter="/+", end_delimiter="+/",
                                                               is_nestable=True),
        "perl_pod_block": CommentSyntaxDefinition(key="perl_pod_block", type=CommentDefinitionType.MULTI_LINE,
                                                  start_delimiter="=pod", end_delimiter="=cut",
                                                  requires_line_start=True, is_doc_comment=True),
        "asciidoc_line": CommentSyntaxDefinition(key="asciidoc_line", type=CommentDefinitionType.SINGLE_LINE,
                                                 start_delimiter="//"),
        "asciidoc_block": CommentSyntaxDefinition(key="asciidoc_block", type=CommentDefinitionType.MULTI_LINE,
                                                  start_delimiter="////", end_delimiter="////",
                                                  requires_line_start=True),
        "rst_dot_dot_space_line": CommentSyntaxDefinition(key="rst_dot_dot_space_line",
                                                          type=CommentDefinitionType.SINGLE_LINE, start_delimiter=".. ",
                                                          requires_line_start=True),
        "wat_paren_semicolon_block": CommentSyntaxDefinition(key="wat_paren_semicolon_block",
                                                             type=CommentDefinitionType.MULTI_LINE,
                                                             start_delimiter="(;", end_delimiter=";)",
                                                             is_nestable=True),
        "coffeescript_block": CommentSyntaxDefinition(key="coffeescript_block", type=CommentDefinitionType.MULTI_LINE,
                                                      start_delimiter="###", end_delimiter="###", is_doc_comment=True),
        "cfml_block": CommentSyntaxDefinition(key="cfml_block", type=CommentDefinitionType.MULTI_LINE,
                                              start_delimiter="<!---", end_delimiter="--->"),
        "forth_backslash_space_line": CommentSyntaxDefinition(key="forth_backslash_space_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="\\ "),
        "forth_backslash_line": CommentSyntaxDefinition(key="forth_backslash_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="\\"),
        "forth_paren_spaced_block": CommentSyntaxDefinition(key="forth_paren_spaced_block",
                                                            type=CommentDefinitionType.MULTI_LINE, start_delimiter="( ",
                                                            end_delimiter=" )"),
        "forth_paren_unspaced_block": CommentSyntaxDefinition(key="forth_paren_unspaced_block",
                                                            type=CommentDefinitionType.MULTI_LINE, start_delimiter="(",
                                                            end_delimiter=")"),
        "tlaplus_line": CommentSyntaxDefinition(key="tlaplus_line", type=CommentDefinitionType.SINGLE_LINE,
                                                start_delimiter="\\*"),
        "xquery_block": CommentSyntaxDefinition(key="xquery_block", type=CommentDefinitionType.MULTI_LINE,
                                                start_delimiter="(:", end_delimiter=":)", is_nestable=True),
        "plantuml_single_quote_line": CommentSyntaxDefinition(key="plantuml_single_quote_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="'"),
        "plantuml_slash_apostrophe_block": CommentSyntaxDefinition(key="plantuml_slash_apostrophe_block",
                                                                   type=CommentDefinitionType.MULTI_LINE,
                                                                   start_delimiter="/'", end_delimiter="'/"),
        "idris_doc_line": CommentSyntaxDefinition(key="idris_doc_line", type=CommentDefinitionType.SINGLE_LINE,
                                                  start_delimiter="|||", is_doc_comment=True),
        "idris_doc_block": CommentSyntaxDefinition(key="idris_doc_block", type=CommentDefinitionType.MULTI_LINE,
                                                   start_delimiter="{-|", end_delimiter="|-}", is_nestable=True,
                                                   is_doc_comment=True),
        "dhall_doc_block": CommentSyntaxDefinition(key="dhall_doc_block", type=CommentDefinitionType.MULTI_LINE,
                                                   start_delimiter="{-!-", end_delimiter="-!}", is_nestable=True,
                                                   is_doc_comment=True),
        "cmake_bracket_block": CommentSyntaxDefinition(key="cmake_bracket_block", type=CommentDefinitionType.MULTI_LINE,
                                                       start_delimiter="#[[", end_delimiter="]]"),
        "jsp_block": CommentSyntaxDefinition(key="jsp_block", type=CommentDefinitionType.MULTI_LINE,
                                             start_delimiter="<%--", end_delimiter="--%>"),
        "ejs_block": CommentSyntaxDefinition(key="ejs_block", type=CommentDefinitionType.MULTI_LINE,
                                             start_delimiter="<%#", end_delimiter="%>"),
        "razor_block": CommentSyntaxDefinition(key="razor_block", type=CommentDefinitionType.MULTI_LINE,
                                               start_delimiter="@*", end_delimiter="*@"),
        "smarty_block": CommentSyntaxDefinition(key="smarty_block", type=CommentDefinitionType.MULTI_LINE,
                                                start_delimiter="{*", end_delimiter="*}"),
        "twig_block": CommentSyntaxDefinition(key="twig_block", type=CommentDefinitionType.MULTI_LINE,
                                              start_delimiter="{#", end_delimiter="#}"),
        "freemarker_block": CommentSyntaxDefinition(key="freemarker_block", type=CommentDefinitionType.MULTI_LINE,
                                                    start_delimiter="<#--", end_delimiter="-->"),
        "velocity_double_hash_line": CommentSyntaxDefinition(key="velocity_double_hash_line",
                                                             type=CommentDefinitionType.SINGLE_LINE,
                                                             start_delimiter="##"),
        "velocity_hash_asterisk_block": CommentSyntaxDefinition(key="velocity_hash_asterisk_block",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter="#*", end_delimiter="*#"),
        "mako_doc_block": CommentSyntaxDefinition(key="mako_doc_block", type=CommentDefinitionType.MULTI_LINE,
                                                  start_delimiter="<%doc>", end_delimiter="</%doc>",
                                                  is_doc_comment=True),
        "liquid_comment_block": CommentSyntaxDefinition(key="liquid_comment_block",
                                                        type=CommentDefinitionType.MULTI_LINE,
                                                        start_delimiter="{% comment %}",
                                                        end_delimiter="{% endcomment %}"),
        "handlebars_comment_block": CommentSyntaxDefinition(key="handlebars_comment_block",
                                                            type=CommentDefinitionType.MULTI_LINE,
                                                            start_delimiter="{{!--", end_delimiter="--}}"),
        "mustache_comment_block": CommentSyntaxDefinition(key="mustache_comment_block",
                                                          type=CommentDefinitionType.MULTI_LINE, start_delimiter="{{!",
                                                          end_delimiter="}}"),
        "m4_dnl_line": CommentSyntaxDefinition(key="m4_dnl_line", type=CommentDefinitionType.SINGLE_LINE,
                                               start_delimiter="dnl", requires_line_start=True),
        "viml_double_quote_line": CommentSyntaxDefinition(key="viml_double_quote_line",
                                                          type=CommentDefinitionType.SINGLE_LINE, start_delimiter='"',
                                                          requires_line_start=True),
        "mermaid_double_percent_line": CommentSyntaxDefinition(key="mermaid_double_percent_line",
                                                               type=CommentDefinitionType.SINGLE_LINE,
                                                               start_delimiter="%%"),
        "slim_slash_line": CommentSyntaxDefinition(key="slim_slash_line", type=CommentDefinitionType.SINGLE_LINE,
                                                   start_delimiter="/", requires_line_start=True),
        "haml_hyphen_hash_line": CommentSyntaxDefinition(key="haml_hyphen_hash_line",
                                                         type=CommentDefinitionType.SINGLE_LINE, start_delimiter="-#",
                                                         requires_line_start=True),
        "pug_unbuffered_line": CommentSyntaxDefinition(key="pug_unbuffered_line",
                                                       type=CommentDefinitionType.SINGLE_LINE, start_delimiter="//"),
        "pug_silent_block_starter_line": CommentSyntaxDefinition(key="pug_silent_block_starter_line",
                                                                 type=CommentDefinitionType.SINGLE_LINE,
                                                                 start_delimiter="//-"),
        "sas_asterisk_semicolon_block": CommentSyntaxDefinition(key="sas_asterisk_semicolon_block",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter="*", end_delimiter=";",
                                                                requires_line_start=False), # SAS * comment ; can be anywhere
        "rebol_comment_brace_block": CommentSyntaxDefinition(key="rebol_comment_brace_block",
                                                             type=CommentDefinitionType.MULTI_LINE,
                                                             start_delimiter="comment {", end_delimiter="}"),
        "rebol_comment_bracket_block": CommentSyntaxDefinition(key="rebol_comment_bracket_block",
                                                               type=CommentDefinitionType.MULTI_LINE,
                                                               start_delimiter="comment [", end_delimiter="]"),
        "abap_asterisk_line": CommentSyntaxDefinition(key="abap_asterisk_line", type=CommentDefinitionType.SINGLE_LINE,
                                                      start_delimiter="*", requires_line_start=True),
        "abap_double_quote_line_non_col1": CommentSyntaxDefinition(key="abap_double_quote_line_non_col1",
                                                                   type=CommentDefinitionType.SINGLE_LINE,
                                                                   start_delimiter='"'),
        "rpm_spec_changelog_block_comment": CommentSyntaxDefinition(key="rpm_spec_changelog_block_comment",
                                                                    type=CommentDefinitionType.MULTI_LINE,
                                                                    start_delimiter="%changelog", end_delimiter="",
                                                                    requires_line_start=True),
        "jsx_tsx_curly_slash_asterisk": CommentSyntaxDefinition(key="jsx_tsx_curly_slash_asterisk",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter="{/*", end_delimiter="*/}"),
        "autoit_hash_cs_ce_block": CommentSyntaxDefinition(key="autoit_hash_cs_ce_block",
                                                           type=CommentDefinitionType.MULTI_LINE, start_delimiter="#cs",
                                                           end_delimiter="#ce"),
        "autoit_hash_comments_block": CommentSyntaxDefinition(key="autoit_hash_comments_block",
                                                              type=CommentDefinitionType.MULTI_LINE,
                                                              start_delimiter="#comments-start",
                                                              end_delimiter="#comments-end"),
        "gams_dollar_onoff_text_block": CommentSyntaxDefinition(key="gams_dollar_onoff_text_block",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter="$ontext", end_delimiter="$offtext",
                                                                requires_line_start=True),
        "gcode_paren_block": CommentSyntaxDefinition(key="gcode_paren_block", type=CommentDefinitionType.MULTI_LINE,
                                                     start_delimiter="(", end_delimiter=")"),
        "inform7_bracket_block": CommentSyntaxDefinition(key="inform7_bracket_block",
                                                         type=CommentDefinitionType.MULTI_LINE, start_delimiter="[",
                                                         end_delimiter="]", is_doc_comment=True),
        "lean_slash_hyphen_doc_block": CommentSyntaxDefinition(key="lean_slash_hyphen_doc_block",
                                                               type=CommentDefinitionType.MULTI_LINE,
                                                               start_delimiter="/--", end_delimiter="--/",
                                                               is_doc_comment=True, is_nestable=True),
        "lean_slash_hyphen_comment_block": CommentSyntaxDefinition(key="lean_slash_hyphen_comment_block",
                                                                   type=CommentDefinitionType.MULTI_LINE,
                                                                   start_delimiter="/-", end_delimiter="-/",
                                                                   is_nestable=True),
        "octave_hash_brace_block": CommentSyntaxDefinition(key="octave_hash_brace_block",
                                                           type=CommentDefinitionType.MULTI_LINE, start_delimiter="#{",
                                                           end_delimiter="}", is_nestable=True),
        "papyrus_brace_block": CommentSyntaxDefinition(key="papyrus_brace_block", type=CommentDefinitionType.MULTI_LINE,
                                                       start_delimiter="{", end_delimiter="}",
                                                       requires_line_start=True),
        "simula_comment_keyword_block": CommentSyntaxDefinition(key="simula_comment_keyword_block",
                                                                type=CommentDefinitionType.MULTI_LINE,
                                                                start_delimiter="COMMENT", end_delimiter=";"),
        "wenyan_shu_yue_block": CommentSyntaxDefinition(key="wenyan_shu_yue_block",
                                                        type=CommentDefinitionType.MULTI_LINE, start_delimiter="疏曰。「",
                                                        end_delimiter="」", is_doc_comment=True),
        "raku_hash_paren_block": CommentSyntaxDefinition(key="raku_hash_paren_block",
                                                         type=CommentDefinitionType.MULTI_LINE, start_delimiter="#(",
                                                         end_delimiter=")"),
        "raku_embedded_doc_block": CommentSyntaxDefinition(key="raku_embedded_doc_block",
                                                           type=CommentDefinitionType.MULTI_LINE,
                                                           start_delimiter="=begin comment",
                                                           end_delimiter="=end comment", requires_line_start=True,
                                                           is_doc_comment=True),
        "ceylon_triple_quote_doc_block": CommentSyntaxDefinition(key="ceylon_triple_quote_doc_block",
                                                                 type=CommentDefinitionType.MULTI_LINE,
                                                                 start_delimiter="\"\"\"", end_delimiter="\"\"\"",
                                                                 is_doc_comment=True),
        "note_foxpro_line": CommentSyntaxDefinition(key="note_foxpro_line", type=CommentDefinitionType.SINGLE_LINE,
                                                    start_delimiter="NOTE", requires_line_start=True),
        "double_ampersand_xbase_line": CommentSyntaxDefinition(key="double_ampersand_xbase_line",
                                                               type=CommentDefinitionType.SINGLE_LINE,
                                                               start_delimiter="&&"),
        "nb_dot_jlang_line": CommentSyntaxDefinition(key="nb_dot_jlang_line", type=CommentDefinitionType.SINGLE_LINE,
                                                     start_delimiter="NB."),
        "jcl_double_slash_star_line": CommentSyntaxDefinition(key="jcl_double_slash_star_line",
                                                              type=CommentDefinitionType.SINGLE_LINE,
                                                              start_delimiter="//*", requires_line_start=True),
        "dot_backslash_double_quote_roff_line": CommentSyntaxDefinition(key="dot_backslash_double_quote_roff_line",
                                                                        type=CommentDefinitionType.SINGLE_LINE,
                                                                        start_delimiter=".\\\"",
                                                                        requires_line_start=True),
        "faust_triple_hyphen_doc_line": CommentSyntaxDefinition(key="faust_triple_hyphen_doc_line",
                                                                type=CommentDefinitionType.SINGLE_LINE,
                                                                start_delimiter="---", is_doc_comment=True),
        "clarion_pipe_line": CommentSyntaxDefinition(key="clarion_pipe_line", type=CommentDefinitionType.SINGLE_LINE,
                                                     start_delimiter="|", requires_line_start=True),
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
    if LANGUAGE_PROFILES_REGISTRY: return

    def create_profile(lang_id: str, syntax_keys: Tuple[str, ...], handle_strings: bool = True):
        options = {"handle_string_literals": handle_strings}
        return LanguageCommentProfile(language_id=lang_id, syntax_keys=syntax_keys, parser_options=options)

    c_style_base = ("c_line_comment", "c_block_comment")
    c_style_nestable_block = ("c_line_comment", "c_block_comment_nestable")
    c_style_doc = c_style_base + ("javadoc_block_comment", "csharp_doc_line")
    rust_style_full = ("c_line_comment", "c_block_comment_nestable", "csharp_doc_line", "rust_inner_doc_line",
                       "javadoc_block_comment", "rust_inner_doc_block")
    pascal_style_blocks = ("pascal_curly_brace_block", "pascal_paren_asterisk_block")
    haskell_style_blocks = ("double_hyphen_line", "haskell_curly_hyphen_block")
    template_engine_percent_hyphen = ("jsp_block",) # Used by JSP, ASP classic variant, EJS (though EJS is <%# %>)
    template_engine_curly_hash = ("twig_block",) # Twig, Jinja, Nunjucks
    template_engine_curly_exclamation = ("mustache_comment_block",) # Mustache, Handlebars variant
    template_engine_curly_exclamation_dash = ("handlebars_comment_block",) # Handlebars

    profiles = [
        create_profile("python",
                       ("python_hash_line", "python_triple_double_quote_block", "python_triple_single_quote_block")),
        create_profile("csharp", c_style_doc + ("c_preprocessor_block",)),
        create_profile("c", c_style_base + ("c_preprocessor_block",)),
        create_profile("cpp", c_style_doc + ("c_preprocessor_block",)),
        create_profile("java", c_style_doc),
        create_profile("javascript", c_style_doc),
        create_profile("typescript", c_style_doc),
        create_profile("jsx", c_style_doc + ("jsx_tsx_curly_slash_asterisk",)),
        create_profile("tsx", c_style_doc + ("jsx_tsx_curly_slash_asterisk",)),
        create_profile("go", c_style_base),
        create_profile("rust", rust_style_full),
        create_profile("swift", c_style_nestable_block + ("csharp_doc_line",)),
        create_profile("kotlin", c_style_doc),
        create_profile("scala", c_style_doc),
        create_profile("php", ("c_line_comment", "hash_line", "c_block_comment", "javadoc_block_comment")),
        create_profile("html", ("html_xml_block",), handle_strings=False),
        create_profile("xml", ("html_xml_block",), handle_strings=False),
        create_profile("svg", ("html_xml_block",), handle_strings=False),
        create_profile("css", ("c_block_comment",), handle_strings=True),
        create_profile("less", ("c_line_comment", "c_block_comment"), handle_strings=True),
        create_profile("sass", c_style_nestable_block, handle_strings=True), # SCSS syntax
        create_profile("stylus", c_style_nestable_block, handle_strings=True),
        create_profile("sql", ("double_hyphen_line", "c_block_comment")),
        create_profile("plsql", ("double_hyphen_line", "c_block_comment")),
        create_profile("tsql", ("double_hyphen_line", "c_block_comment")),
        create_profile("yaml", ("hash_line",), handle_strings=False),
        create_profile("json", c_style_base, handle_strings=False), # For JSONC/JSON5 variants
        create_profile("json5", c_style_base, handle_strings=True),
        create_profile("toml", ("hash_line",), handle_strings=False),
        create_profile("ini", ("semicolon_line_requires_start", "hash_line"), handle_strings=False),
        create_profile("unreal_config_ini", ("semicolon_line_requires_start",), handle_strings=False),
        create_profile("editorconfig", ("hash_line", "semicolon_line_requires_start"), handle_strings=False),
        create_profile("dotenv", ("hash_line",), handle_strings=False),
        create_profile("properties", ("hash_line", "fortran_exclamation_line"), handle_strings=False),
        create_profile("git_ignore", ("hash_line",), handle_strings=False),
        create_profile("assembly", ("semicolon_line", "hash_line", "c_block_comment")), # Broad category
        create_profile("bash", ("hash_line",)),
        create_profile("shell", ("hash_line",)),
        create_profile("zsh", ("hash_line",)),
        create_profile("dockerfile", ("hash_line",), handle_strings=False),
        create_profile("makefile", ("hash_line",), handle_strings=False),
        create_profile("cmake", ("hash_line", "cmake_bracket_block")),
        create_profile("terraform", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("ada", ("double_hyphen_line",)),
        create_profile("cobol", ("cobol_fixed_star_col7_line", "cobol_free_form_line")), # Fixed and free
        create_profile("fortran",
                       ("fortran_exclamation_line", "fortran_fixed_c_col1_line", "fortran_fixed_star_col1_line",
                        "fortran_fixed_alt_c_col1_line", "fortran_fixed_star_spaced_line_comment", "fortran_fixed_c_space_col1_line")),
        create_profile("pascal", ("c_line_comment",) + pascal_style_blocks),
        create_profile("delphi", ("c_line_comment",) + pascal_style_blocks),
        create_profile("object_pascal", ("c_line_comment",) + pascal_style_blocks),
        create_profile("lua", ("double_hyphen_line", "lua_long_bracket_block")),
        create_profile("perl", ("hash_line", "perl_pod_block")),
        create_profile("powershell", ("hash_line", "powershell_hash_bracket_block")),
        create_profile("r", ("hash_line",)),
        create_profile("ruby", ("hash_line", "ruby_begin_end_block")),
        create_profile("dart", c_style_doc),
        create_profile("groovy", c_style_doc),
        create_profile("haskell", haskell_style_blocks),
        create_profile("clojure", ("semicolon_line",)),
        create_profile("common_lisp", ("semicolon_line", "scheme_hash_pipe_block")),
        create_profile("scheme", ("semicolon_line", "scheme_hash_pipe_block")),
        create_profile("racket", ("semicolon_line", "scheme_hash_pipe_block")),
        create_profile("emacs_lisp", ("semicolon_line", "scheme_hash_pipe_block")),
        create_profile("elixir", ("hash_line",)),
        create_profile("erlang", ("percent_line",)),
        create_profile("julia", ("hash_line", "julia_hash_equals_block")),
        create_profile("nim", ("nim_hash_line", "nim_doc_line", "nim_hash_bracket_discard_block",
                               "nim_hash_double_bracket_doc_block")),
        create_profile("ocaml", ("pascal_paren_asterisk_block",)),
        create_profile("fsharp", ("c_line_comment", "pascal_paren_asterisk_block", "csharp_doc_line")),
        create_profile("matlab", ("percent_line", "matlab_percent_brace_block")),
        create_profile("octave",
                       ("percent_line", "hash_line", "matlab_percent_brace_block", "octave_hash_brace_block")),
        create_profile("latex", ("percent_line",), handle_strings=False),
        create_profile("tex_plain", ("percent_line",), handle_strings=False),
        create_profile("bibtex", ("percent_line",), handle_strings=False),
        create_profile("prolog", ("percent_line", "c_block_comment")),
        create_profile("objectivec", c_style_doc + ("c_preprocessor_block",)),
        create_profile("markdown", ("html_xml_block",), handle_strings=False),
        create_profile("restructuredtext", ("rst_dot_dot_space_line",), handle_strings=False),
        create_profile("asciidoc", ("asciidoc_line", "asciidoc_block"), handle_strings=False),
        create_profile("orgmode", ("hash_space_line",), handle_strings=False),
        create_profile("bat", ("rem_keyword_line", "rem_lowercase_line", "rem_capitalized_line", "batch_double_colon_line", "at_sign_batch_line"),
                       handle_strings=False),
        create_profile("viml", ("viml_double_quote_line",)),
        create_profile("m4", ("hash_line", "m4_dnl_line")),
        create_profile("coffeescript", ("hash_line", "coffeescript_block")),
        create_profile("cfml", ("cfml_block",)),
        create_profile("forth", ("forth_backslash_space_line", "forth_backslash_line", "forth_paren_spaced_block", "forth_paren_unspaced_block"), handle_strings=False),
        create_profile("twig", template_engine_curly_hash, handle_strings=True),
        create_profile("jinja", template_engine_curly_hash, handle_strings=True),
        create_profile("liquid_tpl", ("liquid_comment_block",), handle_strings=True),
        create_profile("handlebars", template_engine_curly_exclamation_dash + template_engine_curly_exclamation, handle_strings=True),
        create_profile("mustache", template_engine_curly_exclamation, handle_strings=True),
        create_profile("ejs", ("ejs_block",), handle_strings=True),
        create_profile("xquery", ("xquery_block",)),
        create_profile("asp_classic", ("vb_single_quote_line",) + template_engine_percent_hyphen, handle_strings=True),
        create_profile("jsp", template_engine_percent_hyphen, handle_strings=True),
        create_profile("aspx", template_engine_percent_hyphen + ("html_xml_block",), handle_strings=True),
        create_profile("unreal_build_script_cs", c_style_doc),
        create_profile("unreal_shader_file", c_style_base),
        create_profile("unreal_shader_header", c_style_base),
        create_profile("unreal_project", c_style_base, handle_strings=True), # JSONC-like
        create_profile("unreal_plugin_descriptor", c_style_base, handle_strings=True), # JSONC-like
        create_profile("verse", ("hash_line", "powershell_hash_bracket_block")), # Verse uses <# #> for multiline
        create_profile("text", (), handle_strings=False),
        create_profile("unknown", (), handle_strings=False),
        create_profile("diff", (), handle_strings=False),
        create_profile("csv", ("hash_line",), handle_strings=False),
        create_profile("tsv", ("hash_line",), handle_strings=False),
        create_profile("d",
                       ("c_line_comment", "c_block_comment_nestable", "d_slash_plus_nestable_block", "csharp_doc_line",
                        "javadoc_block_comment", "rust_inner_doc_block")),
        create_profile("hocon", ("c_line_comment", "hash_line")),
        create_profile("cypher", ("c_line_comment",)),
        create_profile("sparql", ("hash_line",)),
        create_profile("glsl", c_style_base + ("c_preprocessor_block",)),
        create_profile("hlsl", c_style_base + ("c_preprocessor_block",)),
        create_profile("gradle", c_style_base),
        create_profile("protobuf", ("c_line_comment", "c_block_comment")),
        create_profile("textproto", ("hash_line",)),
        create_profile("kconfig", ("hash_line",), handle_strings=False),
        create_profile("rpm_spec", ("hash_line", "rpm_spec_changelog_block_comment"), handle_strings=False),
        create_profile("solidarity", c_style_doc),
        create_profile("zig", ("c_line_comment",)),
        create_profile("crystal", ("hash_line",)),
        create_profile("haxe", c_style_doc),
        create_profile("pug", ("pug_unbuffered_line", "pug_silent_block_starter_line"), handle_strings=False),
        create_profile("slim_tpl", ("slim_slash_line", "html_xml_block"), handle_strings=False),
        create_profile("haml", ("haml_hyphen_hash_line",), handle_strings=False),
        create_profile("mako", ("velocity_double_hash_line", "mako_doc_block"), handle_strings=True),
        create_profile("smarty_tpl", ("smarty_block",), handle_strings=True),
        create_profile("freemarker_tpl", ("freemarker_block",), handle_strings=True),
        create_profile("velocity_tpl", ("velocity_double_hash_line", "velocity_hash_asterisk_block"),
                       handle_strings=True),
        create_profile("wren", c_style_base),
        create_profile("stan", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("thrift", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("edgeql", ("hash_line",)),
        create_profile("rego", ("hash_line",)),
        create_profile("caddyfile", ("hash_line",), handle_strings=False),
        create_profile("webassembly_text", ("wat_double_semicolon_line", "wat_paren_semicolon_block")),
        create_profile("jenkinsfile", c_style_base),
        create_profile("robot", ("hash_line",), handle_strings=False),
        create_profile("idris",
                       ("double_hyphen_line", "idris_doc_line", "haskell_curly_hyphen_block", "idris_doc_block")),
        create_profile("purescript", haskell_style_blocks),
        create_profile("elm", haskell_style_blocks),
        create_profile("dhall", ("double_hyphen_line", "haskell_curly_hyphen_block", "dhall_doc_block")),
        create_profile("openscad", c_style_base),
        create_profile("ant", ("html_xml_block",), handle_strings=False),
        create_profile("maven_pom", ("html_xml_block",), handle_strings=False),
        create_profile("windows_registry", ("semicolon_line_requires_start",), handle_strings=False),
        create_profile("jsonnet", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("gemfile", ("hash_line",)),
        create_profile("tcl", ("hash_line",)),
        create_profile("awk", ("hash_line",)),
        create_profile("autohotkey", ("semicolon_line_requires_start", "c_block_comment", "autoit_hash_cs_ce_block",
                                      "autoit_hash_comments_block")), # AHK uses ; for line comments and /* */
        create_profile("applescript", ("double_hyphen_line", "pascal_paren_asterisk_block")),
        create_profile("apex", c_style_doc),
        create_profile("coq", ("pascal_paren_asterisk_block",)),
        create_profile("gamemaker_language", c_style_doc),
        create_profile("hacklang", ("c_line_comment", "hash_line", "c_block_comment")),
        create_profile("livescript", ("hash_line", "c_block_comment")),
        create_profile("lookml", ("hash_line",), handle_strings=False),
        create_profile("meson", ("hash_line",), handle_strings=False),
        create_profile("modula2", ("pascal_paren_asterisk_block",)),
        create_profile("moonscript", ("double_hyphen_line", "lua_long_bracket_block")),
        create_profile("nsis", ("semicolon_line", "hash_line", "c_block_comment")),
        create_profile("openedge_abl", ("c_block_comment",)),
        create_profile("postscript", ("percent_line",), handle_strings=False),
        create_profile("povray_sdl", ("c_line_comment", "c_block_comment")),
        create_profile("processing", c_style_doc),
        create_profile("qml", ("c_line_comment", "c_block_comment")),
        create_profile("raml", ("hash_line",), handle_strings=False),
        create_profile("reasonml", c_style_doc), # Uses /* */ and //
        create_profile("red_lang", ("semicolon_line", "rebol_comment_brace_block", "rebol_comment_bracket_block")),
        create_profile("rebol", ("semicolon_line", "rebol_comment_brace_block", "rebol_comment_bracket_block")),
        create_profile("renpy", ("hash_line",)),
        create_profile("sas_lang", ("fortran_fixed_star_col1_line", "sas_asterisk_semicolon_block", "c_block_comment")), # SAS fixed format * at col 1
        create_profile("scilab", ("c_line_comment",)),
        create_profile("sourcepawn", c_style_base),
        create_profile("sqf", c_style_base),
        create_profile("sml", ("pascal_paren_asterisk_block",)),
        create_profile("stata", ("fortran_fixed_star_col1_line", "c_line_comment", "c_block_comment")),
        create_profile("tla_plus", ("tlaplus_line", "pascal_paren_asterisk_block")),
        create_profile("unrealscript", c_style_doc),
        create_profile("vala", c_style_doc),
        create_profile("vcl", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("vbscript", ("vb_single_quote_line", "rem_keyword_line")),
        create_profile("webidl", c_style_base),
        create_profile("wdl", ("hash_line",)),
        create_profile("yang", c_style_base),
        create_profile("csound", ("semicolon_line", "c_block_comment")),
        create_profile("supercollider", c_style_doc),
        create_profile("chuck", c_style_base),
        create_profile("faust", ("c_line_comment", "faust_triple_hyphen_doc_line", "c_block_comment")),
        create_profile("blitzmax", ("blitzmax_single_quote_line", "rem_lowercase_line", "rem_capitalized_line")),
        create_profile("boo", ("hash_line", "c_block_comment")),
        create_profile("abap", ("abap_asterisk_line", "abap_double_quote_line_non_col1")),
        create_profile("agda", haskell_style_blocks),
        create_profile("autoit",
                       ("semicolon_line_requires_start", "autoit_hash_cs_ce_block", "autoit_hash_comments_block")),
        create_profile("smalltalk", ("smalltalk_double_quote_block","smalltalk_exclamation_line")),
        create_profile("cabal", ("double_hyphen_line",), handle_strings=False),
        create_profile("clojurescript", ("semicolon_line",)),
        create_profile("cuda", c_style_doc + ("c_preprocessor_block",)), # CUDA C++
        create_profile("graphviz", ("c_line_comment", "c_block_comment", "hash_line")),
        create_profile("nginx", ("hash_line",), handle_strings=False),
        create_profile("apacheconf", ("hash_line",), handle_strings=False),
        create_profile("xslt_lang", ("html_xml_block",), handle_strings=False),
        create_profile("xsl", ("html_xml_block",), handle_strings=False),
        create_profile("actionscript", c_style_doc),
        create_profile("ags_script", c_style_base),
        create_profile("alloy", ("c_line_comment", "double_hyphen_line")),
        create_profile("angelscript", c_style_base),
        create_profile("antlr", c_style_doc),
        create_profile("api_blueprint", ("html_xml_block",), handle_strings=False),
        create_profile("asn1", ("double_hyphen_line",)),
        create_profile("asp", ("vb_single_quote_line",) + template_engine_percent_hyphen), # ASP (classic VBScript)
        create_profile("aspectj", c_style_doc),
        create_profile("ats", ("c_line_comment", "pascal_paren_asterisk_block")),
        create_profile("augeas", (), handle_strings=False), # No standard comment syntax
        create_profile("avro_idl", c_style_base),
        create_profile("ballerina", ("c_line_comment",)),
        create_profile("bicep", c_style_base),
        create_profile("bitbake", ("hash_line",)),
        create_profile("blitzbasic", ("rem_lowercase_line", "rem_capitalized_line", "semicolon_line")), # Blitz Basic REM or ;
        create_profile("brightscript", ("vb_single_quote_line", "rem_keyword_line")),
        create_profile("bsv", c_style_base), # Bluespec SystemVerilog
        create_profile("cadence", c_style_base), # Cadence SKILL or other Cadence languages
        create_profile("ceylon",
                       ("c_line_comment", "c_block_comment", "javadoc_block_comment", "ceylon_triple_quote_doc_block")),
        create_profile("chapel", c_style_base),
        create_profile("cil", c_style_base), # CIL / MSIL
        create_profile("clarion", ("fortran_exclamation_line", "clarion_pipe_line")),
        create_profile("clean", ("c_line_comment", "c_block_comment")),
        create_profile("clipper",
                       ("c_line_comment", "c_block_comment", "abap_asterisk_line", "double_ampersand_xbase_line")),
        create_profile("component_pascal", ("pascal_paren_asterisk_block",)),
        create_profile("cool", ("double_hyphen_line", "pascal_paren_asterisk_block")),
        create_profile("cue_lang", c_style_base),
        create_profile("cython",
                       ("python_hash_line", "python_triple_double_quote_block", "python_triple_single_quote_block")),
        create_profile("dafny", c_style_base),
        create_profile("dylan", ("c_line_comment", "c_block_comment")),
        create_profile("ecl", ("c_line_comment", "c_block_comment")),
        create_profile("eiffel", ("double_hyphen_line",)),
        create_profile("factor", ("hash_line", "fortran_exclamation_line")), # ! and # comments
        create_profile("fantom", c_style_base),
        create_profile("fstar", ("c_line_comment", "pascal_paren_asterisk_block")),
        create_profile("gams", ("abap_asterisk_line", "gams_dollar_onoff_text_block")),
        create_profile("gcode", ("semicolon_line", "gcode_paren_block")),
        create_profile("gherkin", ("hash_line",), handle_strings=False),
        create_profile("gnuplot", ("hash_line",)),
        create_profile("gosu", c_style_base),
        create_profile("harbour",
                       ("c_line_comment", "c_block_comment", "abap_asterisk_line", "double_ampersand_xbase_line")),
        create_profile("idl", ("semicolon_line",)), # Interactive Data Language
        create_profile("inform", ("fortran_exclamation_line", "inform7_bracket_block")), # Inform 6 and 7
        create_profile("io_lang", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("isabelle", ("pascal_paren_asterisk_block",)),
        create_profile("j_lang", ("nb_dot_jlang_line",)),
        create_profile("jcl", ("jcl_double_slash_star_line",)),
        create_profile("jolie", c_style_base),
        create_profile("jsoniq", ("xquery_block",)),
        create_profile("kusto_kql", ("c_line_comment",)),
        create_profile("lasso", ("c_line_comment", "c_block_comment")),
        create_profile("lean",
                       ("double_hyphen_line", "lean_slash_hyphen_doc_block", "lean_slash_hyphen_comment_block")),
        create_profile("ligo", ("c_line_comment", "pascal_paren_asterisk_block")),
        create_profile("llvm_ir", ("semicolon_line",)),
        create_profile("logo", ("semicolon_line",)),
        create_profile("logtalk", ("percent_line", "c_block_comment")),
        create_profile("lsl", ("c_line_comment",)), # Linden Scripting Language
        create_profile("maple", ("hash_line",)),
        create_profile("mathematica", ("pascal_paren_asterisk_block",)),
        create_profile("wolfram", ("pascal_paren_asterisk_block",)), # Alias for Mathematica
        create_profile("maxscript", ("double_hyphen_line", "c_block_comment")),
        create_profile("mercury", ("percent_line", "c_block_comment")),
        create_profile("metal", c_style_base), # Apple Metal Shading Language
        create_profile("modelica", ("c_line_comment", "c_block_comment")),
        create_profile("modula3", ("pascal_paren_asterisk_block",)),
        create_profile("monkey_c", c_style_base),
        create_profile("monkeyx", ("blitzmax_single_quote_line",)), # Monkey X uses '
        create_profile("move_lang", c_style_base),
        create_profile("mql", ("c_line_comment", "c_block_comment", "hash_line")), # MQL4/MQL5
        create_profile("myrddin", ("hash_line",)),
        create_profile("netlogo", ("semicolon_line",)),
        create_profile("newlisp", ("semicolon_line", "hash_line", "scheme_hash_pipe_block")),
        create_profile("nextflow", c_style_base),
        create_profile("nu", ("semicolon_line", "c_block_comment")), # Nu programming language
        create_profile("nunjucks_tpl", template_engine_curly_hash, handle_strings=True),
        create_profile("nwscript", c_style_base), # Neverwinter Nights Script
        create_profile("objectivej", c_style_base),
        create_profile("odin", c_style_base),
        create_profile("openclc", c_style_base), # OpenCL C
        create_profile("openqasm", ("c_line_comment",)),
        create_profile("oz", ("percent_line",)),
        create_profile("p4_lang", c_style_base),
        create_profile("papyrus_script", ("semicolon_line", "papyrus_brace_block")),
        create_profile("parasail", c_style_base),
        create_profile("pawn", c_style_base),
        create_profile("picat", ("percent_line",)),
        create_profile("pico_lisp", ("hash_line",)),
        create_profile("pike", c_style_base),
        create_profile("plantuml", ("plantuml_single_quote_line", "plantuml_slash_apostrophe_block")),
        create_profile("pony", c_style_base),
        create_profile("powerbuilder", ("c_line_comment", "c_block_comment")),
        create_profile("powerfx", c_style_base),
        create_profile("promela", c_style_base),
        create_profile("purebasic", ("semicolon_line",)),
        create_profile("puppet", ("hash_line", "c_block_comment")),
        create_profile("qsharp", ("c_line_comment", "csharp_doc_line")),
        create_profile("rexx", ("c_block_comment",)), # REXX uses /* ... */
        create_profile("ring", ("hash_line", "c_line_comment", "c_block_comment")),
        create_profile("roff", ("dot_backslash_double_quote_roff_line", "hash_line")), # .\" or \# for roff/troff/groff
        create_profile("rpg", ("c_line_comment", "c_block_comment")), # RPGLE free-form
        create_profile("sas", ("abap_asterisk_line", "sas_asterisk_semicolon_block", "c_block_comment")), # * ... ; and /* ... */
        create_profile("seed7", ("hash_line", "pascal_paren_asterisk_block")),
        create_profile("self_lang", ("smalltalk_double_quote_block",)),
        create_profile("shen", ("forth_backslash_line", "pascal_paren_asterisk_block")), # \ and (* *)
        create_profile("simula", ("simula_comment_keyword_block",)),
        create_profile("smali", ("hash_line",)),
        create_profile("snakemake", ("hash_line",)),
        create_profile("snobol", ("abap_asterisk_line",)), # SNOBOL4 uses * at line start
        create_profile("squirrel", c_style_base),
        create_profile("starlark", ("hash_line",)), # Bazel/Starlark
        create_profile("swig", ("c_line_comment", "c_block_comment", "hash_line")),
        create_profile("systemverilog", c_style_base),
        create_profile("tads", c_style_base), # TADS 2/3
        create_profile("textile", ("html_xml_block",), handle_strings=False), # Uses HTML comments
        create_profile("turing", ("percent_line",)),
        create_profile("unicon", ("hash_line",)),
        create_profile("urweb", ("pascal_paren_asterisk_block",)),
        create_profile("v", c_style_base), # V lang
        create_profile("verilog", c_style_base),
        create_profile("vhdl", ("double_hyphen_line",)),
        create_profile("visual_foxpro", ("abap_asterisk_line", "double_ampersand_xbase_line", "note_foxpro_line")),
        create_profile("vyper", ("hash_line",)),
        create_profile("wenyan", ("hash_line", "python_triple_single_quote_block", "wenyan_shu_yue_block")),
        create_profile("wgsl", c_style_base), # WebGPU Shading Language
        create_profile("whiley", ("c_line_comment",)),
        create_profile("wikitext", ("html_xml_block",), handle_strings=False), # MediaWiki uses HTML comments
        create_profile("x10", c_style_base),
        create_profile("xojo", ("vb_single_quote_line", "c_line_comment", "rem_keyword_line")),
        create_profile("xtend", c_style_doc),
        create_profile("zeek", ("hash_line",)), # Zeek (Bro)
        create_profile("zephir", c_style_base),
        create_profile("zimpl", ("hash_line",)),
    ]

    for profile in profiles:
        LANGUAGE_PROFILES_REGISTRY[profile.language_id] = profile

    if "none" not in LANGUAGE_PROFILES_REGISTRY: # Ensure fallback profile
        LANGUAGE_PROFILES_REGISTRY["none"] = create_profile("none", (), handle_strings=False)


# _initialize_comment_configurations()
# _populate_language_profiles_registry()