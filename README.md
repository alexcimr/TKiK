# Skaner

Skaner dla wyrażeń matematycznych, który przekształca ciąg znaków wejściowych na ciąg tokenów.

Język implementacji: ***Python***

## Zbiór Tokenów
Poniższa tabela przedstawia zbiór tokenów rozpoznawanych przez skaner, ich nazwy, opisy oraz użyte kolory.

| Nazwa | Opis | Kolor (HTML) |
| :--- | :--- | :--- |
| **LICZBA** | Liczba całkowita. | **Zielony** (`green`) |
| **ID** | Identyfikator / zmienna. | **Niebieski** (`blue`) |
| **PLUS** | Operator dodawania `+`. | **Pomarańczowy** (`orange`) |
| **MINUS** | Operator odejmowania `-`. | **Fioletowy** (`purple`) |
| **MNOZENIE** | Operator mnożenia `*`. | **Magenta** (`magenta`) |
| **DZIELENIE** | Operator dzielenia `/`. | **Cyjan** (`cyan`) |
| **LNAWIAS** | Lewy nawias okrągły `(`. | **Brązowy** (`brown`) |
| **PNAWIAS** | Prawy nawias okrągły `)`. | **Różowy** (`deeppink`) |
| **BLAD** | Nieznany znak lub zły format liczby. | **Czerwony** (`red`) |