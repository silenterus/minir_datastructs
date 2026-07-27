from typing import Dict, Set
from minir_datastructs.enum.enum_string_aliases_description import EnumStringAliasesDescription

from .language_kind import LanguageKind


class LanguageWorkspaceGroupKind(EnumStringAliasesDescription):
    # Tuple format: (value_str, value_int, aliases_str, description_str)
    NONE = ("none", 0, "", "")
    UNKNOWN = ("unknow", 9999, "", "")

    UNREAL_5 = ("unreal5", 1, "unreal_engine_project,uproject_workspace",
                "Unreal Engine 5 project (identified by .uproject file and UE folder structure)")
    POETRY = ("poetry_project", 2, "poetry,python_poetry,pyproject_poetry,python_project_poetry",
              "Python projects managed with Poetry (pyproject.toml with poetry tool section, poetry.lock)")
    VUE = ("vue_cli_project", 3, "vue_project,vuejs_project,vue_npm_project,vue_cli",
                       "Vue.js projects typically scaffolded with Vue CLI (uses package.json, vue.config.js)")
    NPM = ("npm_project", 4,
                   "npm,node_project,javascript_project,typescript_project,yarn_project,pnpm_project,package_json_project",
                   "Node.js/JavaScript/TypeScript projects managed with npm, yarn, or pnpm (package.json), not fitting a more specific framework group")
    OBSIDIAN = ("obsidian_vault", 5, "obsidian,markdown_notes_vault,obsidian_md_vault",
                      "Obsidian Markdown notes vault (identified by .obsidian folder)")

    PYTHON = ("python_standard_project", 6,
                               "python_project_generic,setuptools_project,requirements_txt_project,pip_project,hatch_project,flit_project",
                               "Python project using standard packaging (e.g., requirements.txt, setup.py, or generic pyproject.toml for tools like Hatch, Flit)")
    CMAKE = ("cmake_project", 7, "cmake,c_project_cmake,cpp_project_cmake,cmakelists_project",
                     "CMake-based project (C, C++, etc., identified by CMakeLists.txt)")
    MAKEFILE = ("makefile_project", 8, "make_project,gnumake_project,bsdmake_project,makefile_build",
                        "Project built with Makefiles (Makefile, GNUmakefile, etc.)")
    GRADLE = ("gradle_project", 9,
                      "gradle,android_studio_project,kotlin_gradle_project,java_gradle_project,groovy_gradle_project",
                      "Gradle project (Java, Kotlin, Groovy, Android, identified by build.gradle or build.gradle.kts)")
    MAVEN = ("maven_project", 10, "maven,mvn_project,java_maven_project,pom_xml_project",
                     "Maven project (Java, identified by pom.xml)")
    ANT = ("ant_project", 11, "ant_build,java_ant_project,ant_xml_project",
                   "Ant project (Java, identified by build.xml)")

    RUBY = ("ruby_bundler_project", 12, "ruby_project,gemfile_project,rails_project,ruby_bundler",
                            "Ruby project using Bundler (identified by Gemfile), e.g., Rails")
    RUST = ("rust_cargo_project", 13, "rust_project,cargo_project,cargo_toml_project",
                          "Rust project using Cargo (identified by Cargo.toml)")
    GO = ("go_modules_project", 14, "golang_project,go_project,go_mod_project",
                          "Go project using Go Modules (identified by go.mod)")
    SWIFT = ("swift_package_manager_project", 15,
                                     "swift_project_spm,swift_project,package_swift_project,swift_pm",
                                     "Swift project using Swift Package Manager (identified by Package.swift)")
    XCODE = ("xcode_project", 16,
                     "xcode_workspace,ios_project,macos_project,swift_xcode_project,objc_xcode_project,xcodeproj_file,xcworkspace_file",
                     "Xcode project or workspace (Swift/Objective-C, identified by .xcodeproj or .xcworkspace)")

    UNITY = ("unity_project", 17, "unity3d_project,unity_engine_project,csharp_unity_project,unity_game",
                     "Unity game engine project (Assets, ProjectSettings folders, .sln for C#)")
    GODOT = ("godot_project", 18, "godot_engine_project,gdscript_project,project_godot_file,godot_game",
                     "Godot game engine project (identified by project.godot file)")
    GAMEMAKER_STUDIO = ("gamemaker_studio_project", 19, "gml_project,yyp_project,gamemaker_project,gms_project",
                                "GameMaker Studio project (identified by .yyp file)")

    DOCKER_COMPOSE = ("docker_compose_workspace", 20,
                                "docker_project,docker_compose_project,compose_yaml_project,docker_env",
                                "Project workspace defined by Docker Compose (identified by docker-compose.yml or compose.yaml)")
    TERRAFORM = ("terraform_workspace", 21,
                           "terraform_project,tf_project,iac_terraform_project,hcl_terraform_project",
                           "Terraform Infrastructure-as-Code workspace (collection of .tf, .tfvars files)")

    LATEX = ("latex_project", 22, "latex_document,tex_project,tex_document_collection,pdflatex_project",
                     "LaTeX document/project (main .tex file, often with .cls, .sty, bibliography)")
    FLUTTER = ("flutter_project", 23, "flutter_app,dart_flutter_project,dart_mobile_project,flutter_dart",
                       "Flutter project for mobile/web/desktop apps (identified by pubspec.yaml with flutter SDK dependency)")
    ARDUINO = ("arduino_project", 24, "arduino_sketch,ino_project,arduino_ide_project",
                       "Arduino sketch/project (.ino file in a matching folder name, possibly with libraries or platformio.ini)")
    PLATFORMIO = ("platformio_project", 25,
                          "platformio,embedded_platformio_project,iot_platformio_project,platformio_ini_project",
                          "PlatformIO-based embedded project (identified by platformio.ini)")

    ROS = ("ros_workspace", 26,
                     "robot_os_project,catkin_workspace,ament_workspace,ros_project,ros2_workspace",
                     "Robot Operating System (ROS/ROS2) workspace (e.g., package.xml, CMakeLists.txt in src, colcon build)")
    VSCODE = ("vscode_extension_project", 27, "vscode_plugin_project,vsix_project,vscode_dev_project",
                                "Visual Studio Code extension project (package.json with vscode engine and contribution points)")
    BROWSER_EXTENSION = ("browser_extension_project", 28,
                                 "chrome_extension_project,firefox_addon_project,web_extension_project,manifest_json_extension",
                                 "Browser extension project (e.g., manifest.json for Chrome/Firefox/Edge)")

    HUGO = ("hugo_site", 29, "hugo_project,static_site_generator_hugo,go_hugo_site",
                 "Hugo static site generator project (hugo.toml, config.toml/yaml/json, content/ folder)")
    JEKYLL = ("jekyll_site", 30,
                   "jekyll_project,github_pages_jekyll_site,static_site_generator_jekyll,ruby_jekyll_site",
                   "Jekyll static site generator project (_config.yml, Gemfile, _posts/ folder)")
    DOCUSAURUS = ("docusaurus_site", 31,
                       "docusaurus_project,react_documentation_site,static_site_generator_docusaurus,mdx_docs_site",
                       "Docusaurus static site generator project (docusaurus.config.js, package.json)")
    SPHINX_DOCS = ("sphinx_docs_project", 32,
                           "sphinx_documentation,python_docs_project,rest_docs_project,conf_py_project",
                           "Sphinx documentation project (conf.py, .rst or .md files, _build directory)")

    ELIXIR_MIX = ("elixir_mix_project", 33,
                          "elixir_project,phoenix_framework_project,mix_exs_project,ex_project",
                          "Elixir project using Mix (identified by mix.exs), e.g., Phoenix framework")
    PHP_COMPOSER = ("php_composer_project", 34,
                            "php_project,laravel_project,symfony_project,composer_json_project",
                            "PHP project using Composer (identified by composer.json)")
    SBT = ("sbt_project", 35, "scala_project_sbt,scala_build_tool_project,build_sbt_project,scala_project",
                   "Scala project using sbt (identified by build.sbt and project directory)")
    LEININGEN = ("leiningen_project", 36,
                         "clojure_project_lein,clj_lein_project,project_clj_file,clojure_project",
                         "Clojure project using Leiningen (identified by project.clj)")
    CLOJURE = ("clojure_cli_project", 37,
                           "clj_project_deps,deps_edn_project,clojure_tools_deps_project,cljs_project_cli",
                           "Clojure/ClojureScript project using CLI tools (identified by deps.edn)")

    HASKELL_STACK = ("haskell_stack_project", 38,
                             "stack_project,hs_stack_project,stack_yaml_project,haskell_project",
                             "Haskell project using Stack (identified by stack.yaml)")
    HASKELL_CABAL = ("haskell_cabal_project", 39,
                             "cabal_project,hs_cabal_project,cabal_file_project,haskell_cabal",
                             "Haskell project using Cabal (identified by .cabal file, cabal.project)")
    PERL = ("perl_distribution", 40,
                         "perl_project,cpan_module_project,perl_module_build_project,perl_eumm_project",
                         "Perl distribution/module (Makefile.PL or Build.PL)")

    DUNE = ("dune_project", 41,
                    "ocaml_dune_project,reasonml_dune_project,ocaml_project,reason_project,dune_build",
                    "OCaml/ReasonML project using Dune (dune-project, dune files)")
    IDRIS = ("idris_package", 42, "idris_project,idris_ipkg_project,ipkg_project,idr_project",
                     "Idris project/package (identified by .ipkg file)")
    PURESCRIPT_SPAGO = ("purescript_spago_project", 43,
                                "purescript_project,purs_spago_project,dhall_config_spago,purs_project",
                                "PureScript project using Spago (spago.dhall, packages.dhall)")
    NIMBLE = ("nimble_package", 44, "nim_project,nim_nimble_project,nimble_file_project,nim_pkg",
                      "Nim project/package using Nimble (identified by .nimble file)")

    ELECTRON = ("electron_app", 45, "electron_project,desktop_app_electron,nodejs_gui_electron,electron_js_app",
                    "Electron application project (package.json with electron dependency/scripts, main.js)")
    BAZEL = ("bazel_workspace", 46, "bazel_project,google_bazel_project,starlark_build_project,bazel_build",
                       "Bazel build system workspace (WORKSPACE, BUILD files)")
    QUARTO = ("quarto_project", 47,
                      "quarto_document_project,quarto_site_project,qmd_project,quarto_book_project,_quarto_yml",
                      "Quarto project (documents, books, websites, presentations, identified by _quarto.yml)")

    PLAIN = ("plain_content_collection", 48,
                                "text_files_workspace,markdown_workspace,generic_documents_workspace,notes_collection",
                                "Generic workspace with primarily text/markdown files not part of a specific framework or tool (e.g., personal notes, simple scripts folder)")
    SQL = ("sql_database_project", 49,
                            "db_scripts_project,sql_migrations_project,database_schema_project,sql_files_project",
                            "Project focused on SQL scripts for database schemas, migrations, queries, or administration")
    VIM = ("vim_configuration", 50,
                         "vimrc_project,neovim_config_project,vim_plugin_project,viml_scripts_project,init_vim_project",
                         "Vim/Neovim configuration or plugin development workspace (e.g. init.vim, .vimrc, plugin/ folder)")
    JAVA = ("java_plain_project", 51,
                          "simple_java_project,java_scripts_folder,bare_java_project,no_buildtool_java",
                          "Java project without a recognized build tool (e.g., collection of .java files, common for small examples or educational purposes)")

    ADOBE_FLASH_FLEX = ("adobe_flash_flex_project", 52,
                                "flex_project,actionscript_project,flash_builder_project,mxml_project,as_project",
                                "Adobe Flash/Flex Builder project (ActionScript, MXML, often .actionScriptProperties or .project files)")
    COLDFUSION = ("coldfusion_project", 53, "cfml_project,cf_application_project,coldfusion_app,lucee_project",
                          "ColdFusion/CFML project (typically with Application.cfc or .cfconfig.json)")

    SVELTE = ("svelte_project", 54, "svelte_app,sveltekit_project,svelte_npm_project,vite_svelte_project",
                      "Svelte or SvelteKit project (uses package.json, svelte.config.js)")
    REACT = ("react_project", 55,
                     "react_app,cra_project,nextjs_project,gatsby_project,vite_react_project,remix_project,react_npm_project",
                     "React-based frontend project (e.g., Create React App, Next.js, Gatsby, Vite+React, Remix, uses package.json)")
    ANGULAR = ("angular_cli_project", 56,
                           "angular_project,ng_project,angular_workspace_project,angular_npm_project",
                           "Angular project scaffolded with Angular CLI (angular.json, uses package.json)")
    DART = ("dart_package", 57,
                    "dart_library_project,pubspec_yaml_project,dart_cli_project,dart_generic_project",
                    "Generic Dart package/library (pubspec.yaml without flutter dependency, typically for command-line tools or server-side apps)")

    DOTNET = ("dotnet", 58, "dot_net,csharp_project,fsharp_project,vb_project,sln_workspace",
              "Microsoft .NET ecosystem (e.g., .sln, .csproj, .fsproj files)")







