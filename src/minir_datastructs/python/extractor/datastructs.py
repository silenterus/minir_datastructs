

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Set, Tuple, Any, Dict
import keyword as kw
import string
import inspect

@dataclass(frozen=True)
class Position:
    line: int
    column: int

@dataclass(frozen=True)
class FileData:
    path: str
    content: Optional[str] = None

@dataclass(frozen=True)
class ProcessedProjectData:
    project_name: str
    project_path_abs: str
    files: List[FileData]

class PythonAccessConvention(Enum):
    PUBLIC = 'public'
    PROTECTED_INTERNAL = 'protected_internal'
    PRIVATE_NAME_MANGLED = 'private_name_mangled'
    SPECIAL_DUNDER = 'special_dunder'
    NOT_APPLICABLE = 'not_applicable'

class PythonDeclarationKind(Enum):
    MODULE_DEFINITION = 'Module Definition (Python File)'
    MODULE_DOCSTRING = "Module Docstring"
    CLASS_DOCSTRING = "Class Docstring"
    FUNCTION_DOCSTRING = "Function/Method Docstring"
    SHEBANG = "Shebang (e.g., #!/usr/bin/python)"
    ENCODING_DECLARATION = "Source File Encoding Declaration (e.g., # -*- coding: utf-8 -*-)"
    FUTURE_IMPORT_STATEMENT = "Future Import Statement (from __future__ import ...)"
    IMPORT_MODULE = 'Import Module (e.g., import math)'
    IMPORT_MODULE_ALIAS = 'Import Module with Alias (e.g. import foo as bar)'
    IMPORT_FROM = 'Import From (e.g., from math import sqrt)'
    FROM_IMPORT_NAME = 'From Import Name (e.g. from foo import bar)'
    FROM_IMPORT_NAME_ALIAS = 'From Import Name with Alias (e.g. from foo import bar as baz)'
    FROM_IMPORT_WILDCARD_STATEMENT = 'From Import Wildcard Statement (e.g. from foo import *)'
    ALL_DUNDER_ASSIGNMENT = "__all__ Assignment"
    TYPE_ALIAS_ASSIGNMENT = 'Type Alias Assignment (e.g., MyList = list[int], or type NewType = OldType)'
    TYPE_VARIABLE_ASSIGNMENT = 'Type Variable Assignment (e.g., T = TypeVar("T"))'
    PARAM_SPEC_ASSIGNMENT = "ParamSpec Assignment (P = ParamSpec('P'))"
    TYPE_VAR_TUPLE_ASSIGNMENT = "TypeVarTuple Assignment (Ts = TypeVarTuple('Ts'))"
    NEWTYPE_DECLARATION = 'NewType Declaration (e.g., UserId = NewType("UserId", int))'
    GLOBAL_VARIABLE_ASSIGNMENT = 'Global Variable Assignment (module level)'
    GLOBAL_CONSTANT_ASSIGNMENT = 'Global Constant Assignment (module level, by convention)'
    LOCAL_VARIABLE_ASSIGNMENT = "Local Variable Assignment"
    CLASS_VARIABLE_ASSIGNMENT = 'Class Variable Assignment'
    CLASS_CONSTANT_ASSIGNMENT = "Class Constant Assignment (by convention)"
    INSTANCE_VARIABLE_ASSIGNMENT = 'Instance Variable Assignment (typically in __init__)'
    INSTANCE_VARIABLE_ANNOTATION = "Instance Variable Annotation (PEP 526)"
    VARIABLE_ANNOTATION = 'Variable Annotation (e.g., x: int)'
    UNPACKING_ASSIGNMENT = "Unpacking Assignment (e.g. a, b = c)"
    CONSTANT_ASSIGNMENT = 'Constant Assignment (by convention, e.g., MY_CONSTANT = 1)'
    FUNCTION_DEFINITION = 'Function Definition (def)'
    ASYNC_FUNCTION_DEFINITION = 'Async Function Definition (async def)'
    LAMBDA_DEFINITION = 'Lambda Definition'
    DECORATOR_DEFINITION = 'Decorator Function/Class Definition'
    CLASS_DEFINITION = 'Class Definition'
    NESTED_CLASS_DEFINITION = 'Nested Class Definition'
    ENUM_DEFINITION = 'Enum Definition (class MyEnum(Enum):)'
    NESTED_ENUM_DEFINITION = 'Nested Enum Definition'
    DATACLASS_DEFINITION = 'Dataclass Definition (@dataclass)'
    TYPING_PROTOCOL_DEFINITION = 'Typing Protocol Definition (class P(Protocol):)'
    GENERIC_CLASS_DEFINITION = 'Generic Class Definition (class C(Generic[T]): or class C[T]:)'
    ABSTRACT_BASE_CLASS_DEFINITION = 'Abstract Base Class Definition (class MyABC(ABC):)'
    EXCEPTION_DEFINITION = 'Exception Class Definition'
    FINAL_CLASS_DEFINITION = 'Final Class Definition (@typing.final)'
    INITIALIZER_METHOD_DEFINITION = "Initializer Method Definition (__init__)"
    NEW_METHOD_DEFINITION = "Instance Creation Method Definition (__new__)"
    FINALIZER_METHOD_DEFINITION = "Finalizer Method Definition (__del__)"
    METHOD_DEFINITION = 'Method Definition'
    ASYNC_METHOD_DEFINITION = 'Async Method Definition'
    STATIC_METHOD_DEFINITION = 'Static Method Definition (@staticmethod)'
    CLASS_METHOD_DEFINITION = 'Class Method Definition (@classmethod)'
    DUNDER_METHOD_DEFINITION = 'Dunder/Magic Method Definition (e.g., __str__, __add__)'
    SPECIAL_METHOD_DEFINITION = "Special (Dunder) Method Definition (e.g., __str__, __add__)"
    ABSTRACT_METHOD_DEFINITION = 'Abstract Method Definition (@abc.abstractmethod)'
    FINAL_METHOD_DEFINITION = 'Final Method Definition (@typing.final)'
    PROPERTY_DEFINITION = 'Property Definition (@property)'
    PROPERTY_SETTER_DEFINITION = 'Property Setter Definition (@<name>.setter)'
    PROPERTY_DELETER_DEFINITION = 'Property Deleter Definition (@<name>.deleter)'
    GENERIC_METHOD_DEFINITION = "Generic Method Definition (def func[T](...) or using TypeVars)"
    NESTED_FUNCTION_DEFINITION = 'Nested Function Definition (closure)'
    PARAMETER = 'Function/Method Parameter'
    VAR_POSITIONAL_PARAMETER = 'Variable Positional Parameter (*args)'
    VAR_KEYWORD_PARAMETER = 'Variable Keyword Parameter (**kwargs)'
    POSITIONAL_ONLY_PARAMETER_SEPARATOR = 'Positional-Only Parameter Separator (/)'
    KEYWORD_ONLY_PARAMETER_SEPARATOR = 'Keyword-Only Parameter Separator (*)'
    KEYWORD_ONLY_PARAMETER_DEFINITION = "Keyword-Only Parameter (after * or *args)"
    POSITIONAL_ONLY_PARAMETER_DEFINITION = "Positional-Only Parameter (before /)"
    DECORATOR_APPLICATION = 'Decorator Application (@decorator)'
    IF_STATEMENT = 'If Statement'
    ELIF_CLAUSE = 'Elif Clause'
    ELSE_CLAUSE = 'Else Clause'
    MATCH_STATEMENT = 'Match Statement (Python 3.10+)'
    CASE_CLAUSE = 'Case Clause (in match)'
    CASE_GUARD_CLAUSE = 'Case Guard Clause (if ... in case)'
    CASE_WILDCARD_CLAUSE = 'Case Wildcard Clause (_ in case)'
    FOR_LOOP_STATEMENT = 'For Loop Statement'
    ASYNC_FOR_LOOP_STATEMENT = 'Async For Loop Statement'
    WHILE_LOOP_STATEMENT = 'While Loop Statement'
    TRY_STATEMENT = 'Try Statement'
    EXCEPT_CLAUSE = 'Except Clause'
    FINALLY_CLAUSE = 'Finally Clause'
    ELSE_AFTER_LOOP_OR_TRY_CLAUSE = 'Else Clause (after loop or try)'
    WITH_STATEMENT = 'With Statement'
    ASYNC_WITH_STATEMENT = 'Async With Statement'
    WITH_ITEM = 'With Item (context_manager [as target])'
    EXPRESSION_STATEMENT = 'Expression Statement (e.g., func_call())'
    ASSIGNMENT_EXPRESSION = 'Assignment Expression (Walrus Operator :=)'
    RETURN_STATEMENT = 'Return Statement'
    YIELD_EXPRESSION = 'Yield Expression / Yield From Expression'
    RAISE_STATEMENT = 'Raise Statement'
    ASSERT_STATEMENT = 'Assert Statement'
    PASS_STATEMENT = 'Pass Statement'
    BREAK_STATEMENT = 'Break Statement'
    CONTINUE_STATEMENT = 'Continue Statement'
    DEL_STATEMENT = 'Del Statement'
    GLOBAL_STATEMENT = 'Global Statement (global var1, var2)'
    NONLOCAL_STATEMENT = 'Nonlocal Statement (nonlocal var1, var2)'
    AWAIT_EXPRESSION = "Await Expression"
    LIST_COMPREHENSION = 'List Comprehension'
    SET_COMPREHENSION = 'Set Comprehension'
    DICT_COMPREHENSION = 'Dictionary Comprehension'
    GENERATOR_EXPRESSION = 'Generator Expression'
    TYPE_HINT_VARIABLE = 'Variable Type Hint (e.g., x: int)'
    TYPE_HINT_PARAMETER = 'Parameter Type Hint'
    TYPE_HINT_RETURN = 'Return Type Hint'
    TYPE_COMMENT = 'Type Comment (# type: ...)'
    TYPE_IGNORE_COMMENT = 'Type Ignore Comment (# type: ignore[...])'
    LINTER_CONTROL_COMMENT = 'Linter Control Comment (e.g., # noqa)'
    ENUM_MEMBER = 'Enum Member Definition'
    FSTRING = 'Formatted String Literal (f-string)'
    ELLIPSIS_NODE = 'Ellipsis Literal (...)'
    IF_MAIN_BLOCK = 'If __name__ == "__main__": Block'
    TYPE_PARAMETER_DECLARATION_PEP695 = "Type Parameter Declaration (PEP 695)"
    UNKNOWN_PYTHON_CONSTRUCT = 'Unknown Python Construct'

