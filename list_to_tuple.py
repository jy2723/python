user_input = input("Enter elements for the list separated by spaces: ")

elements_list = user_input.split()

tuple_from_list = tuple(elements_list)

print("Original List:", elements_list)
print("Tuple from List:", tuple_from_list)
