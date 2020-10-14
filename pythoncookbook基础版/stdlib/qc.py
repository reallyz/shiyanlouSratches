def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()

# DeprecationWarning:
# the imp module is deprecated in favour of importlib;
# see the module's documentation for alternative uses