class PythonParameterKind(Enum):
    POSITIONAL_ONLY = auto()
    POSITIONAL_OR_KEYWORD = auto()
    VAR_POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    VAR_KEYWORD = auto()

    @staticmethod
    def from_inspect_kind(kind: inspect.Parameter.Kind) -> 'PythonParameterKind':
        _map = {
            inspect.Parameter.POSITIONAL_ONLY: PythonParameterKind.POSITIONAL_ONLY,
            inspect.Parameter.POSITIONAL_OR_KEYWORD: PythonParameterKind.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.VAR_POSITIONAL: PythonParameterKind.VAR_POSITIONAL,
            inspect.Parameter.KEYWORD_ONLY: PythonParameterKind.KEYWORD_ONLY,
            inspect.Parameter.VAR_KEYWORD: PythonParameterKind.VAR_KEYWORD,
        }
        return _map[kind]

class PythonFunctionKind(Enum):
    REGULAR_FUNCTION = 'Regular Function'
    METHOD = 'Instance Method'
    STATIC_METHOD = 'Static Method'
    CLASS_METHOD = 'Class Method'
    LAMBDA_FUNCTION = 'Lambda Function'
    INITIALIZER_METHOD = 'Initializer Method (__init__)'
    NEW_METHOD = "Instance Creation Method (__new__)"
    FINALIZER_METHOD = 'Finalizer Method (__del__)'
    PROPERTY_GETTER = 'Property Getter Method'
    PROPERTY_SETTER = 'Property Setter Method'
    PROPERTY_DELETER = 'Property Deleter Method'
    DUNDER_METHOD_OPERATOR = 'Dunder Method (Operator Overload, e.g., __add__)'
    DUNDER_METHOD_CONVERSION = 'Dunder Method (Conversion, e.g., __str__, __bool__)'
    DUNDER_METHOD_CONTEXT_MANAGER = 'Dunder Method (Context Manager, e.g., __enter__, __exit__)'
    DUNDER_METHOD_DESCRIPTOR = 'Dunder Method (Descriptor, e.g., __get__, __set__)'
    DUNDER_METHOD_ITERATOR = 'Dunder Method (Iterator, e.g., __iter__, __next__)'
    DUNDER_METHOD_CALLABLE = 'Dunder Method (Callable Instance, e.g., __call__)'
    DUNDER_METHOD_OTHER = 'Dunder Method (Other Special Behavior)'
    SPECIAL_METHOD = 'Special Method (e.g., __str__, __add__, excluding __init__)'
    GENERATOR_FUNCTION = 'Generator Function (contains yield or yield from)'
    ASYNC_FUNCTION = 'Asynchronous Function (defined with async def)'
    ASYNC_METHOD = 'Asynchronous Method (defined with async def in a class)'
    ASYNC_GENERATOR_FUNCTION = 'Async Generator Function (async def with yield/yield from)'
    NESTED_FUNCTION = 'Nested Function (defined inside another function/method)'
    TEST_FUNCTION = 'Test Function (by naming convention or framework)'
    DECORATOR_FUNCTION = 'Decorator Function (a function designed to be used as a decorator)'
    SCRIPT_MAIN_EXECUTION_BLOCK_FUNCTION = 'Script Main Execution Block Function'
    NOT_APPLICABLE = 'N/A'

