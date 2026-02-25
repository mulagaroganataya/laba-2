from phone_regex import find_phone_numbers, normalize_phone


def main() -> None:
    text = "abc+79991234567def Контакты: +7 999 123-45-67 и 8 (912) 000-11-22"
    found = find_phone_numbers(text)
    print("Found:", found)
    for p in found:
        print(" ", p, "->", normalize_phone(p))


if __name__ == "__main__":
    main()
