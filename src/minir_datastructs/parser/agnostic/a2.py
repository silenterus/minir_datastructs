from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Any, Dict, Union

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
    project_root_abs: str
    files: List[FileData]

class Visibility(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()
    INTERNAL = auto()
    PACKAGE = auto()
    FILE_PRIVATE = auto()
    NOT_APPLICABLE = auto()
    LANG_SPECIFIC = auto()
    UNKNOWN = auto()

class GeneralPurposeModifier(Enum):
    ABSTRACT = auto()
    ASYNC = auto()
    ATOMIC = auto()
    CONST = auto()
    CONST_METHOD = auto()
    COMPTIME = auto()
    DEFAULT = auto()
    EXPLICIT = auto()
    EXTERN = auto()
    FINAL = auto()
    GENERATOR = auto()
    INFIX = auto()
    INLINE = auto()
    LAZY = auto()
    LATEINIT = auto()
    MUTABLE = auto()
    NOEXCEPT = auto()
    OPERATOR = auto()
    OVERRIDE = auto()
    PARTIAL = auto()
    READONLY = auto()
    REFIX = auto()
    SEALED = auto()
    STATIC = auto()
    SYNCHRONIZED = auto()
    TRANSIENT = auto()
    UNSAFE = auto()
    VIRTUAL = auto()
    VOLATILE = auto()
    LANG_SPECIFIC = auto()
    NONE = auto()

class StorageSpecifier(Enum):
    NONE = auto()
    STATIC = auto()
    EXTERN = auto()
    MUTABLE_MEMBER = auto()
    THREAD_LOCAL = auto()
    REGISTER = auto()
    GLOBAL_KEYWORD = auto()
    NONLOCAL_KEYWORD = auto()
    LET_OR_FINAL_VAR = auto()
    VAR_OR_MUTABLE_BINDING = auto()

class DeclarationType(Enum):
    NAMESPACE_OR_MODULE = auto()
    CLASS_OR_STRUCT = auto()
    INTERFACE_OR_PROTOCOL_OR_TRAIT = auto()
    UNION = auto()
    ENUM = auto()
    ENUM_MEMBER = auto()
    FUNCTION_OR_METHOD = auto()
    CONSTRUCTOR = auto()
    DESTRUCTOR_OR_FINALIZER = auto()
    VARIABLE_OR_FIELD = auto()
    CONSTANT = auto()
    PARAMETER = auto()
    TYPE_ALIAS_OR_TYPEDEF = auto()
    GENERIC_TYPE_PARAMETER = auto()
    GENERIC_VALUE_PARAMETER = auto()
    GENERIC_TEMPLATE_PARAMETER = auto()
    IMPORT_OR_USING_DIRECTIVE = auto()
    ATTRIBUTE_OR_DECORATOR_OR_ANNOTATION = auto()
    MACRO_DEFINITION = auto()
    PREPROCESSOR_DIRECTIVE = auto()
    COMMENT_BLOCK = auto()
    DOC_COMMENT = auto()
    ACCESS_SPECIFIER_KEYWORD = auto()
    CONTROL_FLOW_STRUCTURE = auto()
    EXPRESSION_STATEMENT = auto()
    LAMBDA_OR_ANONYMOUS_FUNCTION = auto()
    OPERATOR_OVERLOAD = auto()
    PROPERTY = auto()
    EVENT = auto()
    DELEGATE = auto()
    MODULE_LEVEL_BLOCK = auto()
    LABEL = auto()
    ANNOTATION_DEFINITION = auto()
    CONCEPT_DEFINITION = auto()
    EXCEPTION_DEFINITION = auto()
    ERROR_NODE = auto()
    UNKNOWN = auto()

class FunctionSpecificKind(Enum):
    REGULAR = auto()
    CONSTRUCTOR_DEFAULT = auto()
    CONSTRUCTOR_USER_DEFINED = auto()
    DESTRUCTOR_OR_FINALIZER = auto()
    GETTER = auto()
    SETTER = auto()
    OPERATOR_BINARY = auto()
    OPERATOR_UNARY = auto()
    OPERATOR_OVERLOAD = auto()
    CONVERSION_OPERATOR = auto()
    EVENT_HANDLER = auto()
    MAIN_ENTRY_POINT = auto()
    TEST_CASE = auto()
    HELPER_OR_UTILITY = auto()
    LAMBDA_OR_CLOSURE_HANDLER = auto()
    INITIALIZER_BLOCK = auto()
    STATIC_METHOD = auto()
    CLASS_METHOD = auto()
    ABSTRACT_METHOD = auto()
    EXTENSION_METHOD = auto()
    COROUTINE_OR_ASYNC_GENERATOR = auto()
    NOT_APPLICABLE = auto()

class CommentType(Enum):
    SINGLE_LINE = auto()
    MULTI_LINE_BLOCK = auto()
    DOCUMENTATION_LINE = auto()
    DOCUMENTATION_BLOCK = auto()
    PREPROCESSOR_COMMENT = auto()
    FILE_HEADER = auto()
    SHEBANG = auto()
    ENCODING_DECLARATION = auto()
    LINTER_CONTROL = auto()

class ParameterPassingConvention(Enum):
    BY_VALUE = auto()
    BY_REFERENCE = auto()
    BY_POINTER = auto()
    IN_PARAMETER = auto()
    OUT_PARAMETER = auto()
    INPUT_OUTPUT = auto()
    COPY_IN_COPY_OUT = auto()
    NOT_APPLICABLE = auto()

class FunctionProperty(Enum):
    NOEXCEPT = auto()
    CONST_METHOD = auto()
    INFIX = auto()

class ErrorSeverity(Enum):
    ERROR = auto()
    WARNING = auto()
    INFO = auto()

@dataclass(frozen=True)
class Comment:
    content: str
    raw_text: str
    location: SourceLocation
    type: CommentType
    is_documentation_for_next: bool = False
    is_documentation_for_parent: bool = False
    is_documentation_for_previous: bool = False

@dataclass(frozen=True)
class ExtractedAttributeOrDecorator:
    name_or_expression: str
    arguments_str: Optional[str] = None
    location: SourceLocation
    qualname_parts: List[str] = field(default_factory=list)
    language_specific_raw: Optional[Any] = None

@dataclass(frozen=True)
class ExtractedParameter:
    name: str
    location: SourceLocation
    name_location: Optional[SourceLocation] = None
    type_str: Optional[str] = None
    default_value_str: Optional[str] = None
    is_variadic: bool = False
    is_keyword_variadic: bool = False
    is_keyword_only: bool = False
    is_positional_only: bool = False
    passing_convention: Optional[ParameterPassingConvention] = None
    general_modifiers: List[GeneralPurposeModifier] = field(default_factory=list)
    attributes_or_decorators: List[ExtractedAttributeOrDecorator] = field(default_factory=list)
    language_specific_kind: Optional[str] = None
    full_text: Optional[str] = None

@dataclass(frozen=True)
class ExtractedGenericParameter:
    name: str
    constraints_str_list: Optional[List[str]] = None
    variance_str: Optional[str] = None
    default_type_str: Optional[str] = None
    location: SourceLocation
    is_variadic_pack: bool = False
    kind: Optional[str] = None

@dataclass
class BaseExtractedDeclaration:
    name: Optional[str]
    declaration_type: DeclarationType
    file_data: FileData
    location: SourceLocation
    language_specific_kind: Optional[str] = None

    name_location: Optional[SourceLocation] = None
    body_location: Optional[SourceLocation] = None
    qualified_name_parts: List[str] = field(default_factory=list)
    scope_qualname_parts: List[str] = field(default_factory=list)
    visibility: Visibility = Visibility.NOT_APPLICABLE
    general_modifiers: List[GeneralPurposeModifier] = field(default_factory=list)
    storage_specifiers: List[StorageSpecifier] = field(default_factory=list)
    attributes_or_decorators: List[ExtractedAttributeOrDecorator] = field(default_factory=list)
    doc_comment: Optional[Comment] = None
    leading_comments: List[Comment] = field(default_factory=list)
    trailing_comment: Optional[Comment] = None
    full_text_snippet: Optional[str] = None
    signature_text_snippet: Optional[str] = None
    body_text_snippet: Optional[str] = None
    language_specific_details: Dict[str, Any] = field(default_factory=dict)
    is_definition: bool = True
    raw_ast_node_type: Optional[str] = None

@dataclass(frozen=True)
class ExtractedNamespaceOrModule(BaseExtractedDeclaration):
    pass

@dataclass(frozen=True)
class ExtractedVariableOrField(BaseExtractedDeclaration):
    type_str: Optional[str] = None
    initializer_str: Optional[str] = None
    is_property_backing_field: bool = False

@dataclass(frozen=True)
class ExtractedFunctionOrMethod(BaseExtractedDeclaration):
    return_type_str: Optional[str] = None
    parameters: List[ExtractedParameter] = field(default_factory=list)
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)
    throws_exceptions_str: List[str] = field(default_factory=list)
    role: FunctionSpecificKind = FunctionSpecificKind.REGULAR
    is_extension_method: bool = False
    function_properties: List[FunctionProperty] = field(default_factory=list)