class PythonDecoratorType(Enum):
    STATICMETHOD = '@staticmethod'
    CLASSMETHOD = '@classmethod'
    PROPERTY = '@property'
    PROPERTY_SETTER = '@<property_name>.setter'
    PROPERTY_DELETER = '@<property_name>.deleter'
    ABSTRACTMETHOD = '@abc.abstractmethod'
    ASYNCIO_COROUTINE = '@asyncio.coroutine'
    DATACLASS = '@dataclasses.dataclass'
    DATACLASS_FIELD = '@dataclasses.field'
    FINAL = '@typing.final'
    OVERRIDE = '@typing.override'
    OVERLOAD = '@typing.overload'
    TOTAL_ORDERING = '@functools.total_ordering'
    LRU_CACHE = '@functools.lru_cache'
    CACHED_PROPERTY = '@functools.cached_property'
    WRAPS = '@functools.wraps'
    SINGLEDISPATCH = '@functools.singledispatch'
    SINGLEDISPATCHMETHOD = '@functools.singledispatchmethod'
    CONTEXTMANAGER = '@contextlib.contextmanager'
    ASYNC_CONTEXTMANAGER = '@contextlib.asynccontextmanager'
    TYPE_CHECKED = '@typing.type_checked'
    TYPECHECKER_ONLY = '@typing.type_check_only'
    CUSTOM = 'Custom Decorator'
    UNKNOWN = 'Unknown Decorator'

