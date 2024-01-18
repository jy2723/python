def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    if n > 1:
        factors.append(n)

    return factors

num_str = input("Enter a number :")

if num_str.isdigit():
    num = int(num_str)
    if num > 0:
        result = prime_factors(num)
        print("Prime factors of {} are: {}".format(num, result))
    else:
        print("Please enter a positive integer")
else:
    print("Invalid input")
