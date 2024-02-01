def display_array(arr):
    print("Array items:", arr)

    for i in range(len(arr)):
        print(f"Element at index {i}: {arr[i]}")

def main():
    my_array = []
    for i in range(n):
        user_input = int(input(f"Enter integer for index {i}: "))
        my_array.append(user_input)

    display_array(my_array)

if __name__ == "__main__":
    print("enter array size:")
    n=int(input())
    main()
