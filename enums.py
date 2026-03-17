import enum

class TokenType(enum.Enum):
    LICZBA = "LICZBA"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MNOZENIE = "MNOZENIE"
    DZIELENIE = "DZIELENIE"
    LNAWIAS = "LNAWIAS"
    PNAWIAS = "PNAWIAS"
    ID = "ID"
    BLAD = "BLAD"
