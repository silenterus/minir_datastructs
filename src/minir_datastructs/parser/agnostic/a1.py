from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Any, Dict, Union, Tuple

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
    language: str
    content: Optional[str] = None

@dataclass(frozen=True)
class ProjectContext:
    project_name: str
    project_root_path_abs: str
    files: List[FileData]

class DeclarationType(Enum):
    NAMESPACE_OR_MODULE = auto()
    CLASS = auto()
    STRUCT = auto()
    INTERFACE_OR_PROTOCOL_OR_TRAIT = auto()
    UNION = auto()
    ENUM = auto()
    ENUM_MEMBER = auto()
    FUNCTION_OR_METHOD = auto()
    CONSTRUCTOR = auto()
    DESTRUCTOR_OR_FINALIZER = auto()
    VARIABLE_OR_FIELD = auto()
    CONSTANT = auto()
    TYPE_ALIAS_OR_TYPEDEF = auto()
    IMPORT_OR_USING_DIRECTIVE = auto()
    ATTRIBUTE_OR_DECORATOR_DEFINITION = auto()
    MACRO_DEFINITION = auto()
    PREPROCESSOR_DIRECTIVE = auto()
    COMMENT_BLOCK_ELEMENT = auto()
    DOC_COMMENT_ELEMENT = auto()
    ACCESS_SPECIFIER_KEYWORD_BLOCK = auto()
    CONTROL_FLOW_STRUCTURE = auto()
    EXPRESSION_STATEMENT = auto()
    LAMBDA_OR_ANONYMOUS_FUNCTION = auto()
    OPERATOR_OVERLOAD_DECL = auto()
    PROPERTY = auto()
    EVENT = auto()
    DELEGATE = auto()
    RECORD = auto()
    ERROR_TYPE_DECLARATION = auto()
    MODULE_LEVEL_CODE_BLOCK = auto()
    LABEL = auto()
    TYPE_HINT_DECLARATION = auto()
    FILE_SCOPE_ENTITY = auto()
    ERROR_NODE = auto()
    UNKNOWN = auto()

class Visibility(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()
    INTERNAL = auto()
    PACKAGE_PRIVATE = auto()
    FILE_PRIVATE = auto()
    NOT_APPLICABLE = auto()
    UNKNOWN = auto()
    LANG_SPECIFIC = auto()

class Modifier(Enum):
    STATIC = auto()
    INSTANCE = auto()
    ABSTRACT = auto()
    FINAL = auto()
    SEALED = auto()
    CONST = auto()
    READONLY = auto()
    MUTABLE = auto()
    VOLATILE = auto()
    SYNCHRONIZED = auto()
    ASYNC = auto()
    GENERATOR = auto()
    UNSAFE = auto()
    EXTERN = auto()
    VIRTUAL = auto()
    OVERRIDE = auto()
    INLINE = auto()
    EXPLICIT = auto()
    DEFAULT_IMPL = auto()
    COMPTIME = auto()
    LAZY = auto()
    PARTIAL = auto()
    OPERATOR_KEYWORD = auto()
    REFIX = auto()
    THREAD_LOCAL = auto()
    REGISTER_HINT = auto()
    GLOBAL_KEYWORD_USAGE = auto()
    NONLOCAL_KEYWORD_USAGE = auto()
    LANG_SPECIFIC = auto()
    NONE = auto()

class FunctionRole(Enum):
    REGULAR = auto()
    CONSTRUCTOR_USER_DEFINED = auto()
    CONSTRUCTOR_DEFAULT = auto()
    CONSTRUCTOR_IMPLICIT = auto()
    DESTRUCTOR_OR_FINALIZER = auto()
    GETTER = auto()
    SETTER = auto()
    OPERATOR_UNARY = auto()
    OPERATOR_BINARY = auto()
    CONVERSION_OPERATOR = auto()
    STATIC_METHOD = auto()
    CLASS_METHOD = auto()
    ABSTRACT_METHOD = auto()
    EXTENSION_METHOD = auto()
    EVENT_HANDLER = auto()
    MAIN_ENTRY_POINT = auto()
    TEST_CASE = auto()
    HELPER_OR_UTILITY = auto()
    LAMBDA_OR_CLOSURE_HANDLER = auto()
    STATIC_INITIALIZER_BLOCK = auto()
    INSTANCE_INITIALIZER_BLOCK = auto()
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

class GenericParameterKind(Enum):
    TYPE = auto()
    VALUE = auto()
    TEMPLATE = auto()
    LIFETIME = auto()
    CONSTRAINT = auto()

@dataclass(frozen=True)
class ExtractedComment:
    text_content: str
    location: SourceLocation
    type: CommentType
    is_doc_comment: bool
    is_documentation_for_next: bool = False
    is_documentation_for_parent: bool = False
    is_documentation_for_previous: bool = False
    language_specific_type: Optional[str] = None

@dataclass(frozen=True)
class ExtractedAttributeOrDecorator:
    name_or_expression: str
    location: SourceLocation
    language_specific_raw: Optional[Any] = None
    qualname_parts: List[str] = field(default_factory=list)
    arguments_str: Optional[str] = None

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
    passing_mechanism_str: Optional[str] = None
    modifiers: List[Modifier] = field(default_factory=list)
    attributes_or_decorators: List[ExtractedAttributeOrDecorator] = field(default_factory=list)
    language_specific_kind_str: Optional[str] = None
    full_text_snippet: Optional[str] = None

@dataclass(frozen=True)
class ExtractedGenericParameter:
    name: str
    location: SourceLocation
    constraints_str_list: Optional[List[str]] = None
    variance_str: Optional[str] = None
    default_type_str: Optional[str] = None
    kind: GenericParameterKind = GenericParameterKind.TYPE
    is_variadic_pack: bool = False

@dataclass(frozen=True)
class BaseExtractedDeclaration:
    name: Optional[str]
    declaration_type: DeclarationType
    file_data: FileData
    location: SourceLocation
    name_location: Optional[SourceLocation] = None
    body_location: Optional[SourceLocation] = None
    qualified_name_parts: List[str] = field(default_factory=list)
    scope_qualname_parts: List[str] = field(default_factory=list)
    visibility: Visibility = Visibility.NOT_APPLICABLE
    modifiers: List[Modifier] = field(default_factory=list)
    attributes_or_decorators: List[ExtractedAttributeOrDecorator] = field(default_factory=list)
    doc_comment: Optional[ExtractedComment] = None
    other_comments: List[ExtractedComment] = field(default_factory=list)
    full_text_snippet: Optional[str] = None
    signature_text_snippet: Optional[str] = None
    body_text_snippet: Optional[str] = None
    language_specific_kind_str: Optional[str] = None
    language_specific_details: Dict[str, Any] = field(default_factory=dict)
    is_definition: bool = True

@dataclass(frozen=True)
class ExtractedNamespaceOrModule(BaseExtractedDeclaration):
    pass

@dataclass(frozen=True)
class ExtractedAggregate(BaseExtractedDeclaration):
    base_types_str: List[str] = field(default_factory=list)
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)

