from dataclasses import field, dataclass
from dataclasses import field, dataclass
from pathlib import Path
from typing import List, Dict, Optional

from .enum_string import BaseEnumString


class LicenseType(BaseEnumString):
    NONE =      ("none",      0,    "No license specified.")
    COPYRIGHT = ("copyright", 1,    "Standard Copyright statement.")
    MIT =       ("mit",       2,    "Permissive MIT License.")



class ReadmeType(BaseEnumString):
    NONE =    ("none",    0, "No README file will be generated.")
    MINIMAL = ("minimal", 1, "Generate a minimal README.md file.")


class EditorType(BaseEnumString):
    NONE =    ("none",    0, "No editor-specific configuration.")
    PYCHARM = ("pycharm", 1, "Generate PyCharm .idea configuration.")
    FLEET =   ("fleet",   2, "Generate JetBrains Fleet .fleet configuration.")
    VIM =     ("vim",     3, "Generate a basic Vim setup (e.g., .vimrc hints).")


class TestsType(BaseEnumString):
    NONE =     ("none",     0, "No test framework setup.")
    TEST =     ("test",     1, "Basic pytest setup with a tests/ directory.")
    CONFTEST = ("conftest", 2, "Pytest setup including a basic conftest.py.")


class BuildPipelineType(BaseEnumString):
    NONE =   ("none",  0, "No CI/CD pipeline configuration.")
    WINDOWS =("win",   1, "Generate GitHub Actions workflow for Windows.")
    LINUX =  ("linux", 2, "Generate GitHub Actions workflow for Linux (Ubuntu).")
    MAC =    ("mac",   3, "Generate GitHub Actions workflow for macOS.")



class AgentsPromptType(BaseEnumString):
    NONE =        ("none",        0, "No Boilerplate Agent Prompts to create.")
    DEFAULT =     ("default",     1, "creates Merger,Pytest")


class ClickParameterType(BaseEnumString):
    NONE =       ("none",     0, "No specific type (or handled manually).")
    DIR =        ("dir",      1, "Path (writeable directory, creates if needed).")
    DIR_EXIST =  ("dire",     2, "Path (existing readable directory).")
    FILE =       ("file",     3, "Path (writeable file path).")
    FILE_EXIST = ("filee",    4, "Path (existing readable file).")
    STR =        ("str",      5, "String type.")
    BOOL =       ("bool",     6, "Boolean type (flag).")
    INT =        ("int",      7, "Integer type.")
    FLOAT =      ("float",    8, "Float type.")
    POS_DIR =        ("posdir",   9, "Positional Path (writeable directory, creates if needed).")
    POS_DIR_EXIST =  ("posdire", 10, "Positional Path (existing readable directory).")
    POS_FILE =       ("posfile", 11, "Positional Path (writeable file path).")
    POS_FILE_EXIST = ("posfilee",12, "Positional Path (existing readable file).")
    POS_STR =        ("posstr",  13, "Positional String type.")

class ParameterType(BaseEnumString):
    NONE =  ("none",  0, "No specific type.")
    STR =   ("str",   1, "String type.")
    BOOL =  ("bool",  2, "Boolean type.")
    INT =   ("int",   3, "Integer type.")
    FLOAT = ("float", 4, "Float type.")
    PATH =  ("path",  5, "Path type (represents pathlib.Path).")


class ObjectParameterType(BaseEnumString):
    NONE =  ("none",  0, "No specific type.")
    PRIMITIVE =   ("primitive",   1, "one of ParameterType's ones.")
    ENUM =   ("enum",   2, "Enum type.")
    ENTITY =  ("entity",  3, "Entity type.")
    DATA =   ("data",   4, "Data type.")
    CONTAINER = ("container", 5, "Container type.")

@dataclass()
class DataFieldDefinition:
    name: str

@dataclass()
class DataDefinition:
    name: str
    values: Dict[str, DataFieldDefinition] = field(default_factory=dict)


@dataclass()
class EntityFieldDefinition:
    name: str


@dataclass()
class EntityDefinition:
    name: str
    values: Dict[str, EntityFieldDefinition] = field(default_factory=dict)


@dataclass()
class EntityContainerDefinition:
    name: str
    values: Dict[str, EntityDefinition] = field(default_factory=dict)


@dataclass()
class EnumFieldDefinition:
    name: str                       # Name of the enum value (e.g., 'none')
    description: str = ""
    enum_value: str = ""            # The actual fixed value assigned (e.g., '0')
    enum_id: Optional[int] = None   # Optional numeric ID derived from enum_value

@dataclass()
class EnumDefinition:
    """Represents the definition of an enumeration."""
    name_file: str      # Source filename qualifier (optional, defaults to empty string)
    name: str           # The Python name of the Enum class
    description: str = "" # Docstring or description of the enum (Not directly parsable from grammar)
    values: Dict[str, EnumFieldDefinition] = field(default_factory=dict)

