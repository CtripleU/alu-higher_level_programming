def add_integer(a=0, b=98):
    """Adds two numbers and returns the sum"""

    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
