from typing import Dict, Tuple, List, Optional, Set

from minir_datastructs.enum.enum_string_aliases_description import EnumStringAliasesDescription



class LanguageKind(EnumStringAliasesDescription):
    _INTERNAL_NONE = "none", -1, "none", "Internal placeholder for no specific language"
    TEXT = "text", 0, "text,txt,plaintext", "Plain text, no specific syntax"
    UNKNOWN = "unknown", 999, "unknown", "Language could not be identified"
    TEST_LANG = "testlang", 1, "unknown", "Language could not be identified"

    ASSEMBLY = "assembly", 10, "assembly,asm,nasm", "Low-level programming language for a computer or other programmable device specific to a particular computer architecture"
    BASH = "bash", 11, "bash", "Bourne Again SHell, a Unix shell and command language"
    CSHARP = "csharp", 15, "csharp,cs,c#", "Multi-paradigm programming language developed by Microsoft"
    C = "c", 12, "c", "General-purpose, procedural computer programming language"
    CLOJURE = "clojure", 13, "clojure,clj", "Dynamic, general-purpose programming language, combining the approachability and interactive development of a scripting language with an efficient and robust infrastructure for multithreaded programming"
    CPP = "cpp", 14, "cpp,c++,cc,cxx,hpp,hxx,h", "General-purpose programming language created as an extension of the C programming language, or C with Classes"
    CSS = "css", 16, "css", "Cascading Style Sheets, a style sheet language used for describing the presentation of a document written in a markup language like HTML"
    DART = "dart", 17, "dart", "Programming language designed for client development, such as for the web and mobile apps"
    DIFF = "diff", 18, "diff,patch", "Data comparison utility that outputs the differences between two files"
    DOCKERFILE = "dockerfile", 19, "dockerfile,docker,Dockerfile", "Text document that contains all the commands a user could call on the command line to assemble an image"
    DOT = "dot", 20, "dot,graphviz", "Graph description language used by Graphviz"
    ELIXIR = "elixir", 21, "elixir,ex,exs", "Dynamic, functional language designed for building scalable and maintainable applications"
    FSHARP = "fsharp", 22, "fsharp,fs,f#", "Functional-first, general purpose, strongly typed, multi-paradigm programming language that encompasses functional, imperative, and object-oriented programming methods"
    GO = "go", 23, "go,golang", "Statically typed, compiled programming language designed at Google"
    GRAPHQL = "graphql", 24, "graphql,gql", "Query language for APIs and a server-side runtime for executing queries by using a type system you define for your data"
    HASKELL = "haskell", 25, "haskell,hs,lhs", "Statically typed, purely functional programming language with type inference and lazy evaluation"
    HTML = "html", 26, "html,htm", "HyperText Markup Language, the standard markup language for documents designed to be displayed in a web browser"
    JAVA = "java", 27, "java", "Class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible"
    JAVASCRIPT = "javascript", 28, "javascript,js,mjs,cjs,node", "High-level, often just-in-time compiled, and multi-paradigm programming language that conforms to the ECMAScript specification"
    JSON = "json", 29, "json,jsonc", "JavaScript Object Notation, an open standard file format and data interchange format that uses human-readable text to store and transmit data objects"
    JSX = "jsx", 30, "jsx", "Syntax extension for JavaScript, often used with React to describe what the UI should look like"
    KOTLIN = "kotlin", 31, "kotlin,kt,kts", "Cross-platform, statically typed, general-purpose programming language with type inference"
    LESS = "less", 32, "less", "Dynamic preprocessor style sheet language that can be compiled into Cascading Style Sheets (CSS)"
    LUA = "lua", 33, "lua", "Lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications"
    MARKDOWN = "markdown", 34, "markdown,md,mkd,mdwn,mdown,mdx", "Lightweight markup language for creating formatted text using a plain-text editor"
    MERMAID = "mermaid", 35, "mermaid,mmd", "JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions to create and modify diagrams dynamically"
    OBJECTIVEC = "objectivec", 36, "objectivec,objc,obj-c,objective-c,m,mm,h", "General-purpose, object-oriented programming language that adds Smalltalk-style messaging to the C programming language"
    OCAML = "ocaml", 37, "ocaml,ml,mli", "General-purpose, multi-paradigm programming language which extends the Caml dialect of ML with object-oriented features"
    PERL = "perl", 38, "perl,pl,pm,t", "Family of two high-level, general-purpose, interpreted, dynamic programming languages"
    PHP = "php", 39, "php,php3,php4,php5,phtml", "General-purpose scripting language especially suited to web development"
    PLANTUML = "plantuml", 40, "plantuml,puml,pu,plant", "Open-source tool allowing users to create UML diagrams from a simple textual description language"
    POWERSHELL = "powershell", 41, "powershell,ps1,psm1,psd1,pwsh", "Task automation and configuration management framework from Microsoft, consisting of a command-line shell and associated scripting language"
    PYTHON = "python", 42, "python,py,py3,pyw,ipynb,python3", "Interpreted, high-level and general-purpose programming language"
    PYTHONREPL = "pythonrepl", 43, "pythonrepl,pycon,python_repl", "Python Read-Eval-Print Loop session or console interaction"
    R = "r", 44, "r,R", "Programming language and free software environment for statistical computing and graphics"
    RUBY = "ruby", 45, "ruby,rb,rbw,rake,gemspec", "Interpreted, high-level, general-purpose programming language"
    RUST = "rust", 46, "rust,rs", "Multi-paradigm systems programming language focused on safety, especially safe concurrency"
    SASS = "sass", 47, "sass,scss", "Preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS). SCSS is a superset of CSS."
    SCALA = "scala", 48, "scala,sc", "Strongly statically typed, high-level language that combines object-oriented and functional programming"
    SHELL = "shell", 49, "shell,sh,bash,zsh,ksh,tcsh,ash,dash,fish,console,session", "Command-line interpreter or shell script, providing a user interface for access to an operating system's services"
    SQL = "sql", 50, "sql,ddl,dml", "Structured Query Language, a domain-specific language used in programming and designed for managing data held in a relational database management system"
    SWIFT = "swift", 51, "swift", "General-purpose, multi-paradigm, compiled programming language developed by Apple Inc."
    TERRAFORM = "terraform", 52, "terraform,tf,tfvars,hcl", "Open-source infrastructure as code software tool created by HashiCorp"
    TSX = "tsx", 53, "tsx", "Syntax extension for TypeScript, similar to JSX for JavaScript, used with React and TypeScript"
    TYPESCRIPT = "typescript", 54, "typescript,ts,mts,cts", "Programming language developed by Microsoft which is a strict syntactical superset of JavaScript and adds optional static typing"
    VBNET = "vbnet", 55, "vbnet,vb.net,vb,visualbasic", "Visual Basic .NET, a multi-paradigm, object-oriented programming language, implemented on the .NET Framework"
    VUE = "vue", 56, "vue", "Single-file components for Vue.js, a progressive framework for building user interfaces"
    XML = "xml", 57, "xml,xsd,xsl,xslt,rss,atom,kml,svg,plist", "Extensible Markup Language, a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable"
    YAML = "yaml", 58, "yaml,yml", "Human-readable data-serialization language, often used for configuration files and in applications where data is being stored or transmitted"
    BAT = "bat", 59, "bat,batch,cmd", "Batch file, a script file in DOS, OS/2 and Microsoft Windows"

    ADA = "ada", 60, "ada,ada,adb,ads", "Structured, statically typed, imperative, and object-oriented high-level computer programming language"
    COBOL = "cobol", 61, "cobol,cob,cbl,cpy", "Common Business-Oriented Language, a compiled English-like computer programming language designed for business use"
    ERLANG = "erlang", 62, "erlang,erl,hrl", "General-purpose, concurrent, functional programming language, and a garbage-collected runtime system"
    FORTRAN = "fortran", 63, "fortran,f,f77,f90,f95,f03,f08,for", "General-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing"
    GROOVY = "groovy", 64, "groovy,groovy,gvy,gy,gsh", "Java-syntax-compatible object-oriented programming language for the Java platform"
    JULIA = "julia", 65, "julia,jl", "High-level, high-performance, dynamic programming language for technical computing"
    COMMON_LISP = "common_lisp", 66, "common_lisp,lisp,cl,l,lsp,fasl", "Dialect of the Lisp programming language, published in ANSI standard document ANSI INCITS 226-1994"
    SCHEME = "scheme", 67, "scheme,scm,ss", "Multi-paradigm programming language, one of the two main dialects of Lisp"
    MATLAB = "matlab", 68, "matlab,m", "Proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks"
    PASCAL = "pascal", 69, "pascal,pas,pp,p,inc", "Imperative and procedural programming language, designed for teaching structured programming and data structuring"
    PROLOG = "prolog", 70, "prolog,pl,pro,P", "Logic programming language associated with artificial intelligence and computational linguistics"
    RACKET = "racket", 71, "racket,rkt,rktl,scrbl", "General-purpose, multi-paradigm programming language based on the Scheme dialect of Lisp"
    SMALLTALK = "smalltalk", 72, "smalltalk,st", "Object-oriented, dynamically typed reflective programming language"
    TCL = "tcl", 73, "tcl,tcl,tk,itk", "Tool Command Language, a high-level, general-purpose, interpreted, dynamic programming language"
    VERILOG = "verilog", 74, "verilog,v", "Hardware description language (HDL) used to model electronic systems"
    VHDL = "vhdl", 75, "vhdl,vhd,vhdl", "VHSIC (Very High Speed Integrated Circuit) Hardware Description Language, a hardware description language used in electronic design automation"
    AWK = "awk", 76, "awk,awk,gawk,mawk,nawk", "Domain-specific language designed for text processing and typically used as a data extraction and reporting tool"
    AUTOHOTKEY = "autohotkey", 77, "autohotkey,ahk", "Free, open-source custom scripting language for Microsoft Windows"
    APPLESCRIPT = "applescript", 78, "applescript,scpt,scptd,applescript", "Scripting language created by Apple Inc. that facilitates automated control over scriptable Mac applications"
    ASCIIDOC = "asciidoc", 79, "asciidoc,adoc,asc", "Human-readable document format, semantically equivalent to DocBook XML, but using a plain-text markup syntax"
    RESTRUCTUREDTEXT = "restructuredtext", 80, "restructuredtext,rst,rest", "File format for textual data used primarily in the Python programming language community for technical documentation"
    LATEX = "latex", 81, "latex,tex,ltx,cls,sty,dtx,ins", "Software system for document preparation, widely used for scientific and technical documents"
    TEX_PLAIN = "tex_plain", 82, "tex_plain,tex,plain_tex", "Plain TeX, the basic TeX typesetting system"
    ORGMODE = "org", 83, "org,org,org_mode", "Document editing, formatting, and organizing mode, designed for notes, planning, and authoring within the free software text editor Emacs"
    TOML = "toml", 84, "toml,toml", "Tom's Obvious, Minimal Language, a configuration file format designed to be easy to read due to its simple semantics"
    PROTOBUF = "protobuf", 85, "protobuf,proto", "Protocol Buffers, a free and open-source cross-platform data format used to serialize structured data"
    CSV = "csv", 86, "csv,csv", "Comma-Separated Values, a delimited text file that uses a comma to separate values"
    TSV = "tsv", 87, "tsv,tsv", "Tab-Separated Values, a delimited text file that uses a tab to separate values"
    BSON = "bson", 88, "bson,bson", "Binary JSON, a computer data interchange format used mainly as a data storage and network transfer format in the MongoDB database"
    INI = "ini", 89, "ini,ini,cfg,conf,prefs,properties,desktop,directory,gitconfig", "Configuration file format for computer software that consists of a text-based content with a structure and syntax comprising key-value pairs for properties, and sections that organize the properties"
    DOTENV = "dotenv", 90, "dotenv,dotenv,.env", "File format for storing environment variables as plain text"
    NGINX = "nginx", 91, "nginx,nginx.conf,conf", "Configuration file format for Nginx, a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache"
    APACHECONF = "apacheconf", 92, "apacheconf,httpd.conf,.htaccess,conf", "Configuration file format for the Apache HTTP Server"
    HOCON = "hocon", 93, "hocon,hocon,conf", "Human-Optimized Config Object Notation, a superset of JSON, intended to be more human-readable"
    CYPHER = "cypher", 94, "cypher,cql,cypher", "Declarative graph query language that allows for expressive and efficient data querying in a property graph"
    SPARQL = "sparql", 95, "sparql,rq,sparql", "SPARQL Protocol and RDF Query Language, an RDF query language—that is, a semantic query language for databases—able to retrieve and manipulate data stored in Resource Description Framework (RDF) format"
    JINJA = "jinja", 96, "jinja,jinja,jinja2,j2", "Modern and designer-friendly templating language for Python, modelled after Django’s templates"
    HANDLEBARS = "handlebars", 97, "handlebars,hbs,handlebars", "Semantic web template system, a superset of Mustache"
    MUSTACHE = "mustache", 98, "mustache,mustache,mst", "Logic-less template syntax, can be used for HTML, config files, source code – anything"
    EJS = "ejs", 99, "ejs,ejs", "Embedded JavaScript templating; a simple templating language that lets you generate HTML markup with plain JavaScript"
    GLSL = "glsl", 100, "glsl,glsl,vert,frag,geom,tesc,tese,comp,glslf,vs,fs,gs,tcs,tes,cs", "OpenGL Shading Language, a high-level shading language with a syntax based on the C programming language"
    HLSL = "hlsl", 101, "hlsl,hlsl,fx,fxh,vsh,psh,gsh,hsh,dsh,csh", "High-Level Shading Language for DirectX, a proprietary shading language developed by Microsoft"
    CMAKE = "cmake", 102, "cmake,cmake,CMakeLists.txt", "Cross-platform free and open-source software tool for managing the build process of software using a compiler-independent method"
    MAKEFILE = "makefile", 103, "makefile,Makefile,makefile,GNUmakefile,GNUMakefile,bsdmakefile,mk,mak", "File (by default named Makefile) containing a set of directives used by a make build automation tool to generate a target/goal"
    GRADLE = "gradle", 104, "gradle,gradle,gradle.kts", "Build automation tool for multi-language software development, primarily used for Java, Kotlin, and Groovy projects"
    BIBTEX = "bibtex", 105, "bibtex,bib", "Reference management software for formatting lists of references, often used with LaTeX"
    PROPERTIES = "properties", 106, "properties,properties", ".properties file format, primarily used in Java related technologies to store configuration parameters"
    SOLIDITY = "solidity", 107, "solidity,sol", "Object-oriented programming language for writing smart contracts, primarily on Ethereum"
    SYSTEMVERILOG = "systemverilog", 108, "systemverilog,sv,svh,svi", "Hardware description and hardware verification language used to model, design, simulate, test and implement electronic systems"
    JSON5 = "json5", 109, "json5,json5", "Proposed extension to JSON that aims to make it easier for humans to write and maintain by hand"
    TEXTPROTO = "textproto", 110, "textproto,textpb,pb.txt,pbtxt", "Text format for Google's Protocol Buffers"
    KCONFIG = "kconfig", 111, "kconfig,Kconfig,defconfig", "Language and set of tools used for configuring Linux kernel options and other software projects"
    ARDUINO = "arduino", 112, "arduino,ino", "Programming language for Arduino microcontrollers, based on C/C++"
    CUDA = "cuda", 113, "cuda,cu,cuh", "Parallel computing platform and application programming interface (API) model created by Nvidia"
    SVELTE = "svelte", 114, "svelte,svelte", "Component framework that compiles HTML, CSS, and JavaScript into efficient imperative code"
    ZIG = "zig", 115, "zig,zig", "General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software"
    NIM = "nim", 116, "nim,nim,nims", "Statically typed, imperative programming language that tries to give the programmer ultimate power without compromises on runtime efficiency"
    CRYSTAL = "crystal", 117, "crystal,cr", "General-purpose, object-oriented programming language, with static type-checking but no need to specify types of variables or method arguments"
    HAXE = "haxe", 118, "haxe,hx", "High-level cross-platform multi-paradigm programming language and compiler"
    PUG = "pug", 119, "pug,pug,jade", "High-performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers (formerly Jade)"
    SLIM_TPL = "slim_tpl", 120, "slim_tpl,slim", "Slim is a template language whose goal is to reduce the view syntax to the essential parts without becoming cryptic"
    HAML = "haml", 121, "haml,haml", "HTML Abstraction Markup Language, a templating system that is designed to avoid writing inline code in a web document and to make the HTML cleaner"
    MAKO = "mako", 122, "mako,mako,mao", "Template library written in Python, providing a familiar, non-XML syntax which compiles into Python modules for maximum performance"
    SMARTY_TPL = "smarty_tpl", 123, "smarty_tpl,tpl", "Web template system written in PHP"
    XSLT_LANG = "xslt_lang", 124, "xslt_lang,xslt,xsl", "XSL Transformations, a language for transforming XML documents into other XML documents, or other formats such as HTML for web pages, plain text or XSL Formatting Objects"
    WREN = "wren", 125, "wren,wren", "Small, fast, class-based concurrent scripting language"
    AUGEAS = "augeas", 126, "augeas,aug", "Configuration editing tool. It parses configuration files in their native formats and transforms them into a tree"
    STAN = "stan", 127, "stan,stan", "Probabilistic programming language for statistical modeling, data analysis, and prediction"
    THRIFT = "thrift", 128, "thrift,thrift", "Interface definition language and binary communication protocol used for defining and creating services for numerous languages"
    EDGEQL = "edgeql", 129, "edgeql,esdl,edgeql", "Query language for EdgeDB, a next-generation graph-relational database"
    REGO = "rego", 130, "rego,rego", "Policy language used by Open Policy Agent (OPA)"
    GRAPHQL_SCHEMA = "graphqls", 131, "graphqls,graphqls,graphql_schema,gqls,sdl", "GraphQL Schema Definition Language (SDL), used to define the types and relationships in a GraphQL API"
    CADDYFILE = "caddyfile", 132, "caddyfile", "Configuration file format for the Caddy web server"
    EDITORCONFIG = "editorconfig", 133, "editorconfig,.editorconfig", ".editorconfig files used to define and maintain consistent coding styles between different editors and IDEs"
    HAR = "har", 134, "har,har", "HTTP Archive format, a JSON-formatted archive file format for logging of a web browser's interaction with a site"
    WEBASSEMBLY_TEXT = "wat", 135, "wat,wast,wat,webassembly_text", "WebAssembly Text Format (WAT), a human-readable textual representation of WebAssembly binary format"
    WEBASSEMBLY_BINARY = "wasm", 136, "wasm,wasm,webassembly_binary", "WebAssembly (Wasm) binary format, a low-level binary instruction format for a stack-based virtual machine"
    JENKINSFILE = "jenkinsfile", 137, "jenkinsfile,Jenkinsfile", "Text file that contains the definition of a Jenkins Pipeline and is checked into source control"
    SVG = "svg", 138, "svg,svg,svg", "Scalable Vector Graphics, an XML-based vector image format for two-dimensional graphics with support for interactivity and animation"
    ROBOT = "robot", 139, "robot,robot,resource", "Robot Framework, a generic open source automation framework for acceptance testing, acceptance test-driven development (ATDD), and robotic process automation (RPA)"
    IDRIS = "idris", 140, "idris,idr,lidr", "General-purpose pure functional programming language with dependent types"
    PURESCRIPT = "purescript", 141, "purescript,purs", "Strongly-typed, purely functional programming language that compiles to JavaScript"
    OPENSCAD = "openscad", 142, "openscad,scad", "Software for creating solid 3D CAD objects. It is a script-only based modeller that uses its own description language"
    ANT = "ant", 143, "ant,build.xml,ant.xml,xml", "Apache Ant, a software tool for automating software build processes, typically using XML-based configuration files (build.xml)"
    MAVEN_POM = "pom_xml", 144, "pom_xml,pom.xml,xml", "Project Object Model (POM) file for Apache Maven, an XML file that contains information about the project and configuration details used by Maven to build the project"
    WINDOWS_REGISTRY = "reg", 145, "reg,reg,.reg", ".reg files, text files for storing portions of the Windows Registry"
    CLOJURESCRIPT = "clojurescript", 146, "clojurescript,cljs,cljc", "Compiler for Clojure that targets JavaScript, allowing Clojure code to be run in web browsers and Node.js"
    ELM = "elm", 147, "elm,elm", "Domain-specific programming language for declaratively creating web browser-based graphical user interfaces"
    DHALL = "dhall", 148, "dhall,dhall", "Programmable configuration language that is not Turing-complete"
    RAZOR = "razor", 149, "razor,cshtml,vbhtml", "ASP.NET programming syntax used to create dynamic web pages with C# or VB.NET"
    STYLUS = "stylus", 150, "stylus,styl,stylus", "Dynamic stylesheet preprocessor language that is compiled into CSS, influenced by SASS and LESS"
    CABAL = "cabal", 151, "cabal,cabal", "Configuration files for Cabal, the package system for Haskell"
    NIX = "nix", 152, "nix,nix", "Purely functional package manager and its associated language for describing packages and configurations"
    JSONNET = "jsonnet", 153, "jsonnet,jsonnet,libsonnet", "Data templating language that helps you define JSON data"
    GEMFILE = "gemfile", 154, "gemfile,Gemfile", "File used by Bundler in Ruby projects to specify the gems (libraries) required for the project"
    M4 = "m4", 155, "m4,m4", "General-purpose macro processor, often used with Autoconf"
    D = "d", 156, "d,d,di", "Multi-paradigm system programming language created as a successor to C++"
    VIML = "viml", 157, "viml,vim,vimrc,vba,viml", "Vim script, the scripting language used in the Vim text editor"
    RPM_SPEC = "rpm_spec", 158, "rpm_spec,spec", ".spec files used by RPM Package Manager to build packages"

    COFFEESCRIPT = "coffeescript", 159, "coffeescript,coffee,litcoffee,_coffee", "Programming language that transcompiles into JavaScript, aiming to enhance JavaScript's brevity and readability"
    RAKU = "raku", 160, "raku,raku,rakumod,rakutest,pm6,pl6,p6", "Member of the Perl family of programming languages (formerly Perl 6)"
    GDSCRIPT = "gdscript", 161, "gdscript,gd", "High-level, dynamically typed programming language used in the Godot game engine"
    ACTIONSCRIPT = "actionscript", 162, "actionscript,as", "Object-oriented programming language originally developed by Macromedia Inc. (now Adobe Inc.) for Adobe Flash Player and Adobe AIR"
    APEX = "apex", 163, "apex,cls,trigger", "Proprietary object-oriented programming language provided by Salesforce for building applications on the Salesforce platform"
    CFML = "cfml", 164, "cfml,cfm,cfc,cfml", "ColdFusion Markup Language, a scripting language for web development that runs on the JVM, the .NET framework, and Google App Engine"
    COQ = "coq", 165, "coq,v,coq", "Interactive theorem prover and proof assistant"
    EMACS_LISP = "emacs_lisp", 166, "emacs_lisp,el,elisp", "Dialect of the Lisp programming language used as a scripting language by Emacs text editors"
    FORTH = "forth", 167, "forth,fth,4th,frt,forth,fs", "Procedural, stack-oriented programming language and interactive environment"
    GAMEMAKER_LANGUAGE = "gml", 168, "gml,gml", "GameMaker Language, a scripting language used by GameMaker Studio"
    HACKLANG = "hack", 169, "hack,hack,hh,php", "Programming language for the HipHop Virtual Machine (HHVM), created by Facebook as a dialect of PHP"
    LIVESCRIPT = "livescript", 170, "livescript,ls,_ls", "Language that compiles to JavaScript, with a focus on functional programming and readability"
    LOOKML = "lookml", 171, "lookml,lkml,lookml", "Language for Looker, a business intelligence software and big data analytics platform"
    MESON = "meson", 172, "meson,meson.build,meson_options.txt", "Open source build system meant to be both extremely fast, and, even more importantly, as user friendly as possible"
    MODULA2 = "modula2", 173, "modula2,mod,def", "General purpose, procedural programming language, a descendant of Pascal"
    MOONSCRIPT = "moonscript", 174, "moonscript,moon", "Dynamic scripting language that compiles into Lua"
    NSIS = "nsis", 175, "nsis,nsi,nsh", "Nullsoft Scriptable Install System, a script-driven installer authoring tool for Microsoft Windows"
    OPENCL = "opencl", 176, "opencl,cl,opencl", "Open Computing Language, a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, DSPs, FPGAs and other processors"
    OPENEDGE_ABL = "openedge_abl", 177, "openedge_abl,p,cls,w", "OpenEdge Advanced Business Language, a business application development language created and maintained by Progress Software Corporation"
    POSTSCRIPT = "postscript", 178, "postscript,ps,eps", "Page description language in the electronic publishing and desktop publishing realm"
    POVRAY_SDL = "povray_sdl", 179, "povray_sdl,pov,inc", "Persistence of Vision Raytracer (POV-Ray) Scene Description Language, used to create 3D graphics"
    PROCESSING = "processing", 180, "processing,pde", "Flexible software sketchbook and a language for learning how to code within the context of the visual arts"
    QML = "qml", 181, "qml,qml", "Qt Meta-object Language or Qt Modelling Language, a user interface markup language"
    RAML = "raml", 182, "raml,raml", "RESTful API Modeling Language, a YAML-based language for describing RESTful APIs"
    REASONML = "reasonml", 183, "reasonml,re,rei", "Syntax extension and toolchain for OCaml, designed to be familiar to JavaScript programmers"
    RED_LANG = "red", 184, "red,red,reds", "Programming language inspired by REBOL, designed to be both human and machine readable"
    RENPYSCRIPT = "renpy", 185, "renpy,rpy", "Scripting language for the Ren'Py visual novel engine, based on Python"
    SAS_LANG = "sas", 186, "sas,sas", "SAS language, a programming language used for statistical analysis, developed by SAS Institute"
    SCILAB = "scilab", 187, "scilab,sci,sce", "Free and open-source, cross-platform numerical computational package and a high-level, numerically oriented programming language"
    SOURCEPAWN = "sourcepawn", 188, "sourcepawn,sp,inc", "Scripting language used for plugins in Source engine games"
    SQF = "sqf", 189, "sqf,sqf", "Status Quo Function, a scripting language used in Bohemia Interactive's game engines (e.g., Arma series)"
    SML = "sml", 190, "sml,sml,sig,fun", "Standard ML, a general-purpose, modular, functional programming language with compile-time type checking and type inference"
    STATA = "stata", 191, "stata,do,ado", "General-purpose statistical software package"
    TEXTILE = "textile", 192, "textile,textile", "Lightweight markup language that uses a text formatting syntax to convert plain text into structured HTML markup"
    TLA_PLUS = "tla", 193, "tla,tla", "TLA+, a high-level language for modeling programs and systems—especially concurrent and distributed ones"
    TWIG = "twig", 194, "twig,twig", "Flexible, fast, and secure template engine for PHP"
    UNREALSCRIPT = "unrealscript", 195, "unrealscript,uc", "Native scripting language for the Unreal Engine, used for authoring game code and gameplay events before C++ became more prominent"
    VALA = "vala", 196, "vala,vala,vapi", "Object-oriented programming language with a self-hosting compiler that generates C code and uses the GObject system"
    VCL = "vcl", 197, "vcl,vcl", "Varnish Configuration Language, a domain-specific language used to configure the Varnish Cache HTTP accelerator"
    VBSCRIPT = "vbscript", 198, "vbscript,vbs", "Active Scripting language developed by Microsoft that is modeled on Visual Basic"
    VELOCITY = "velocity", 199, "velocity,vtl", "Apache Velocity, a Java-based template engine that provides a simple yet powerful template language to reference objects defined in Java code"
    WEBIDL = "webidl", 200, "webidl,webidl", "Web Interface Definition Language, an OMG IDL dialect for describing interfaces that are intended to be implemented in web browsers"
    WDL = "wdl", 201, "wdl,wdl", "Workflow Description Language, a way to specify data processing workflows with a human-readable and -writable syntax"
    WIKITEXT = "wikitext", 202, "wikitext,wiki,mediawiki", "Markup language used to write pages in wiki websites, such as Wikipedia"
    XQUERY = "xquery", 203, "xquery,xq,xqy,xquery,xqm,xqs", "Query and functional programming language that queries and transforms collections of structured and unstructured data, usually in the form of XML"
    YANG = "yang", 204, "yang,yang", "Data modeling language used to model configuration and state data manipulated by the Network Configuration Protocol (NETCONF)"
    PLSQL = "plsql", 205, "plsql,sql,pls,plb,pks,pkb,plsql", "Procedural Language/SQL, Oracle Corporation's procedural extension for SQL and the Oracle relational database"
    TSQL = "tsql", 206, "tsql,sql,tsql", "Transact-SQL, Microsoft's and Sybase's proprietary extension to SQL"
    ASP_CLASSIC = "asp_classic", 207, "asp_classic,asp", "Active Server Pages (Classic ASP), Microsoft's first server-side script engine for dynamically generated web pages"
    JSP = "jsp", 208, "jsp,jsp,jspf", "JavaServer Pages, a technology that helps software developers create dynamically generated web pages based on HTML, XML, or other document types"
    API_BLUEPRINT = "api_blueprint", 209, "api_blueprint,apib", "Markdown-based document format for writing API descriptions and documentation"
    CSOUND = "csound", 210, "csound,csd,orc,sco", "User-programmable computer music software, a sound and music computing system"
    PUREDATA_PATCH = "puredata_patch", 211, "puredata_patch,pd", "Pure Data (Pd), a visual programming language developed for creating interactive computer music and multimedia works"
    SUPERCOLLIDER = "supercollider", 212, "supercollider,sc,scd", "Platform for audio synthesis and algorithmic composition, used by musicians, artists, and researchers working with sound"
    CHUCK = "chuck", 213, "chuck,ck", "Concurrent, strongly timed audio programming language for real-time synthesis, composition, and performance"
    FAUST = "faust", 214, "faust,dsp", "Functional AUdio STream, a functional programming language for sound synthesis and audio processing"
    ASPX = "aspx", 215, "aspx,aspx", "ASP.NET Web Forms, a file extension for web pages created using ASP.NET technology"
    BLITZMAX = "blitzmax", 216, "blitzmax,bmx", "Game programming language, successor to BlitzBasic and Blitz3D"
    BOO = "boo", 217, "boo,boo", "Object-oriented, statically typed programming language for the .NET Framework and Mono with a Python-inspired syntax"
    ABAP = "abap", 218, "abap,sap", "SAP Advanced Business Application Programming language"
    AGDA = "agda", 220, "agda,lagda", "Agda dependently typed functional language"
    AGS_SCRIPT = "ags_script", 221, "ags_script,asc,ash", "Adventure Game Studio Scripting language"
    ALLOY = "alloy", 222, "alloy,als", "Alloy declarative modeling language based on first-order logic"
    ANGELSCRIPT = "angelscript", 223, "angelscript,as,asc", "AngelScript game scripting language (.as also used by ActionScript)"
    ANTLR = "antlr", 224, "antlr,g,g4,antlr4", "ANother Tool for Language Recognition parser generator"
    ASN1 = "asn1", 226, "asn,asn1", "Abstract Syntax Notation One"
    ASPECTJ = "aspectj", 227, "aspectj,aj", "AspectJ aspect-oriented extension for Java"
    ASYNCAPI = "asyncapi", 229, "asyncapi,yaml,yml,json", "AsyncAPI Specification for event-driven APIs"
    ATS = "ats", 230, "ats,dats,sats,hats", "ATS programming language with dependent types and linear types"
    AUTOIT = "autoit", 231, "autoit,au3", "AutoIt scripting language for Windows automation (Freeware BASIC-like)"
    AVRO_IDL = "avro_idl", 232, "avro_idl,avdl", "Apache Avro Interface Definition Language"
    AVRO_SCHEMA = "avro_schema", 233, "avro_schema,avsc", "Apache Avro schema definition"
    BALLERINA = "ballerina", 234, "ballerina,bal,balx", "Ballerina cloud-native programming language"
    BICEP = "bicep", 235, "bicep", "Bicep language for Azure resource deployment (Azure Declarative Resource Deployment)"
    BISON = "bison", 236, "bison,y,yacc", "GNU parser generator Yacc compatible"
    BITBAKE = "bitbake", 237, "bitbake,bb,bbappend,bbclass,conf,inc", "Build tool recipes/config for Yocto Project"
    BLITZBASIC = "blitzbasic", 238, "blitzbasic,bb,decls", "BlitzBASIC game programming language"
    BRAINFUCK = "brainfuck", 240, "brainfuck,b,bf", "Esoteric Turing-complete programming language"
    BRIGHTSCRIPT = "brightscript", 241, "brightscript,brs", "BrightScript language for Roku platform"
    BSV = "bsv", 242, "bsv", "Bluespec SystemVerilog hardware description language"
    CADENCE = "cadence", 243, "cadence,cdc", "Cadence resource-oriented programming language for Flow blockchain"
    CAPNPROTO_SCHEMA = "capnproto_schema", 244, "capnproto_schema,capnp", "Cap'n Proto schema definition language"
    CEYLON = "ceylon", 245, "ceylon", "Ceylon object-oriented statically-typed language (archived)"
    CHAPEL = "chapel", 246, "chapel,chpl", "Chapel parallel programming language by Cray"
    CIL = "cil", 248, "cil,il", "Common Intermediate Language for .NET Framework"
    CLARION = "clarion", 249, "clarion,clw", "Clarion data-centric programming language"
    CLEAN = "clean", 250, "clean,icl,dcl", "Clean purely functional programming language"
    CLIPPER = "clipper", 251, "clipper,prg,ch", "xBase dialect for DOS"
    COMPONENT_PASCAL = "component_pascal", 252, "component_pascal,cp,cps", "Dialect of Oberon programming language"
    COOL = "cool", 253, "cool,cl", "Classroom Object Oriented Language"
    CUE_LANG = "cue", 255, "cue", "CUE configuration language"
    CWL = "cwl", 256, "cwl", "Common Workflow Language for data analysis workflows"
    CYTHON = "cython", 257, "cython,pyx,pxd,pxi", "Cython optimizing static compiler for Python and Cython"
    DAFNY = "dafny", 258, "dafny,dfy", "Dafny verification-aware programming language"
    DELPHI = "delphi", 259, "delphi,pas,dpr,dpk,dfm,lfm", "Delphi, Object Pascal dialect by Embarcadero (Embarcadero Delphi)"
    DYLAN = "dylan", 260, "dylan,lid", "Dylan dynamic object-oriented language"
    ECL = "ecl", 261, "ecl", "HPCC Systems Enterprise Control Language"
    EIFFEL = "eiffel", 262, "eiffel,e,eif", "Eiffel object-oriented language (Design by Contract language)"
    ESLINT_CONFIG = "eslint_config", 263, "eslintrc.js,eslintrc.cjs,eslintrc.yaml,eslintrc.yml,eslintrc.json,.eslintrc", "ESLint Configuration"
    FACTOR = "factor", 264, "factor", "Factor stack-based concatenative programming language"
    FANTOM = "fantom", 265, "fantom,fan", "Fantom portable language for JVM/.NET/JS (General-purpose object-oriented)"
    FLATBUFFERS_SCHEMA = "flatbuffers_schema", 267, "flatbuffers_schema,fbs", "FlatBuffers schema definition language"
    FREEMARKER_TPL = "freemarker_tpl", 268, "freemarker_tpl,ftl", "Apache FreeMarker Template Language"
    FSTAR = "fstar", 269, "fstar,fst,fsti", "F* (FStar), ML-like functional language for verification"
    GAMS = "gams", 270, "gams,gms", "General Algebraic Modeling System for mathematical optimization"
    GCODE = "gcode", 271, "gcode,nc,tap,gco", "G-code CNC programming language"
    GHERKIN = "gherkin", 272, "gherkin,feature", "Gherkin language for behavior descriptions (Cucumber)"
    GIT_IGNORE = "gitignore", 273, "gitignore,.gitignore,.dockerignore,.npmignore,.eslintignore,.hgignore,.p4ignore,ignore,.gitattributes,.gitmodules,.mailmap", "File pattern ignore syntax (e.g. .gitignore)"
    GNUPLOT = "gnuplot", 274, "gnuplot,gp,gnu,plot,plt", "Gnuplot command-driven interactive plotting program"
    GOSU = "gosu", 275, "gosu,gs,gsp,gst,gsx", "Gosu pragmatic language for the JVM"
    HARBOUR = "harbour", 276, "harbour,prg,hrb,ch", "Harbour xBase-compatible compiler (Clipper-compatible)"
    IDL = "idl", 277, "idl,pro,sav", "Interactive Data Language for data analysis and visualization"
    INFORM = "inform", 278, "inform,inf,ulx,z5,z8,ni,i7x,i6,ulx", "Inform language for interactive fiction (Inform 6/7, interactive fiction development system)"
    IO_LANG = "io", 279, "io", "Io small prototype-based programming language" # Merged IO_LANG and IO, value_str "io"
    ISABELLE = "isabelle", 280, "isabelle,thy", "Isabelle generic proof assistant (Isabelle/HOL)"
    J_LANG = "j_lang", 281, "j_lang,ijs,j", "J array programming language (APL-like)"
    JCL = "jcl", 282, "jcl,job", "Job Control Language for IBM mainframes"
    JOLIE = "jolie", 283, "jolie,ol,iol", "Jolie service-oriented programming language"
    JQ = "jq", 284, "jq", "jq command-line JSON processor"
    JSONIQ = "jsoniq", 285, "jsoniq,jq", "JSONiq query and functional programming language for JSON" # Note: .jq extension conflict with JQ tool
    KAITAI_STRUCT = "kaitai_struct", 286, "kaitai_struct,ksy", "Kaitai Struct declarative language for binary data formats (Declarative binary format parsing language)"
    KUSTO_KQL = "kusto_kql", 287, "kusto_kql,kql,csl", "Kusto Query Language (KQL) for Azure Data Explorer"
    LABVIEW = "labview", 288, "labview,vi,ctl,lvproj,lvlib", "LabVIEW graphical programming language by National Instruments"
    LASSO = "lasso", 289, "lasso,lasso9,lasso8,inc,ldml", "Lasso programming language for web development (Web application server and language)"
    LEAN = "lean", 290, "lean,hlean", "Lean theorem prover and functional programming language"
    LEX = "lex", 291, "lex,l,flex", "Lexical analyzer generator (Flex)"
    LIGO = "ligo", 292, "ligo,mligo,religo,jsligo", "LIGO smart contract language for Tezos"
    LIQUID_TPL = "liquid_tpl", 293, "liquid_tpl,liquid", "Liquid template language by Shopify"
    LLVM_IR = "llvm_ir", 294, "llvm_ir,ll", "LLVM Intermediate Representation"
    LOGO = "logo", 295, "logo,lgo", "Logo educational programming language"
    LOGTALK = "logtalk", 296, "logtalk,lgt", "Logtalk object-oriented logic programming language"
    LSL = "lsl", 297, "lsl", "Linden Scripting Language for Second Life"
    MAPLE = "maple", 298, "maple,mpl,mw", "Maple symbolic computation software and language"
    MATHEMATICA = "mathematica", 299, "mathematica,wl,nb,m,ma,cdf", "Wolfram Language (Mathematica) symbolic computation"
    MAXMSP = "maxmsp", 300, "maxmsp,maxpat,maxhelp,maxjs,mxt", "Max/MSP visual programming patcher files (graphical dataflow programming environment)" # Merged MAXMSP_PATCHER
    MAXSCRIPT = "maxscript", 301, "maxscript,ms,mcr", "MaxScript scripting language for Autodesk 3ds Max"
    MERCURY = "mercury", 302, "mercury,m,moo", "Mercury logic/functional programming language"
    METAL = "metal", 303, "metal", "Apple's Metal Shading Language" # Merged METAL_SHADING
    MODELICA = "modelica", 304, "modelica,mo", "Modelica object-oriented modeling language for physical systems"
    MODULA3 = "modula3", 305, "modula3,m3,i3,mg,ig", "Modula-3 systems programming language"
    MONKEY_C = "monkey_c", 306, "monkey_c,mc", "Monkey C language for Garmin Connect IQ devices"
    MONKEYX = "monkeyx", 307, "monkeyx,monkey,monkey2,cxs,build,resource", "Game programming language (Monkey X/Monkey 2/Cerberus X)"
    MOVE_LANG = "move", 308, "move", "Move programming language for Sui/Aptos blockchains"
    MQL = "mql", 309, "mql,mq4,mq5,mqh", "MetaQuotes Language for MetaTrader (MQL4/MQL5)"
    MUPAD = "mupad", 310, "mupad,mu", "MuPAD symbolic computation language (Matlab)"
    MXML = "mxml", 311, "mxml", "Adobe Flex MXML language"
    MYRDDIN = "myrddin", 312, "myrddin,myr", "Myrddin systems programming language"
    NETLOGO = "netlogo", 313, "netlogo,nlogo,nlogo3d", "NetLogo agent-based modeling environment language"
    NEWLISP = "newlisp", 314, "newlisp,lsp,nl,kif", "NewLISP Lisp-like scripting language"
    NEXTFLOW = "nextflow", 315, "nextflow,nf", "Nextflow language for data-driven computational pipelines (Workflow system scripting language)"
    NU = "nu", 316, "nu", "Nu interpreted object-oriented language (Lisp dialect on Obj-C runtime)"
    NUNJUCKS_TPL = "nunjucks_tpl", 317, "nunjucks_tpl,njk,nunjucks", "Nunjucks template engine by Mozilla"
    NWSCRIPT = "nwscript", 318, "nwscript,nss", "NWScript language for Neverwinter Nights"
    OBERON = "oberon", 319, "oberon,ob2,mod", "Oberon general-purpose programming language"
    OBJECT_PASCAL = "object_pascal", 320, "object_pascal,delphi,lazarus,pas,dpr,dpk,lpr,lpk,inc", "Object Pascal for Delphi, Free Pascal/Lazarus"
    OBJECTIVEJ = "objectivej", 321, "objectivej,j,sj", "Objective-J programming language for web (Cappuccino framework)" # Merged OBJECTIVE_J
    OCTAVE = "octave", 322, "octave,m", "GNU Octave, high-level language for numerical computations"
    ODIN = "odin", 323, "odin", "Odin data-oriented programming language for high performance (High-performance systems programming language)" # Merged ODIN_LANG
    OPENAPI = "openapi", 324, "openapi,yaml,yml,json,swagger", "OpenAPI Specification for REST APIs (Swagger)"
    OPENQASM = "openqasm", 325, "openqasm,qasm", "OpenQASM Quantum Assembly Language"
    OZ = "oz", 326, "oz", "Oz multi-paradigm programming language"
    P4_LANG = "p4_lang", 327, "p4_lang,p4", "Programming Protocol-independent Packet Processors (P4)"
    PAPYRUS_SCRIPT = "papyrus_script", 328, "papyrus_script,psc", "Papyrus scripting language for Bethesda games (Skyrim, Fallout)"
    PARASAIL = "parasail", 329, "parasail,psi,psl", "ParaSail parallel programming language"
    PAWN = "pawn", 330, "pawn,pwn,inc,sma", "Pawn (formerly Small C) scripting language"
    PICAT = "picat", 331, "picat,pi", "Picat logic-based multi-paradigm programming language"
    PICO_LISP = "pico_lisp", 332, "pico_lisp,l", "PicoLisp minimalist Lisp dialect"
    PIKE = "pike", 333, "pike,pmod", "Pike dynamic programming language"
    PONY = "pony", 334, "pony", "Pony actor-model, capabilities-secure language"
    POSTCSS = "postcss", 335, "postcss,pcss", "PostCSS (tool for transforming CSS)"
    POWERBUILDER = "powerbuilder", 336, "powerbuilder,powerscript,pbl,sra,sru,srw,srf,srs,srd,pbt", "PowerBuilder (PowerScript language for client/server applications)"
    POWERFX = "powerfx", 337, "powerfx,pfx,fx", "Microsoft Power Fx language"
    PRETTIER_CONFIG = "prettier_config", 338, ".prettierrc,.prettierrc.json,.prettierrc.yml,.prettierrc.yaml,.prettierrc.js,.prettierrc.cjs,prettier.config.js,prettier.config.cjs", "Prettier Configuration"
    PROMELA = "promela", 339, "promela,pml", "Promela (Process Meta Language) for SPIN model checker"
    PUREBASIC = "purebasic", 340, "purebasic,pb,pbi", "PureBasic BASIC-based compiled programming language (BASIC dialect with native compiler)"
    PUPPET = "puppet", 341, "puppet,pp", "Puppet configuration management language"
    QSHARP = "qsharp", 343, "qsharp,qs", "Q# (Q-sharp) quantum programming language by Microsoft"
    RBS = "rbs", 344, "rbs", "RBS language for Ruby type signatures"
    REBOL = "rebol", 345, "rebol,r,r3,reb", "REBOL (Relative Expression Based Object Language) scripting language"
    RESCRIPT = "rescript", 346, "rescript,res,resi", "ReScript language (compiles to JavaScript)"
    REXX = "rexx", 347, "rexx,rex,rx,cmd,pprx", "REXX (Restructured Extended Executor) interpreted scripting language"
    RING = "ring", 348, "ring", "Ring general-purpose dynamic programming language"
    ROFF = "roff", 349, "roff,man,mdoc,me,ms,mom,tmac,1,2,3,4,5,6,7,8,9", "Roff family of text-formatting languages (troff, nroff, groff)"
    RPG = "rpg", 350, "rpg,rpgle,sqlrpgle", "IBM RPG (Report Program Generator), typically RPGLE"
    SEED7 = "seed7", 351, "seed7,s7i,sd7", "Seed7 extensible general-purpose programming language"
    SELF_LANG = "self", 352, "self", "Self prototype-based dynamic object-oriented language"
    SHEN = "shen", 353, "shen", "Shen portable functional programming language"
    SIMULA = "simula", 354, "simula,sim", "Simula, first object-oriented programming language"
    SMALI = "smali", 355, "smali", "Smali assembler for Android's Dalvik/ART virtual machine"
    SNAKEMAKE = "snakemake", 356, "snakemake,smk,Snakefile", "Snakemake workflow definition language (Python-based)"
    SNOBOL = "snobol", 357, "snobol,sno,spt", "SNOBOL (String Oriented Symbolic Language) for string manipulation"
    SQUIRREL = "squirrel", 358, "squirrel,nut,gnut", "Squirrel lightweight, embeddable scripting language (High-level imperative object-oriented)"
    STARLARK = "starlark", 359, "starlark,bzl,bazel", "Starlark configuration language for Bazel build system"
    SWAGGER = "swagger", 361, "swagger,json,yaml,yml", "Swagger API Specification (OpenAPI 2.0)"
    SWIG = "swig", 362, "swig,i", "SWIG (Simplified Wrapper and Interface Generator)"
    TADS = "tads", 363, "tads,t,t3,td,t3s,t3m,dat", "TADS (Text Adventure Development System) language"
    TEA_LANG = "tea", 364, "tea", "Tea high-level scripting language"
    TERSER = "terser", 365, "terser,js,.terserrc,.terserrc.json,terser.config.js", "Terser (JavaScript parser, mangler and compressor)"
    TURING = "turing", 366, "turing,t,tu", "Turing educational programming language"
    UNICON = "unicon", 367, "unicon,icn,u,ui", "Unicon unified extended dialect of Icon"
    URWEB = "urweb", 368, "urweb,ur,urs,urp", "Ur/Web functional language for type-safe web applications"
    VISUAL_BASIC_CLASSIC = "vb_classic", 369, "vb_classic,bas,frm,cls,ctl,dsr,vbp,vba,vbs", "Microsoft Visual Basic (classic), VBA, VBScript"
    VISUAL_FOXPRO = "visual_foxpro", 370, "visual_foxpro,prg,vcx,scx,dbc,frx,lbx,mnx,pjx,qpr", "Visual FoxPro data-centric OOP language"
    VLANG = "vlang", 371, "vlang,v,vsh", "V programming language (Statically typed compiled language)"
    VYPER = "vyper", 372, "vyper,vy", "Vyper Pythonic smart contract language for Ethereum"
    WENYAN = "wenyan", 373, "wenyan,wy", "Wenyan-lang programming language in classical Chinese"
    WGSL = "wgsl", 374, "wgsl", "WebGPU Shading Language"
    WHILEY = "whiley", 375, "whiley", "Whiley programming language with extended static checking"
    WOLFRAM = "wolfram", 376, "wolfram,wl,nb,m,wls", "Wolfram Language for Mathematica"
    X10 = "x10", 377, "x10", "X10 parallel programming language by IBM"
    XAML = "xaml", 378, "xaml", "Microsoft XAML (Extensible Application Markup Language)"
    XOJO = "xojo", 379, "xojo,xojo_code,xojo_project,xojo_window,xojo_menu,xojo_toolbar", "Xojo object-oriented cross-platform development language"
    XPROC = "xproc", 380, "xproc,xpl", "XProc XML Pipeline Language"
    XTEND = "xtend", 381, "xtend", "Xtend flexible and expressive JVM language (Statically-typed language for JVM)"
    YACC = "yacc", 382, "yacc,y,bison", "Yet Another Compiler Compiler (Yacc) parser generator, also Bison"
    ZEEK = "zeek", 383, "zeek,bro,bif", "Zeek network security monitoring scripting language (formerly Bro)"
    ZEPHIR = "zephir", 384, "zephir,zep", "Zephir language for creating PHP extensions"
    ZIMPL = "zimpl", 385, "zimpl,zpl,zmpl", "Zimpl mathematical modeling language for optimization"


    UNREAL_PROJECT = "unreal_project", 501, "unreal_project,uproject", "Unreal Engine project file, defines project settings, modules, and other project-specific information (JSON format)."
    UNREAL_PLUGIN_DESCRIPTOR = "unreal_plugin_descriptor", 502, "unreal_plugin_descriptor,uplugin", "Unreal Engine plugin descriptor file, defines plugin information, modules, and dependencies (JSON format)."
    UNREAL_CONFIG_INI = "unreal_config_ini", 503, "unreal_config_ini,ini,ue_ini,unreal_ini", "Unreal Engine configuration files (e.g., DefaultEngine.ini, DefaultGame.ini). This is distinct from generic INI files due to Unreal-specific sections and usage (.ini text format for UE)."
    UNREAL_SHADER_FILE = "unreal_shader_file", 504, "unreal_shader_file,usf,ush,ue_shader", "Unreal Engine Shader Files, used for custom shader code (HLSL-based syntax; e.g., .usf for shader source, .ush for shader headers)."
    UNREAL_SHADER_HEADER = "unreal_shader_header", 505, "unreal_shader_header,ush", "Unreal Engine Shader Header file (.ush), used for including common shader code, definitions, or utility functions."
    UNREAL_BUILD_SCRIPT_CS = "unreal_build_script_cs", 506, "unreal_build_script_cs,cs,Build.cs,Target.cs,ubt_cs,unreal_build_cs", "Unreal Engine Build Tool C# scripts, defining modules and targets (e.g., MyModule.Build.cs, MyProject.Target.cs)."
    UNREAL_ASSET = "unreal_asset", 507, "unreal_asset,uasset", "Unreal Engine generic asset file (binary format, e.g., Blueprints, Materials, Animations, Sounds, Textures)."
    UNREAL_MAP = "unreal_map", 508, "unreal_map,umap", "Unreal Engine map or level file (binary format, stores level data, actor placements, and environment settings)."
    UNREAL_MODULES_FILE = "unreal_modules_file", 509, "unreal_modules_file,modules", "Unreal Engine modules file (e.g., Engine.modules, Game.modules), specifies module definition and loading information for precompiled engines or plugins (JSON format)."
    UNREAL_VERSION_FILE = "unreal_version_file", 510, "unreal_version_file,version,Engine.version", "Unreal Engine version file (e.g., Engine.version, ProjectName.version, Build.version), stores build GUID, changelist, and version information (JSON format)."
    UNREAL_H_GENERATED = "unreal_h_generated", 511, "unreal_h_generated,gen.h,generated.h", "Unreal Engine UHeaderTool (UHT) Generated C++ Header file (e.g., MyClass.generated.h from UObjects, an intermediate build file)."

    # Unreal 5 releated
    VERSE = "verse", 512, "verse", "Verse scripting language for Unreal Engine (UEFN) and Fortnite."
    UNREAL_ASSET_BINARY = "unreal_asset_binary", 513, "unreal_asset_binary,uasset,umap", "Unreal Engine binary asset files, encompassing various types like Blueprints, Materials, Textures, Skeletal Meshes, and Levels/Maps. This is a broader category for .uasset and .umap files."
    UNREAL_PLUGIN_MANIFEST = "unreal_plugin_manifest", 514, "unreal_plugin_manifest,upluginmanifest", "Unreal Engine plugin manifest file (often distinct from UGS-specific ones), used for plugin packaging and distribution, often containing precompiled build information (JSON format)."
    UNREAL_AUTOMATION_TEST_JSON = "unreal_automation_test_json", 515, "unreal_automation_test_json,automation.json", "Unreal Engine automation test definition files, typically ending with .automation.json (JSON format)."
    UNREAL_UBT_MANIFEST = "unreal_ubt_manifest", 516, "unreal_ubt_manifest,ubtmanifest,manifest", "Unreal Build Tool manifest file (JSON format), tracks build outputs, dependencies, and actions. Distinct from XML version."
    UNREAL_BUILD_RECEIPT = "unreal_build_receipt", 517, "unreal_build_receipt,target", "Unreal Engine build receipt file (e.g., MyProject.target), details build information, modules, and artifacts (can be JSON or XML format). Distinct from .target JSON definitions."
    UNREAL_BUILD_RESPONSE_FILE = "unreal_build_response_file", 518, "unreal_build_response_file,response", "Unreal Engine build response files (e.g., *.response), containing compiler or linker arguments, typically plain text."
    UNREAL_LEGACY_PACKAGE = "unreal_legacy_package", 519, "unreal_legacy_package,upk,udk", "Legacy Unreal Engine package file (UE3-era and earlier, binary, e.g., .upk, .udk)."
    UNREAL_LEGACY_COMPILED_SCRIPT = "unreal_legacy_compiled_script", 520, "unreal_legacy_compiled_script,u", "Legacy Unreal Engine compiled UnrealScript file (UE3-era and earlier, binary)."
    UNREAL_LOC_MANIFEST = "unreal_loc_manifest", 521, "unreal_loc_manifest,manifest", "Unreal Engine localization manifest file (JSON format, e.g., Game.manifest). Note: .manifest can be XML in other contexts (like UBT Manifests)."
    UNREAL_LOC_ARCHIVE = "unreal_loc_archive", 522, "unreal_loc_archive,archive", "Unreal Engine localization archive file (JSON format, e.g., Game.archive)."
    UNREAL_LOC_PO = "unreal_loc_po", 523, "unreal_loc_po,po", "Unreal Engine localization text file (Portable Object format, .po)."
    UNREAL_PLUGIN_MANIFEST_UGS = "unreal_plugin_manifest_ugs", 524, "unreal_plugin_manifest_ugs,upluginmanifest", "Unreal Engine Game Sync (UGS) plugin manifest file (JSON format). Specific to UGS usage."
    UNREAL_TARGET_DEF_JSON = "unreal_target_def_json", 525, "unreal_target_def_json,target", "Unreal Engine build target definition file (JSON format, e.g., MyGame.target, ShaderCompileWorker.target). Defines a target for UBT, distinct from build receipts."
    UNREAL_SHADER_PIPELINE_CACHE = "unreal_shader_pipeline_cache", 526, "unreal_shader_pipeline_cache,upipelinecache,shk", "Unreal Engine shader pipeline cache file (binary, e.g., .upipelinecache, .shk)."
    UNREAL_SHADER_MAP_COOKED = "unreal_shader_map_cooked", 527, "unreal_shader_map_cooked,ushadermap", "Unreal Engine cooked shader map file (binary)."
    UNREAL_GLOBAL_SHADER_CACHE = "unreal_global_shader_cache", 528, "unreal_global_shader_cache,gsc", "Unreal Engine Global Shader Cache file (binary, e.g., PCD3D_SM5.gsc)."
    UNREAL_PLUGIN_FRIEND_DECL = "unreal_plugin_friend", 529, "unreal_plugin_friend,upluginfriend", "Unreal Engine plugin friend declaration file (JSON format)."
    UNREAL_PROJECT_DIRS_UGS = "unreal_project_dirs_ugs", 530, "unreal_project_dirs_ugs,uprojectdirs", "Unreal Engine Game Sync (UGS) project directories file (plain text)."
    UNREAL_BUILD_TOOL_MANIFEST_XML = "unreal_build_tool_manifest_xml", 531, "unreal_build_tool_manifest_xml,ubtmanifest,xml", "Unreal Build Tool (UBT) manifest file (XML format). Distinct from JSON UBT Manifest."
    UNREAL_BUILD_GRAPH_XML = "unreal_build_graph_xml", 532, "unreal_build_graph_xml,xml", "Unreal Engine BuildGraph script (XML format for build automation)."
    UNREAL_REMOTE_EXECUTION_SETTINGS = "unreal_remote_exec_settings", 533, "unreal_remote_exec_settings,urs,xml", "Unreal Engine Remote Execution Settings file (XML format)."
    UNREAL_DATA_ASSET = "unreal_data_asset", 534, "unreal_data_asset,uasset", "Unreal Engine Data Asset, a specific type of .uasset for storing strongly-typed data structures (binary asset)."
    UNREAL_TRANSLATION_PICKLE = "unreal_translation_pickle", 535, "unreal_translation_pickle,utp", "Unreal Engine Translation Pickle, used in localization (binary)."
    UNREAL_SHADER_DEBUG_INFO = "unreal_shader_debug_info", 536, "unreal_shader_debug_info,ushaderdebuginfo", "Unreal Engine Shader Debug Info file (binary)."
    UNREAL_PLUGIN_RESOURCES = "unreal_plugin_resources", 537, "unreal_plugin_resources,uresources", "Unreal Engine Plugin Resources file (binary archive)."
    UNREAL_INPUT_MAPPING_PROFILE = "unreal_input_mapping_profile", 538, "unreal_input_mapping_profile,uinputprofile", "Unreal Engine Input Mapping Profile (binary)."
    UNREAL_ANIMATION_CURVE_COMPRESSION_SETTINGS = "unreal_anim_curve_compression", 539, "unreal_anim_curve_compression,uac", "Unreal Engine Animation Curve Compression Settings (binary asset)."
    UNREAL_NATIVE_VISUALIZER = "unreal_natvis", 540, "unreal_natvis,ue_natvis,natvis", "Unreal Engine debugger type visualizer (.natvis XML format)."
    UNREAL_CPP_INL = "unreal_cpp_inl", 541, "unreal_cpp_inl,unrealinl,inl", "Unreal Engine C++ Inline implementation file."
    UNREAL_CPP_GENERATED = "unreal_cpp_generated", 542, "unreal_cpp_generated,unrealgencpp,gencpp,gen.cpp", "Unreal Engine UHT Generated C++ Source file (e.g., MyClass.gen.cpp)."
    UNREAL_LOG = "unreal_log", 543, "unreal_log,unreallog,log", "Unreal Engine Log file."
    UNREAL_UHT_MANIFEST = "unreal_uht_manifest", 544, "unreal_uht_manifest,uhtmanifest", "Unreal Engine Header Tool Manifest file (JSON format)."


    TREE = "tree", 545, "tree,dir", "Dir representation "




