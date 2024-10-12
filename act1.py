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

# Assuming you have values for base and exponent
base = 2  # Replace with your desired base
exponent = 3  # Replace with your desired exponent

# Calculate the power
power_result = power(base, exponent)

# The calculated power is stored in power_result