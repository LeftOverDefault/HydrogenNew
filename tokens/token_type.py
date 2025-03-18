from enum import Enum, auto


class TokenType(Enum):
    Punctuator = "Punctuator",
    Keyword = "Keyword",
    IntegerLiteral = "IntegerLiteral",
    RealLiteral = "RealLiteral",
    BooleanLiteral = "BooleanLiteral",
    StringLiteral = "StringLiteral",
    UnaryOperator = "UnaryOperator",
    ArithmeticOperator = "ArithmeticOperator",
    RelationalOperator = "RelationalOperator",
    LogicalOperator = "LogicalOperator",
    AssignmentOperator = "AssignmentOperator",
    BitwiseOperator = "BitwiseOperator",
    TernaryOperator = "TernaryOperator",
    Constant = "Constant",
    Identifier = "Identifier",