@dataclass()
class FieldDefinition:
    name: str                       # Name of the parameter
    parameter_type: ParameterType   # The underlying data type
    object_parameter_type: ObjectParameterType   # The underlying object data type is not primitive

    click_parameter_type: ClickParameterType # The corresponding Click type
    description: str = ""
    default_value: Optional[str] = None # Default value as string from DSL

    # Property to determine requirement based on default value
    @property
    def required(self) -> bool:
        return self.default_value is None

    # Default value for click (can be same as default_value or processed)
    @property
    def default_value_click(self) -> Optional[str]:
        return self.default_value


@dataclass()
class MethodDefinition:
    """Represents the definition of a method, potentially exposed as a CLI command."""
    name_file: str      # Source filename qualifier (optional, defaults to empty string)
    name: str           # The Python name of the method/function
    description: str = "" # Docstring (Not directly parsable from grammar)


    parameters: Dict[str, FieldDefinition] = field(default_factory=dict)

    # Flags derived from syntax (apply to the method itself):
    no_command: bool = False                # Triggered by ! before method name
    no_test: bool = False                   # Triggered by ? before method name

@dataclass()
class SkeletonDefinition:
    methods: Dict[str, MethodDefinition] = field(default_factory=dict)
    enums:   Dict[str, EnumDefinition] = field(default_factory=dict)
    datatypes:   Dict[str, DataDefinition] = field(default_factory=dict)
    entity_container:   Dict[str, EntityContainerDefinition] = field(default_factory=dict)


# Holds all configuration and data for a specific project instance being created.
@dataclass()
class ProjectDataWithDefintions:
    name: str
    description: str = "Module for Minir"
    author_name: str = "silenterus"
    author_mail: str = "neo-neu@web.de"
    name_prefix: str = ""

    version: str = "0.1.0"


    prompt: str = ""

    console: List[str] = field(default_factory=lambda: ["main"]) #TODO if a str is matched with MethodDefinition.name_command then it should be added as a group command, if its empty all should be selected, if main then it should remain as it is

    # List to hold dynamically generated method structures
    methods: List[MethodDefinition] = field(default_factory=list) # TODO needs to be replaced by methods_skeleton

    methods_skeleton: SkeletonDefinition = field(default_factory=SkeletonDefinition)



    script_command: str = ""
    name_method_appendix: str = "er"
    name_console_method_appendix: str = "_cli"




    editor:EditorType = EditorType.PYCHARM
    tests:TestsType = TestsType.CONFTEST

    readme:ReadmeType = ReadmeType.NONE
    license:LicenseType = LicenseType.NONE
    build:BuildPipelineType = BuildPipelineType.NONE
    agents:AgentsPromptType = AgentsPromptType.NONE


    python_version: str = "3.11.3"




    dependencies: Dict[str,str] = field(default_factory=lambda: {
        "pytest": "^8.3.0",
        "pytest-cov": "^3.0.0",
        "mypy": "^1.15.0",
        "pyright": "^1.1.370",
        "pyinstaller": "^6.13.0",
        "poetry-core": ">=2.0.0,<3.0.0",
    })
    dev_dependencies: Dict[str,str] = field(default_factory=dict)

    # Base directory for placing the generated project folder
    output_base_dir: Path = Path(".")






    @property
    def full_project_name(self) -> str:
        """Calculates the full project name including the prefix."""
        return f"{self.name_prefix}{self.name}"

    @property
    def method_name(self) -> str:
        return f"{self.name}{self.name_method_appendix}"



    @property
    def init_imports(self) -> str:
        all_imports = ""
        if len(self.console) > 0 and self.console[0] != "main":
            for imports in self.console:
                all_imports += f"\nfrom .{imports} import {imports}{self.name_console_method_appendix}"

        else:
            all_imports = f"from .{self.name} import {self.method_name}"
        return all_imports

    @property
    def init_public(self) -> str:
        if len(self.console) > 0 and self.console[0] != "main":
            publics = []
            for public in self.console:
                publics.append(f"{public}{self.name_console_method_appendix}")

            all_temp = "','".join(publics)
            all_publics = f"__all__ = ['{all_temp}']"
            pass
        else:
            all_publics = f"__all__ = ['{self.method_name}']"


        return all_publics

    @property
    def poetry_dependencies_dev(self) -> str:
        return self._poetry_dependencies_build()

    @property
    def poetry_dependencies(self) -> str:
        return self._poetry_dependencies_build(True)


    def _poetry_dependencies_build(self, dev:bool = False) -> str:

        if dev:
            selected = self.dev_dependencies.items()
        else:
            selected = self.dependencies.items()

        if len(selected) > 0:
            has_dependencies = ""
            for d_key, d_item in selected:
                has_dependencies += f"\n{d_key} = \"{d_item}\""
        else:
            has_dependencies = ""


        return has_dependencies


    @property
    def poetry_scripts_build(self) -> str:

        if self.methods:
            script_name = self.full_project_name.replace("_", "-")
            return f'{script_name} = "{self.full_project_name}.cli.main:cli"'
        elif self.console:
             script_name = self.full_project_name.replace("_", "-")
             return f'{script_name} = "{self.full_project_name}.cli.main:cli"'
        else:
            return ""


    @property
    def poetry_click_build(self) -> str:
        return ""


    @property
    def output_dir(self) -> Path:
        """Calculates the final output directory path for the project."""
        return (self.output_base_dir / self.full_project_name).resolve()

