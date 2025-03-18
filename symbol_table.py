class SymbolTable:
    def __init__(self):
        self.table = {}

    def define(self, token):
        """Add an identifier to the symbol table with a unique hash key."""
        index = hash(token.value) % 1000  # Simple hash function for indexing
        self.table[index] = {
            "Token Value": token.value,
            "Token Type": token.type.name,
            "Data Type": None  # Data type is determined during syntax analysis
        }

    def __repr__(self):
        """Formats the symbol table as a readable string."""
        output = "+---------+---------------+--------------------+-------------+\n"
        output += "|  Index  |  Token Value  |  Token Type        |  Data Type  |\n"
        output += "+---------+---------------+--------------------+-------------+\n"
        for index, entry in self.table.items():
            output += f"| {str(index).ljust(7)} | {entry['Token Value'].ljust(13)} | {entry['Token Type'].ljust(18)} | {str(entry['Data Type']).ljust(11)} |\n"
        output += "+---------+---------------+--------------------+-------------+\n"
        return output
