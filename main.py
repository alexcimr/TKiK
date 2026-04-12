from scanner import Scanner


def main():

    text = "2 + &&3 * (10 1a / 2)"

    scanner = Scanner()
    scanner.scan(text)
    tokens = scanner.get_tokens()

    print("===TOKENY===")
    for token in tokens:
        print(token)
    print("============")

    
    in_file = "dane.txt"
    out_file = "wynik.html"
    scanner.to_html(in_file, out_file)

if __name__ == "__main__":
    main()