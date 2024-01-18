def largest_number(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = largest_number(num1, num2, num3)

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
