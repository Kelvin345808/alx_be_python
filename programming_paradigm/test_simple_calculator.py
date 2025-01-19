import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(-1.5, -2.5), -4.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
        self.assertEqual(self.calc.multiply(-1.5, -2), 3.0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(1, 3), 1 / 3)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(1.5, 0.5), 3.0)
        self.assertEqual(self.calc.divide(-1.5, -0.5), 3.0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(6, 0), "Division by zero should return None")
        self.assertIsNone(self.calc.divide(0, 0), "0 divided by 0 should return None")

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        # Adding large numbers
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        # Subtracting large numbers
        self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
        # Multiplying large numbers
        self.assertEqual(self.calc.multiply(1e10, 2), 2e10)
        # Dividing large numbers
        self.assertEqual(self.calc.divide(1e10, 2), 5e9)


if __name__ == "__main__":
    unittest.main()
