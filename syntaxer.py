import json

from tokens.token_type import TokenType


class ASTNode:
    """Represents a node in the Abstract Syntax Tree."""
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # e.g., "Function", "Expression", "Assignment"
        self.value = value  # The value of the node (if any)
        self.children = []  # Child nodes

    def add_child(self, child):
        """Adds a child node to this AST node."""
        self.children.append(child)

    def to_dict(self):
        """Converts the AST into a dictionary for easy JSON serialization."""
        return {
            "node_type": self.node_type,
            "value": self.value,
            "children": [child.to_dict() for child in self.children]
        }


class AST:
    """Manages the construction of the AST from tokens and the symbol table."""
    def __init__(self, tokens, symbol_table):
        self.tokens = tokens
        self.symbol_table = symbol_table
        self.root = ASTNode("Program")  # The root of the AST

    def build_ast(self):
        """Parses tokens to create an AST."""
        token_iterator = iter(self.tokens)

        for token in token_iterator:
            if token.type == TokenType.Keyword:
                if token.value in {"func", "mthd"}:  # Function definition
                    function_node = ASTNode("Function", token.value)
                    next_token = next(token_iterator, None)

                    if next_token and next_token.type == TokenType.Identifier:
                        function_node.add_child(ASTNode("Identifier", next_token.value))

                    self.root.add_child(function_node)

                elif token.value in {"let", "const"}:  # Variable declaration
                    next_token = next(token_iterator, None)
                    if next_token and next_token.type == TokenType.Identifier:
                        var_node = ASTNode("VariableDeclaration", next_token.value)
                        self.root.add_child(var_node)

                elif token.value in {"return"}:  # Return statement
                    return_node = ASTNode("ReturnStatement")
                    next_token = next(token_iterator, None)
                    if next_token:
                        return_node.add_child(ASTNode("Expression", next_token.value))
                    self.root.add_child(return_node)

            elif token.type == TokenType.AssignmentOperator:  # Assignment statements
                prev_token = self.tokens[self.tokens.index(token) - 1]
                next_token = next(token_iterator, None)
                if prev_token and next_token:
                    assign_node = ASTNode("Assignment", token.value)
                    assign_node.add_child(ASTNode("Identifier", prev_token.value))
                    assign_node.add_child(ASTNode("Expression", next_token.value))
                    self.root.add_child(assign_node)

    def to_json(self):
        """Converts the AST to a JSON string."""
        return json.dumps(self.root.to_dict(), indent=4)
