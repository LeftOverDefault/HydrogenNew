from src.lexer import Lexer


source_code = """
let x: int = 42;
const y: str = "Hello, World!";

class MyClass {
    mthd myMethod(param1, param2) {
        let z: bool = true;
        let pi: int = 3.141_592_654;
    }
}
"""


if __name__ == "__main__":
    lexer = Lexer()
    for lexeme in lexer.tokenize(source_code):
        print(lexeme)
