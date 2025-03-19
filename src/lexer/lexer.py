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
        self.col = 0      # Reset column counter
        current_col = 0   # Tracks column correctly after newlines
        
        for match in self.token_pattern.finditer(source):
            value = match.group()
            start = match.start()
            
            # Update line and column tracking
            while self.start < start:
                if source[self.start] == '\n':
                    self.line += 1
                    current_col = 0
                else:
                    current_col += 1
                self.start += 1
            
            self.col = current_col  # Set column before token
            
            # Create and add the token
            token = Token(self._get_token_type(value), value, start, self.line, self.col)
            self.tokens.append(token)

            # Update column tracking for next token
            current_col += len(value)
            self.start = start + len(value)
        
        return self.tokens


    def _update_position(self, source: str, start: int):
        """Update the line and column numbers using iteration instead of rfind."""
        if start < self.start:
            return  # Prevent regression in tracking

        # Iterate through the substring to count newlines and track column position
        for i in range(self.start, start):
            if source[i] == '\n':
                self.line += 1
                self.col = 0  # Reset column after newline
            else:
                self.col += 1  # Increment column for non-newline characters

        self.start = start


    def _get_token_type(self, value: str) -> str:
        """Determine the type of the token based on its value."""
        if re.fullmatch(r'\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?', value):
            return 'NUMBER'
        elif re.fullmatch(r'\b\w+(?:_\w+)*\b', value):
            return 'IDENTIFIER'
        elif re.fullmatch(r'"[^"]*"', value):
            return 'STRING'
        elif re.fullmatch(r'==|<=|>=', value):
            return 'OPERATOR'
        elif re.fullmatch(r'[\+\-\*/(){}=;:,.]', value):
            return 'SYMBOL'
        else:
            return 'UNKNOWN'
