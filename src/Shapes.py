import turtle as t
class Shapes:

    def __init__(self) -> int:
        """
        length = float\n
        angle = float\n
        direction = string\n
        returns = int
        """
        self.length:float = 0
        self.angle:float = 0
        self.direction:str = "l"

    # Accessor Methods
    def get_length(self):
        return self.length
    
    def get_angle(self):
        return self.angle
    
    def get_direction(self):
        return self.direction
    # Operator Methods
    def square(self, length, direction:str):
        """
        Adds a uniform square of the same size. User gets to pick which direction.\n
        direction = takes a users choice of the direction of the turtle, but defaults to left.

        """
        if direction.lower == 'l':
            for i in range(4):
                t.fd(length)
                t.left(90)
        elif direction.lower == 'r':
            for i in range(4):
                t.fd(length)
                t.right(90)
        else:
            for i in range(4):
                t.fd(length)
                t.left(90)

    def square(self):
        """Creates a fixed sized square of 100 units where the direction is to the left."""
        for i in range(4):
            t.fd(100)
            t.left(90)

    # Circle of user choice of size
    def circle(self):
        pass
    # Triangle (fixed)
    def triangle(self):
        pass
    # Triangle (user input of size)
    def trianlge(self):
        pass

    pass