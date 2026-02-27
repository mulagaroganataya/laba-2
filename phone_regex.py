import re
from dataclasses import dataclass
from typing import List

PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+7|8|7)\s*\(?\d{3}\)?[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}(?!\w)"
)


def find_phone_numbers(text: str) -> List[str]:
    """Найти все телефоны в тексте по регулярному выражению (raw-совпадения)."""
    return PHONE_PATTERN.findall(text)


def normalize_phone(phone: str) -> str:
    """
    Нормализует телефон к формату +7XXXXXXXXXX.
    Допускает входные варианты с +7 / 7 / 8, пробелами/скобками/дефисами.
    """
    digits = re.sub(r"\D+", "", phone)

    if len(digits) != 11:
        raise ValueError(f"Invalid length after cleanup: {digits}")

    if digits[0] == "8":
        digits = "7" + digits[1:]
    elif digits[0] != "7":
        raise ValueError(f"Invalid prefix: {digits}")

    return "+" + digits


@dataclass(frozen=True)
class PhoneHit:
    """Результат поиска телефона: исходный вид и нормализованное значение."""
    raw: str
    normalized: str


def extract_hits(text: str) -> List[PhoneHit]:
    """Найти телефоны и вернуть список PhoneHit (raw + normalized)."""
    hits: List[PhoneHit] = []
    for raw in find_phone_numbers(text):
        try:
            hits.append(PhoneHit(raw=raw, normalized=normalize_phone(raw)))
        except ValueError:
            pass
    return hits