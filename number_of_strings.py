def same_first_last(strings):
    count = 0

    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1

    return count

user_input = input("Enter a list of strings separated by spaces: ")

string_list = user_input.split()

result = same_first_last(string_list)

print(f"The number of strings with the same first and last character: {result}")