class PythonScopeKind(Enum):
    MODULE_SCOPE = 'Module Scope (Top-Level)'
    CLASS_SCOPE = 'Class Definition Scope'
    FUNCTION_SCOPE = 'Function Definition Scope'
    LAMBDA_SCOPE = 'Lambda Expression Scope'
    COMPREHENSION_SCOPE = 'Comprehension Scope (List, Set, Dict, Generator Expression)'
    CONTROL_FLOW_BLOCK = "Control Flow Block (e.g., if, for, while, try, with, match case)"

class PythonVariableScopeKeyword(Enum):
    NONE = 'None'
    GLOBAL = 'global'
    NONLOCAL = 'nonlocal'

class PythonVariableContext(Enum):
    UNKNOWN = 'Unknown context'
    GLOBAL_EXPLICIT = 'Explicit Global (declared with "global" keyword)'
    NONLOCAL_EXPLICIT = 'Explicit Nonlocal (declared with "nonlocal" keyword)'
    MODULE_LEVEL = 'Module-level Variable (implicit global)'
    CLASS_LEVEL = 'Class-level Variable'
    INSTANCE_LEVEL = 'Instance-level Variable (e.g., self.var)'
    FUNCTION_LOCAL = 'Function/Method Local Variable'
    PARAMETER = 'Function/Method Parameter'
    COMPREHENSION_VARIABLE = 'Variable defined in a comprehension'

