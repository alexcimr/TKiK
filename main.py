from scanner import Scanner


def main():
    equation = "2 +3   + a * (76+ 8  / 3.1) $+ 3 * (9 - 3) 1ab"
    scanner = Scanner(equation)
    scanner.scan()
    scanner.show_tokens()

if __name__ == "__main__":
    main()