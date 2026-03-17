from enums import TokenType

class Token():
    def __init__(self, token_type: TokenType, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"[{self.token_type.name}, {self.value}]"