class PythonTokenType(Enum):
    ENDMARKER = auto()
    NAME = auto()
    NUMBER = auto()
    STRING = auto()
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    LPAR = auto()
    RPAR = auto()
    LSQB = auto()
    RSQB = auto()
    COLON = auto()
    COMMA = auto()
    SEMI = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    VBAR = auto()
    AMPER = auto()
    LESS = auto()
    GREATER = auto()
    EQUAL = auto()
    DOT = auto()
    PERCENT = auto()
    LBRACE = auto()
    RBRACE = auto()
    EQEQUAL = auto()
    NOTEQUAL = auto()
    LESSEQUAL = auto()
    GREATEREQUAL = auto()
    TILDE = auto()
    CIRCUMFLEX = auto()
    LEFTSHIFT = auto()
    RIGHTSHIFT = auto()
    DOUBLESTAR = auto()
    PLUSEQUAL = auto()
    MINEQUAL = auto()
    STAREQUAL = auto()
    SLASHEQUAL = auto()
    PERCENTEQUAL = auto()
    AMPEREQUAL = auto()
    VBAREQUAL = auto()
    CIRCUMFLEXEQUAL = auto()
    LEFTSHIFTEQUAL = auto()
    RIGHTSHIFTEQUAL = auto()
    DOUBLESTAREQUAL = auto()
    DOUBLESLASH = auto()
    DOUBLESLASHEQUAL = auto()
    AT = auto()
    ATEQUAL = auto()
    RARROW = auto()
    ELLIPSIS = auto()
    COLONEQUAL = auto()
    OP = auto()
    AWAIT = auto()
    ASYNC = auto()
    TYPE_IGNORE = auto()
    TYPE_COMMENT = auto()
    ERRORTOKEN = auto()
    COMMENT = auto()
    NL = auto()
    ENCODING = auto();
    FSTRING_START = auto()
    FSTRING_MIDDLE = auto()
    FSTRING_END = auto()
    IDENTIFIER = auto()
    KEYWORD = auto()
    SOFT_KEYWORD = auto()
    UNKNOWN = auto()

class PythonCommentType(Enum):
    HASH_COMMENT = auto()
    SHEBANG = auto()
    ENCODING_DECLARATION = auto()
    TYPE_HINT_COMMENT = auto()
    LINTER_CONTROL_COMMENT = auto()

@dataclass(frozen=True)
class PythonComment:
    content: str
    raw_text: str
    start_pos: Position
    end_pos: Position
    type: PythonCommentType

@dataclass(frozen=True)
class PythonDocstring:
    content: str
    cleaned_content: str
    start_pos: Position
    end_pos: Position
    is_triple_single_quotes: bool
    indentation_level: int

@dataclass(frozen=True)
class PythonToken:
    type: PythonTokenType
    value: str
    full_text: str
    start_pos: Position
    end_pos: Position
    file_data: FileData

@dataclass(frozen=True)
class PythonExtractionError:
    file_data: FileData
    error_message: str
    start_pos: Optional[Position] = None
    end_pos: Optional[Position] = None
    context_snippet: Optional[str] = None

@dataclass(frozen=True)
class PythonParameter:
    name: str
    start_pos: Position
    end_pos: Position
    name_pos: Position
    kind: PythonParameterKind = PythonParameterKind.POSITIONAL_OR_KEYWORD
    annotation_str: Optional[str] = None
    default_value_str: Optional[str] = None
    full_text: Optional[str] = None

@dataclass(frozen=True)
class PythonDecorator:
    name_or_expr_str: str
    start_pos: Position
    end_pos: Position
    type: PythonDecoratorType = PythonDecoratorType.UNKNOWN
    qualname_parts: List[str] = field(default_factory=list)
    args_str: Optional[str] = None


@dataclass(frozen=True)
class PythonImportItem:
    name: str
    start_pos: Position
    end_pos: Position
    as_name: Optional[str] = None

@dataclass(frozen=True)
class PythonImportData:
    module_name_parts: List[str] = field(default_factory=list)
    imported_items: Optional[List[PythonImportItem]] = None
    level: int = 0
    is_star_import: bool = False
    is_future_import: bool = False

