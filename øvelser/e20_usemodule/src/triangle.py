"""Dette modul indeholder beregninger for en retvinklet trekant"""
from math import sqrt

__version__ = "1.0"
__author__ = "MasterBlaster"


def hypothenuse(a, b):
    """Returnerer hypotenusen i retvinklet trekant"""
    return sqrt(a**2 + b**2)


def area(h, g):
    """Returnere arealet af en retvinklet trekant"""
    return 0.5 * h * g
