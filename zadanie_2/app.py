import math
import re
from datetime import datetime

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$' #wyrazenie regularne spraewdzajace poprawnosc adresu email
    return re.match(pattern, email) is not None

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("podstawa/wysokość nie mogą być ujemne.")
    return 0.5 * base * height

def return_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def convert_date_format(date_str, input_format="%d-%m-%Y", output_format="%Y/%m/%d"):
    """Konwertuje datę z jednego formatu do drugiego. Podstawowy format wejściowy to DD-MM-YYYY."""
    return datetime.strptime(date_str, input_format).strftime(output_format)

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
