class Token:
    def __init__(self, name, value, start, line, col):
        self.name = name
        self.value = value
        self.start = start
        self.line = line
        self.col = col

    def __repr__(self):
        first = f"[ {self.name:20} : {self.value:20} ]" 
        return f"{first:50} [ {self.line:4} : {self.col:4} ]"


# keyword
# identifier
# constant
# operator
# symbol