@dataclass(frozen=True)
class ExtractedClass(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedStruct(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedInterface(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedUnion(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedEnum(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedRecord(ExtractedAggregate):
    pass

@dataclass(frozen=True)
class ExtractedEnumMember(BaseExtractedDeclaration):
    value_str: Optional[str] = None

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
    exceptions_thrown_str_list: List[str] = field(default_factory=list)
    role: FunctionRole = FunctionRole.REGULAR
    is_extension_method: bool = False

@dataclass(frozen=True)
class ExtractedProperty(BaseExtractedDeclaration):
    type_str: Optional[str] = None
    getter: Optional[ExtractedFunctionOrMethod] = None
    setter: Optional[ExtractedFunctionOrMethod] = None

@dataclass(frozen=True)
class ExtractedImportDirective(BaseExtractedDeclaration):
    path_parts: List[str] = field(default_factory=list)
    imported_items: Optional[List[Tuple[str, Optional[str]]]] = None
    is_wildcard_import: bool = False
    is_relative_import: bool = False
    relative_import_level: int = 0

@dataclass(frozen=True)
class ExtractedTypeAlias(BaseExtractedDeclaration):
    original_type_str: str
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)

@dataclass(frozen=True)
class ExtractedEvent(BaseExtractedDeclaration):
    type_str: Optional[str] = None

@dataclass(frozen=True)
class ExtractedDelegate(BaseExtractedDeclaration):
    return_type_str: Optional[str] = None
    parameters: List[ExtractedParameter] = field(default_factory=list)
    generic_parameters: List[ExtractedGenericParameter] = field(default_factory=list)

@dataclass(frozen=True)
class ExtractedMacroDefinition(BaseExtractedDeclaration):
    parameters_str: Optional[str] = None
    body_str: Optional[str] = None

@dataclass(frozen=True)
class ExtractedPreprocessorDirective(BaseExtractedDeclaration):
    directive_content: str

@dataclass(frozen=True)
class ExtractedErrorNode(BaseExtractedDeclaration):
    error_message: str

class GenericTokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    SEPARATOR_OR_PUNCTUATOR = auto()
    LITERAL_STRING = auto()
    LITERAL_NUMBER = auto()
    LITERAL_CHAR = auto()
    LITERAL_BOOLEAN = auto()
    LITERAL_NULL_OR_NONE = auto()
    COMMENT = auto()
    PREPROCESSOR_TEXT = auto()
    WHITESPACE = auto()
    NEWLINE = auto()
    EOF = auto()
    UNKNOWN_OR_ERROR = auto()

@dataclass(frozen=True)
class GenericToken:
    type: GenericTokenType
    token_text: str
    location: SourceLocation
    file_data: FileData
    processed_value: Optional[Any] = None
    language_specific_type_name: Optional[str] = None
    full_source_text: Optional[str] = None

@dataclass(frozen=True)
class ExtractionError:
    file_data: FileData
    message: str
    location: Optional[SourceLocation] = None
    context_snippet: Optional[str] = None
    language_specific_error_code: Optional[str] = None

AnyExtractedDeclaration = Union[
    BaseExtractedDeclaration,
    ExtractedNamespaceOrModule,
    ExtractedClass,
    ExtractedStruct,
    ExtractedInterface,
    ExtractedUnion,
    ExtractedEnum,
    ExtractedRecord,
    ExtractedEnumMember,
    ExtractedVariableOrField,
    ExtractedFunctionOrMethod,
    ExtractedProperty,
    ExtractedImportDirective,
    ExtractedTypeAlias,
    ExtractedEvent,
    ExtractedDelegate,
    ExtractedMacroDefinition,
    ExtractedPreprocessorDirective,
    ExtractedErrorNode
]

@dataclass(frozen=True)
class ExtractionResult:
    file_data: FileData
    declarations: List[AnyExtractedDeclaration] = field(default_factory=list)
    errors: List[ExtractionError] = field(default_factory=list)
    tokens: List[GenericToken] = field(default_factory=list)