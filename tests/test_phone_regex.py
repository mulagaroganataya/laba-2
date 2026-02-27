import unittest
from phone_regex import find_phone_numbers, normalize_phone, extract_hits


class TestPhoneRegex(unittest.TestCase):
    def test_find_valid_phones(self):
        text = "Контакты: +7 999 123-45-67, 8 (912) 000-11-22 и +7(495)1234567."
        found = find_phone_numbers(text)
        self.assertEqual(len(found), 3)

    def test_normalize_from_8(self):
        self.assertEqual(normalize_phone("8 (999) 123-45-67"), "+79991234567")

    def test_normalize_from_plus7(self):
        self.assertEqual(normalize_phone("+7 912 0001122"), "+79120001122")

    def test_normalize_reject_wrong_length(self):
        with self.assertRaises(ValueError):
            normalize_phone("+7 999 123-45-6")

    def test_extract_hits_pairs(self):
        text = "Мой номер: 8 (999) 123-45-67."
        hits = extract_hits(text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].raw, "8 (999) 123-45-67")
        self.assertEqual(hits[0].normalized, "+79991234567")

    def test_not_match_inside_word(self):
        text = "abc+79991234567def"
        self.assertEqual(find_phone_numbers(text), [])


if __name__ == "__main__":
    unittest.main()