@dataclass(frozen=True)
class ExtractedPythonDeclaration:
    name: Optional[str]
    kind: PythonDeclarationKind
    file_data: FileData
    start_pos: Position
    end_pos: Position
    name_pos: Optional[Position] = None

    qualname_parts: List[str] = field(default_factory=list)
    nesting_qualname_parts: List[str] = field(default_factory=list)

    access_convention: Optional[PythonAccessConvention] = None
    scope_keyword: Optional[PythonVariableScopeKeyword] = None
    variable_context: Optional[PythonVariableContext] = None

    function_kind: Optional[PythonFunctionKind] = None
    parameters: Optional[List[PythonParameter]] = None
    return_type_hint_str: Optional[str] = None
    is_async: bool = False
    is_generator: bool = False
    generic_type_params_str_list: Optional[List[str]] = None

    base_classes_str_list: Optional[List[str]] = None
    metaclass_str: Optional[str] = None
    class_slots_str_list: Optional[List[str]] = None
    class_keyword_args_str: Optional[str] = None
    is_generic_class: bool = False

    assigned_value_str: Optional[str] = None
    variable_type_hint_str: Optional[str] = None
    is_constant_convention: bool = False

    import_data: Optional[PythonImportData] = None
    decorators: List[PythonDecorator] = field(default_factory=list)

    docstring_obj: Optional[PythonDocstring] = None
    leading_comments: List[PythonComment] = field(default_factory=list)
    comment_inline_obj: Optional[PythonComment] = None

    full_declaration_text: Optional[str] = None
    signature_text: Optional[str] = None
    body_text: Optional[str] = None
    body_start_pos: Optional[Position] = None
    body_end_pos: Optional[Position] = None

    is_abstract: bool = False
    is_final: bool = False
    is_dataclass: bool = False
    is_enum: bool = False
    is_exception: bool = False

    raw_ast_node: Optional[Any] = None

    condition_str: Optional[str] = None
    iterable_str: Optional[str] = None
    target_str_list: Optional[List[str]] = None
    exception_types_str_list: Optional[List[str]] = None
    exception_target_str: Optional[str] = None
    with_items: Optional[List[Tuple[str, Optional[str]]]] = None
    match_subject_str: Optional[str] = None
    case_pattern_str: Optional[str] = None
    case_guard_str: Optional[str] = None

