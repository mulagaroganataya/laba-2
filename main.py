from fetcher import load_text_from_url
from phone_regex import extract_hits


def main() -> None:
    url = "https://example.com"
    try:
        text = load_text_from_url(url)
        print(f"Loaded {len(text)} chars from {url}")
        print("Hits:", extract_hits(text))
    except Exception as e:
        print("URL loading failed (ok for offline env):", repr(e))


if __name__ == "__main__":
    main()