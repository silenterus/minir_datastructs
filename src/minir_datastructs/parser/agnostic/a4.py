from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Any, Dict, Tuple, Union

# --- Core Primitives ---

@dataclass(frozen=True)
class SourcePosition:
    line: int  # 1-indexed
    column: int # 0-indexed or 1-indexed, be consistent

@dataclass(frozen=True)
class SourceRange:
    start: SourcePosition
    end: SourcePosition

@dataclass(frozen=True)
class SourceFileReference:
    path: str
    # Content might be loaded on demand or stored if actively used
    content_hash: Optional[str] = None # To detect changes if content not stored

@dataclass(frozen=True)
class ExtractionError:
    file: SourceFileReference
    message: str
    range: Optional[SourceRange] = None
    context_snippet: Optional[str] = None
    tool_name: Optional[str] = None # e.g., "CppParser", "PythonASTParser"

# --- General Enums ---

class LanguageKind(Enum):
    CPP = auto()
    PYTHON = auto()
    ODIN = auto()
    CSHARP = auto()
    JAVA = auto()
    GO = auto()
    RUST = auto()
    ZIG = auto()
    JAVASCRIPT = auto()
    TYPESCRIPT = auto()
    KOTLIN = auto()
    SWIFT = auto()
    SCALA = auto()
    OTHER = auto()

class DeclarationKind(Enum):
    # Groupings / Scopes
    FILE_ROOT = "File Root / Compilation Unit" # Implicit top-level container
    MODULE = "Module"
    PACKAGE = "Package"
    NAMESPACE = "Namespace"
    LIBRARY = "Library" # For multi-file constructs

    # Type Definitions
    CLASS = "Class Definition"
    STRUCT = "Struct Definition" # Could be class-like (C++) or value-like (C#, Go, Rust)
    INTERFACE = "Interface Definition"
    TRAIT = "Trait Definition" # Rust, Scala
    ENUM = "Enum Definition"
    UNION = "Union Definition" # C-style, tagged union (Rust, Zig, Odin)
    OBJECT_SINGLETON = "Object/Singleton Definition" # Scala, Kotlin

    # Function-like Definitions
    FUNCTION = "Function / Procedure"
    METHOD = "Instance Method"
    STATIC_METHOD = "Static/Class Method"
    CONSTRUCTOR = "Constructor"
    DESTRUCTOR = "Destructor / Finalizer"
    LAMBDA_EXPRESSION = "Lambda Expression / Anonymous Function"
    OPERATOR_OVERLOAD = "Operator Overload Definition"
    CONVERSION_OPERATOR = "Conversion Operator Definition"

    # Variable/Data Definitions
    VARIABLE = "Variable Declaration/Definition"
    CONSTANT = "Constant Declaration/Definition"
    FIELD = "Field / Member Variable" # Inside a class/struct
    PARAMETER = "Function/Method Parameter"
    ENUM_MEMBER = "Enum Member / Variant"
    PROPERTY = "Property (with getter/setter semantics)" # C#, Python @property
    GLOBAL_VARIABLE = "Global Variable"
    LOCAL_VARIABLE = "Local Variable"

    # Type Aliasing and Generics
    TYPE_ALIAS = "Type Alias / Typedef"
    NEW_TYPE = "New Distinct Type (wrapper)" # e.g. Odin distinct, Python NewType
    GENERIC_TYPE_PARAMETER = "Generic Type Parameter (e.g., T in List<T>)"
    GENERIC_FUNCTION_PARAMETER = "Generic Function Parameter (e.g. N in func<N: int>)" # For const generics

    # Meta/Organizational
    IMPORT_DIRECTIVE = "Import/Using Directive"
    EXPORT_DIRECTIVE = "Export Directive" # JS, TS modules, C++20 export
    ATTRIBUTE_DECORATOR_ANNOTATION = "Attribute/Decorator/Annotation Definition or Application"
    COMMENT_BLOCK = "Comment Block (significant, e.g., file header)"
    DOC_COMMENT = "Documentation Comment"
    MACRO_DEFINITION = "Macro Definition"
    MACRO_INVOCATION = "Macro Invocation"
    COMPILER_DIRECTIVE = "Compiler Directive / Pragma" # e.g. #pragma, Odin #assert
    LINKAGE_SPECIFICATION = "Linkage Specification (e.g. extern \"C\")"
    REGION_MARKER = "Code Region Marker (e.g. #region)"

    # Control Flow / Statements (if extending beyond pure declarations)
    # IF_STATEMENT, FOR_LOOP, TRY_CATCH_BLOCK etc. - typically not primary focus for "declaration extraction"

    UNKNOWN = "Unknown Construct"

