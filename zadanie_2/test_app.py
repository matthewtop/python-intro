import unittest
from app import (
    is_valid_email,
    calculate_triangle_area,
    return_even_numbers,
    convert_date_format,
    is_palindrome
)

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        self.valid_emails = ["test@example.com", "student@merito.pl", "johndoe9@domain.de"]
        self.invalid_emails = ["invalid-email", "abc@com", "@test.com"]

        self.date_cases = [
            ("05-04-2025", "2025/04/05"),
            ("10-10-2020", "2020/10/10")
        ]

        self.palindromes = [
            "potop",
            "12321",
            "kamil Ślimak"
        ]
        self.non_palindromes = ["test", "mateusz","programowanie zaawansowane"]

    def test_is_valid_email(self):
        # Test poprawnych adresów e-mail
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

        # Test niepoprawnych adresów e-mail
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_calculate_triangle_area(self):
        # Test typowego przypadku
        self.assertEqual(calculate_triangle_area(10, 5), 25)
        
        # Test przypadku brzegowego
        self.assertEqual(calculate_triangle_area(0, 10), 0)

        # Test blednych danych (ujemne wartosci)
        with self.assertRaises(ValueError):
            calculate_triangle_area(-100, 2)

    def test_return_even_numbers(self):
        # Test dla typowej listy liczb
        self.assertEqual(return_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        
        # Test dla listy bez liczb parzystych
        self.assertEqual(return_even_numbers([1, 3, 5]), [])

        # Test dla pustej listy
        self.assertEqual(return_even_numbers([]), [])

    def test_convert_date_format(self):
        # Test poprawnych konwersji dat
        for original, expected in self.date_cases:
            with self.subTest(date=original):
                self.assertEqual(convert_date_format(original), expected)

        # Test blednego formatu wejściowego
        with self.assertRaises(ValueError):
            convert_date_format("2025/04/05")  

    def test_is_palindrome(self):
        # Testy dla palindromów z uwzglednieniem wielkosci liter i znaków interpunkcyjnych
        for text in self.palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

        # Testy dla nie-palindromów
        for text in self.non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

if __name__ == '__main__':
    unittest.main()
