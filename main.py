from fetcher import load_text_from_file
from phone_regex import extract_hits


def main() -> None:
    demo_path = "demo_input.txt"
    with open(demo_path, "w", encoding="utf-8") as f:
        f.write("Звоните: +7 903 111-22-33 или 8(495)7778899")

    text = load_text_from_file(demo_path)
    hits = extract_hits(text)
    print("Text:", text)
    print("Hits:", hits)


if __name__ == "__main__":
    main()
