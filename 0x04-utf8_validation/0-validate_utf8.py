#!/usr/bin/python3
"""
Validate a UTF-8 data set for proper encoding.

Validation steps:
1. Convert each int into 8-bit binary by getting the 8 LSBs
2. Loop through each byte in the sequence while inspecting
 the leading bytes.
The leading byte must be followed by the appropriate number
of continuation bytes.
"""

import re


def validUTF8(data) -> bool:
    """
    Check if the data has been properly encoded in UTF-8.

    The data is assumed to not contain the null  termination byte.
    """
    len_data = len(data)
    data = [int_to_bytes(_) for _ in data]
    i = 0
    while i < len_data:
        b = data[i]
        if is_leading_byte(b):
            n = byte_sequence_size(b)
            if n == 1:
                i += 1
                continue
            try:
                continuation_bytes = data[i+1: i+n]
            except IndexError:
                return False

            # Check if the right number of continuation bytes are present
            if len(continuation_bytes) != (n - 1):
                return False
            if not all(is_continuation_byte(j) for j in continuation_bytes):
                return False
            i += n  # Skip the continuation bytes

        else:
            return False

    return True


def int_to_bytes(x: int) -> str:
    """
    Encode x into binary and return the str repr of the 1's and 0's.

    The integer must be between 0-128. The 8-bit representation is returned.

    Example:int_to_bytes(3)
    >>> int_to_bytes(3)
    '00000011'
    """
    result = ''
    for _ in range(8):
        lsb = x & 1
        result += str(lsb)
        x >>= 1

    # Reverse the string to get the right bit sequence
    return result[::-1]


def is_leading_byte(x: str) -> bool:
    """
    Check if x is a valid leading byte.

    Valid representations of a leading byte are: 0XX, 110XX, 1110XX,
    and 11110XX.

    Examples:
    >>> is_leading_byte('10000000')
    False
    >>> is_leading_byte('01000010')
    True
    >>> is_leading_byte('11001011')
    True
    >>> is_leading_byte('11101011')
    True
    >>> is_leading_byte('11111111')
    False
    """
    pattern = re.compile('^(0|110|1110|11110)')
    return bool(pattern.match(x))


def is_continuation_byte(x: str):
    """
    Check if x is a continuation byte.

    Examples:
    >>> is_continuation_byte('10010101')
    True
    >>> is_continuation_byte('11000001')
    False
    """
    return x.startswith('10')


def byte_sequence_size(x: str) -> int:
    """
    Infer the size of a byte sequence from a leading byte (x).

    Assumes x is a valid encoding of a leading byte.

    >>> byte_sequence_size('01010101')
    1
    >>> byte_sequence_size('11010101')
    2
    >>> byte_sequence_size('11100010')
    3
    >>> byte_sequence_size('11110101')
    4
    """
    if x.startswith('0'):
        return 1

    n = 0
    for bit in x:
        if bit == '1':
            n += 1
        else:
            return n
