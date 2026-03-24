import html
from enums import TokenType
from scanner import Scanner


class Reporter:
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

    def print_tokens(self, text: str):
        """Wypisuje tokeny w konsoli korzystając z formatowania w klasie Token."""
        scanner = Scanner()
        scanner.scan(text)
        tokens = scanner.get_tokens()

        print("===TOKENY===")
        for token in tokens:
            print(token)
        print("============")

    def to_html(self, in_file: str, out_file: str):
        """Generuje pokolorowany plik HTML na podstawie pliku tekstowego z zachowaniem układu."""
        with open(in_file, "r", encoding="utf-8") as f:
            text = f.read()

        scanner = Scanner()
        scanner.scan(text)
        tokens = scanner.get_tokens()

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