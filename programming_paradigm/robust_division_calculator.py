def safe_divide(numerator, denominator):
    """
    Perform division with error handling.

    :param numerator: str or float, the numerator of the division
    :param denominator: str or float, the denominator of the division
    :return: str, result of the division or an error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt to perform division
        result = num / denom
        
        # Format the result to avoid unnecessary trailing zeroes
        return f"The result of the division is {result:g}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
