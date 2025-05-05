import pytest
from src.merito_library.encode_decode import (encode_base64,decode_base64,url_encode,url_decode,hex_encode,hex_decode, binary_encode, binary_decode)

def test_encode_base64():
    assert encode_base64("Hello") == "SGVsbG8="
    assert encode_base64(b"Hello") == "SGVsbG8="
    assert encode_base64("") == ""
    assert encode_base64(b"") == ""
    with pytest.raises(TypeError):
        encode_base64(123)
    with pytest.raises(TypeError):
        encode_base64(None)
    assert encode_base64("merito library") == "bWVyaXRvIGxpYnJhcnk="

def test_decode_base64():
    assert decode_base64("SGVsbG8=") == b"Hello"
    assert decode_base64("") == b""
    with pytest.raises(TypeError):
        decode_base64(123)
    with pytest.raises(ValueError):
        decode_base64("Invalid Base64")
    assert decode_base64("bWVyaXRvIGxpYnJhcnk=") == b"merito library"
    assert decode_base64("SGVsbG8gV29ybGQh") == b"Hello World!"

def test_url_encode():
    assert url_encode("Hello World!") == "Hello%20World%21"
    assert url_encode("") == ""
    with pytest.raises(TypeError):
        url_encode(123)
    with pytest.raises(TypeError):
        url_encode(None)
    assert url_encode("merito library") == "merito%20library"
    assert url_encode("Hello, world!") == "Hello%2C%20world%21"

def test_url_decode():
    assert url_decode("Hello%20World%21") == "Hello World!"
    assert url_decode("") == ""
    with pytest.raises(TypeError):
        url_decode(123)
    with pytest.raises(TypeError):
        url_decode(None)
    assert url_decode("merito%20library") == "merito library"
    assert url_decode("Hello%2C%20world%21") == "Hello, world!"

def test_hex_encode():
    assert hex_encode("Hello") == "48656c6c6f"
    assert hex_encode(b"Hello") == "48656c6c6f"
    assert hex_encode("") == ""
    assert hex_encode(b"") == ""
    with pytest.raises(TypeError):
        hex_encode(123)
    with pytest.raises(TypeError):
        hex_encode(None)
    assert hex_encode("merito library") == "6d657269746f206c696272617279"

def test_hex_decode():
    assert hex_decode("48656c6c6f") == b"Hello"
    assert hex_decode("") == b""
    with pytest.raises(TypeError):
        hex_decode(123)
    with pytest.raises(ValueError):
        hex_decode("Invalid Hex")
    assert hex_decode("6d657269746f206c696272617279") == b"merito library"
    assert hex_decode("48656c6c6f20576f726c6421") == b"Hello World!"

def test_binary_encode():
    assert binary_encode("Hello") == "0100100001100101011011000110110001101111"
    assert binary_encode(b"Hello") == "0100100001100101011011000110110001101111"
    assert binary_encode("") == ""
    assert binary_encode(b"") == ""
    with pytest.raises(TypeError):
        binary_encode(123)
    with pytest.raises(TypeError):
        binary_encode(None)
    assert binary_encode("merito library") == "0110110101100101011100100110100101110100011011110010000001101100011010010110001001110010011000010111001001111001"
    assert binary_encode("Hello World!") == "010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001"

def test_binary_decode():
    assert binary_decode("0100100001100101011011000110110001101111") == b"Hello"
    assert binary_decode("") == b""
    with pytest.raises(TypeError):
        binary_decode(123)
    with pytest.raises(ValueError):
        binary_decode("Invalid Binary")
    assert binary_decode("0110110101100101011100100110100101110100011011110010000001101100011010010110001001110010011000010111001001111001") == b"merito library"
    assert binary_decode("010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001") == b"Hello World!"

