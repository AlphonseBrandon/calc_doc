from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and returns the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0
    
    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Computes the difference between two numbers

    Examples:
    >>> subtract(4.0, 2.0)
    2.0
    >>> subtract(4, 2)
    2.0
    
    Args:
        a: A number representing the first number in the substraction.
        b: A number representing the second number in the substraction.

    Returns:
        float: A number representing the difference of the two numbers `a` and `b`
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Computes the multiplication of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0
    
    Args:
        a: A number representing the first number in the multiplication.
        b: A number representing the second number in the multiplication

    Returns:
        float: A number representing the difference between the two numbers `a` and `b`
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Computes the division of two numbers.
    
    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
    
    Args:
        a: A number representing the divident in the division.
        b: A number representing the divisor of the division

    Returns:
        float: A number representing the result of the division of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero not allowed")
    return float(a / b)