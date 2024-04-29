#!/usr/bin/python3

def islower(char):
    """Check for lowercase charactaers."""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False
