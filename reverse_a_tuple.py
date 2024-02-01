user_input = input("Enter elements for the tuple separated by spaces: ")

user_tuple = tuple(user_input.split())
reverse_tuple = user_tuple[::-1]
print("Tuple:", user_tuple)
print("after reverse:", reverse_tuple)
