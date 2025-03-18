class Token:
    def __init__(self, name, value, start, line, col):
        self.name = name
        self.value = value
        self.start = start
        self.line = line
        self.col = col

    def __repr__(self):
        return f"[{self.name}:{self.value}] ({self.line}:{self.col})"


# keyword
# identifier
# constant
# operator
# symbol
