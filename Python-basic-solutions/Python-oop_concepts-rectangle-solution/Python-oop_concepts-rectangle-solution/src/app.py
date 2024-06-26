import math

from check import print_rectangle_properties

class Rectangle:

    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
         width2 = math.pow(self.width, 2)
         height2 = math.pow(self.height, 2)
         return math.sqrt(width2 + height2)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


def main():
    rectangle1 = Rectangle(9, 12)
    rectangle2 = Rectangle(17, 13)

    print_rectangle_properties(rectangle1)
    print_rectangle_properties(rectangle2)

if __name__ == "__main__":
    main()
