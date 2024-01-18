def compute_quotient_remainder(dividend, divisor):
    if divisor == 0:
        print("Division by zero is undefined")
        return None, None
    
    quotient = dividend // divisor
    remainder = dividend % divisor

    return quotient, remainder

dividend_input = input("Enter the dividend: ")
divisor_input = input("Enter the divisor: ")

if dividend_input.isdigit() and divisor_input.isdigit():
    dividend = int(dividend_input)
    divisor = int(divisor_input)

    if divisor != 0:
        quotient, remainder = compute_quotient_remainder(dividend, divisor)
        print("Quotient:", quotient)
        print("Remainder:", remainder)
    else:
        print("Error: Division by zero is undefined.")
else:
    print("Invalid input. Please enter valid integers for the dividend and divisor.")
