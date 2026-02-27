import unittest
from phone_regex import find_phone_numbers


class TestPhoneRegex(unittest.TestCase):
    def test_find_valid_phones(self):
        text = "Контакты: +7 999 123-45-67, 8 (912) 000-11-22 и +7(495)1234567."
        found = find_phone_numbers(text)
        self.assertEqual(len(found), 3)


if __name__ == "__main__":
    unittest.main()
