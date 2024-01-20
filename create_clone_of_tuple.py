def clone_tuple(original_tuple):
    cloned_tuple = tuple(original_tuple)
    return cloned_tuple

user_input = input("Enter elements for the tuple separated by spaces: ")

elements = user_input.split()

original_tuple = tuple(elements)

cloned_tuple = clone_tuple(original_tuple)

print("Original Tuple:", original_tuple)
print("Cloned Tuple:", cloned_tuple)
