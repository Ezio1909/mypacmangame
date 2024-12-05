import unittest
from src.vector import Vector  # Assuming the Vector class is in a file named vector.py

class TestVector(unittest.TestCase):
    def test_addition(self):
        # Test addition with positive, negative, and zero values
        v1 = Vector(1, 2)
        v2 = Vector(-1, -2)
        v3 = Vector(0, 0)
        self.assertEqual(v1 + v2, Vector(0, 0))
        self.assertEqual(v1 + v3, v1)

    def test_subtraction(self):
        # Test subtraction with positive, negative, and zero values
        v1 = Vector(5, 5)
        v2 = Vector(2, 3)
        v3 = Vector(0, 0)
        self.assertEqual(v1 - v2, Vector(3, 2))
        self.assertEqual(v1 - v3, v1)

    def test_multiplication(self):
        # Test scalar multiplication with positive, negative, and zero values
        v1 = Vector(2, 3)
        self.assertEqual(v1 * 2, Vector(4, 6))
        self.assertEqual(v1 * -1, Vector(-2, -3))
        self.assertEqual(v1 * 0, Vector(0, 0))

    def test_division(self):
        # Test scalar division with positive, negative, and zero values
        v1 = Vector(6, 3)
        self.assertEqual(v1 / 3, Vector(2, 1))
        self.assertEqual(v1 / -3, Vector(-2, -1))
        with self.assertRaises(ValueError):
            v1 / 0  # Division by zero

    def test_equality(self):
        # Test equality with threshold
        v1 = Vector(1.0000001, 1.0000001)
        v2 = Vector(1.0, 1.0)
        self.assertTrue(v1 == v2)

        v3 = Vector(1.00001, 1.00001)
        self.assertFalse(v1 == v3)

    def test_magnitude(self):
        # Test magnitude calculation
        v1 = Vector(3, 4)
        self.assertEqual(v1.magnitude(), 5.0)

    def test_magnitude_squared(self):
        # Test squared magnitude calculation
        v1 = Vector(3, 4)
        self.assertEqual(v1.magnitude_squared(), 25.0)

    def test_copy(self):
        # Test copying the vector
        v1 = Vector(2, 3)
        v2 = v1.copy()
        self.assertEqual(v1, v2)
        self.assertIsNot(v1, v2)  # Ensure it's a different object

    def test_as_tuple(self):
        # Test conversion to tuple
        v1 = Vector(2.5, 3.5)
        self.assertEqual(v1.as_tuple(), (2.5, 3.5))

    def test_as_int_tuple(self):
        # Test conversion to tuple of integers
        v1 = Vector(2.9, 3.7)
        self.assertEqual(v1.as_int_tuple(), (2, 3))

    def test_string_representation(self):
        # Test string representation
        v1 = Vector(2.5, 3.5)
        self.assertEqual(str(v1), "<2.5,3.5>")

    def test_edge_cases(self):
        # Edge cases with very large and very small numbers
        v1 = Vector(1e10, -1e10)
        v2 = Vector(1e-10, 1e-10)
        self.assertEqual(v1 + v2, Vector(1e10, -1e10))  # Small value doesn't affect large value
        self.assertEqual(v2 - v2, Vector(0, 0))  # Subtracting identical vectors

if __name__ == "__main__":
    unittest.main()