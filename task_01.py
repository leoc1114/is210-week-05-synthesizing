#! usr/bin/env python
# _*_ coding: utf-8 _*_
"""Created Task 1"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')
ABSOLUTE = ABSOLUTE_DIFFERENCE


def fahrenheit_to_celsius(degrees):
    """converting fahrenheit degrees to celsius degrees.

    Args:
        degrees(int): to convert fahrenheit to celsius

    Returns:
        a number in decimal

    Examples:
        >>>fahrenheit_to_celsius(212)
        Decimal('100')
    """
    celsius_degrees = (decimal.Decimal(degrees) - 32) * 5 / 9
    return decimal.Decimal(celsius_degrees)


def celsius_to_kelvin(celsius_degrees):
    """converting celsius degrees to kelvin degrees.

    Args:
        celsius_dgrees(mix): to convert celsius to kelvin

    Returns:
        a number in decimal

    Examples:
        >>>celsius_to_kelvin(100)
        Decimal('373.15')
    """
    kelvin_degrees = celsius_degrees + ABSOLUTE_DIFFERENCE
    return decimal.Decimal(kelvin_degrees)


def fahrenheit_to_kelvin(degrees):
    """Converting fahrenheit to kelvin.

    Args:
        fahrenheit_degrees(mix): to convert fahrenheit to kelvin

    Returns:
        a number in decimal

    Examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    kelvin_degrees = (decimal.Decimal(degrees) - 32) * 5 / 9 + ABSOLUTE
    return decimal.Decimal(kelvin_degrees)