class AccessModifier(Enum):
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"
    INTERNAL = "internal" # C#, Swift (module-private)
    FILE_PRIVATE = "fileprivate" # Swift
    PACKAGE_PRIVATE = "package_private" # Java default, Go (unexported)
    UNSPECIFIED_OR_DEFAULT = "unspecified_or_default" # Context-dependent
    NOT_APPLICABLE = "not_applicable"

class StorageSemantic(Enum): # Renamed from StorageModifier to avoid clash with lexical modifiers
    INSTANCE = "instance_member"  # Default for non-static members
    STATIC_OR_TYPE = "static_or_type_member" # static in C++/Java/C#, classmethod in Python, package-level in Go
    GLOBAL = "global_scope"
    LOCAL_BLOCK = "local_block_scope"
    CLOSURE_CAPTURED = "closure_captured"
    NONE = "none"

class LexicalModifier(Enum): # Modifiers that affect linkage, mutability, behavior
    # Mutability/Constness
    CONST = "const_value_or_pointer" # C++ const, JS const
    FINAL_VARIABLE = "final_variable" # Java final variable
    READONLY_FIELD = "readonly_field" # C# readonly
    MUTABLE = "mutable" # Rust mut, C++ mutable

    # Inheritance/Overriding
    ABSTRACT = "abstract_method_or_class"
    VIRTUAL = "virtual_method"
    OVERRIDE = "override_method_or_property"
    FINAL_CLASS_OR_METHOD = "final_sealed_class_or_method" # Java final, C# sealed

    # Concurrency/Behavior
    SYNCHRONIZED = "synchronized_method_or_block"
    VOLATILE = "volatile_field"
    TRANSIENT = "transient_field" # Java

    # Linkage/Visibility within compilation units
    EXTERN = "extern_linkage"
    INLINE = "inline_hint"
    STATIC_LINKAGE = "static_internal_linkage" # C/C++ static at file scope

    # Language Specific - High Frequency
    ASYNC = "asynchronous_function_or_block"
    UNSAFE = "unsafe_code_block_or_function" # Rust, C#
    EXPLICIT_CONSTRUCTOR = "explicit_constructor" # C++
    DEFAULT_IMPLEMENTATION = "default_implementation_in_interface" # Java, C#
    LAZY_INITIALIZATION = "lazy_initialization"

    # Default/No specific lexical modifier
    NONE = "none"


class FunctionFlavor(Enum): # Distinguishes primary role of a function-like declaration
    REGULAR = "regular_function_or_method"
    GETTER = "getter_method"
    SETTER = "setter_method"
    CONVERSION = "type_conversion_operator_or_method"
    MAIN_ENTRY_POINT = "main_entry_point"
    TEST_CASE = "test_case_or_benchmark"
    EVENT_HANDLER = "event_handler"
    CLOSURE_OR_LAMBDA_IMPLEMENTATION = "closure_or_lambda_implementation_body"
    NOT_APPLICABLE = "not_applicable"

class CodeBlockType(Enum): # For body_blocks
    FUNCTION_BODY = auto()
    CLASS_BODY = auto()
    IF_BRANCH = auto()
    LOOP_BODY = auto()
    TRY_BLOCK = auto()
    CATCH_BLOCK = auto()
    FINALLY_BLOCK = auto()
    RAW_TEXT = auto() # For simple string body_text
    # ... and so on