@dataclass(frozen=True)
class ExtractedProperty(BaseExtractedDeclaration):
    type_str: Optional[str] = None
    getter: Optional[ExtractedFunctionOrMethod] = None
    setter: Optional[ExtractedFunctionOrMethod] = None

@dataclass(frozen=True)
class ExtractedAggregate(BaseExtractedDeclaration):
    base_type_signatures_str_list: List[str] = field(default_factory=list)
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)
    is_abstract_type: bool = False
    is_final_type: bool = False

@dataclass(frozen=True)
class ExtractedEnumMember(BaseExtractedDeclaration):
    value_str: Optional[str] = None

@dataclass(frozen=True)
class ExtractedImportItem:
    name: str
    alias: Optional[str] = None
    is_type_only_import: bool = False

@dataclass(frozen=True)
class ExtractedImport(BaseExtractedDeclaration):
    module_or_namespace_path_parts: List[str] = field(default_factory=list)
    imported_items: Optional[List[ExtractedImportItem]] = None
    is_wildcard_import: bool = False
    is_relative: bool = False
    relative_level: int = 0

@dataclass(frozen=True)
class ExtractedTypeAlias(BaseExtractedDeclaration):
    original_type_str: str
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)

@dataclass(frozen=True)
class GenericToken:
    class Type(Enum):
        IDENTIFIER = auto()
        KEYWORD = auto()
        OPERATOR = auto()
        PUNCTUATOR_OR_DELIMITER = auto()
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

    type: Type
    language_specific_type: Optional[str]
    text: str
    value: Optional[Any] = None
    location: SourceLocation
    file_data: FileData
    full_raw_text: Optional[str] = None

@dataclass(frozen=True)
class ExtractionError:
    file_data: FileData
    message: str
    location: Optional[SourceLocation] = None
    context_snippet: Optional[str] = None
    language_specific_error_code: Optional[str] = None
    severity: ErrorSeverity = ErrorSeverity.ERROR

AnyExtractedDeclaration = Union[
    BaseExtractedDeclaration,
    ExtractedNamespaceOrModule,
    ExtractedVariableOrField,
    ExtractedFunctionOrMethod,
    ExtractedProperty,
    ExtractedAggregate,
    ExtractedEnumMember,
    ExtractedImport,
    ExtractedTypeAlias
]

@dataclass(frozen=True)
class ExtractionResult:
    file_data: FileData
    declarations: List[AnyExtractedDeclaration] = field(default_factory=list)
    errors: List[ExtractionError] = field(default_factory=list)