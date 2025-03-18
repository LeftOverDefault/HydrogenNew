from symbol_table import SymbolTable

from tokens.token import Token
from tokens.token_type import TokenType


class Lexer():
    def __init__(self):
        self.source: str
        self.characters = []
        self.tokens: list[Token] = []

        self.punctuators = ["(", ")", "[", "]", "{", "}", ",", ":", ";", "."]
        self.keywords = ["class", "func", "mthd", "let", "const", "return", "true", "false"]
        self.arithmetic_operators = ["+", "-", "*", "/", "%"]
        self.relational_operators = ["==", "<", "<=", ">", ">=", "!=", "===", "!=="]
        self.assignment_operators = ["=", "+=", "-=", "*=", "/=", "%="]

        self.symbol_table = SymbolTable()  # Single global symbol table


    def add_source(self, source):
        self.source = source


    def tokenize(self):
        src = list(self.source)

        def shift(shift_index: int = 1) -> str:
            """Advances the cursor and returns the next character(s)."""
            output = ""
            for _ in range(shift_index):
                if src:
                    output += src.pop(0)
            return output
            # i = 0
            # output = ""
            # character = src[shift_index - 1]
            # while i < shift_index:
            #     src.remove(src[0])
            #     output += character
            #     i += 1
            # return str(output)

        while len(src) > 0:
            # PRIORITY
            # Punctuators: ()[]{},:;*=#.~
            # Keywords: str, int, for, if, else, while, return, etc.
            # Strings
            # Operators: 
            #   Unary Operators (++, --)
            #   Binary Operators:
            #       Arithmetic operators (+, -, /, *)
            #       Relational Operators (>=, >, <, <=, ==, !=, ===, !==)
            #       Logical Operators (&&, ||, !) (For True/False Values)
            #       Assignment Operators (=, +=, -=, *=, /=, %=)
            #       Bitwise Operator (&&, ||, !) (For Integer Bits)
            #   Ternary Operator (condition ? resultIfTrue : resultIfFalse )
            # Constants
            # Identifiers
            if src[0] in self.punctuators:
                self.tokens.append(Token(shift(), TokenType.Punctuator))
            elif src[0].isnumeric():
                number = ""
                while src[0].isnumeric() or src[0] == "." or src[0] == "_":
                    if src[0] == "_":
                        shift()
                    else:
                        number += str(shift())

                self.tokens.append(Token(number, TokenType.RealLiteral if "." in list(number) else TokenType.IntegerLiteral))
            elif src[0].isalnum():
                identifier = ""
                while src[0].isalnum() or src[0] == "_":
                    identifier += shift()

                if identifier.lower() in ["true", "false"]:
                    self.tokens.append(Token(identifier, TokenType.BooleanLiteral))
                elif identifier.lower() == "const":
                    self.tokens.append(Token(identifier, TokenType.Constant))
                elif identifier.lower() in self.keywords:
                    self.tokens.append(Token(identifier, TokenType.Keyword))
                else:
                    self.tokens.append(Token(identifier, TokenType.Identifier))
            elif src[0] == "\"":
                shift()
                string_literal = r""
                while src[0] != "\"":
                    if src[0] == "\\" and src[1] == "\"":
                        shift(2)
                        string_literal += "\\\""
                    else:
                        string_literal += shift()
                shift()
                self.tokens.append(Token(string_literal, TokenType.StringLiteral))
            elif src[0] in self.arithmetic_operators:
                self.tokens.append(Token(shift(), TokenType.ArithmeticOperator))
            elif src[0] in [">", "<", "=", "!"]:
                operator = shift()
                if src[0] == "=":
                    operator += shift()
                    if src[0] == "=" and list(operator)[0] not in [">", "<"]:
                        operator += shift()
                self.tokens.append(Token(operator, TokenType.RelationalOperator))
            elif src[0] in self.assignment_operators:
                self.tokens.append(Token(shift(), TokenType.AssignmentOperator))
            elif src[0] in ["&", "|", "!"]:
                if src[0] == "&" and src[1] == "&":
                    self.tokens.append(Token(shift(2), TokenType.LogicalOperator))
                elif src[0] == "|" and src[1] == "|":
                    self.tokens.append(Token(shift(2), TokenType.LogicalOperator))
                elif src[0] == "|":
                    self.tokens.append(Token(shift(), TokenType.LogicalOperator))
                elif src[0] == "!":
                    self.tokens.append(Token(shift(), TokenType.LogicalOperator))
                else:
                    raise SyntaxError(f"Token '{shift()}' does not exist in Current Hydrogen Tokens.")
            elif src[0] in ["\n", "\t", " "]:
                shift()
            else:
                raise SyntaxError(f"Token '{shift()}' does not exist in Current Hydrogen Tokens.")


    def create_symbol_table(self):
        """Adds identifiers and constants to the symbol table."""
        for token in self.tokens:
            if token.type in {TokenType.Identifier, TokenType.Constant}:
                self.symbol_table.define(token)
            else:
                self.symbol_table.define(token)


    def print_symbol_table(self):
        """Prints the symbol table."""
        print(self.symbol_table)
