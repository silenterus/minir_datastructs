from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Any, Dict

@dataclass(frozen=True)
class Position:
    line: int
    column: int

@dataclass(frozen=True)
class SourceLocation:
    start: Position
    end: Position

@dataclass(frozen=True)
class FileData:
    path: str
    content: Optional[str] = None
    language: Optional[str] = None

@dataclass(frozen=True)
class ProjectContext:
    project_name: str
    project_root_abs_path: str
    files: List[FileData]

class AgnosticErrorSeverity(Enum):
    ERROR = auto()
    WARNING = auto()
    INFO = auto()

@dataclass(frozen=True)
class AgnosticExtractionError:
    file_data: FileData
    message: str
    start_pos: Optional[Position] = None
    end_pos: Optional[Position] = None
    context_snippet: Optional[str] = None
    severity: AgnosticErrorSeverity = AgnosticErrorSeverity.ERROR
    language_specific_error_code: Optional[str] = None

class AgnosticDeclarationKind(Enum):
    MODULE = auto()
    NAMESPACE_OR_PACKAGE = auto()
    CLASS = auto()
    STRUCT = auto()
    INTERFACE = auto()
    PROTOCOL = auto()
    ENUM = auto()
    UNION = auto()
    TYPE_ALIAS = auto()
    FUNCTION = auto()
    METHOD = auto()
    CONSTRUCTOR = auto()
    DESTRUCTOR = auto()
    VARIABLE = auto()
    CONSTANT = auto()
    FIELD = auto()
    ENUM_MEMBER = auto()
    PROPERTY = auto()
    EVENT = auto()
    DELEGATE = auto()
    RECORD = auto()
    ANNOTATION_TYPE = auto()
    ERROR_TYPE = auto()
    BITFIELD = auto()
    CONCEPT = auto()
    PARAMETER = auto()
    GENERIC_PARAMETER = auto()
    IMPORT_DIRECTIVE = auto()
    ATTRIBUTE_OR_DECORATOR_APPLICATION = auto()
    PREPROCESSOR_DIRECTIVE = auto()
    MACRO_DEFINITION = auto()
    MACRO_INVOCATION = auto()
    LINKAGE_SPECIFICATION = auto()
    MODULE_EXPORT = auto()
    TYPE_HINT = auto()
    EXCEPTION_DEFINITION = auto()
    MODULE_LEVEL_CODE_BLOCK = auto()
    IF_STATEMENT = auto()
    ELSE_IF_CLAUSE = auto()
    ELSE_CLAUSE = auto()
    SWITCH_STATEMENT = auto()
    CASE_CLAUSE = auto()
    FOR_LOOP = auto()
    WHILE_LOOP = auto()
    DO_WHILE_LOOP = auto()
    TRY_BLOCK = auto()
    CATCH_CLAUSE = auto()
    FINALLY_BLOCK = auto()
    MATCH_EXPRESSION = auto()
    WITH_STATEMENT = auto()
    RETURN_STATEMENT = auto()
    YIELD_STATEMENT = auto()
    BREAK_STATEMENT = auto()
    CONTINUE_STATEMENT = auto()
    GOTO_STATEMENT = auto()
    ASSERT_STATEMENT = auto()
    EXPRESSION_STATEMENT = auto()
    COMPOUND_STATEMENT = auto()
    LAMBDA_OR_ANONYMOUS_FUNCTION = auto()
    DOC_COMMENT = auto()
    COMMENT_BLOCK = auto()
    ERROR_DECLARATION = auto()
    UNKNOWN = auto()

