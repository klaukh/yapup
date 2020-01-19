"""
Utilities for general use
"""

import pandas as pd
import random
import string


def randomstring(length=10):
    """Generate a random string of fixed length
    :param length: The length of string to produce; default=10
    :return: Random string of ASCII lowercase characters

    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