# --- Detailed Structures ---

@dataclass(frozen=True)
class CommentInfo:
    text_content: str
    is_documentation: bool
    # Differentiating type helps renderer or analyzer (e.g., Doxygen, Javadoc, Rustdoc)
    style: str # e.g., "JAVADOC_BLOCK", "TRIPLE_SLASH_LINE", "STANDARD_MULTI_LINE"
    range: SourceRange

@dataclass(frozen=True)
class AnnotationArgument:
    name: Optional[str] # For named arguments: @Arg(name="value")
    value_expression: str # String representation of the argument's value
    range: SourceRange

@dataclass(frozen=True)
class AnnotationInfo:
    # Name or qualified name of the annotation/decorator/attribute
    # e.g., "Override", "dataclasses.dataclass", "[[nodiscard]]"
    name_or_identifier: str
    range: SourceRange
    qualname_parts: List[str] = field(default_factory=list) # If resolvable
    arguments: Optional[List[AnnotationArgument]] = None

@dataclass(frozen=True)
class ParameterInfo:
    name: str
    range: SourceRange
    type_signature: Optional[str] = None # e.g., "int", "List<String>", "void*"
    default_value_expression: Optional[str] = None
    is_variadic: bool = False # e.g. C ... , Python *args, Java String...
    # For languages like Swift (inout param), C# (ref, out, in)
    # For Go receiver: (p *MyType)
    passing_mechanism_or_role: Optional[str] = None # e.g., "receiver", "ref", "out", "inout", "keyword_only", "positional_only"
    annotations: List[AnnotationInfo] = field(default_factory=list)
    leading_comments: List[CommentInfo] = field(default_factory=list)
    name_range: Optional[SourceRange] = None

@dataclass(frozen=True)
class GenericParameterInfo:
    name: str # e.g., "T", "K", "V", "'a" (Rust lifetime)
    range: SourceRange
    constraints_signatures: List[str] = field(default_factory=list) # e.g. ["Comparable", "Debug"]
    variance: Optional[str] = None # e.g., "in", "out", "invariant" (for C#/Kotlin/Scala etc.)
    default_type_signature: Optional[str] = None
    # For const generics (C++ template <int N>, Rust fn foo<const N: usize>)
    is_const_generic: bool = False
    const_generic_type: Optional[str] = None # e.g. "int", "usize"

@dataclass(frozen=True)
class ImportItemInfo:
    source_name: str # Name as it is in the source module
    range: SourceRange
    alias: Optional[str] = None # Local alias for the imported item

@dataclass(frozen=True)
class ImportDirectiveInfo:
    # e.g. ["java", "util"], ["my_project", "utils"], or just "math"
    module_or_path_parts: List[str]
    # Specific items imported, if not a whole module import.
    # e.g. for `from collections import defaultdict, Counter as Cnt`
    # items = [ImportItemInfo("defaultdict"), ImportItemInfo("Counter", "Cnt")]
    imported_items: Optional[List[ImportItemInfo]] = None
    is_wildcard_import: bool = False # e.g. from foo import *
    # For module itself if aliased, e.g. import numpy as np
    alias_for_module: Optional[str] = None
    # For C++ `using namespace std;` or Python `from x import *` applied to current scope
    imports_into_current_namespace: bool = False


@dataclass(frozen=True)
class CodeBlock:
    type: CodeBlockType
    # Can be raw text or a list of further AbstractDeclarations if parsing statements
    content: Union[str, List['AbstractDeclaration']]
    range: SourceRange


