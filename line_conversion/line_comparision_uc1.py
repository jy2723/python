import math

def calculate_line_length(x1, y1, x2, y2):
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return length

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

line_length = calculate_line_length(x1, y1, x2, y2)

print(f"The length of the line between ({x1}, {y1}) and ({x2}, {y2}) is: {line_length}")
