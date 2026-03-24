from enums import TokenType
from token import Token

class Scanner:
    math_chars = {
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
        '*': TokenType.MNOZENIE,
        '/': TokenType.DZIELENIE,
        '(': TokenType.LNAWIAS,
        ')': TokenType.PNAWIAS,
    }

    def __init__(self):
        self.tokens: list[Token] = []
        self.pos = 0

    def reset_tokens(self):
        self.tokens = []
        self.pos = 0

    def scan(self, equation: str):
        self.equation = equation
        self.reset_tokens()

        while True:
            token = self.next_token()
            if token is None:
                break
            self.tokens.append(token)

    def next_token(self) -> Token:
        # Pomijanie spacji
        while self.pos < len(self.equation) and self.equation[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.equation):
            return None

        char = self.equation[self.pos]
        start_pos = self.pos

        # Liczby
        if char.isdigit():
            token_val = ""
            while self.pos < len(self.equation) and self.equation[self.pos].isdigit():
                token_val += self.equation[self.pos]
                self.pos += 1

            # Sprawdzanie poprawności liczby
            if self.pos < len(self.equation) and self.equation[self.pos].isalpha():
                while self.pos < len(self.equation) and self.equation[self.pos].isalnum():
                    token_val += self.equation[self.pos]
                    self.pos += 1
                return Token(TokenType.BLAD, token_val, start_pos, self.pos)

            return Token(TokenType.LICZBA, token_val, start_pos, self.pos)

        # ID - zmienne
        if char.isalpha():
            token_val = ""
            while self.pos < len(self.equation) and self.equation[self.pos].isalnum():
                token_val += self.equation[self.pos]
                self.pos += 1

            return Token(TokenType.ID, token_val, start_pos, self.pos)

        # Operatory matematyczne
        if char in self.math_chars:
            self.pos += 1
            return Token(self.math_chars[char], char, start_pos, self.pos)

        # Obsluga bledu
        self.pos += 1
        return Token(TokenType.BLAD, char, start_pos, self.pos)

    def get_tokens(self):
        return self.tokens