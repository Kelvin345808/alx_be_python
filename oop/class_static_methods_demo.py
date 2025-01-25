class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method that performs addition
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method that prints the calculation type and performs multiplication
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
