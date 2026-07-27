from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class ProjectTemplate:
    author_name_replacement: str = "AUTHORNAMEINSERT"
    author_mail_replacement: str = "AUTHORMAILINSERT"
    description_replacement: str = "DESCRIPTIONINSERT"

    version_replacement: str = "VERSIONINSERT"
    python_version_replacement: str = "VERSIONPYTHONINSERT"

    # This marker is used for both content replacement and filename/directory renaming by mreplace
    name_replacement: str = "block"
    name_prefix_replacement: str = "minir_"

    # Static list of extensions mreplace should treat as text files for content replacement
    text_extensions: List[str] = field(default_factory=lambda: [
        ".txt", ".py", ".md", ".toml", ".json", ".yaml", ".yml",
        ".sh", ".ini", ".cfg", ".xml", ".html", ".css", ".js",
        ".ts", ".jsx", ".tsx", ".markdown", ".gitignore", ".iml" # .xml and .iml needed for PyCharm files
    ])
