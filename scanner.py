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

    def __init__(self, equation: str):
        self.equation = equation
        self.tokens: list[Token] = []
        self.pos = 0

    def scan(self):
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
        start_col = self.pos + 1

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
                return Token(TokenType.BLAD, f"Niepoprawny format liczby '{token_val}' w kolumnie {start_col}")

            return Token(TokenType.LICZBA, int(token_val))

        # ID - zmienne
        if char.isalpha():
            token_val = ""
            while self.pos < len(self.equation) and self.equation[self.pos].isalnum():
                token_val += self.equation[self.pos]
                self.pos += 1

            return Token(TokenType.ID, token_val)

        # Operatory matematyczne
        if char in self.math_chars:
            self.pos += 1
            return Token(self.math_chars[char], char)

        # Obsluga bledu
        self.pos += 1
        return Token(TokenType.BLAD, f"Nieznany znak '{char}' w kolumnie {start_col}")

    def show_tokens(self):
        for token in self.tokens:
            print(token)

    def get_tokens(self):
        return self.tokens