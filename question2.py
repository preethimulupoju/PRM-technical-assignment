class Shape:
    def __init__(self, sides):
        self.sides = sides

    def validate_triangle(self):
        sides = sorted(self.sides)
        if sides[0] + sides[1] > sides[2]:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")

    def validate_rectangle(self):
        sides = self.sides
        if sides[0] == sides[2] and sides[1] == sides[3]:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")

if __name__ == '__main__':
    sides = list(map(int, input().strip().split()))
    triangle = Shape(sides[:3])
    triangle.validate_triangle()
    rectangle = Shape(sides[3:])
    rectangle.validate_rectangle()
