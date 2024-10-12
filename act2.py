def power(base, exponent):
    """Calculates the power of a base raised to an exponent.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        The result of the calculation.
    """

    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Get user input for base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
power_result = power(base, exponent)

# Print the result
print("The power of", base, "raised to", exponent, "is", power_result)