LANGUAGE_EXTENSIONS_MAPPING: Dict[LanguageKind, Tuple[str, List[str]]] = {
    LanguageKind.TEXT: ("txt", ["txt"]),
    LanguageKind.ASSEMBLY: ("asm", ["asm", "s", "nasm"]),
    LanguageKind.BASH: ("bash", ["bash", "sh"]),
    LanguageKind.CSHARP: ("cs", ["cs"]),
    LanguageKind.C: ("c", ["c", "h"]),
    LanguageKind.CLOJURE: ("clj", ["clj", "cljc"]),
    LanguageKind.CPP: ("cpp", ["cpp", "cxx", "cc", "hpp", "hxx", "h", "hh"]),
    LanguageKind.CSS: ("css", ["css"]),
    LanguageKind.DART: ("dart", ["dart"]),
    LanguageKind.DIFF: ("diff", ["diff", "patch"]),
    LanguageKind.DOCKERFILE: ("Dockerfile", ["Dockerfile", "dockerfile"]),
    LanguageKind.DOT: ("dot", ["dot", "gv"]),
    LanguageKind.ELIXIR: ("ex", ["ex", "exs"]),
    LanguageKind.FSHARP: ("fs", ["fs", "fsi", "fsx", "fsscript"]),
    LanguageKind.GO: ("go", ["go"]),
    LanguageKind.GRAPHQL: ("graphql", ["graphql", "gql"]),
    LanguageKind.HASKELL: ("hs", ["hs", "lhs"]),
    LanguageKind.HTML: ("html", ["html", "htm", "xhtml"]),
    LanguageKind.JAVA: ("java", ["java", "jar"]),
    LanguageKind.JAVASCRIPT: ("js", ["js", "mjs", "cjs"]),
    LanguageKind.JSON: ("json", ["json", "jsonc", "geojson", "topojson"]),
    LanguageKind.JSX: ("jsx", ["jsx"]),
    LanguageKind.KOTLIN: ("kt", ["kt", "kts"]),
    LanguageKind.LESS: ("less", ["less"]),
    LanguageKind.LUA: ("lua", ["lua"]),
    LanguageKind.MARKDOWN: ("md", ["md", "markdown", "mkd", "mdwn", "mdown", "mdx"]),
    LanguageKind.MERMAID: ("mmd", ["mmd", "mermaid"]),
    LanguageKind.OBJECTIVEC: ("m", ["m", "mm", "h"]),
    LanguageKind.OCAML: ("ml", ["ml", "mli"]),
    LanguageKind.PERL: ("pl", ["pl", "pm", "t", "pod"]),
    LanguageKind.PHP: ("php", ["php", "php3", "php4", "php5", "phtml"]),
    LanguageKind.PLANTUML: ("puml", ["puml", "pu", "plantuml"]),
    LanguageKind.POWERSHELL: ("ps1", ["ps1", "psm1", "psd1"]),
    LanguageKind.PYTHON: ("py", ["py", "py3", "pyw", "ipynb"]),
    LanguageKind.PYTHONREPL: ("pycon", ["pycon"]),
    LanguageKind.R: ("r", ["r", "R", "Rmd", "Rnw"]),
    LanguageKind.RUBY: ("rb", ["rb", "rbw", "rake", "gemspec", "ru"]),
    LanguageKind.RUST: ("rs", ["rs"]),
    LanguageKind.SASS: ("scss", ["scss", "sass"]),
    LanguageKind.SHELL: ("sh", ["sh", "bash", "zsh", "ksh", "tcsh", "fish", "tool"]),
    LanguageKind.SQL: ("sql", ["sql", "ddl", "dml"]),
    LanguageKind.SWIFT: ("swift", ["swift"]),
    LanguageKind.TERRAFORM: ("tf", ["tf", "tfvars", "hcl"]),
    LanguageKind.TSX: ("tsx", ["tsx"]),
    LanguageKind.TYPESCRIPT: ("ts", ["ts", "mts", "cts"]),
    LanguageKind.VBNET: ("vb", ["vb"]),
    LanguageKind.VUE: ("vue", ["vue"]),
    LanguageKind.XML: ("xml", ["xml", "xsd", "xsl", "xslt", "rss", "atom", "kml", "svg", "plist", "wsdl", "pom", "manifest"]),
    LanguageKind.YAML: ("yml", ["yml", "yaml"]),
    LanguageKind.BAT: ("bat", ["bat", "cmd"]),
    LanguageKind.ADA: ("adb", ["adb", "ads", "ada"]),
    LanguageKind.COBOL: ("cob", ["cob", "cbl", "cpy"]),
    LanguageKind.ERLANG: ("erl", ["erl", "hrl"]),
    LanguageKind.FORTRAN: ("f90", ["f", "f77", "f90", "f95", "f03", "f08", "for"]),
    LanguageKind.GROOVY: ("groovy", ["groovy", "gvy", "gy", "gsh"]),
    LanguageKind.JULIA: ("jl", ["jl"]),
    LanguageKind.COMMON_LISP: ("lisp", ["lisp", "cl", "l", "lsp", "fas", "fasl"]),
    LanguageKind.SCHEME: ("scm", ["scm", "ss"]),
    LanguageKind.MATLAB: ("m", ["m"]),
    LanguageKind.PASCAL: ("pas", ["pas", "pp", "p", "inc"]),
    LanguageKind.PROLOG: ("pl", ["pl", "pro", "P"]),
    LanguageKind.RACKET: ("rkt", ["rkt", "rktl", "scrbl"]),
    LanguageKind.SMALLTALK: ("st", ["st"]),
    LanguageKind.TCL: ("tcl", ["tcl", "tk", "itk"]),
    LanguageKind.VERILOG: ("v", ["v"]),
    LanguageKind.VHDL: ("vhd", ["vhd", "vhdl"]),
    LanguageKind.AWK: ("awk", ["awk", "gawk", "mawk", "nawk"]),
    LanguageKind.AUTOHOTKEY: ("ahk", ["ahk"]),
    LanguageKind.APPLESCRIPT: ("scpt", ["scpt", "applescript", "scptd"]),
    LanguageKind.ASCIIDOC: ("adoc", ["adoc", "asc"]),
    LanguageKind.RESTRUCTUREDTEXT: ("rst", ["rst", "rest"]),
    LanguageKind.LATEX: ("tex", ["tex", "ltx", "cls", "sty", "dtx", "ins"]),
    LanguageKind.TEX_PLAIN: ("tex", ["tex", "plain_tex"]),
    LanguageKind.ORGMODE: ("org", ["org", "org_mode"]),
    LanguageKind.TOML: ("toml", ["toml"]),
    LanguageKind.PROTOBUF: ("proto", ["proto"]),
    LanguageKind.CSV: ("csv", ["csv"]),
    LanguageKind.TSV: ("tsv", ["tsv"]),
    LanguageKind.BSON: ("bson", ["bson"]),
    LanguageKind.INI: ("ini", ["ini", "cfg", "conf", "prefs", "properties", "desktop", "directory", "gitconfig"]),
    LanguageKind.DOTENV: (".env", [".env", "dotenv"]),
    LanguageKind.NGINX: ("conf", ["conf", "nginx.conf"]),
    LanguageKind.APACHECONF: ("conf", ["conf", ".htaccess", "httpd.conf"]),
    LanguageKind.HOCON: ("conf", ["conf", "hocon"]),
    LanguageKind.CYPHER: ("cql", ["cql", "cypher"]),
    LanguageKind.SPARQL: ("rq", ["rq", "sparql"]),
    LanguageKind.JINJA: ("j2", ["j2", "jinja", "jinja2"]),
    LanguageKind.HANDLEBARS: ("hbs", ["hbs", "handlebars"]),
    LanguageKind.MUSTACHE: ("mustache", ["mustache", "mst"]),
    LanguageKind.EJS: ("ejs", ["ejs"]),
    LanguageKind.GLSL: ("glsl",    ["glsl", "vert", "frag", "geom", "tesc", "tese", "comp", "glslf", "vs", "fs", "gs", "tcs",   "tes", "cs"]),
    LanguageKind.HLSL: ("hlsl", ["hlsl", "fx", "fxh", "vsh", "psh", "gsh", "hsh", "dsh", "csh"]),
    LanguageKind.CMAKE: ("cmake", ["cmake", "cmake.in", "CMakeLists.txt"]),
    LanguageKind.MAKEFILE: ("Makefile",  ["Makefile", "makefile", "GNUmakefile", "GNUMakefile", "bsdmakefile", "mk", "mak"]),
    LanguageKind.GRADLE: ("gradle", ["gradle", "gradle.kts"]),
    LanguageKind.BIBTEX: ("bib", ["bib"]),
    LanguageKind.PROPERTIES: ("properties", ["properties"]),
    LanguageKind.SOLIDITY: ("sol", ["sol"]),
    LanguageKind.SYSTEMVERILOG: ("sv", ["sv", "svh", "svi"]),
    LanguageKind.JSON5: ("json5", ["json5"]),
    LanguageKind.TEXTPROTO: ("textproto", ["textproto", "textpb", "pb.txt", "pbtxt"]),
    LanguageKind.KCONFIG: ("Kconfig", ["Kconfig", "defconfig"]),
    LanguageKind.ARDUINO: ("ino", ["ino"]),
    LanguageKind.CUDA: ("cu", ["cu", "cuh"]),
    LanguageKind.SVELTE: ("svelte", ["svelte"]),
    LanguageKind.ZIG: ("zig", ["zig"]),
    LanguageKind.NIM: ("nim", ["nim", "nims"]),
    LanguageKind.CRYSTAL: ("cr", ["cr"]),
    LanguageKind.HAXE: ("hx", ["hx"]),
    LanguageKind.PUG: ("pug", ["pug", "jade"]),
    LanguageKind.SLIM_TPL: ("slim", ["slim"]),
    LanguageKind.HAML: ("haml", ["haml"]),
    LanguageKind.MAKO: ("mako", ["mako", "mao"]),
    LanguageKind.SMARTY_TPL: ("tpl", ["tpl"]),
    LanguageKind.XSLT_LANG: ("xsl", ["xsl", "xslt"]),
    LanguageKind.WREN: ("wren", ["wren"]),
    LanguageKind.AUGEAS: ("aug", ["aug"]),
    LanguageKind.STAN: ("stan", ["stan"]),
    LanguageKind.THRIFT: ("thrift", ["thrift"]),
    LanguageKind.EDGEQL: ("edgeql", ["edgeql", "esdl"]),
    LanguageKind.REGO: ("rego", ["rego"]),
    LanguageKind.GRAPHQL_SCHEMA: ("graphqls", ["graphqls", "gqls", "sdl"]),
    LanguageKind.CADDYFILE: ("Caddyfile", ["Caddyfile"]),
    LanguageKind.EDITORCONFIG: (".editorconfig", [".editorconfig"]),
    LanguageKind.HAR: ("har", ["har"]),
    LanguageKind.WEBASSEMBLY_TEXT: ("wat", ["wat", "wast"]),
    LanguageKind.WEBASSEMBLY_BINARY: ("wasm", ["wasm"]),
    LanguageKind.JENKINSFILE: ("Jenkinsfile", ["Jenkinsfile"]),
    LanguageKind.SVG: ("svg", ["svg"]),
    LanguageKind.ROBOT: ("robot", ["robot", "resource"]),
    LanguageKind.IDRIS: ("idr", ["idr", "lidr"]),
    LanguageKind.PURESCRIPT: ("purs", ["purs"]),
    LanguageKind.OPENSCAD: ("scad", ["scad"]),
    LanguageKind.ANT: ("xml", ["xml", "ant.xml", "build.xml"]),
    LanguageKind.MAVEN_POM: ("xml", ["xml", "pom.xml"]),
    LanguageKind.WINDOWS_REGISTRY: ("reg", ["reg", ".reg"]),
    LanguageKind.CLOJURESCRIPT: ("cljs", ["cljs", "cljc"]),
    LanguageKind.ELM: ("elm", ["elm"]),
    LanguageKind.DHALL: ("dhall", ["dhall"]),
    LanguageKind.RAZOR: ("cshtml", ["cshtml", "vbhtml"]),
    LanguageKind.STYLUS: ("styl", ["styl", "stylus"]),
    LanguageKind.CABAL: ("cabal", ["cabal"]),
    LanguageKind.NIX: ("nix", ["nix"]),
    LanguageKind.JSONNET: ("jsonnet", ["jsonnet", "libsonnet"]),
    LanguageKind.GEMFILE: ("Gemfile", ["Gemfile"]),
    LanguageKind.M4: ("m4", ["m4"]),
    LanguageKind.D: ("d", ["d", "di"]),
    LanguageKind.VIML: ("vim", ["vim", "vimrc", "vba", "viml"]),
    LanguageKind.RPM_SPEC: ("spec", ["spec"]),

    LanguageKind.COFFEESCRIPT: ("coffee", ["coffee", "litcoffee", "_coffee"]),
    LanguageKind.RAKU: ("raku", ["raku", "rakumod", "rakutest", "pm6", "pl6", "p6"]),
    LanguageKind.GDSCRIPT: ("gd", ["gd"]),
    LanguageKind.ACTIONSCRIPT: ("as", ["as"]),
    LanguageKind.APEX: ("cls", ["cls", "trigger"]),
    LanguageKind.CFML: ("cfm", ["cfm", "cfc", "cfml"]),
    LanguageKind.COQ: ("v", ["v", "coq"]),
    LanguageKind.EMACS_LISP: ("el", ["el", "elisp"]),
    LanguageKind.FORTH: ("fth", ["fth", "4th", "frt", "forth", "fs"]),
    LanguageKind.GAMEMAKER_LANGUAGE: ("gml", ["gml"]),
    LanguageKind.HACKLANG: ("hack", ["hack", "hh", "php"]),
    LanguageKind.LIVESCRIPT: ("ls", ["ls", "_ls"]),
    LanguageKind.LOOKML: ("lkml", ["lkml", "lookml"]),
    LanguageKind.MESON: ("meson.build", ["meson.build", "meson_options.txt"]),
    LanguageKind.MODULA2: ("mod", ["mod", "def"]),
    LanguageKind.MOONSCRIPT: ("moon", ["moon"]),
    LanguageKind.NSIS: ("nsi", ["nsi", "nsh"]),
    LanguageKind.OPENCL: ("cl", ["cl", "opencl"]),
    LanguageKind.OPENEDGE_ABL: ("p", ["p", "cls", "w"]),
    LanguageKind.POSTSCRIPT: ("ps", ["ps", "eps"]),
    LanguageKind.POVRAY_SDL: ("pov", ["pov", "inc"]),
    LanguageKind.PROCESSING: ("pde", ["pde"]),
    LanguageKind.QML: ("qml", ["qml"]),
    LanguageKind.RAML: ("raml", ["raml"]),
    LanguageKind.REASONML: ("re", ["re", "rei"]),
    LanguageKind.RED_LANG: ("red", ["red", "reds"]),
    LanguageKind.RENPYSCRIPT: ("rpy", ["rpy"]),
    LanguageKind.SAS_LANG: ("sas", ["sas"]),
    LanguageKind.SCILAB: ("sci", ["sci", "sce"]),
    LanguageKind.SOURCEPAWN: ("sp", ["sp", "inc"]),
    LanguageKind.SQF: ("sqf", ["sqf"]),
    LanguageKind.SML: ("sml", ["sml", "sig", "fun"]),
    LanguageKind.STATA: ("do", ["do", "ado"]),
    LanguageKind.TEXTILE: ("textile", ["textile"]),
    LanguageKind.TLA_PLUS: ("tla", ["tla"]),
    LanguageKind.TWIG: ("twig", ["twig"]),
    LanguageKind.UNREALSCRIPT: ("uc", ["uc"]),
    LanguageKind.VALA: ("vala", ["vala", "vapi"]),
    LanguageKind.VCL: ("vcl", ["vcl"]),
    LanguageKind.VBSCRIPT: ("vbs", ["vbs"]),
    LanguageKind.VELOCITY: ("vtl", ["vtl"]),
    LanguageKind.WEBIDL: ("webidl", ["webidl"]),
    LanguageKind.WDL: ("wdl", ["wdl"]),
    LanguageKind.WIKITEXT: ("wiki", ["wiki", "mediawiki"]),
    LanguageKind.XQUERY: ("xq", ["xq", "xqy", "xquery", "xqm", "xqs"]),
    LanguageKind.YANG: ("yang", ["yang"]),
    LanguageKind.PLSQL: ("sql", ["sql", "pls", "plb", "pks", "pkb", "plsql"]),
    LanguageKind.TSQL: ("sql", ["sql", "tsql"]),
    LanguageKind.ASP_CLASSIC: ("asp", ["asp"]),
    LanguageKind.JSP: ("jsp", ["jsp", "jspf"]),
    LanguageKind.API_BLUEPRINT: ("apib", ["apib"]),
    LanguageKind.CSOUND: ("csd", ["csd", "orc", "sco","csound"]),
    LanguageKind.PUREDATA_PATCH: ("pd", ["pd"]),
    LanguageKind.SUPERCOLLIDER: ("scd", ["scd", "sc"]),
    LanguageKind.FAUST: ("dsp", ["dsp"]),
    LanguageKind.BOO: ("boo", ["boo"]),

    LanguageKind.ABAP: ("abap", ["abap", "sap"]),
    LanguageKind.AGDA: ("agda", ["agda", "lagda"]),
    LanguageKind.AGS_SCRIPT: ("asc", ["asc", "ash", "ags_script"]),
    LanguageKind.ALLOY: ("als", ["als", "alloy"]),
    LanguageKind.ANGELSCRIPT: ("as", ["as", "asc", "angelscript"]),
    LanguageKind.ANTLR: ("g4", ["g", "g4", "antlr", "antlr4"]),
    LanguageKind.ASN1: ("asn", ["asn", "asn1"]),
    LanguageKind.ASPECTJ: ("aj", ["aj", "aspectj"]),
    LanguageKind.ASPX: ("aspx", ["aspx"]),
    LanguageKind.ASYNCAPI: ("yaml", ["yaml", "yml", "json", "asyncapi", "asyncapi.yaml", "asyncapi.yml", "asyncapi.json"]),
    LanguageKind.ATS: ("dats", ["dats", "sats", "hats", "ats"]),
    LanguageKind.AUTOIT: ("au3", ["au3", "autoit"]),
    LanguageKind.AVRO_IDL: ("avdl", ["avdl", "avro_idl"]),
    LanguageKind.AVRO_SCHEMA: ("avsc", ["avsc", "avro_schema"]),
    LanguageKind.BALLERINA: ("bal", ["bal", "balx", "ballerina"]),
    LanguageKind.BICEP: ("bicep", ["bicep"]),
    LanguageKind.BISON: ("y", ["y", "yacc", "bison"]),
    LanguageKind.BITBAKE: ("bb", ["bb", "bbappend", "bbclass", "conf", "inc", "bitbake"]),
    LanguageKind.BLITZBASIC: ("bb", ["bb", "decls", "blitzbasic"]),
    LanguageKind.BLITZMAX: ("bmx", ["bmx", "blitzmax"]),
    LanguageKind.BRAINFUCK: ("bf", ["b", "bf", "brainfuck"]),
    LanguageKind.BRIGHTSCRIPT: ("brs", ["brs", "brightscript"]),
    LanguageKind.BSV: ("bsv", ["bsv"]),
    LanguageKind.CADENCE: ("cdc", ["cdc", "cadence"]),
    LanguageKind.CAPNPROTO_SCHEMA: ("capnp", ["capnp", "capnproto_schema"]),
    LanguageKind.CEYLON: ("ceylon", ["ceylon"]),
    LanguageKind.CHAPEL: ("chpl", ["chpl", "chapel"]),
    LanguageKind.CHUCK: ("ck", ["ck", "chuck"]),
    LanguageKind.CIL: ("il", ["il", "cil"]),
    LanguageKind.CLARION: ("clw", ["clw", "clarion"]),
    LanguageKind.CLEAN: ("icl", ["icl", "dcl", "abc", "clean"]),
    LanguageKind.CLIPPER: ("prg", ["prg", "ch", "clipper"]),
    LanguageKind.COMPONENT_PASCAL: ("cp", ["cp", "cps", "component_pascal"]),
    LanguageKind.COOL: ("cl", ["cl", "cool"]),
    LanguageKind.CUE_LANG: ("cue", ["cue", "cue_lang"]),
    LanguageKind.CWL: ("cwl", ["cwl"]),
    LanguageKind.CYTHON: ("pyx", ["pyx", "pxd", "pxi", "cython"]),
    LanguageKind.DAFNY: ("dfy", ["dfy", "dafny"]),
    LanguageKind.DELPHI: ("dpr", ["pas", "dpr", "dpk", "dfm", "lfm", "delphi", "inc"]),
    LanguageKind.DYLAN: ("dylan", ["dylan", "lid", "intr"]),
    LanguageKind.ECL: ("ecl", ["ecl"]),
    LanguageKind.EIFFEL: ("e", ["e", "eif", "eiffel"]),
    LanguageKind.ESLINT_CONFIG: (".eslintrc.js", ["eslintrc.js", "eslintrc.cjs", "eslintrc.yaml", "eslintrc.yml", "eslintrc.json",    ".eslintrc", "eslint_config"]),
    LanguageKind.FACTOR: ("factor", ["factor"]),
    LanguageKind.FANTOM: ("fan", ["fan", "fantom"]),
    LanguageKind.FLATBUFFERS_SCHEMA: ("fbs", ["fbs", "flatbuffers_schema"]),
    LanguageKind.FREEMARKER_TPL: ("ftl", ["ftl", "freemarker_tpl"]),
    LanguageKind.FSTAR: ("fst", ["fst", "fsti", "fstar"]),
    LanguageKind.GAMS: ("gms", ["gms", "gams"]),
    LanguageKind.GCODE: ("gcode", ["gcode", "nc", "tap", "gco", "ngc", "cnc"]),
    LanguageKind.GHERKIN: ("feature", ["feature", "gherkin"]),
    LanguageKind.GIT_IGNORE: (".gitignore",  [".gitignore", ".dockerignore", ".npmignore", ".eslintignore", ".hgignore", ".p4ignore",    "ignore", ".gitattributes", ".gitmodules", ".mailmap", "gitignore"]),
    LanguageKind.GNUPLOT: ("gp", ["gp", "gnu", "plot", "plt", "gnuplot"]),
    LanguageKind.GOSU: ("gs", ["gs", "gsp", "gst", "gsx", "gosu"]),
    LanguageKind.HARBOUR: ("prg", ["prg", "hrb", "ch", "harbour"]),
    LanguageKind.IDL: ("pro", ["pro", "sav", "idl"]),
    LanguageKind.INFORM: ("inf", ["inf", "ulx", "z5", "z8", "ni", "i7x", "i6", "inform"]),
    LanguageKind.IO_LANG: ("io", ["io"]),
    LanguageKind.ISABELLE: ("thy", ["thy", "isabelle"]),
    LanguageKind.J_LANG: ("ijs", ["ijs", "j", "j_lang"]),
    LanguageKind.JCL: ("jcl", ["jcl", "job"]),
    LanguageKind.JOLIE: ("ol", ["ol", "iol", "jolie"]),
    LanguageKind.JQ: ("jq", ["jq"]),
    LanguageKind.JSONIQ: ("jsoniq", ["jq", "jsoniq"]),
    LanguageKind.KAITAI_STRUCT: ("ksy", ["ksy", "kaitai_struct"]),
    LanguageKind.KUSTO_KQL: ("kql", ["kql", "csl", "kusto_kql"]),
    LanguageKind.LABVIEW: ("vi", ["vi", "ctl", "lvproj", "lvlib", "labview"]),
    LanguageKind.LASSO: ("lasso", ["lasso", "lasso9", "lasso8", "inc", "ldml"]),
    LanguageKind.LEAN: ("lean", ["lean", "hlean"]),
    LanguageKind.LEX: ("l", ["l", "lex", "flex"]),
    LanguageKind.LIGO: ("ligo", ["ligo", "mligo", "religo", "jsligo"]),
    LanguageKind.LIQUID_TPL: ("liquid", ["liquid", "liquid_tpl"]),
    LanguageKind.LLVM_IR: ("ll", ["ll", "llvm_ir"]),
    LanguageKind.LOGO: ("lgo", ["lgo", "logo"]),
    LanguageKind.LOGTALK: ("lgt", ["lgt", "logtalk"]),
    LanguageKind.LSL: ("lsl", ["lsl"]),
    LanguageKind.MAPLE: ("mpl", ["mpl", "mw", "maple"]),
    LanguageKind.MATHEMATICA: ("wl", ["wl", "nb", "m", "ma", "cdf", "mathematica", "mt", "nbp"]),
    LanguageKind.MAXMSP: ("maxpat",  ["maxpat", "maxhelp", "maxjs", "mxt", "jit", "jxs", "maxproj", "maxcollective", "maxmsp"]),
    LanguageKind.MAXSCRIPT: ("ms", ["ms", "mcr", "maxscript"]),
    LanguageKind.MERCURY: ("m", ["m", "moo", "mercury"]),
    LanguageKind.METAL: ("metal", ["metal"]),
    LanguageKind.MODELICA: ("mo", ["mo", "modelica"]),
    LanguageKind.MODULA3: ("m3", ["m3", "i3", "mg", "ig", "modula3"]),
    LanguageKind.MONKEY_C: ("mc", ["mc", "monkey_c"]),
    LanguageKind.MONKEYX: ("monkey", ["monkey", "monkey2", "cxs", "build", "resource", "monkeyx"]),
    LanguageKind.MOVE_LANG: ("move", ["move", "move_lang"]),
    LanguageKind.MQL: ("mq4", ["mq4", "mq5", "mqh", "mql"]),
    LanguageKind.MUPAD: ("mu", ["mu", "mupad"]),
    LanguageKind.MXML: ("mxml", ["mxml"]),
    LanguageKind.MYRDDIN: ("myr", ["myr", "myrddin"]),
    LanguageKind.NETLOGO: ("nlogo", ["nlogo", "nlogo3d", "netlogo"]),
    LanguageKind.NEWLISP: ("lsp", ["lsp", "nl", "kif", "newlisp"]),
    LanguageKind.NEXTFLOW: ("nf", ["nf", "nextflow"]),
    LanguageKind.NU: ("nu", ["nu"]),
    LanguageKind.NUNJUCKS_TPL: ("njk", ["njk", "nunjucks", "nunjucks_tpl"]),
    LanguageKind.NWSCRIPT: ("nss", ["nss", "nwscript"]),
    LanguageKind.OBERON: ("ob2", ["ob2", "mod", "oberon"]),
    LanguageKind.OBJECT_PASCAL: ("pas", ["pas", "dpr", "dpk", "lpr", "lpk", "inc", "lfm", "object_pascal", "delphi","lazarus"]),
    LanguageKind.OBJECTIVEJ: ("j", ["j", "sj", "objectivej"]),
    LanguageKind.OCTAVE: ("m", ["m", "octave"]),
    LanguageKind.ODIN: ("odin", ["odin"]),
    LanguageKind.OPENAPI: ("yaml",  ["yaml", "yml", "json", "openapi", "openapi.yaml", "openapi.yml", "openapi.json", "swagger", "swagger.yaml", "swagger.yml", "swagger.json"]),
    LanguageKind.OPENQASM: ("qasm", ["qasm", "openqasm"]),
    LanguageKind.OZ: ("oz", ["oz"]),
    LanguageKind.P4_LANG: ("p4", ["p4", "p4_lang"]),
    LanguageKind.PAPYRUS_SCRIPT: ("psc", ["psc", "papyrus_script"]),
    LanguageKind.PARASAIL: ("psi", ["psi", "psl", "parasail"]),
    LanguageKind.PAWN: ("pwn", ["pwn", "inc", "sma", "pawn"]),
    LanguageKind.PICAT: ("pi", ["pi", "picat"]),
    LanguageKind.PICO_LISP: ("l", ["l", "pico_lisp"]),
    LanguageKind.PIKE: ("pike", ["pike", "pmod"]),
    LanguageKind.PONY: ("pony", ["pony"]),
    LanguageKind.POSTCSS: ("pcss", ["pcss", "postcss"]),
    LanguageKind.POWERBUILDER: ("pbl", ["pbl", "sra", "sru", "srw", "srf", "srs", "srd", "pbt", "powerbuilder",     "powerscript"]),
    LanguageKind.POWERFX: ("pfx", ["pfx", "fx", "powerfx"]),
    LanguageKind.PRETTIER_CONFIG: (".prettierrc", [".prettierrc", ".prettierrc.json", ".prettierrc.yml", ".prettierrc.yaml",  ".prettierrc.js", ".prettierrc.cjs", "prettier.config.js", "prettier.config.cjs",  "prettier_config"]),
    LanguageKind.PROMELA: ("pml", ["pml", "promela"]),
    LanguageKind.PUREBASIC: ("pb", ["pb", "pbi", "purebasic"]),
    LanguageKind.PUPPET: ("pp", ["pp", "puppet"]),
    LanguageKind.QSHARP: ("qs", ["qs", "qsharp"]),
    LanguageKind.RBS: ("rbs", ["rbs"]),
    LanguageKind.REBOL: ("reb", ["r", "r3", "reb", "rebol"]),
    LanguageKind.RESCRIPT: ("res", ["res", "resi", "rescript"]),
    LanguageKind.REXX: ("rexx", ["rexx", "rex", "rx", "cmd", "pprx"]),
    LanguageKind.RING: ("ring", ["ring"]),
    LanguageKind.ROFF: ("roff",    ["roff", "man", "mdoc", "me", "ms", "mom", "tmac", "1", "2", "3", "4", "5", "6", "7", "8",   "9"]),
    LanguageKind.RPG: ("rpgle", ["rpgle", "rpg", "sqlrpgle"]),
    LanguageKind.SEED7: ("s7i", ["s7i", "sd7", "seed7"]),
    LanguageKind.SELF_LANG: ("self", ["self", "self_lang"]),
    LanguageKind.SHEN: ("shen", ["shen"]),
    LanguageKind.SIMULA: ("sim", ["sim", "simula"]),
    LanguageKind.SMALI: ("smali", ["smali"]),
    LanguageKind.SNAKEMAKE: ("smk", ["smk", "Snakefile", "snakemake"]),
    LanguageKind.SNOBOL: ("sno", ["sno", "snobol", "spt"]),
    LanguageKind.SQUIRREL: ("nut", ["nut", "gnut", "squirrel"]),
    LanguageKind.STARLARK: ("bzl", ["bzl", "bazel", "starlark"]),
    LanguageKind.SWAGGER: ("json", ["json", "yaml", "yml", "swagger"]),
    LanguageKind.SWIG: ("i", ["i", "swg", "swig"]),
    LanguageKind.TADS: ("t", ["t", "t3", "td", "t3s", "t3m", "dat", "tads"]),
    LanguageKind.TEA_LANG: ("tea", ["tea", "tea_lang"]),
    LanguageKind.TERSER: (".terserrc", ["js", ".terserrc", ".terserrc.json", "terser.config.js", "terser"]),
    LanguageKind.TURING: ("t", ["t", "tu", "tur", "turing"]),
    LanguageKind.UNICON: ("icn", ["icn", "u", "ui", "unicon"]),
    LanguageKind.URWEB: ("ur", ["ur", "urs", "urp", "urweb"]),
    LanguageKind.VISUAL_BASIC_CLASSIC: ("bas",["bas", "frm", "cls", "ctl", "dsr", "vbp", "vba", "vbs", "vb_classic", "vb"]),
    LanguageKind.VISUAL_FOXPRO: ("prg",["prg", "vcx", "scx", "dbc", "frx", "lbx", "mnx", "pjx", "qpr", "visual_foxpro", "dbf", "h"]),
    LanguageKind.VLANG: ("v", ["v", "vsh", "vlang"]),
    LanguageKind.VYPER: ("vy", ["vy", "vyper"]),
    LanguageKind.WENYAN: ("wy", ["wy", "wenyan"]),
    LanguageKind.WGSL: ("wgsl", ["wgsl"]),
    LanguageKind.WHILEY: ("whiley", ["whiley"]),
    LanguageKind.WOLFRAM: ("wl", ["wl", "nb", "m", "wls", "wolfram"]),
    LanguageKind.X10: ("x10", ["x10"]),
    LanguageKind.XAML: ("xaml", ["xaml"]),
    LanguageKind.XOJO: ("xojo_code", ["xojo_code", "xojo_project", "xojo_window", "xojo_menu", "xojo_toolbar", "xojo"]),
    LanguageKind.XPROC: ("xpl", ["xpl", "xproc"]),
    LanguageKind.XTEND: ("xtend", ["xtend"]),
    LanguageKind.YACC: ("y", ["y", "yacc", "bison"]),
    LanguageKind.ZEEK: ("zeek", ["zeek", "bro", "bif"]),
    LanguageKind.ZEPHIR: ("zep", ["zep", "zephir"]),
    LanguageKind.ZIMPL: ("zpl", ["zpl", "zmpl", "zimpl"]),




    # Unreal 5 releated
    LanguageKind.UNREAL_PROJECT: ("uproject", ["uproject"]),
    LanguageKind.UNREAL_PLUGIN_DESCRIPTOR: ("uplugin", ["uplugin"]),
    LanguageKind.UNREAL_CONFIG_INI: ("ini", ["ini"]),  # Primary 'ini' for broader matching
    LanguageKind.UNREAL_SHADER_FILE: ("usf", ["usf", "ush"]),  # 'usf' primary, also matches 'ush'
    LanguageKind.UNREAL_SHADER_HEADER: ("ush", ["ush"]),
    LanguageKind.UNREAL_BUILD_SCRIPT_CS: ("cs", ["cs", "Build.cs", "Target.cs"]),  # Primary 'cs'
    LanguageKind.UNREAL_ASSET: ("uasset", ["uasset"]),
    LanguageKind.UNREAL_MAP: ("umap", ["umap"]),
    LanguageKind.UNREAL_MODULES_FILE: ("modules", ["modules"]),  # Filename based
    LanguageKind.UNREAL_VERSION_FILE: ("version", ["version", "Engine.version"]),  # Filename pattern
    LanguageKind.UNREAL_H_GENERATED: ("generated.h", ["generated.h", "gen.h"]),  # More specific first

    LanguageKind.VERSE: ("verse", ["verse"]),
    LanguageKind.UNREAL_ASSET_BINARY: ("uasset", ["uasset", "umap"]),  # Covers both
    LanguageKind.UNREAL_PLUGIN_MANIFEST: ("upluginmanifest", ["upluginmanifest"]),
    LanguageKind.UNREAL_AUTOMATION_TEST_JSON: ("automation.json", ["automation.json"]),  # Full filename
    LanguageKind.UNREAL_UBT_MANIFEST: ("ubtmanifest", ["ubtmanifest", "manifest"]),  # manifest is more generic
    LanguageKind.UNREAL_BUILD_RECEIPT: ("target", ["target"]),  # Can be MyProject.target
    LanguageKind.UNREAL_BUILD_RESPONSE_FILE: ("response", ["response"]),  # Typically *.response

    LanguageKind.UNREAL_LEGACY_PACKAGE: ("upk", ["upk", "udk"]),
    LanguageKind.UNREAL_LEGACY_COMPILED_SCRIPT: ("u", ["u"]),
    LanguageKind.UNREAL_LOC_MANIFEST: ("manifest", ["manifest"]),  # e.g., Game.manifest
    LanguageKind.UNREAL_LOC_ARCHIVE: ("archive", ["archive"]),  # e.g., Game.archive
    LanguageKind.UNREAL_LOC_PO: ("po", ["po"]),
    LanguageKind.UNREAL_PLUGIN_MANIFEST_UGS: ("upluginmanifest", ["upluginmanifest"]),  # Specific to UGS
    LanguageKind.UNREAL_TARGET_DEF_JSON: ("target", ["target"]),  # e.g., MyGame.target (JSON definition)
    LanguageKind.UNREAL_SHADER_PIPELINE_CACHE: ("upipelinecache", ["upipelinecache", "shk"]),
    LanguageKind.UNREAL_SHADER_MAP_COOKED: ("ushadermap", ["ushadermap"]),
    LanguageKind.UNREAL_GLOBAL_SHADER_CACHE: ("gsc", ["gsc"]),
    LanguageKind.UNREAL_PLUGIN_FRIEND_DECL: ("upluginfriend", ["upluginfriend"]),
    LanguageKind.UNREAL_PROJECT_DIRS_UGS: ("uprojectdirs", ["uprojectdirs"]),
    LanguageKind.UNREAL_BUILD_TOOL_MANIFEST_XML: ("ubtmanifest", ["ubtmanifest", "xml"]),  # XML variant
    LanguageKind.UNREAL_BUILD_GRAPH_XML: ("xml", ["xml"]),  # Typically named *.Build.xml or similar
    LanguageKind.UNREAL_REMOTE_EXECUTION_SETTINGS: ("urs", ["urs", "xml"]),
    LanguageKind.UNREAL_DATA_ASSET: ("uasset", ["uasset"]),  # Specific type of uasset
    LanguageKind.UNREAL_TRANSLATION_PICKLE: ("utp", ["utp"]),
    LanguageKind.UNREAL_SHADER_DEBUG_INFO: ("ushaderdebuginfo", ["ushaderdebuginfo"]),
    LanguageKind.UNREAL_PLUGIN_RESOURCES: ("uresources", ["uresources"]),
    LanguageKind.UNREAL_INPUT_MAPPING_PROFILE: ("uinputprofile", ["uinputprofile"]),
    LanguageKind.UNREAL_ANIMATION_CURVE_COMPRESSION_SETTINGS: ("uac", ["uac"]),
    LanguageKind.UNREAL_NATIVE_VISUALIZER: ("natvis", ["natvis"]),
    LanguageKind.UNREAL_CPP_INL: ("inl", ["inl"]),
    LanguageKind.UNREAL_CPP_GENERATED: ("gen.cpp", ["gen.cpp", "generated.cpp"]),  # Common patterns
    LanguageKind.UNREAL_LOG: ("log", ["log"]),
    LanguageKind.UNREAL_UHT_MANIFEST: ("uhtmanifest", ["uhtmanifest"]),
    LanguageKind.TREE: ("txt", ["txt"]),


}



def get_all_extensions() -> List[str]:
    all_exts: set[str] = set()
    for _, (_, extensions_list) in LANGUAGE_EXTENSIONS_MAPPING.items():
        for ext in extensions_list:
            all_exts.add(ext.lstrip('.'))
    return sorted(list(all_exts))


ALL_EXTENSION_SET = set(f"{e}" for e in get_all_extensions())
ALL_LANGUAGES_SET: Set[str] = set(f"{e.value}" for e in LanguageKind)
