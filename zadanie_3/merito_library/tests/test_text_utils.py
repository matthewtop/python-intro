import pytest
from src.merito_library.text_utils import (count_words,reverse_words,reverse_string,count_characters,is_palindrome,find_most_common_word)

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("This is a test.") == 4
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("Hello, world!") == 2
    with pytest.raises(TypeError):
        count_words(123)
    with pytest.raises(TypeError):
        count_words(None)
    assert count_words("Hello, world! Hello!") == 3

def test_reverse_words():
    assert reverse_words("Hello world") == "world Hello"
    assert reverse_words("This is a test.") == "test. a is This"
    assert reverse_words("") == ""
    assert reverse_words("Hello, world!") == "world! Hello,"
    with pytest.raises(TypeError):
        reverse_words(123)
    with pytest.raises(TypeError):
        reverse_words(None)
    assert reverse_words("Hello, world! Hello!") == "Hello! world! Hello,"
    assert reverse_words("merito library") == "library merito"

def test_reverse_string():
    assert reverse_string("Hello world") == "dlrow olleH"
    assert reverse_string("This is a test.") == ".tset a si sihT"
    assert reverse_string("") == ""
    assert reverse_string("   ") == "   "
    assert reverse_string("Hello, world!") == "!dlrow ,olleH"
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(None)
    assert reverse_string("merito library") == "yrarbil otirem"

def test_count_characters():
    assert count_characters("Hello world") == 11
    assert count_characters("This is a test.") == 15
    assert count_characters("") == 0
    assert count_characters("   ") == 3
    assert count_characters("Hello, world!") == 13
    with pytest.raises(TypeError):
        count_characters(123)
    with pytest.raises(TypeError):
        count_characters(None)
    assert count_characters("merito library") == 14

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("merito") == False
    assert is_palindrome("kajak") == True
    assert is_palindrome("kobyła ma mały bok") == True
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_find_most_common_word():
    assert find_most_common_word("Hello world hello") == {"word": "hello", "count": 2}
    assert find_most_common_word("This is a test. This test is only a test.") == {"word": "test", "count": 3}
    assert find_most_common_word("Hello, world! Hello!") == {"word": "hello", "count": 2}
    with pytest.raises(TypeError):
        find_most_common_word(123)
    with pytest.raises(TypeError):
        find_most_common_word(None)
    assert find_most_common_word("merito library merito") == {"word": "merito", "count": 2}
    assert find_most_common_word("testy testy testy") == {"word": "testy", "count": 3}