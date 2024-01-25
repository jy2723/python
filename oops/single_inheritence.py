class polygon:
    def __init__(self,sides):
        self.sides = sides

    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
class Triangle(polygon):
    def display(self):
        print("triangle has 3 sides")
class quadrilateral(polygon):
    def display(self):
        print("quadrilateral has 4 sides")
t = Triangle([2,3,6])
perimeter = t.perimeter()
display = t.display()
print(display)
print("perimeter is:", perimeter)
q = quadrilateral([1,5,6,4])
perimeter = q.perimeter()
display = q.display()
print(display)
print("quadrilateral perimeter:",perimeter)