class PythonUtils:
    _PYTHON_WHITESPACE_CHARS: Set[str] = set(string.whitespace)
    _PYTHON_DIGIT_CHARS: Set[str] = set(string.digits)
    _PYTHON_HEX_DIGIT_CHARS: Set[str] = set(string.hexdigits)
    _PYTHON_OCTAL_DIGIT_CHARS: Set[str] = set(string.octdigits)
    _PYTHON_BINARY_DIGIT_CHARS: Set[str] = {'0', '1'}

    _PYTHON_KEYWORDS: Set[str] = set(kw.kwlist)
    _PYTHON_SOFT_KEYWORDS: Set[str] = set(getattr(kw, 'softkwlist', {'match', 'case', '_', 'type'}))

    _PYTHON_BUILTIN_NAMES: Set[str] = {
                                          name for name, obj_ in inspect.getmembers(__builtins__) if callable(obj_) or isinstance(obj_, type)
                                      } | {'None', 'True', 'False', 'NotImplemented', 'Ellipsis', '__debug__'}


    _MULTI_CHAR_OPERATORS_AND_DELIMITERS: Set[str] = {
        '**=', '//=', '<<=', '>>=', '&=', '|=', '^=', '+=', '-=', '*=', '/=', '%=', '@=',
        '**', '//', '<<', '>>', '<=', '>=', '==', '!=',
        ':=', '->', '...'
    }
    _SINGLE_CHAR_OPERATORS_AND_DELIMITERS: Set[str] = {
        '+', '-', '*', '/', '%', '@', '&', '|', '^', '~', '<', '>', '=',
        '(', ')', '[', ']', '{', '}', ',', ':', '.', ';'
    }
    _ALL_OPERATORS_AND_DELIMITERS_SORTED: Optional[List[str]] = None

    _COMMON_TYPING_COLLECTION_TYPES: Set[str] = {
        'List', 'Dict', 'Tuple', 'Set', 'Sequence', 'Mapping', 'Iterable', 'Iterator',
        'Callable', 'Any', 'Union', 'Optional', 'TypeVar', 'Generic', 'Protocol',
        'ByteString', 'Type', 'NewType', 'ClassVar', 'Final', 'Annotated',
        'Coroutine', 'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
        'ContextManager', 'AsyncContextManager', 'Deque', 'DefaultDict', 'OrderedDict',
        'Counter', 'ChainMap', 'FrozenSet'
    }

    _COMMON_DUNDER_NAMES: Set[str] = {
        "__init__", "__new__", "__del__", "__repr__", "__str__", "__bytes__", "__format__",
        "__lt__", "__le__", "__eq__", "__ne__", "__gt__", "__ge__",
        "__hash__", "__bool__",
        "__getattr__", "__getattribute__", "__setattr__", "__delattr__", "__dir__",
        "__get__", "__set__", "__delete__",
        "__instancecheck__", "__subclasscheck__",
        "__class_getitem__",
        "__call__",
        "__len__", "__length_hint__", "__getitem__", "__setitem__", "__delitem__", "__missing__",
        "__iter__", "__reversed__", "__contains__",
        "__add__", "__sub__", "__mul__", "__matmul__", "__truediv__", "__floordiv__", "__mod__",
        "__divmod__", "__pow__", "__lshift__", "__rshift__", "__and__", "__xor__", "__or__",
        "__radd__", "__rsub__", "__rmul__", "__rmatmul__", "__rtruediv__", "__rfloordiv__", "__rmod__",
        "__rdivmod__", "__rpow__", "__rlshift__", "__rrshift__", "__rand__", "__rxor__", "__ror__",
        "__iadd__", "__isub__", "__imul__", "__imatmul__", "__itruediv__", "__ifloordiv__", "__imod__",
        "__ipow__", "__ilshift__", "__irshift__", "__iand__", "__ixor__", "__ior__",
        "__neg__", "__pos__", "__abs__", "__invert__",
        "__complex__", "__int__", "__float__", "__round__", "__index__",
        "__enter__", "__exit__", "__aenter__", "__aexit__",
        "__await__", "__aiter__", "__anext__",
        "__slots__", "__dict__", "__weakref__",
        "__module__", "__qualname__", "__name__", "__doc__", "__annotations__",
        "__class__", "__bases__", "__mro__", "__subclasses__",
        "__copy__", "__deepcopy__",
        "__getnewargs_ex__", "__getnewargs__", "__getstate__", "__setstate__", "__reduce__", "__reduce_ex__",
        "__init_subclass__", "__set_name__",
        "__main__", "__file__", "__path__", "__package__", "__loader__", "__spec__",
        "__version__", "__author__", "__all__", "__metaclass__"
    }

    @staticmethod
    def get_sorted_operators_and_delimiters() -> List[str]:
        if PythonUtils._ALL_OPERATORS_AND_DELIMITERS_SORTED is None:
            combined = PythonUtils._MULTI_CHAR_OPERATORS_AND_DELIMITERS | PythonUtils._SINGLE_CHAR_OPERATORS_AND_DELIMITERS
            PythonUtils._ALL_OPERATORS_AND_DELIMITERS_SORTED = sorted(list(combined), key=len, reverse=True)
        return PythonUtils._ALL_OPERATORS_AND_DELIMITERS_SORTED

    @staticmethod
    def is_python_whitespace(char: str) -> bool:
        return char in PythonUtils._PYTHON_WHITESPACE_CHARS

    @staticmethod
    def is_identifier_start_char(char: str) -> bool:
        return char.isalpha() or char == '_'

    @staticmethod
    def is_identifier_char(char: str) -> bool:
        return char.isalnum() or char == '_'

    @staticmethod
    def is_digit(char: str) -> bool:
        return char in PythonUtils._PYTHON_DIGIT_CHARS

    @staticmethod
    def is_hex_digit(char: str) -> bool:
        return char in PythonUtils._PYTHON_HEX_DIGIT_CHARS

    @staticmethod
    def is_octal_digit(char: str) -> bool:
        return char in PythonUtils._PYTHON_OCTAL_DIGIT_CHARS

    @staticmethod
    def is_binary_digit(char: str) -> bool:
        return char in PythonUtils._PYTHON_BINARY_DIGIT_CHARS

    @staticmethod
    def is_keyword(identifier: str) -> bool:
        return identifier in PythonUtils._PYTHON_KEYWORDS

    @staticmethod
    def is_soft_keyword(identifier: str) -> bool:
        return identifier in PythonUtils._PYTHON_SOFT_KEYWORDS

    @staticmethod
    def is_builtin_name(identifier: str) -> bool:
        return identifier in PythonUtils._PYTHON_BUILTIN_NAMES

    @staticmethod
    def get_access_convention(name: str) -> PythonAccessConvention:
        if name.startswith("__") and name.endswith("__") and len(name) > 4:
            return PythonAccessConvention.SPECIAL_DUNDER
        elif name.startswith("__"):
            return PythonAccessConvention.PRIVATE_NAME_MANGLED
        elif name.startswith("_"):
            return PythonAccessConvention.PROTECTED_INTERNAL
        else:
            return PythonAccessConvention.PUBLIC

