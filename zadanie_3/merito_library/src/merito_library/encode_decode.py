#src/merito_library/encode_decode.py

import base64
import binascii
import urllib.parse
from typing import Union

def encode_base64(data: Union[str, bytes]) -> str:
    """Encode data to Base64 format."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes.")
    
    encoded_data = base64.b64encode(data)
    return encoded_data.decode('utf-8')

def decode_base64(encoded_data: str) -> bytes:
    """Decode Base64 encoded data."""
    if not isinstance(encoded_data, str):
        raise TypeError("Input must be a string.")
    
    try:
        decoded_data = base64.b64decode(encoded_data)
    except binascii.Error as e:
        raise ValueError("Invalid Base64 encoded data.") from e
    
    return decoded_data

def url_encode(data: str) -> str:
    """URL encode a string."""
    if not isinstance(data, str):
        raise TypeError("Input must be a string.")
    
    encoded_data = urllib.parse.quote(data)
    return encoded_data

def url_decode(encoded_data: str) -> str:
    """URL decode a string."""
    if not isinstance(encoded_data, str):
        raise TypeError("Input must be a string.")
    
    decoded_data = urllib.parse.unquote(encoded_data)
    return decoded_data

def hex_encode(data: Union[str, bytes]) -> str:
    """Encode data to hexadecimal format."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes.")
    
    encoded_data = data.hex()
    return encoded_data

def hex_decode(encoded_data: str) -> bytes:
    """Decode hexadecimal encoded data."""
    if not isinstance(encoded_data, str):
        raise TypeError("Input must be a string.")
    
    try:
        decoded_data = bytes.fromhex(encoded_data)
    except ValueError as e:
        raise ValueError("Invalid hexadecimal encoded data.") from e
    
    return decoded_data

def binary_encode(data: Union[str, bytes]) -> str:
    """Encode data to binary format."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes.")
    
    encoded_data = ''.join(format(byte, '08b') for byte in data)
    return encoded_data

def binary_decode(encoded_data: str) -> bytes:
    """Decode binary encoded data."""
    if not isinstance(encoded_data, str):
        raise TypeError("Input must be a string.")
    
    if len(encoded_data) % 8 != 0:
        raise ValueError("Invalid binary encoded data length.")
    
    decoded_data = bytes(int(encoded_data[i:i+8], 2) for i in range(0, len(encoded_data), 8))
    return decoded_data


