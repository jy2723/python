def display_array(arr):
    print("Array items:", arr)

def remove_first_occurrence(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"Removed the first occurrence of {element}.")
    else:
        print(f"{element} not found in the array.")

def main():
    my_array = []
    for i in range(n):
        user_input = int(input(f"Enter integer for index {i}: "))
        my_array.append(user_input)

    display_array(my_array)

    element_to_remove = int(input("Enter the element to remove: "))

    remove_first_occurrence(my_array, element_to_remove)

    display_array(my_array)

if __name__ == "__main__":
    print("enter array size:")
    n=int(input())
    main()
