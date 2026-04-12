from enums import TokenType
from token import Token
import html

class Scanner:
    math_chars = {
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
        '*': TokenType.MNOZENIE,
        '/': TokenType.DZIELENIE,
        '(': TokenType.LNAWIAS,
        ')': TokenType.PNAWIAS,
    }

    COLORS = {
        TokenType.LICZBA: "green",
        TokenType.ID: "blue",
        TokenType.PLUS: "orange",
        TokenType.MINUS: "purple",
        TokenType.MNOZENIE: "magenta",
        TokenType.DZIELENIE: "cyan",
        TokenType.LNAWIAS: "brown",
        TokenType.PNAWIAS: "deeppink",
        TokenType.BLAD: "red"
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

    def to_html(self, in_file: str, out_file: str):
        """Generuje pokolorowany plik HTML na podstawie pliku tekstowego z zachowaniem układu."""
        with open(in_file, "r", encoding="utf-8") as f:
            text = f.read()

        self.reset_tokens()
        self.scan(text)
        tokens = self.get_tokens()

        html_body = ""
        current_pos = 0

        # Przechodzenie przez tokeny
        for t in tokens:
            while current_pos < t.start_pos:
                html_body += html.escape(text[current_pos])
                current_pos += 1

            color = self.COLORS[t.token_type]
            val = html.escape(str(t.value))
            html_body += f'<span style="color: {color};">{val}</span>'

            current_pos = t.end_pos

        # Dodawanie bialych znakow po ostatnim tokenie
        while current_pos < len(text):
            html_body += html.escape(text[current_pos])
            current_pos += 1

        with open(out_file, "w", encoding="utf-8") as f:
            # <pre>: zachowanie układu (znaki białe)
            # monospace: czcionka stałoszerokościowa
            # font-size: wielkość czcionki
            # line-height przerwa między wierszami
            f.write(f"<pre style='font-family: monospace; font-size: 20px; line-height: 1.5;'>{html_body}</pre>")
