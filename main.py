import re


def main() -> None:
    text = "Контакты: +7 999 123-45-67, 8 (912) 000-11-22, +7(495)1234567"
    pattern = re.compile(r"(?:\+7|8)\s*\(?\d{3}\)?[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}")
    matches = pattern.findall(text)
    print("Matches:", matches)


if __name__ == "__main__":
    main()
