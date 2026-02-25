from phone_regex import extract_hits


def main() -> None:
    text = """
    Контакты: +7 999 123-45-67, 8 (912) 000-11-22, +7(495)1234567.
    Мусор: +7 999 123-45-6, abc+79991234567def
    """
    hits = extract_hits(text)
    print(f"Hits: {len(hits)}")
    for i, h in enumerate(hits, 1):
        print(f"{i}. raw={h.raw} -> normalized={h.normalized}")


if __name__ == "__main__":
    main()