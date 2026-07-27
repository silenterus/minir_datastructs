import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

DEFAULT_PYTHON_VERSION_CONSTRAINT = "3.11.3"

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ProjectConfig:
    """Configuration for a single project skeleton."""
    name: str
    base_dir: Path
    python_version_constraint: str = DEFAULT_PYTHON_VERSION_CONSTRAINT
    src_dir: Path = field(init=False)
    package_dir: Path = field(init=False)
    cli_dir: Path = field(init=False)
    tests_dir: Path = field(init=False)
    tests_module_dir: Path = field(init=False)

    research_dir: Path = field(init=False)
    blank_dir: Path = field(init=False)
    working_dir: Path = field(init=False)

    def __post_init__(self):

        object.__setattr__(self, "research_dir", self.base_dir / "research")
        object.__setattr__(self, "blank_dir", self.base_dir / "research" / "blank")
        object.__setattr__(self, "working_dir", self.base_dir / "research" / "working")

        object.__setattr__(self, "src_dir", self.base_dir / "src")
        object.__setattr__(self, "package_dir", self.base_dir / "src" / self.name)
        object.__setattr__(self, "cli_dir", self.base_dir / "src" / "cli")
        object.__setattr__(self, "tests_dir", self.base_dir / "tests")
        object.__setattr__(self, "tests_module_dir", self.base_dir / "tests" / self.name)


