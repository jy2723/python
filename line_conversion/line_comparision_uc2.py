class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __eq__(self, other):
        if isinstance(other, Line):
            return (self.x1, self.y1, self.x2, self.y2) == (other.x1, other.y1, other.x2, other.y2)
        return False

x1_1 = float(input("Enter the x-coordinate of the first point of Line 1: "))
y1_1 = float(input("Enter the y-coordinate of the first point of Line 1: "))
x2_1 = float(input("Enter the x-coordinate of the second point of Line 1: "))
y2_1 = float(input("Enter the y-coordinate of the second point of Line 1: "))

x1_2 = float(input("Enter the x-coordinate of the first point of Line 2: "))
y1_2 = float(input("Enter the y-coordinate of the first point of Line 2: "))
x2_2 = float(input("Enter the x-coordinate of the second point of Line 2: "))
y2_2 = float(input("Enter the y-coordinate of the second point of Line 2: "))

line1 = Line(x1_1, y1_1, x2_1, y2_1)
line2 = Line(x1_2, y1_2, x2_2, y2_2)

print("Are the lines equal", line1 == line2)
