import re
from typing import List

PHONE_PATTERN = re.compile(
    r"(?:\+7|8)\s*\(?\d{3}\)?[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}"
)


def find_phone_numbers(text: str) -> List[str]:
    return PHONE_PATTERN.findall(text)


def main() -> None:
    text = "Контакты: +7 999 123-45-67, 8 (912) 000-11-22, +7(495)1234567"
    print("Found:", find_phone_numbers(text))


if __name__ == "__main__":
    main()
