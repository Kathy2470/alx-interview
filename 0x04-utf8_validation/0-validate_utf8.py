#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Function to check if a data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    def is_continuation(byte):
        """
        Check if a byte is a continuation byte.

        Args:
            byte (int): Byte to check.

        Returns:
            bool: True if the byte is a continuation byte, False otherwise.
        """
        return (byte & 0xC0) == 0x80

    def count_leading_ones(byte):
        """
        Count the number of leading 1s in the byte to determine character length.

        Args:
            byte (int): Byte to check.

        Returns:
            int: Number of leading 1s.
        """
        count = 0
        while (byte & 0x80) != 0:
            count += 1
            byte <<= 1
        return count

    i = 0
    n = len(data)

    while i < n:
        byte = data[i]
        num_leading_ones = count_leading_ones(byte)

        if num_leading_ones == 0:
            i += 1
        elif num_leading_ones == 2:
            if i + 1 >= n:
                return False
            if not is_continuation(data[i + 1]):
                return False
            i += 2
        elif num_leading_ones == 3:
            if i + 2 >= n:
                return False
            if (not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2])):
                return False
            i += 3
        elif num_leading_ones == 4:
            if i + 3 >= n:
                return False
            if (not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2]) or
                    not is_continuation(data[i + 3])):
                return False
            i += 4
        else:
            return False

    return True