WORKSPACE_LANGUAGE_MAPPING: Dict[LanguageWorkspaceGroupKind, Set[LanguageKind]] = {
    LanguageWorkspaceGroupKind.NONE: set(),
    LanguageWorkspaceGroupKind.UNKNOWN: set(),

    LanguageWorkspaceGroupKind.UNREAL_5: {
        LanguageKind.CPP,
        LanguageKind.UNREAL_BUILD_SCRIPT_CS, # C# for Build.cs, Target.cs
        LanguageKind.CSHARP, # General C# for tools or other scripts
        LanguageKind.UNREAL_CONFIG_INI, # .ini files
        LanguageKind.INI, # Other .ini files
        LanguageKind.UNREAL_SHADER_FILE, # .usf
        LanguageKind.UNREAL_SHADER_HEADER, # .ush
        LanguageKind.HLSL, # General HLSL if not specific .usf/.ush
        LanguageKind.UNREAL_PROJECT, # .uproject (JSON)
        LanguageKind.UNREAL_PLUGIN_DESCRIPTOR, # .uplugin (JSON)
        LanguageKind.JSON, # Other JSON files
        LanguageKind.UNREAL_BUILD_GRAPH_XML, # BuildGraph .xml
        LanguageKind.UNREAL_BUILD_TOOL_MANIFEST_XML, # UBT Manifest .xml
        LanguageKind.UNREAL_NATIVE_VISUALIZER, # .natvis (XML)
        LanguageKind.XML, # Other XML files
        LanguageKind.PYTHON, # Editor scripting, utilities
        LanguageKind.UNREAL_ASSET_BINARY, # .uasset, .umap (Binary, but often listed)
        LanguageKind.UNREAL_H_GENERATED, # .generated.h (C++)
        LanguageKind.UNREAL_CPP_GENERATED, # .gen.cpp (C++)
        LanguageKind.UNREAL_CPP_INL, # .inl (C++)
        LanguageKind.VERSE, # .verse
        LanguageKind.UNREAL_LOG, # .log (Text)
        LanguageKind.TEXT, # For .log and other plain text files
        LanguageKind.UNREAL_UHT_MANIFEST, # .uhtmanifest (JSON)
        LanguageKind.UNREAL_MODULES_FILE, # .modules (JSON)
        LanguageKind.UNREAL_VERSION_FILE, # .version (JSON)
        LanguageKind.UNREAL_PLUGIN_MANIFEST, # .upluginmanifest (JSON)
        LanguageKind.UNREAL_AUTOMATION_TEST_JSON, # .automation.json (JSON)
        LanguageKind.UNREAL_UBT_MANIFEST, # UBT .ubtmanifest (JSON)
        LanguageKind.UNREAL_BUILD_RECEIPT, # .target (JSON/XML)
        LanguageKind.UNREAL_BUILD_RESPONSE_FILE, # .response (Text)
        LanguageKind.UNREAL_LOC_MANIFEST, # Localization .manifest (JSON)
        LanguageKind.UNREAL_LOC_ARCHIVE, # Localization .archive (JSON)
        LanguageKind.UNREAL_LOC_PO, # .po files (Text-based, specific format)
        LanguageKind.UNREAL_TARGET_DEF_JSON, # Build target .target (JSON)
    },
    LanguageWorkspaceGroupKind.POETRY: {
        LanguageKind.PYTHON,
        LanguageKind.TOML,    # pyproject.toml
        LanguageKind.TEXT,    # poetry.lock
        LanguageKind.MARKDOWN,
        LanguageKind.YAML,    # CI/CD configs
        LanguageKind.JSON,
        LanguageKind.SHELL,
        LanguageKind.MAKEFILE,
    },
    LanguageWorkspaceGroupKind.VUE: {
        LanguageKind.VUE,
        LanguageKind.JAVASCRIPT,
        LanguageKind.TYPESCRIPT,
        LanguageKind.HTML,
        LanguageKind.CSS,
        LanguageKind.SASS,
        # LanguageKind.SCSS, # SASS has scss alias
        LanguageKind.LESS,
        LanguageKind.STYLUS,
        LanguageKind.JSON,    # package.json, vue.config.js (if json content), tsconfig.json
        LanguageKind.MARKDOWN,
        LanguageKind.JSX,
        LanguageKind.TSX,
        LanguageKind.PUG,
    },
    LanguageWorkspaceGroupKind.NPM: {
        LanguageKind.JAVASCRIPT,
        LanguageKind.TYPESCRIPT,
        LanguageKind.JSON,    # package.json, various .json configs
        LanguageKind.HTML,    # If it's a web project
        LanguageKind.CSS,     # If it's a web project
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.STYLUS,
        LanguageKind.MARKDOWN,
        LanguageKind.YAML,    # CI/CD, .npmrc (can be ini-like or yaml)
        LanguageKind.JSX,
        LanguageKind.TSX,
        LanguageKind.SHELL,   # Scripts in package.json, utility scripts
        LanguageKind.DOCKERFILE,
        LanguageKind.TEXT,    # .npmrc, .yarnrc (can be various formats)
        LanguageKind.DOTENV,
        LanguageKind.VUE,     # Could be a Vue project managed by generic npm
        LanguageKind.SVELTE,  # Could be a Svelte project
        LanguageKind.GRAPHQL,
        # LanguageKind.MDX,
    },
    LanguageWorkspaceGroupKind.OBSIDIAN: {
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,    # .obsidian folder config files
        LanguageKind.CSS,     # Custom themes, snippets
        LanguageKind.JAVASCRIPT, # Plugins
        LanguageKind.TYPESCRIPT, # Plugins (source)
        LanguageKind.HTML,    # For more complex notes or plugin UIs
        LanguageKind.YAML,    # Frontmatter in markdown
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.PYTHON: {
        LanguageKind.PYTHON,
        LanguageKind.TEXT,    # requirements.txt, MANIFEST.in
        LanguageKind.MARKDOWN,
        LanguageKind.TOML,    # pyproject.toml
        LanguageKind.INI,     # setup.cfg, tox.ini, pylintrc
        LanguageKind.YAML,    # CI/CD, conda env files
        LanguageKind.JSON,
        LanguageKind.SHELL,   # Scripts
        LanguageKind.BAT,     # Scripts
        LanguageKind.MAKEFILE,
        LanguageKind.DOCKERFILE,
        LanguageKind.RESTRUCTUREDTEXT, # .rst for docs
        LanguageKind.JINJA,   # Templates
        LanguageKind.SQL,     # If interacting with DBs
        # LanguageKind.ENV,     # .env files - use DOTENV
        LanguageKind.DOTENV,
    },
    LanguageWorkspaceGroupKind.CMAKE: {
        LanguageKind.CMAKE,   # CMakeLists.txt, .cmake files
        LanguageKind.CPP,
        LanguageKind.C,
        LanguageKind.CSHARP,  # If building C# via CMake (e.g. C++/CLI)
        LanguageKind.PYTHON,  # Helper scripts, custom commands
        LanguageKind.SHELL,   # Build scripts, custom commands
        LanguageKind.FORTRAN,
        LanguageKind.ASSEMBLY,
        LanguageKind.CUDA,
        LanguageKind.OBJECTIVEC,
        LanguageKind.SWIFT,   # Increasingly supported by CMake
        LanguageKind.LEX,     # .l files
        LanguageKind.YACC,    # .y files (Bison)
        LanguageKind.TEXT,
        LanguageKind.MARKDOWN,
        # LanguageKind.NINJA, # if ninja is used as generator
    },
    LanguageWorkspaceGroupKind.MAKEFILE: {
        LanguageKind.MAKEFILE,
        LanguageKind.C,
        LanguageKind.CPP,
        LanguageKind.ASSEMBLY,
        LanguageKind.SHELL,   # Commands within Makefiles, helper scripts
        LanguageKind.PYTHON,  # Helper scripts
        LanguageKind.PERL,    # Helper scripts
        LanguageKind.FORTRAN,
        LanguageKind.OBJECTIVEC,
        LanguageKind.CUDA,
        LanguageKind.AWK,     # Often used with Make
        # LanguageKind.SED,     # Often used with Make (not a distinct language kind, part of shell)
        LanguageKind.TEXT,
        LanguageKind.MARKDOWN,
        LanguageKind.M4,      # For autoconf generated Makefiles
    },
    LanguageWorkspaceGroupKind.GRADLE: {
        LanguageKind.GRADLE,  # build.gradle, settings.gradle, .gradle.kts
        LanguageKind.GROOVY,  # For .gradle files
        LanguageKind.KOTLIN,  # For .gradle.kts files and app code
        LanguageKind.JAVA,    # App code
        LanguageKind.SCALA,   # App code
        # LanguageKind.ANDROID_MANIFEST, # AndroidManifest.xml - this isn't a LanguageKind, use XML
        LanguageKind.XML,     # Android resources, configs
        LanguageKind.JSON,    # Configs
        LanguageKind.PROPERTIES, # gradle.properties
        LanguageKind.CPP,     # Android NDK
        LanguageKind.C,       # Android NDK
        LanguageKind.SHELL,
        LanguageKind.MARKDOWN,
    },
    LanguageWorkspaceGroupKind.MAVEN: {
        LanguageKind.MAVEN_POM, # pom.xml
        LanguageKind.XML,     # pom.xml itself, other configs (checkstyle, etc.)
        LanguageKind.JAVA,
        LanguageKind.KOTLIN,
        LanguageKind.SCALA,
        LanguageKind.GROOVY,
        LanguageKind.PROPERTIES, # project.properties
        LanguageKind.JSON,    # Configs
        LanguageKind.SHELL,
        LanguageKind.MARKDOWN,
        LanguageKind.TEXT,    # mvnw, mvnw.cmd wrapper scripts are shell/batch
        LanguageKind.BAT,
    },
    LanguageWorkspaceGroupKind.ANT: {
        LanguageKind.ANT,     # build.xml
        LanguageKind.XML,     # build.xml itself, other XML configs
        LanguageKind.JAVA,
        LanguageKind.PROPERTIES, # build.properties
        LanguageKind.JAVASCRIPT, # Rhino scripting in Ant tasks
        LanguageKind.SHELL,
        LanguageKind.MARKDOWN,
    },
    LanguageWorkspaceGroupKind.RUBY: {
        LanguageKind.RUBY,
        LanguageKind.GEMFILE, # Gemfile, Gemfile.lock
        LanguageKind.HTML,    # ERB/Haml/Slim templates compile to HTML
        LanguageKind.JAVASCRIPT, # Rails assets
        LanguageKind.TYPESCRIPT, # Rails assets
        LanguageKind.COFFEESCRIPT, # Older Rails assets
        LanguageKind.CSS,     # Rails assets
        LanguageKind.SASS,    # Rails assets
        # LanguageKind.SCSS,
        LanguageKind.YAML,    # Rails configs (database.yml, etc.)
        LanguageKind.SQL,     # Migrations, raw SQL
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,    # Configs
        LanguageKind.SHELL,
        # LanguageKind.RAKE,    # Rakefiles are Ruby (.rake is an alias for Ruby)
        LanguageKind.SLIM_TPL, # Slim templates
        LanguageKind.HAML,    # Haml templates
        # LanguageKind.ERB, # Not a separate lang, but implied by Ruby+HTML
    },
    LanguageWorkspaceGroupKind.RUST: {
        LanguageKind.RUST,
        LanguageKind.TOML,    # Cargo.toml, Cargo.lock
        LanguageKind.MARKDOWN,
        # LanguageKind.MDX, # For tools like mdbook
        LanguageKind.SHELL,   # build.rs (can invoke shell), scripts
        LanguageKind.PYTHON,  # Helper scripts
        LanguageKind.C,       # FFI
        LanguageKind.CPP,     # FFI
        LanguageKind.MAKEFILE,
        LanguageKind.JSON,    # Configs
        # LanguageKind.RON,     # Rust Object Notation (not a lang kind, treat as TEXT or specific if added)
        LanguageKind.TEXT,    # For .ron or other custom formats
    },
    LanguageWorkspaceGroupKind.GO: {
        LanguageKind.GO,
        LanguageKind.TEXT,    # go.mod, go.sum (Go specific format)
        LanguageKind.MARKDOWN,
        LanguageKind.YAML,    # Configs
        LanguageKind.JSON,    # Configs
        LanguageKind.PROTOBUF, # gRPC
        LanguageKind.SHELL,   # Scripts
        LanguageKind.MAKEFILE,
        LanguageKind.C,       # cgo
        LanguageKind.HTML,    # Go templates
        # LanguageKind.GO_TEMPLATE, # A specific kind for Go templates if available, else covered by HTML/TEXT
        LanguageKind.SQL,
    },
    LanguageWorkspaceGroupKind.SWIFT: { # Swift Package Manager
        LanguageKind.SWIFT,   # Package.swift, source files
        LanguageKind.OBJECTIVEC, # Interop
        LanguageKind.C,       # Interop
        LanguageKind.CPP,     # Interop
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,    # Configs, package.resolved
        LanguageKind.SHELL,   # Scripts
        LanguageKind.METAL,   # If graphics related
        LanguageKind.XML,     # Plist for some metadata if targeting Apple platforms
    },
    LanguageWorkspaceGroupKind.XCODE: {
        LanguageKind.SWIFT,
        LanguageKind.OBJECTIVEC,
        LanguageKind.C,
        LanguageKind.CPP,
        LanguageKind.METAL,
        LanguageKind.XML,     # .plist, .xcscheme, .storyboard, .xib, project.pbxproj (inside .xcodeproj)
        # LanguageKind.PLIST,   # (XML dialect)
        LanguageKind.JSON,    # Configs
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,   # Build phase scripts
        LanguageKind.ASSEMBLY,
        # LanguageKind.HEADER, # .h files - covered by C/CPP/ObjectiveC generally but could be distinct
        LanguageKind.APPLESCRIPT, # For automation scripts
        LanguageKind.RUBY,    # CocoaPods (Podfile)
        LanguageKind.GEMFILE, # CocoaPods (Podfile.lock)
    },
    LanguageWorkspaceGroupKind.UNITY: {
        LanguageKind.CSHARP,  # Scripts
        LanguageKind.HLSL,    # Shaders (ShaderLab often uses HLSL/Cg syntax)
        # LanguageKind.CG,      # (HLSL alias)
        LanguageKind.JSON,    # asmdef, package.json (UPM), project settings (some)
        LanguageKind.XML,     # Some legacy project settings, AndroidManifest.xml
        LanguageKind.YAML,    # .unity (scenes), .prefab, .mat, .asset (text-serialized assets), .meta
        LanguageKind.MARKDOWN, # Package documentation
        LanguageKind.TEXT,    # .shader (ShaderLab is custom text), .asmdef (JSON but simple)
        LanguageKind.PYTHON,  # Editor scripts (less common now but possible)
        LanguageKind.SHELL,   # Build scripts
        LanguageKind.GRADLE,  # If exporting for Android (inside Temp/GradleProject)
    },
    LanguageWorkspaceGroupKind.GODOT: {
        LanguageKind.GDSCRIPT, # .gd
        LanguageKind.CSHARP,  # Godot Mono .cs
        LanguageKind.CPP,     # GDExtension/GDNative .cpp, .h
        LanguageKind.C,       # GDExtension/GDNative
        LanguageKind.RUST,    # GDExtension/GDNative with Rust bindings
        LanguageKind.INI,     # project.godot, some .tres, .tscn (Godot Text Resource format is INI-like)
        LanguageKind.TEXT,    # .import files, .godot (project file), .tscn, .tres
        LanguageKind.GLSL,    # Shaders .glsl, .gdshader
        LanguageKind.MARKDOWN, # Documentation
        LanguageKind.JSON,    # Export presets, plugin configs
        LanguageKind.XML,     # Android export template configs
        LanguageKind.SHELL,
        LanguageKind.PYTHON,  # Buildsystem scripts (SCons)
    },
    LanguageWorkspaceGroupKind.GAMEMAKER_STUDIO: {
        LanguageKind.GAMEMAKER_LANGUAGE, # GML .gml
        LanguageKind.JSON,    # .yyp (project file), room files, object files, sprites, etc.
        LanguageKind.XML,     # Some configuration files, extension packages
        LanguageKind.TEXT,    # Notes, script headers
        LanguageKind.INI,     # options.ini
        LanguageKind.GLSL,    # Shaders .fsh, .vsh
        LanguageKind.MARKDOWN, # Marketplace asset info
        LanguageKind.SHELL,   # External tools/scripts
    },
    LanguageWorkspaceGroupKind.DOCKER_COMPOSE: {
        LanguageKind.YAML,    # docker-compose.yml, compose.yaml
        LanguageKind.DOCKERFILE, # Referenced Dockerfiles
        LanguageKind.SHELL,   # Scripts called by compose, entrypoint scripts
        LanguageKind.DOTENV,  # .env files for compose
        # LanguageKind.ENV,     # (alias for DOTENV)
        LanguageKind.JSON,    # Configs that might be mounted or used by services
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.TERRAFORM: {
        LanguageKind.TERRAFORM, # .tf, .tfvars (HCL)
        # LanguageKind.HCL,     # (alias for TERRAFORM)
        LanguageKind.JSON,    # .tf.json files, policy files
        LanguageKind.YAML,    # Input variables, local configs, Terragrunt hcl might use yamlencode
        LanguageKind.SHELL,   # Helper scripts
        LanguageKind.PYTHON,  # Helper scripts, pre-commit hooks
        LanguageKind.MARKDOWN, # Documentation, READMEs
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.LATEX: {
        LanguageKind.LATEX,   # .tex, .cls, .sty, .ltx
        LanguageKind.TEX_PLAIN, # if using plain TeX specific features
        LanguageKind.BIBTEX,  # .bib
        LanguageKind.MAKEFILE,# For build process (latexmk can generate one)
        LanguageKind.PYTHON,  # Helper scripts, e.g. for latexmk or custom pre/post processing
        LanguageKind.PERL,    # latexmk is a Perl script
        LanguageKind.LUA,     # LuaLaTeX uses Lua (.lua files)
        LanguageKind.SHELL,   # Build scripts
        LanguageKind.BAT,     # Build scripts (Windows)
        LanguageKind.TEXT,    # .aux, .log, .toc, etc.
        LanguageKind.MARKDOWN, # If converting MD to LaTeX
        LanguageKind.R,       # knitr/sweave if using R to generate .tex
        LanguageKind.C,       # For custom C tools if any (rare)
        # LanguageKind.METAPOST, # For diagrams (not a LangKind, but .mp files)
        # LanguageKind.ASYMPTOTE, # For diagrams (not a LangKind, but .asy files)
        # LanguageKind.GNUPLOT, # For plots
        # LanguageKind.TIKZ,    # (LaTeX package, not a separate LanguageKind)
    },
    LanguageWorkspaceGroupKind.FLUTTER: {
        LanguageKind.DART,
        LanguageKind.YAML,    # pubspec.yaml, analysis_options.yaml
        LanguageKind.XML,     # Android: AndroidManifest.xml, layout files. iOS: Info.plist (sometimes as XML)
        LanguageKind.JSON,    # Configs, l10n files (.arb are JSON)
        LanguageKind.GRADLE,  # Android build files (Groovy/Kotlin)
        LanguageKind.GROOVY,  # Android build files
        LanguageKind.KOTLIN,  # Android native code, Gradle scripts
        LanguageKind.JAVA,    # Android native code
        LanguageKind.SWIFT,   # iOS native code
        LanguageKind.OBJECTIVEC, # iOS native code
        LanguageKind.MARKDOWN, # README, documentation
        LanguageKind.CPP,     # Desktop/custom embedders, FFI
        LanguageKind.C,       # Desktop/custom embedders, FFI
        LanguageKind.SHELL,   # Build/run scripts
        LanguageKind.POWERSHELL, # Windows scripts
        LanguageKind.METAL,   # For custom rendering on Apple platforms
    },
    LanguageWorkspaceGroupKind.ARDUINO: {
        LanguageKind.ARDUINO, # .ino files (which are C/C++ like)
        LanguageKind.CPP,     # .cpp, .h files in libraries or advanced sketches
        LanguageKind.C,       # .c, .h files
        LanguageKind.ASSEMBLY,# Inline assembly or separate .S files
        LanguageKind.JSON,    # library.json, board definitions (boards.txt is not json)
        LanguageKind.TEXT,    # keywords.txt, boards.txt (custom INI-like format)
        LanguageKind.INI,     # If PlatformIO is used (platformio.ini), but this is specific to PlatformIO
        LanguageKind.PYTHON,  # Uploader scripts or helpers
        LanguageKind.SHELL,   # Scripts
        LanguageKind.MAKEFILE,# If using custom makefile build
        LanguageKind.MARKDOWN,
    },
    LanguageWorkspaceGroupKind.PLATFORMIO: {
        LanguageKind.INI,     # platformio.ini
        LanguageKind.CPP,     # Firmware code
        LanguageKind.C,       # Firmware code
        LanguageKind.ARDUINO, # If Arduino framework is used
        LanguageKind.PYTHON,  # Custom scripts (pio run -t <script>), SCons scripts (platformio internals)
        LanguageKind.JSON,    # Manifests (library.json), board definitions, .pio/build/ (debug configs)
        LanguageKind.SHELL,   # Scripts
        LanguageKind.ASSEMBLY,
        LanguageKind.MAKEFILE,# Can be used by custom platforms
        LanguageKind.CMAKE,   # PlatformIO can generate CMake projects (CMakeLists.txt)
        LanguageKind.TEXT,    # Linker scripts (.ld)
        LanguageKind.MARKDOWN,
    },
    LanguageWorkspaceGroupKind.ROS: {
        LanguageKind.CPP,
        LanguageKind.PYTHON,
        LanguageKind.XML,     # package.xml, launch files, URDF, XACRO, COLLADA (.dae)
        LanguageKind.CMAKE,   # CMakeLists.txt
        LanguageKind.SHELL,   # Scripts, setup files
        LanguageKind.YAML,    # Config files, parameters (.yaml, .yml)
        LanguageKind.MARKDOWN, # README, package documentation
        LanguageKind.TEXT,    # .msg, .srv, .action files (ROS specific formats)
        LanguageKind.IDL,     # For DDS definitions if used directly
        LanguageKind.LUA,     # For some tools like rviz plugins
        LanguageKind.BASH,
    },
    LanguageWorkspaceGroupKind.VSCODE: {
        LanguageKind.TYPESCRIPT,
        LanguageKind.JAVASCRIPT,
        LanguageKind.JSON,    # package.json, launch.json, settings.json, problemMatchers.json
        LanguageKind.MARKDOWN, # README, CHANGELOG, documentation
        LanguageKind.YAML,    # CI/CD (.github/workflows), Azure Pipelines YAML
        LanguageKind.HTML,    # Webview content
        LanguageKind.CSS,     # Webview content styling
        LanguageKind.TSX,     # For React-based webviews
        LanguageKind.JSX,     # For React-based webviews
        LanguageKind.TEXT,    # .vscodeignore, .gitattributes
        LanguageKind.SHELL,   # Build/test scripts
        LanguageKind.POWERSHELL, # Windows scripts
        # LanguageKind.WEBMANIFEST, # if it's a PWA related extension (not standard but seen)
        LanguageKind.SVG,     # Icons
        LanguageKind.DOTENV,
    },
    LanguageWorkspaceGroupKind.BROWSER_EXTENSION: {
        LanguageKind.JAVASCRIPT,
        LanguageKind.TYPESCRIPT,
        LanguageKind.HTML,    # Popup, options page, background page (if HTML)
        LanguageKind.CSS,
        LanguageKind.JSON,    # manifest.json, _locales/*.json
        # LanguageKind.WEBMANIFEST, # (manifest.json is a specific kind of web manifest)
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.YAML,    # Build configs, CI/CD
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.STYLUS,
        LanguageKind.VUE,     # If Vue is used for UI components
        LanguageKind.JSX,
        LanguageKind.TSX,
        LanguageKind.SVELTE,
        LanguageKind.SHELL,   # Build scripts
        LanguageKind.SVG,     # Icons
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.HUGO: {
        LanguageKind.MARKDOWN, # Content files
        LanguageKind.HTML,    # Templates (layouts/, partials/)
        # LanguageKind.GO_TEMPLATE, # (Embedded in HTML)
        LanguageKind.TOML,    # config.toml, hugo.toml, frontmatter
        LanguageKind.YAML,    # config.yaml, frontmatter, data files
        LanguageKind.JSON,    # config.json, frontmatter, data files
        LanguageKind.CSS,
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.JAVASCRIPT, # Custom JS, themes
        LanguageKind.TYPESCRIPT, # If using TS for JS assets
        LanguageKind.SHELL,   # Deployment scripts
        LanguageKind.TEXT,    # .gitattributes, etc.
        LanguageKind.SVG,     # Images/icons
        # LanguageKind.RSS,     # (XML, generated)
        # LanguageKind.ATOM,    # (XML, generated)
        LanguageKind.XML,     # For sitemaps, RSS/Atom (often generated)
    },
    LanguageWorkspaceGroupKind.JEKYLL: {
        LanguageKind.MARKDOWN, # Content files (_posts, pages)
        LanguageKind.HTML,    # Templates (_layouts, _includes)
        LanguageKind.LIQUID_TPL, # Liquid templates (embedded in HTML/Markdown)
        LanguageKind.YAML,    # _config.yml, frontmatter, data files (_data)
        LanguageKind.RUBY,    # Plugins (_plugins), Gemfile
        LanguageKind.GEMFILE, # Gemfile, Gemfile.lock
        LanguageKind.CSS,
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.JAVASCRIPT, # Site interactivity
        LanguageKind.COFFEESCRIPT, # Older Jekyll sites might have it
        LanguageKind.JSON,    # Data files
        LanguageKind.SHELL,   # Deployment scripts
        LanguageKind.TEXT,
        LanguageKind.SVG,
    },
    LanguageWorkspaceGroupKind.DOCUSAURUS: {
        LanguageKind.MARKDOWN, # Documentation files
        # LanguageKind.MDX,     # Markdown with JSX components
        LanguageKind.JAVASCRIPT, # docusaurus.config.js, custom components, swizzled components
        LanguageKind.TYPESCRIPT, # If using TS for config or components
        LanguageKind.JSX,
        LanguageKind.TSX,
        LanguageKind.JSON,    # package.json, sidebars.js (can be JSON), i18n files
        LanguageKind.CSS,     # Styling, Infima CSS variables
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.YAML,    # CI/CD, sometimes for sidebars or plugin config
        LanguageKind.SHELL,   # Deployment scripts
        LanguageKind.SVG,
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.SPHINX_DOCS: {
        LanguageKind.RESTRUCTUREDTEXT, # .rst files (primary)
        LanguageKind.MARKDOWN, # MyST parser allows .md files
        LanguageKind.PYTHON,  # conf.py, custom extensions, doctest snippets
        LanguageKind.JINJA,   # Templates for themes
        LanguageKind.CSS,     # Custom themes, static CSS
        LanguageKind.HTML,    # Generated output, custom static HTML
        LanguageKind.MAKEFILE,# Makefile for building docs (e.g., `make html`)
        LanguageKind.SHELL,   # make.bat, other build scripts
        LanguageKind.BAT,     # make.bat
        LanguageKind.TEXT,    # .nojekyll, various generated files
        LanguageKind.YAML,    # For some sphinx extension configurations
        LanguageKind.JSON,    # For search index, intersphinx inventory
        LanguageKind.JAVASCRIPT, # For themes, search functionality
        LanguageKind.SVG,
    },
    LanguageWorkspaceGroupKind.ELIXIR_MIX: {
        LanguageKind.ELIXIR,  # .ex, .exs files, mix.exs
        # LanguageKind.MIX_EXS, # (mix.exs is Elixir)
        LanguageKind.HTML,    # Phoenix templates (.html.eex, .html.heex, .html.leex)
        # LanguageKind.EEX,     # (Embedded Elixir, used in .eex)
        # LanguageKind.HEEX,    # (HTML-aware EEx, used in .heex)
        # LanguageKind.LEEX,    # (LiveView EEx, used in .leex)
        LanguageKind.JAVASCRIPT, # Phoenix assets (app.js)
        LanguageKind.TYPESCRIPT, # Phoenix assets (if using TS)
        LanguageKind.CSS,     # Phoenix assets (app.css)
        LanguageKind.SASS,    # Phoenix assets
        # LanguageKind.SCSS,
        LanguageKind.JSON,    # Configs, lock files (mix.lock is text but structured)
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.SHELL,   # Scripts
        LanguageKind.TEXT,    # mix.lock
        LanguageKind.SQL,     # Ecto migrations (can contain SQL)
        LanguageKind.ERLANG,  # If using Erlang libraries or writing Erlang modules
    },
    LanguageWorkspaceGroupKind.PHP_COMPOSER: {
        LanguageKind.PHP,
        LanguageKind.JSON,    # composer.json, composer.lock
        LanguageKind.HTML,    # Views (often mixed with PHP)
        LanguageKind.TWIG,    # Symfony/Laravel with Twig templates
        # LanguageKind.BLADE,   # Laravel Blade templates (.blade.php, PHP-like)
        LanguageKind.JAVASCRIPT, # Frontend assets
        LanguageKind.TYPESCRIPT, # Frontend assets
        LanguageKind.CSS,     # Frontend assets
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.XML,     # Configs (e.g., PHPUnit phpunit.xml, DI container XML configs)
        LanguageKind.YAML,    # Configs (e.g., Symfony services.yaml, Doctrine ORM mapping)
        LanguageKind.SQL,     # Migrations, raw SQL
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.SHELL,   # Scripts (bin/console)
        LanguageKind.BAT,
        LanguageKind.DOTENV,  # .env files
        LanguageKind.INI,     # php.ini (though not usually in project repo)
        LanguageKind.APACHECONF, # .htaccess
    },
    LanguageWorkspaceGroupKind.SBT: {
        LanguageKind.SCALA,   # .scala source files, .sbt build files
        LanguageKind.JAVA,    # Mixed Java/Scala projects
        LanguageKind.TEXT,    # build.sbt (Scala syntax), project/*.scala
        LanguageKind.PROPERTIES, # project/build.properties
        LanguageKind.JSON,    # Configs
        LanguageKind.XML,     # Configs (e.g. logback.xml)
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,   # sbt wrapper script
        LanguageKind.BAT,     # sbt wrapper script (Windows)
    },
    LanguageWorkspaceGroupKind.LEININGEN: {
        LanguageKind.CLOJURE, # project.clj (Clojure data), .clj, .cljc source files
        LanguageKind.CLOJURESCRIPT, # .cljs, .cljc source files
        # LanguageKind.EDN,     # project.clj is EDN, other configs (transit, etc.)
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,    # Configs
        LanguageKind.YAML,    # Configs (e.g. for deployment)
        LanguageKind.SHELL,   # lein wrapper script, helper scripts
        LanguageKind.BAT,     # lein wrapper script (Windows)
        LanguageKind.TEXT,    # profiles.clj (EDN)
        LanguageKind.HTML,    # If web development (e.g. with Hiccup, Reagent)
        LanguageKind.CSS,
        LanguageKind.JAVASCRIPT, # For ClojureScript interop or frontend assets
    },
    LanguageWorkspaceGroupKind.CLOJURE: { # deps.edn
        LanguageKind.CLOJURE, # deps.edn (EDN format), .clj, .cljc source files
        LanguageKind.CLOJURESCRIPT, # .cljs, .cljc source files
        # LanguageKind.EDN,     # deps.edn, other configs
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,    # Configs
        LanguageKind.YAML,    # Configs
        LanguageKind.SHELL,   # clj/clojure wrapper script, helper scripts
        LanguageKind.BAT,     # clj/clojure wrapper script (Windows)
        LanguageKind.TEXT,    # Aliases in deps.edn
        LanguageKind.HTML,
        LanguageKind.CSS,
        LanguageKind.JAVASCRIPT,
    },
    LanguageWorkspaceGroupKind.HASKELL_STACK: {
        LanguageKind.HASKELL, # .hs, .lhs source files
        LanguageKind.YAML,    # stack.yaml, package.yaml (hpack)
        LanguageKind.CABAL,   # Generated .cabal file (from package.yaml), or manual .cabal
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,   # Build scripts, hooks
        LanguageKind.TEXT,
        LanguageKind.C,       # FFI
    },
    LanguageWorkspaceGroupKind.HASKELL_CABAL: {
        LanguageKind.HASKELL, # .hs, .lhs source files
        LanguageKind.CABAL,   # .cabal files, cabal.project, cabal.project.freeze
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,   # Build scripts (Setup.hs can be complex)
        LanguageKind.TEXT,    # Cabal file format itself
        LanguageKind.C,       # FFI
        LanguageKind.MAKEFILE, # Sometimes used to wrap cabal commands
    },
    LanguageWorkspaceGroupKind.PERL: {
        LanguageKind.PERL,    # .pl, .pm, .t, .pod
        # LanguageKind.POD,     # (Embedded in Perl or separate .pod files)
        LanguageKind.MAKEFILE,# Makefile.PL (Perl script) generates a Makefile
        LanguageKind.SHELL,   # Scripts
        LanguageKind.YAML,    # META.yml, cpanfile (sometimes)
        LanguageKind.JSON,    # META.json
        LanguageKind.MARKDOWN, # README.md
        LanguageKind.TEXT,    # Build.PL (Perl script), cpanfile
        LanguageKind.C,       # XS modules
        LanguageKind.XML,     # For some testing tools or configs
    },
    LanguageWorkspaceGroupKind.DUNE: {
        LanguageKind.OCAML,   # .ml, .mli
        LanguageKind.REASONML, # .re, .rei
        LanguageKind.TEXT,    # dune, dune-project, dune-workspace files (S-expression like)
        # LanguageKind.LISP,    # Dune files are S-expressions
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,
        LanguageKind.C,       # For C stubs
    },
    LanguageWorkspaceGroupKind.IDRIS: {
        LanguageKind.IDRIS,   # .idr, .lidr
        LanguageKind.TEXT,    # .ipkg files (custom format, key-value pairs)
        LanguageKind.MAKEFILE, # For building, testing
        LanguageKind.SHELL,
        LanguageKind.MARKDOWN,
        LanguageKind.C,       # For FFI code generated or linked
    },
    LanguageWorkspaceGroupKind.PURESCRIPT_SPAGO: {
        LanguageKind.PURESCRIPT, # .purs
        LanguageKind.DHALL,   # spago.dhall, packages.dhall
        LanguageKind.JSON,    # Output from compiler, configs
        LanguageKind.MARKDOWN,
        LanguageKind.JAVASCRIPT, # Compiled output, FFI
        LanguageKind.SHELL,
        LanguageKind.MAKEFILE,
    },
    LanguageWorkspaceGroupKind.NIMBLE: {
        LanguageKind.NIM,     # .nim, .nims source files, .nimble (NimScript)
        # LanguageKind.NIMSCRIPT, # .nimble files are NimScript - (NIM should cover this)
        LanguageKind.JSON,    # .nimble.lock, other JSON configs
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,
        LanguageKind.TOML,    # config.nims can be TOML
        LanguageKind.INI,     # config.nims can be INI
        LanguageKind.TEXT,
    },
    LanguageWorkspaceGroupKind.ELECTRON: {
        LanguageKind.JAVASCRIPT, # Main process, renderer process
        LanguageKind.TYPESCRIPT, # If using TS
        LanguageKind.HTML,    # Renderer process UI
        LanguageKind.CSS,     # Renderer process UI styling
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.JSON,    # package.json, other configs
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.JSX,     # If using React/Vue in renderer
        LanguageKind.TSX,
        LanguageKind.VUE,
        LanguageKind.SVELTE,
        LanguageKind.C,       # Native modules
        LanguageKind.CPP,     # Native modules
        LanguageKind.OBJECTIVEC, # Native modules (macOS)
        LanguageKind.SWIFT,   # Native modules (macOS)
        LanguageKind.RUST,    # Native modules (e.g. Neon)
        LanguageKind.PYTHON,  # For build tools or scripts
        LanguageKind.SHELL,   # Build/packaging scripts
        # LanguageKind.NATIVE_ASSEMBLY, # If very low level modules (rare) - (use ASSEMBLY)
        LanguageKind.ASSEMBLY,
        LanguageKind.DOTENV,
    },
    LanguageWorkspaceGroupKind.BAZEL: {
        LanguageKind.STARLARK, # BUILD, .bzl, WORKSPACE, MODULE.bazel files
        LanguageKind.PYTHON,  # Often used for rules implementation or as a target lang
        LanguageKind.CPP,     # Target language
        LanguageKind.C,       # Target language
        LanguageKind.JAVA,    # Target language
        LanguageKind.KOTLIN,  # Target language
        LanguageKind.SCALA,   # Target language
        LanguageKind.GO,      # Target language
        LanguageKind.RUST,    # Target language
        LanguageKind.SWIFT,   # Target language
        LanguageKind.OBJECTIVEC, # Target language
        LanguageKind.JAVASCRIPT, # Target language (e.g. rules_js)
        LanguageKind.TYPESCRIPT, # Target language
        LanguageKind.PROTOBUF, # .proto files are common with Bazel
        LanguageKind.SHELL,   # For genrules, sh_binary, sh_test
        LanguageKind.TEXT,    # Various config files, e.g. .bazelrc
        LanguageKind.MARKDOWN,
        LanguageKind.JSON,
        LanguageKind.XML,
    },
    LanguageWorkspaceGroupKind.QUARTO: {
        LanguageKind.MARKDOWN, # .qmd files
        LanguageKind.YAML,    # _quarto.yml, frontmatter in .qmd
        LanguageKind.PYTHON,  # Jupyter engine: Python code chunks
        LanguageKind.R,       # Knitr engine: R code chunks
        LanguageKind.JULIA,   # Julia code chunks
        # LanguageKind.OBSERVABLE_JS, # Observable JS chunks - (use JAVASCRIPT)
        LanguageKind.JAVASCRIPT, # Observable JS chunks, custom JS for HTML output
        LanguageKind.HTML,    # Output format, custom templates
        LanguageKind.CSS,     # Styling, custom themes
        # LanguageKind.SCSS,    # If using SCSS for themes
        LanguageKind.SASS,
        LanguageKind.LATEX,   # For PDF output, custom LaTeX templates, raw LaTeX chunks
        LanguageKind.LUA,     # Lua filters
        LanguageKind.JSON,    # Metadata, citation files (.citeproc.json)
        LanguageKind.BIBTEX,  # .bib files for citations
        LanguageKind.SHELL,   # For pre/post render scripts
        LanguageKind.TEXT,
        LanguageKind.SVG,
    },
    LanguageWorkspaceGroupKind.PLAIN: {
        LanguageKind.TEXT,
        LanguageKind.MARKDOWN,
        LanguageKind.CSV,
        LanguageKind.TSV,
        LanguageKind.JSON,    # Simple data files
        LanguageKind.XML,     # Simple data files
        LanguageKind.YAML,    # Simple data files, notes
        LanguageKind.SHELL,   # Incidental scripts
        LanguageKind.PYTHON,  # Incidental scripts
        LanguageKind.ASCIIDOC,
        LanguageKind.ORGMODE,
        LanguageKind.RESTRUCTUREDTEXT,
        LanguageKind.LATEX,   # If it's just a collection of .tex files without a formal project structure
        LanguageKind.DOT,     # Graphviz for diagrams
        LanguageKind.MERMAID, # Mermaid diagrams in Markdown
        LanguageKind.PLANTUML, # PlantUML diagrams
        LanguageKind.SVG,
    },
    LanguageWorkspaceGroupKind.SQL: {
        LanguageKind.SQL,     # Core DDL, DML, query files
        LanguageKind.PLSQL,   # Oracle specific SQL procedural language
        LanguageKind.TSQL,    # SQL Server specific SQL procedural language
        LanguageKind.PYTHON,  # Migration tools (Alembic, Django migrations), scripting
        LanguageKind.RUBY,    # Migration tools (Rails migrations), scripting
        LanguageKind.JAVA,    # Migration tools (Flyway, Liquibase), scripting
        LanguageKind.KOTLIN,  # With tools like Flyway/Liquibase using Kotlin
        LanguageKind.GROOVY,  # With tools like Flyway/Liquibase using Groovy
        LanguageKind.JAVASCRIPT, # Migration tools (Knex.js), scripting
        LanguageKind.TYPESCRIPT, # Migration tools, scripting
        LanguageKind.PHP,     # Migration tools (Phinx, Laravel migrations)
        LanguageKind.XML,     # Liquibase changelogs, other DB tool configs
        LanguageKind.JSON,    # Configs, data seeding
        LanguageKind.YAML,    # Database configs, Ansible playbooks for DB setup
        LanguageKind.SHELL,   # DB CLI scripts, backup/restore scripts
        LanguageKind.BAT,
        LanguageKind.CSHARP,  # Entity Framework migrations, scripting with C#
        LanguageKind.FSHARP,  # For DB scripting/migrations
        LanguageKind.PERL,    # DBI scripts
        LanguageKind.MARKDOWN, # Documentation for schema/migrations
        LanguageKind.TEXT,
        LanguageKind.CYPHER, # If it's a Neo4j project
        LanguageKind.GRAPHQL, # If defining GraphQL views over SQL
    },
    LanguageWorkspaceGroupKind.VIM: {
        LanguageKind.VIML,    # .vim, .vimrc, init.vim
        LanguageKind.LUA,     # Neovim configs (init.lua), plugins
        LanguageKind.PYTHON,  # Plugins with Python support (pynvim)
        LanguageKind.RUBY,    # Plugins with Ruby support
        LanguageKind.PERL,    # Plugins with Perl support
        LanguageKind.SHELL,   # Helper scripts, plugin installers
        LanguageKind.MARKDOWN, # README for plugins, personal notes on config
        LanguageKind.JSON,    # LSP settings (coc-settings.json), other plugin configs
        LanguageKind.TOML,    # Some plugin configs (e.g. dein.toml)
        LanguageKind.YAML,    # Some plugin configs
        LanguageKind.TEXT,
        # LanguageKind.FEN,     # For plugins dealing with chess (not a lang kind)
    },
    LanguageWorkspaceGroupKind.JAVA: { # Java without Maven/Gradle/Ant
        LanguageKind.JAVA,
        LanguageKind.TEXT,    # MANIFEST.MF for JARs, simple configs
        LanguageKind.SHELL,   # Compile/run scripts (javac, java commands)
        LanguageKind.BAT,     # Compile/run scripts on Windows
        LanguageKind.MARKDOWN, # README
        LanguageKind.PROPERTIES, # Simple config files
        LanguageKind.JSON,    # Simple data/config files
        LanguageKind.XML,     # Simple data/config files
        LanguageKind.MAKEFILE, # If using a simple Makefile to compile
    },
    LanguageWorkspaceGroupKind.ADOBE_FLASH_FLEX: {
        LanguageKind.ACTIONSCRIPT, # .as files
        LanguageKind.MXML,    # .mxml files (Flex)
        LanguageKind.XML,     # .actionScriptProperties, .project (Flash Builder), Flex config files
        LanguageKind.CSS,     # Styling in Flex applications
        LanguageKind.HTML,    # Wrapper HTML for Flash/Flex content
        LanguageKind.JAVASCRIPT, # For interaction with HTML wrapper (ExternalInterface)
        LanguageKind.TEXT,
        LanguageKind.SHELL,   # Build scripts if using command-line compilers (Flex SDK)
    },
    LanguageWorkspaceGroupKind.COLDFUSION: {
        LanguageKind.CFML,    # .cfm, .cfc files
        LanguageKind.HTML,    # Often mixed with CFML tags
        LanguageKind.CSS,
        LanguageKind.JAVASCRIPT,
        LanguageKind.SQL,     # Embedded in <cfquery> or separate .sql files
        LanguageKind.JSON,    # .cfconfig.json (Lucee/Adobe CF2016+), other JSON data
        LanguageKind.XML,     # Older configs (Application.xml), component metadata
        LanguageKind.TEXT,    # Application.cfc (CFML syntax)
        LanguageKind.MARKDOWN,
        LanguageKind.SHELL,
        LanguageKind.JAVA,    # If using Java libraries or creating Java extensions for CF
    },
    LanguageWorkspaceGroupKind.SVELTE: {
        LanguageKind.SVELTE,  # .svelte files
        LanguageKind.JAVASCRIPT, # .js files, logic within <script> tags
        LanguageKind.TYPESCRIPT, # .ts files, logic within <script lang="ts">
        LanguageKind.HTML,    # Structure within .svelte files (superset of HTML)
        LanguageKind.CSS,     # Styling within <style> tags or .css files
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.STYLUS,
        LanguageKind.POSTCSS, # Often used with Svelte
        LanguageKind.JSON,    # package.json, tsconfig.json, svelte.config.js (if module.exports style)
        LanguageKind.MARKDOWN, # README, docs (e.g. SvelteKit uses MD for routes)
        # LanguageKind.MDX,     # SvelteKit can use MDsveX
        LanguageKind.SHELL,   # Scripts
        LanguageKind.SVG,
        LanguageKind.DOTENV,
    },
    LanguageWorkspaceGroupKind.REACT: {
        LanguageKind.JAVASCRIPT,
        LanguageKind.TYPESCRIPT,
        LanguageKind.JSX,
        LanguageKind.TSX,
        LanguageKind.HTML,    # index.html shell, public assets
        LanguageKind.CSS,
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.STYLUS,
        LanguageKind.POSTCSS,
        LanguageKind.JSON,    # package.json, tsconfig.json, .eslintrc.json, etc.
        LanguageKind.MARKDOWN, # README, docs
        # LanguageKind.MDX,     # For documentation (Storybook, Next.js MDX pages)
        LanguageKind.GRAPHQL, # If using GraphQL client (Apollo, Relay)
        LanguageKind.SHELL,   # Scripts
        LanguageKind.SVG,
        LanguageKind.DOTENV,
        LanguageKind.TEXT,    # .env files, various ignore files
        LanguageKind.YAML,    # CI/CD configs
    },
    LanguageWorkspaceGroupKind.ANGULAR: {
        LanguageKind.TYPESCRIPT, # Primary language
        LanguageKind.HTML,    # Templates (.html)
        LanguageKind.CSS,     # Styles (.css)
        LanguageKind.SASS,
        # LanguageKind.SCSS,    # Styles (.scss)
        LanguageKind.LESS,    # Styles (.less)
        LanguageKind.STYLUS,  # Styles (.styl)
        LanguageKind.JSON,    # angular.json, package.json, tsconfig.json, tslint.json, .eslintrc.json
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.JAVASCRIPT, # Config files (karma.conf.js, protractor.conf.js - though often TS now)
        LanguageKind.SHELL,   # Scripts
        LanguageKind.SVG,
        LanguageKind.TEXT,    # .browserslistrc, .editorconfig
        LanguageKind.YAML,    # CI/CD configs
        LanguageKind.DOTENV,
    },
    LanguageWorkspaceGroupKind.DART: { # Generic Dart, not Flutter
        LanguageKind.DART,
        LanguageKind.YAML,    # pubspec.yaml, analysis_options.yaml
        LanguageKind.MARKDOWN, # README, CHANGELOG, examples
        LanguageKind.SHELL,   # Scripts (e.g., tool/
        LanguageKind.JSON,    # Configs (e.g., .vscode/launch.json)
        LanguageKind.TEXT,    # .gitignore, .pubignore
        LanguageKind.C,       # For FFI
        LanguageKind.CPP,     # For FFI
        LanguageKind.OBJECTIVEC, # For FFI
        LanguageKind.SWIFT,   # For FFI
        LanguageKind.RUST,    # For FFI
        LanguageKind.MAKEFILE, # For building native parts via FFI
    },
    LanguageWorkspaceGroupKind.DOTNET: {
        LanguageKind.CSHARP,  # .cs, .cshtml, .razor
        LanguageKind.FSHARP,  # .fs, .fsi, .fsx
        LanguageKind.VBNET,   # .vb
        LanguageKind.XML,     # .csproj, .fsproj, .vbproj, .sln (structure), app.config, web.config, .nuspec, .props, .targets, ResX, XAML, .runsettings
        LanguageKind.XAML,    # WPF, UWP, Xamarin.Forms, MAUI
        LanguageKind.JSON,    # appsettings.json, project.json (legacy), launchSettings.json, global.json, NuGet.config (can be json)
        LanguageKind.TEXT,    # .sln (file format), .editorconfig, .gitattributes, .gitignore
        LanguageKind.RAZOR,   # .cshtml, .razor (ASP.NET Core, Blazor)
        LanguageKind.HTML,    # Used with Razor, or static content
        LanguageKind.CSS,
        LanguageKind.JAVASCRIPT, # Frontend for web apps, Blazor interop
        LanguageKind.TYPESCRIPT, # Frontend for web apps
        LanguageKind.SASS,
        # LanguageKind.SCSS,
        LanguageKind.LESS,
        LanguageKind.SQL,     # Entity Framework migrations, .sql files
        LanguageKind.MARKDOWN, # README, docs
        LanguageKind.POWERSHELL, # Build/deploy scripts, .ps1
        LanguageKind.SHELL,   # Build/deploy scripts (bash, zsh for non-Windows)
        LanguageKind.BAT,     # .bat, .cmd scripts
        LanguageKind.CPP,     # C++/CLI projects (.vcxproj), native interop
        LanguageKind.C,       # Native interop
        LanguageKind.CIL,     # .il (MSIL, for inspection or advanced interop)
        LanguageKind.PROPERTIES, # .settings files (legacy), resource files
        LanguageKind.EDITORCONFIG, # .editorconfig
        LanguageKind.HLSL,    # Shaders for DirectX related dev
        LanguageKind.GLSL,    # Shaders for OpenGL related dev
        LanguageKind.DOTENV,  # .env files (less common but can be used)
        LanguageKind.HANDLEBARS, # Some templating engines
        LanguageKind.MUSTACHE, # Some templating engines
        LanguageKind.INI,     # Some legacy config patterns
        LanguageKind.WINDOWS_REGISTRY, # .reg files if project involves registry manipulation


        # .config files (XML)
    },
}

