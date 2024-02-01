def display_array(arr):
    print("Array items:", arr)

def count_occurrences(arr, element):
    occurrences = arr.count(element)
    return occurrences

def main():
    my_array = []
    for i in range(n):
        user_input = int(input(f"Enter integer for index {i}: "))
        my_array.append(user_input)

    display_array(my_array)

    element_to_count = int(input("Enter the element to count: "))

    occurrences = count_occurrences(my_array, element_to_count)

    print(f"\nNumber of occurrences of {element_to_count}: {occurrences}")

if __name__ == "__main__":
    print("enter array size:")
    n=int(input())
    main()
