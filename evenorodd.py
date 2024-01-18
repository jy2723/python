def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

input = int(input("Enter a number: "))

result = even_odd(input)
print(f"The number {input} is {result}.")
