# calculator / calculations.py

def add(a, b):
    """Compute and returns the sum of two numbers.
    
    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a, b):
    """Computes the difference between two numbers
    
    Args:
        a (float): A number representing the first number in the substraction.
        b (float): A number representing the second number in the substraction.

    Returns:
        float: A number representing the difference of the two numbers `a` and `b`
    """
    return float(a, b)

def multiply(a, b):
    """Computes the multiplication of two numbers
    
    Args:
        a (float): A number representing the first number in the multiplication.
        b (float): A number representing the second number in the multiplication

    Returns:
        float: A number representing the difference between the two numbers `a` and `b`
    """
    return float(a, b)

def divide(a, b):
    """Computes the division of two numbers
    
    Args:
        a (float): A number representing the divident in the division.
        b (float): A number representing the divisor of the division

    Returns:
        float: A number representing the result of the division of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero not allowed")
    return float(a / b)