_UNQUALIFIABLE_PYTHON_CONSTRUCTS_FOR_NAMING: Set[PythonDeclarationKind] = {
    PythonDeclarationKind.IF_STATEMENT, PythonDeclarationKind.ELIF_CLAUSE, PythonDeclarationKind.ELSE_CLAUSE,
    PythonDeclarationKind.MATCH_STATEMENT, PythonDeclarationKind.CASE_CLAUSE, PythonDeclarationKind.CASE_GUARD_CLAUSE, PythonDeclarationKind.CASE_WILDCARD_CLAUSE,
    PythonDeclarationKind.FOR_LOOP_STATEMENT, PythonDeclarationKind.ASYNC_FOR_LOOP_STATEMENT, PythonDeclarationKind.WHILE_LOOP_STATEMENT,
    PythonDeclarationKind.TRY_STATEMENT, PythonDeclarationKind.EXCEPT_CLAUSE, PythonDeclarationKind.FINALLY_CLAUSE, PythonDeclarationKind.ELSE_AFTER_LOOP_OR_TRY_CLAUSE,
    PythonDeclarationKind.WITH_STATEMENT, PythonDeclarationKind.ASYNC_WITH_STATEMENT, PythonDeclarationKind.WITH_ITEM,
    PythonDeclarationKind.LIST_COMPREHENSION, PythonDeclarationKind.SET_COMPREHENSION, PythonDeclarationKind.DICT_COMPREHENSION, PythonDeclarationKind.GENERATOR_EXPRESSION,
    PythonDeclarationKind.EXPRESSION_STATEMENT, PythonDeclarationKind.ASSIGNMENT_EXPRESSION, PythonDeclarationKind.AWAIT_EXPRESSION,
    PythonDeclarationKind.RETURN_STATEMENT, PythonDeclarationKind.YIELD_EXPRESSION,
    PythonDeclarationKind.RAISE_STATEMENT, PythonDeclarationKind.ASSERT_STATEMENT, PythonDeclarationKind.PASS_STATEMENT,
    PythonDeclarationKind.BREAK_STATEMENT, PythonDeclarationKind.CONTINUE_STATEMENT, PythonDeclarationKind.DEL_STATEMENT,
    PythonDeclarationKind.GLOBAL_STATEMENT, PythonDeclarationKind.NONLOCAL_STATEMENT,
    PythonDeclarationKind.DECORATOR_APPLICATION,
    PythonDeclarationKind.MODULE_DOCSTRING, PythonDeclarationKind.CLASS_DOCSTRING, PythonDeclarationKind.FUNCTION_DOCSTRING,
    PythonDeclarationKind.POSITIONAL_ONLY_PARAMETER_SEPARATOR, PythonDeclarationKind.KEYWORD_ONLY_PARAMETER_SEPARATOR,
    PythonDeclarationKind.FSTRING, PythonDeclarationKind.SHEBANG, PythonDeclarationKind.ENCODING_DECLARATION,
    PythonDeclarationKind.TYPE_COMMENT, PythonDeclarationKind.TYPE_IGNORE_COMMENT, PythonDeclarationKind.LINTER_CONTROL_COMMENT,
    PythonDeclarationKind.ELLIPSIS_NODE,
    PythonDeclarationKind.FUTURE_IMPORT_STATEMENT, PythonDeclarationKind.FROM_IMPORT_WILDCARD_STATEMENT,
    PythonDeclarationKind.IF_MAIN_BLOCK, PythonDeclarationKind.TYPE_PARAMETER_DECLARATION_PEP695
}