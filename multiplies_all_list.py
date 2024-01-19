def mul_of_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


def main():
    my_list = []
    for i in range(n):
        user_input = int(input(f"Enter integer for index {i}: "))
        my_list.append(user_input)

    result = mul_of_list(my_list)

    print(f"The mul of the list {my_list} is: {result}")



if __name__ == "__main__":
    print("enter array size:")
    n=int(input())
    main()