class AgnosticAccessModifier(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()
    INTERNAL = auto()
    FILE_PRIVATE = auto()
    PACKAGE_PRIVATE = auto()
    NOT_APPLICABLE = auto()
    UNKNOWN = auto()

class AgnosticStorageModifier(Enum):
    STATIC = auto()
    CONST = auto()
    FINAL = auto()
    ABSTRACT = auto()
    VIRTUAL = auto()
    OVERRIDE = auto()
    MUTABLE = auto()
    VOLATILE = auto()
    TRANSIENT = auto()
    SYNCHRONIZED = auto()
    ATOMIC = auto()
    EXTERN = auto()
    INLINE = auto()
    DEFAULT = auto()
    SEALED = auto()
    READONLY = auto()
    LAZY = auto()
    LATEINIT = auto()
    UNSAFE = auto()
    COMPTIME = auto()
    PARTIAL = auto()
    REFIX = auto()
    THREAD_LOCAL = auto()
    REGISTER = auto()
    NONE = auto()

class AgnosticFunctionModifier(Enum):
    ASYNC = auto()
    GENERATOR = auto()
    EXPLICIT = auto()
    NOEXCEPT = auto()
    CONST_METHOD = auto()
    OPERATOR = auto()
    RECURSIVE = auto()
    EXTENSION = auto()
    INFIX = auto()

class AgnosticFunctionRole(Enum):
    REGULAR = auto()
    CONSTRUCTOR_DEFAULT = auto()
    CONSTRUCTOR_USER_DEFINED = auto()
    DESTRUCTOR_OR_FINALIZER = auto()
    GETTER = auto()
    SETTER = auto()
    OPERATOR_BINARY = auto()
    OPERATOR_UNARY = auto()
    CONVERSION_OPERATOR = auto()
    STATIC_METHOD = auto()
    CLASS_METHOD = auto()
    ABSTRACT_METHOD = auto()
    EXTENSION_METHOD = auto()
    MAIN_ENTRY_POINT = auto()
    TEST_CASE = auto()
    HELPER_OR_UTILITY = auto()
    EVENT_HANDLER = auto()
    LAMBDA_OR_CLOSURE_HANDLER = auto()
    STATIC_INITIALIZER_BLOCK = auto()
    INSTANCE_INITIALIZER_BLOCK = auto()
    COROUTINE_OR_ASYNC_GENERATOR = auto()
    NOT_APPLICABLE = auto()

class AgnosticParameterPassingConvention(Enum):
    BY_VALUE = auto()
    BY_REFERENCE = auto()
    BY_POINTER = auto()
    IN_PARAMETER = auto()
    OUT_PARAMETER = auto()
    INPUT_OUTPUT = auto()
    COPY_IN_COPY_OUT = auto()
    RECEIVER = auto()
    NOT_APPLICABLE = auto()

class AgnosticCommentType(Enum):
    SINGLE_LINE = auto()
    MULTI_LINE_BLOCK = auto()
    DOCUMENTATION = auto()
    PREPROCESSOR_COMMENT = auto()
    LINTER_CONTROL = auto()
    HEADER = auto()
    SHEBANG = auto()
    ENCODING_DECLARATION = auto()

@dataclass(frozen=True)
class AgnosticComment:
    content: str
    raw_text: str
    start_pos: Position
    end_pos: Position
    comment_type: AgnosticCommentType

@dataclass(frozen=True)
class AgnosticAnnotationOrDecorator:
    name_or_expression_str: str
    start_pos: Position
    end_pos: Position
    language_specific_raw_ast_node: Optional[Any] = None
    qualname_parts: List[str] = field(default_factory=list)
    arguments_str: Optional[str] = None

@dataclass(frozen=True)
class AgnosticParameter:
    name: Optional[str]
    start_pos: Position
    end_pos: Position
    name_pos: Optional[Position] = None
    type_signature_str: Optional[str] = None
    default_value_str: Optional[str] = None
    passing_convention: Optional[AgnosticParameterPassingConvention] = None
    is_variadic: bool = False
    is_keyword_variadic: bool = False
    is_keyword_only: bool = False
    is_positional_only: bool = False
    annotations_or_decorators: List[AgnosticAnnotationOrDecorator] = field(default_factory=list)
    storage_modifiers: List[AgnosticStorageModifier] = field(default_factory=list)
    language_specific_param_kind: Optional[str] = None
    full_text: Optional[str] = None

class AgnosticGenericParameterKind(Enum):
    TYPE = auto()
    VALUE = auto()
    TEMPLATE = auto()
    LIFETIME = auto()
    CONSTRAINT = auto()

@dataclass(frozen=True)
class AgnosticGenericParameter:
    name: str
    start_pos: Position
    end_pos: Position
    kind: AgnosticGenericParameterKind = AgnosticGenericParameterKind.TYPE
    constraints: Optional[List[str]] = None
    variance: Optional[str] = None
    default_type: Optional[str] = None
    is_variadic_pack: bool = False

@dataclass(frozen=True)
class AgnosticImportItem:
    name: str
    alias: Optional[str] = None
    is_type_only_import: bool = False
    start_pos: Optional[Position] = None
    end_pos: Optional[Position] = None

@dataclass(frozen=True)
class AgnosticImport:
    module_or_path_parts: List[str]
    start_pos: Position
    end_pos: Position
    imported_items: Optional[List[AgnosticImportItem]] = None
    alias_for_module_or_path: Optional[str] = None
    is_wildcard: bool = False
    is_relative: bool = False
    relative_level: int = 0
    source_language_construct: Optional[str] = None


class AgnosticTokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    DELIMITER_OR_PUNCTUATOR = auto()
    LITERAL_STRING = auto()
    LITERAL_NUMBER = auto()
    LITERAL_CHAR = auto()
    LITERAL_BOOLEAN = auto()
    LITERAL_NULL_OR_NONE = auto()
    COMMENT = auto()
    PREPROCESSOR_DIRECTIVE = auto()
    WHITESPACE = auto()
    NEWLINE = auto()
    EOF = auto()
    UNKNOWN_OR_ERROR = auto()

@dataclass(frozen=True)
class AgnosticToken:
    token_type: AgnosticTokenType
    text: str
    full_text: str
    start_pos: Position
    end_pos: Position
    file_data: FileData
    interpreted_value: Optional[Any] = None
    language_specific_token_type_name: Optional[str] = None

@dataclass(frozen=True)
class ExtractedAgnosticDeclaration:
    name: Optional[str]
    kind: AgnosticDeclarationKind
    file_data: FileData
    start_pos: Position
    end_pos: Position
    name_pos: Optional[Position] = None
    qualified_name_parts: List[str] = field(default_factory=list)
    scope_qualname_parts: List[str] = field(default_factory=list)
    access_modifier: Optional[AgnosticAccessModifier] = None
    storage_modifiers: List[AgnosticStorageModifier] = field(default_factory=list)
    other_language_specific_modifiers: List[str] = field(default_factory=list)
    type_signature_str: Optional[str] = None
    initializer_or_default_value_str: Optional[str] = None
    parameters: Optional[List[AgnosticParameter]] = None
    function_role: Optional[AgnosticFunctionRole] = None
    function_modifiers: List[AgnosticFunctionModifier] = field(default_factory=list)
    return_type_signature_str: Optional[str] = None
    exceptions_thrown_str_list: Optional[List[str]] = None
    base_type_signatures_str_list: Optional[List[str]] = None
    is_abstract_type: bool = False
    is_final_type: bool = False
    generic_parameters: Optional[List[AgnosticGenericParameter]] = None
    import_details: Optional[AgnosticImport] = None
    annotations_or_decorators: List[AgnosticAnnotationOrDecorator] = field(default_factory=list)
    documentation: Optional[AgnosticComment] = None
    leading_comments: List[AgnosticComment] = field(default_factory=list)
    inline_comment: Optional[AgnosticComment] = None
    full_text: Optional[str] = None
    signature_text: Optional[str] = None
    body_text: Optional[str] = None
    body_start_pos: Optional[Position] = None
    body_end_pos: Optional[Position] = None
    is_definition: bool = True
    language_name: Optional[str] = None
    language_specific_kind_name: Optional[str] = None
    language_specific_details: Dict[str, Any] = field(default_factory=dict)
    raw_ast_node_type: Optional[str] = None
    is_property_backing_field: bool = False
    property_getter_qualname: Optional[str] = None
    property_setter_qualname: Optional[str] = None
    error_message: Optional[str] = None
    condition_expression_str: Optional[str] = None
    iterable_expression_str: Optional[str] = None
    switch_expression_str: Optional[str] = None

@dataclass(frozen=True)
class AgnosticExtractionResult:
    file_data: FileData
    declarations: List[ExtractedAgnosticDeclaration] = field(default_factory=list)
    errors: List[AgnosticExtractionError] = field(default_factory=list)
    tokens: Optional[List[AgnosticToken]] = None