#src/merito_library/text_utils.py

"""Simple module for text manipulation and analysis."""
import re
from typing import List, Dict, Union

def count_words(text: str) -> int:
    """Count the number of words in a given text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def reverse_words(text: str) -> str:
    """Reverse the order of words in a given text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    words = text.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

def reverse_string(text: str) -> str:
    """Reverse the entire string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text[::-1]

def count_characters(text: str) -> int:
    """Count the number of characters in a given text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return len(text)

def is_palindrome(text: str) -> bool:
    """Check if a given text is a palindrome."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    cleaned_text = re.sub(r'\W+', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

def find_most_common_word(text: str) -> Dict[str, Union[str, int]]:
    """Find the most common word in a given text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_common_word = max(word_count, key=word_count.get)
    return {"word": most_common_word, "count": word_count[most_common_word]}
