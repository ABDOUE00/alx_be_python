class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = SimpleCalculator()
    print(calc.add(5, 3))       # Output: 8
    print(calc.subtract(10, 4)) # Output: 6
    print(calc.multiply(7, 2))  # Output: 14
    print(calc.divide(8, 0))    # Output: None (division by zero)
    print(calc.divide(8, 2))    # Output: 4.0