# --- The Main Declaration Dataclass ---
@dataclass(frozen=True)
class AbstractDeclaration:
    # Identity & Location
    name: Optional[str] # Name of the declared entity (e.g., function name, class name, variable name)
    # Optional for anonymous constructs or directives
    kind: DeclarationKind # Type of declaration
    file_reference: SourceFileReference
    range: SourceRange # Full range of the declaration
    name_range: Optional[SourceRange] = None # Range of the name identifier itself

    # Naming & Scoping
    qualified_name_parts: List[str] = field(default_factory=list) # e.g., ["MyLib", "MyClass", "myMethod"]
    # Qualified name of the direct parent scope (e.g. class for a method, namespace for a class)
    parent_scope_qname_parts: List[str] = field(default_factory=list)

    # Modifiers & Attributes
    access_modifier: AccessModifier = AccessModifier.UNSPECIFIED_OR_DEFAULT
    storage_semantic: StorageSemantic = StorageSemantic.NONE # e.g. static, instance
    lexical_modifiers: List[LexicalModifier] = field(default_factory=list) # e.g. const, async, virtual
    annotations: List[AnnotationInfo] = field(default_factory=list) # Decorators, Attributes, Annotations

    # Documentation
    leading_comments: List[CommentInfo] = field(default_factory=list)
    trailing_comment_on_line: Optional[CommentInfo] = None # For `int x; // comment`
    # Primary docstring/block associated directly with this declaration
    documentation: Optional[CommentInfo] = None

    # Common fields (relevant to many kinds)
    type_signature: Optional[str] = None # For variables, fields, constants, type aliases, function return types
    initializer_expression: Optional[str] = None # For variables, constants, enum members

    # Function/Method/Lambda specific
    function_flavor: Optional[FunctionFlavor] = None
    parameters: Optional[List[ParameterInfo]] = None
    # return_type_signature is often same as type_signature for functions.
    # Can be explicit if type_signature is used for something else for a function kind.
    return_type_signature: Optional[str] = None
    # For languages with explicit throws/checked exceptions (Java, Swift)
    # List of type signatures of exceptions/errors
    exceptions_thrown_signatures: List[str] = field(default_factory=list)

    # Type Definition specific (Class, Struct, Enum, Interface, etc.)
    base_type_signatures: List[str] = field(default_factory=list) # Inherited classes, implemented interfaces
    generic_parameters: Optional[List[GenericParameterInfo]] = None

    # Container for nested declarations (members of a class, items in a namespace, etc.)
    # or statements within a function body if parsing that deep.
    body_blocks: Optional[List[Union['AbstractDeclaration', CodeBlock]]] = None

    # Import/Using specific
    import_details: Optional[ImportDirectiveInfo] = None

    # Raw text (optional, for reconstruction or verbatim display)
    full_source_text: Optional[str] = None
    signature_source_text: Optional[str] = None # e.g. `public int myFunc(string arg)`
    body_source_text: Optional[str] = None # Text content of the body, if not parsed into body_blocks

    # Language-specific details that don't fit well elsewhere
    # Keys could be "cpp_specific", "python_specific" etc.
    # Values could be dictionaries or specific dataclasses.
    language_specific_details: Dict[str, Any] = field(default_factory=dict)

    # For any relationships not covered by parent_scope or body_blocks
    # e.g., friend declarations in C++, extension methods target class
    related_declarations_qnames: Dict[str, List[List[str]]] = field(default_factory=dict) # E.g. {"friend_of": [["OtherClass"]]}

    def __post_init__(self):
        # Basic validation or derived properties can be set here
        if self.name is None and self.kind not in {
            DeclarationKind.LAMBDA_EXPRESSION, DeclarationKind.FILE_ROOT,
            DeclarationKind.IMPORT_DIRECTIVE, DeclarationKind.COMPILER_DIRECTIVE,
            DeclarationKind.COMMENT_BLOCK, DeclarationKind.DOC_COMMENT,
            DeclarationKind.MODULE, DeclarationKind.PACKAGE # Often implicit from file path
        }:
            # This is a soft check, could be a warning or stricter depending on use case
            # print(f"Warning: Nameless declaration of kind {self.kind}")
            pass

@dataclass(frozen=True)
class ProjectContext:
    project_name: str
    project_root_path: str
    all_declarations: List[AbstractDeclaration] # Flat list of all top-level declarations
    source_language: LanguageKind # Which language this declaration is from
    errors: List[ExtractionError] = field(default_factory=list)