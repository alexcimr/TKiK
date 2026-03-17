# Skaner

Skaner dla wyrażeń matematycznych, który przekształca ciąg znaków wejściowych na ciąg tokenów.

Język implementacji: ***Python***


## Zbiór Tokenów
Poniższa tabela przedstawia zbiór tokenów rozpoznawanych przez skaner, ich nazwy oraz opis.

| Nazwa | Opis | Przykład |
| :--- | :--- | :--- |
| **LICZBA** | Liczba całkowita (ciąg cyfr). | `1`, `64`, `123` |
| **ID** | Identyfikator / zmienna (zaczyna się od litery, potem dowolne litery i cyfry). | `x`, `b2`, `wynik` |
| **PLUS** | Operator dodawania `+`. | `+` |
| **MINUS** | Operator odejmowania `-`. | `-` |
| **MNOZENIE** | Operator mnożenia `*`. | `*` |
| **DZIELENIE** | Operator dzielenia `/`. | `/` |
| **LNAWIAS** | Lewy nawias okrągły `(`. | `(` |
| **PNAWIAS** | Prawy nawias okrągły `)`. | `)` |
| **BLAD** | Token błędu (nieznany znak lub niepoprawny format liczby). | `$`, `#`, `12ab` |
