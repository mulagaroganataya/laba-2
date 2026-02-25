import re
from typing import List

PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+7|8)\s*\(?\d{3}\)?[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}(?!\w)"
)


def find_phone_numbers(text: str) -> List[str]:
    return PHONE_PATTERN.findall(text)


def normalize_phone(phone: str) -> str:
    digits = re.sub(r"\D+", "", phone)

    if len(digits) != 11:
        raise ValueError(f"Invalid length after cleanup: {digits}")

    if digits[0] == "8":
        digits = "7" + digits[1:]
    elif digits[0] != "7":
        raise ValueError(f"Invalid prefix: {digits}")

    return "+" + digits


def main() -> None:
    text = "abc+79991234567def Контакты: +7 999 123-45-67 и 8 (912) 000-11-22"
    found = find_phone_numbers(text)
    print("Found:", found)  # должно НЕ цеплять номер внутри abc...def
    for p in found:
        print(" ", p, "->", normalize_phone(p))


if __name__ == "__main__":
    main()
