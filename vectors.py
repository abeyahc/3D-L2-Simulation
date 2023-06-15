import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # displays as Vector(#, #, #)
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # sets up the vector to display #i + #j + #k
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    # tests if there are three vectors if more will display an error
    def __getitem__(self, item): 
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("There are only three elements in the vector")

    # adds two vectors
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    
    # subtracts two vectors
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    
    # multiplication 
    def __mul__(self, other):  

        # multiplies two vectors
        if isinstance(other, Vector):
            return(
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )

        # multiplies vector by a scalar
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other, 
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")

    # divides a vector by a scalar since two vectors cannot be divided
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
