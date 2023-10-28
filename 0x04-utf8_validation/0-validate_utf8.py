#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            if byte >> 7 == 0b0:
                # Single-byte UTF-8 character
                continue
            elif byte >> 5 == 0b110:
                # Two-byte UTF-8 character
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte UTF-8 character
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte UTF-8 character
                remaining_bytes = 3
            else:
                # Invalid UTF-8 character
                return False
        else:
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
