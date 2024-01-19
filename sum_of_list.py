def sum_of_list(lst):
    return sum(lst)


def main():
    my_list = []
    for i in range(n):
        user_input = int(input(f"Enter integer for index {i}: "))
        my_list.append(user_input)

    result = sum_of_list(my_list)

    print(f"The sum of the list {my_list} is: {result}")



if __name__ == "__main__":
    print("enter array size:")
    n=int(input())
    main()
