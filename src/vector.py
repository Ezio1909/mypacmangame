import math

class Vector:
    """
    A class to represent a 2D vector and provide basic vector operations.
    """

    def __init__(self, x=0.0, y=0.0):
        """
        Initialize a Vector instance.

        Args:
            x (float): The x-coordinate of the vector. Default is 0.0.
            y (float): The y-coordinate of the vector. Default is 0.0.
        """
        self.x = x
        self.y = y
        self.threshold = 0.000001

    def __add__(self, other):
        """
        Add two vectors.

        Args:
            other (Vector): The vector to add.

        Returns:
            Vector: A new vector that is the sum of this vector and the other.
        """
        return Vector(x = self.x + other.x, y = self.y + other.y)

    def __sub__(self, other):
        """
        Subtract one vector from another.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            Vector: A new vector that is the difference between this vector and the other.
        """
        return Vector( x = self.x - other.x, y = self.y - other.y)

    def __mul__(self, scalar):
        """
        Multiply vector by a scalar.

        Args:
            scalar (float): The scalar to multiply by.

        Returns:
            Vector: A new vector that is this vector scaled by the scalar.
        """
        return Vector( x = self.x * scalar, y = self.y * scalar)

    def __truediv__(self, scalar):
        """
        Divide vector by a scalar.

        Args:
            scalar (float): The scalar to divide by.

        Returns:
            Vector: A new vector that is this vector divided by the scalar.

        Raises:
            ValueError: If scalar is zero.
        """
        if scalar == 0:
            raise ValueError("scalar cannot be zero")
        return Vector(x=self.x / scalar, y=self.y / scalar)


    def __eq__(self, other):
        """
        Check if two vectors are equal within a small threshold.

        Args:
            other (Vector): The vector to compare with.

        Returns:
            bool: True if vectors are equal within the threshold, False otherwise.
        """
        return True if abs(self.x - other.x) < self.threshold and abs(self.y - other.y) < self.threshold else False

    def magnitude_squared(self):
        """
        Calculate the squared magnitude of the vector.

        Returns:
            float: The squared magnitude of the vector.
        """
        return self.x**2 + self.y**2
    
    def magnitude(self):
        """
        Calculate the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(self.magnitude_squared())

    def copy(self):
        """
        Create a copy of the vector.

        Returns:
            Vector: A new vector with the same x and y values.
        """
        return Vector( x = self.x, y = self.y )

    def as_tuple(self):
        """
        Convert the vector to a tuple.

        Returns:
            tuple: A tuple (x, y) representing the vector.
        """
        return (self.x, self.y)

    def as_int_tuple(self):
        """
        Convert the vector to a tuple of integers.

        Returns:
            tuple: A tuple (int(x), int(y)) representing the vector.
        """
        return (int(self.x), int(self.y))

    def __str__(self):
        """
        String representation of the vector.

        Returns:
            str: A string in the format '<x, y>'.
        """
        return f"<{self.x},{self.y}>"

