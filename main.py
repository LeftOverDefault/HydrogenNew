from syntaxer import AST
from lexer import Lexer


if __name__ == "__main__":
    lexer = Lexer()

    source = ""

    with open("./test.hy", "r") as source_object:
        source = source_object.read()

    lexer.add_source(source)

    lexer.tokenize()
    lexer.create_symbol_table()

    # lexer.print_symbol_table()

    ast = AST(lexer.tokens, lexer.symbol_table)

    ast.build_ast()

    print(ast.to_json())
