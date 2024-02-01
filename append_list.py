def append_lists(list1, list2):
    list1.extend(list2)
    return list1

user_input1 = input("Enter elements for the first list : ")
first_list = [int(item) for item in user_input1.split()]

user_input2 = input("Enter elements for the second list : ")
second_list = [int(item) for item in user_input2.split()]

appended_list = append_lists(first_list, second_list)

print("First List:", first_list)
print("Second List:", second_list)
print("Appended List:", appended_list)
