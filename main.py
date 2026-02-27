from fetcher import load_text_from_file, load_text_from_url
from phone_regex import find_phone_numbers, normalize_phone, extract_hits


def main() -> None:
    print("=== DEMO: regex phone finder + normalize ===")

    sample_text = """
    Контакты:
      +7 999 123-45-67
      8 (912) 000-11-22
      7 901 222-33-44
      +7(495)1234567
    Мусор:
      +7 999 123-45-6   (короткий)
      abc+79991234567def (внутри слова)
    """

    print("\n--- 1) Поиск номеров в строке ---")
    found = find_phone_numbers(sample_text)
    print("Найдено raw-совпадений:", found)

    print("\n--- 2) Нормализация одного номера ---")
    phone = "8 (999) 123-45-67"
    print("raw:", phone, "-> normalized:", normalize_phone(phone))

    print("\n--- 3) Извлечение PhoneHit (raw + normalized) ---")
    hits = extract_hits(sample_text)
    for i, h in enumerate(hits, 1):
        print(f"{i}. raw={h.raw} -> normalized={h.normalized}")

    print("\n--- 4) Загрузка текста из файла (пример) ---")
    demo_path = "demo_input.txt"
    with open(demo_path, "w", encoding="utf-8") as f:
        f.write("Звоните: +7 903 111-22-33 или 8(495)7778899 или 7 901 222-33-44")

    file_text = load_text_from_file(demo_path)
    print("Текст из файла:", file_text)
    print("Телефоны из файла:", extract_hits(file_text))

    print("\n--- 5) Загрузка текста по URL (пример, может зависеть от сети) ---")
    test_url = "https://example.com"
    try:
        url_text = load_text_from_url(test_url)
        print(f"Загружено {len(url_text)} символов с {test_url}")
        print("Телефоны на странице:", extract_hits(url_text))
    except Exception as e:
        print("Не удалось загрузить URL (это нормально для оффлайн-среды):", repr(e))


if __name__ == "__main__":
    main()