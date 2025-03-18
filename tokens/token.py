from tokens.token_type import TokenType


class Token:
	def __init__(self, value, type):
		self.value: str = value
		self.type: TokenType = type
	
	def __repr__(self):
		return f"[{self.type.name}:{self.value}]"
