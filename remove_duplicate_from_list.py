def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

user_input = input("Enter a list of numbers : ")

original_list = [int(num) for num in user_input.split()]

unique_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)
