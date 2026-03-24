from reporter import Reporter


def main():
    reporter = Reporter()

    text = "2 + &&3 * (10 1a / 2)"
    reporter.print_tokens(text)

    in_file = "dane.txt"
    out_file = "wynik.html"
    reporter.to_html(in_file, out_file)

if __name__ == "__main__":
    main()