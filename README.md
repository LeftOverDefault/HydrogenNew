```
hydrogen-compiler/
├── src/                     # Main source code directory
│   ├── lexer/               # Lexer module
│   │   ├── __init__.py      # Lexer package initialization
│   │   ├── lexer.py         # Lexer implementation
│   │   └── tokens.py        # Token class definition
│   ├── parser/              # Parser module
│   │   ├── __init__.py      # Parser package initialization
│   │   ├── parser.py        # Parser implementation
│   │   └── ast.py           # Abstract Syntax Tree (AST) node definitions
│   ├── semantic_analyzer/   # Semantic analyzer module
│   │   ├── __init__.py      # Semantic analyzer package initialization
│   │   └── analyzer.py      # Semantic analyzer implementation
│   ├── code_generator/      # Code generator module
│   │   ├── __init__.py      # Code generator package initialization
│   │   └── generator.py     # Code generator implementation
│   ├── utils/               # Utility functions and helpers
│   │   ├── __init__.py      # Utils package initialization
│   │   ├── errors.py        # Custom error classes
│   │   └── logger.py        # Logging utilities
│   ├── compiler.py          # Main compiler driver
│   └── __init__.py          # Package initialization
├── tests/                   # Unit and integration tests
│   ├── lexer/               # Tests for the lexer
│   │   └── test_lexer.py
│   ├── parser/              # Tests for the parser
│   │   └── test_parser.py
│   ├── semantic_analyzer/   # Tests for the semantic analyzer
│   │   └── test_analyzer.py
│   ├── code_generator/      # Tests for the code generator
│   │   └── test_generator.py
│   └── __init__.py          # Tests package initialization
├── examples/                # Example Hydrogen programs
│   ├── hello.hydrogen       # Example Hydrogen source file
│   └── factorial.hydrogen   # Another example
├── grammar/                 # Grammar and language specification
│   └── grammar.txt          # Formal grammar definition
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── main.py                  # Entry point for the compiler
```
