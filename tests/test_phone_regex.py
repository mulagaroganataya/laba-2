import unittest
from phone_regex import find_phone_numbers, normalize_phone


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


if __name__ == "__main__":
    unittest.main()
