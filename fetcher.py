import requests


def load_text_from_url(url: str, timeout: int = 10) -> str:
    """Скачать страницу по URL и вернуть HTML/текст."""
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def load_text_from_file(path: str, encoding: str = "utf-8") -> str:
    """Загрузить текст из файла."""
    with open(path, "r", encoding=encoding) as f:
        return f.read()