from enums import TokenType

class Token():
    def __init__(self, token_type: TokenType, value, start_pos, end_pos):
        self.token_type = token_type
        self.value = value
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __str__(self):
        if self.token_type != TokenType.BLAD:
            return f"[{self.token_type.name}, {self.value}]"
        elif self.start_pos == self.end_pos:
            return f"[{self.token_type.name}, Nieznany znak '{self.value}' w kolumnie {self.start_pos + 1}]"
        else:
            return f"[{self.token_type.name}, Niepoprawny format liczby '{self.value}' w kolumnie {self.start_pos + 1}]"


