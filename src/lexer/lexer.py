import re

from src.lexer.tokens import Token


class Lexer:
    def __init__(self) -> None:
        self.tokens = []
        self.start = 0
        self.line = 1
        self.col = 1

        self.token_pattern = re.compile(
            # r'\b\w+(?:_\w+)*\b|"[^"]*"|\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?|==|<=|>=|[\+\-\*/(){}=;:,\.]'
            # r'\b\w+(?:_\w+)*\b|"[^"]*"|\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?|==|<=|>=|[\+\-\*/(){}=;:,\.]'
            r'\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?|\b\w+(?:_\w+)*\b|"[^"]*"|==|<=|>=|[\+\-\*/(){}=;:,\.]'
        )
    
    def tokenize(self, source: str) -> list:
        self.tokens = []  # Reset tokens list
        self.start = 0    # Reset start position
        self.line = 1     # Reset line counter
        self.col = 1      # Reset column counter

        # Iterate over matches using finditer
        for match in self.token_pattern.finditer(source):
            value = match.group()
            start = match.start() - 1

            # Calculate line and column numbers
            self._update_position(source, start)

            # Create and add the token
            token = Token(self._get_token_type(value), value, start, self.line, self.col)
            self.tokens.append(token)

            # Update the column position for the next token
            self.col += len(value)

        return self.tokens

    def _update_position(self, source: str, start: int):
        """Update the line and column numbers based on the current position."""
        # Calculate the number of newlines between the last position and the current position
        newline_pos = source.rfind('\n', self.start, start)
        if newline_pos != -1:
            # There is at least one newline between self.start and start
            self.line += source.count('\n', self.start, start)
            self.col = start - newline_pos  # Column is the position after the last newline
        else:
            # No newlines, just increment the column
            self.col += start - self.start

        # Update the start position
        self.start = start

    def _get_token_type(self, value: str) -> str:
        """Determine the type of the token based on its value."""
        if re.match(r'\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?', value):
            return 'NUMBER'
        elif re.match(r'\b\w+(?:_\w+)*\b', value):
            return 'IDENTIFIER'
        elif re.match(r'"[^"]*"', value):
            return 'STRING'
        elif re.match(r'==|<=|>=', value):
            return 'OPERATOR'
        elif re.match(r'[\+\-\*/(){}=;:,\.]', value):
            return 'SYMBOL'
        else:
            return 'UNKNOWN'

    # def tokenize(self, source: str) -> list:
    #     self.tokens = []  # Reset tokens list
    #     self.line = 1     # Reset line counter
    #     self.col = 1      # Reset column counter

    #     for match in self.token_pattern.findall(source):  
    #         token = Token("token", match, self.start, self.line, self.col)
    #         self.tokens.append(token)
        
    #     return self.tokens

