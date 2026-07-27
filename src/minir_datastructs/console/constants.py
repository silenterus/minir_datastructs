
# --- Default Configuration Values ---
# These are names or relative paths. Click options will resolve them against CWD if used as defaults.

# Default name of the poetry project directory. If --project-root is not specified,
# this path is expected to exist relative to the current working directory (CWD).
DEFAULT_PROJECT_DIR_NAME_IN_CWD = "minir_console"

DEFAULT_UPX_DIR = "D:\\IDE\\tools\\upx"

# Subdirectory within project_root where application modules are located
DEFAULT_SRC_SUBDIR_NAME = "src"
# The common name for entry point scripts within each app module
DEFAULT_ENTRY_POINT_FILENAME = "main.py"

# PyInstaller related default names for directories/files created by PyInstaller.
# These are typically created in the CWD of the PyInstaller process (which we set to project_root).
DEFAULT_PYINSTALLER_OUTPUT_DIR_NAME = "dist"  # PyInstaller's temporary dist/ for a single build
DEFAULT_SPEC_FILE_NAME_SUFFIX = ".spec"
DEFAULT_PYINSTALLER_BUILD_DIR_NAME = "build"  # PyInstaller's build/ directory

# Default name for the directory where final executables are collected.
# If --collection-dir is not specified, this directory is created/used relative to CWD.
DEFAULT_COLLECTION_DIR_NAME_IN_CWD = "executables"

# Default name for the assets directory (e.g., for icons).
# If --assets-dir is not specified, this path is used relative to CWD.
DEFAULT_ASSETS_DIR_NAME_IN_CWD = "assets"

# Prefix for discovering app module directories within <project_root>/<src_subdir>/
DEFAULT_MODULE_PREFIX = "minir_"

DEFAULT_NAME_MAPPING = {
    "minir_codex_markdown_console": "mmd",
    "minir_builder_console": "mbuild",
    "minir_codex_python_console": "mpython",
    "minir_project_console": "mproject",
    "minir_replace_console": "mreplace",
    "minir_clippy_console": "mclip",
    "minir_copy_console": "mbackup",
    "minir_runner_manager_console": "mmanager",
    "minir_runner_selenium_console": "mrun",
    "minir_runner_selenium_profile_console": "mmanager_profile",
    "minir_console_console": "mcompile",

}

DEFAULT_ICON_MAPPING = {
    "minir_codex_markdown_console": "applicationIcon.ico",
    "minir_builder_console": "applicationIcon.ico",
    "minir_codex_python_console": "applicationIcon.ico",
    "minir_project_console": "applicationIcon.ico",
    "minir_replace_console": "applicationIcon.ico",
    "minir_clippy_console": "applicationIcon.ico",
    "minir_copy_console": "applicationIcon.ico",
    "minir_runner_manager_console": "applicationIcon.ico",
    "minir_runner_selenium_console": "applicationIcon.ico",
    "minir_runner_selenium_profile_console": "applicationIcon.ico",
    "minir_console_console": "applicationIcon.ico",
}

HIDDEN_IMPORTS = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

COLLECT_SUBMODULES = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

COLLECT_DATA = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

COLLECT_ALL = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

COLLECT_BINARIES = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

ADD_BINARY = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

ADD_DATA = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

COPY_METADATA = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

RECURSIVE_COPY_METADATA = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

ADDITIONAL_HOOKS_DIR = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

RUNTIME_HOOK = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

EXCLUDE_MODULE = {
    "minir_codex_markdown_console": [""],
    "minir_builder_console": [""],
    "minir_codex_python_console": [""],
    "minir_project_console": [""],
    "minir_replace_console": [""],
    "minir_clippy_console": [""],
    "minir_copy_console": [""],
    "minir_runner_manager_console": [""],
    "minir_runner_selenium_console": [""],
    "minir_runner_selenium_profile_console": [""],
    "minir_console_console": [""],
}

UPX_EXCLUDE = {
    "minir_codex_markdown_console": ["_uuid.pyd"],
    "minir_builder_console": ["_uuid.pyd"],
    "minir_codex_python_console": ["_uuid.pyd"],
    "minir_project_console": ["_uuid.pyd"],
    "minir_replace_console": ["_uuid.pyd"],
    "minir_clippy_console": ["_uuid.pyd"],
    "minir_copy_console": ["_uuid.pyd"],
    "minir_runner_manager_console": ["_uuid.pyd"],
    "minir_runner_selenium_console": ["_uuid.pyd"],
    "minir_runner_selenium_profile_console": ["_uuid.pyd"],
    "minir_console_console": ["_uuid.pyd"],
}

