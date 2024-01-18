def check_vowel_consonant(char):
    char = char.lower()

    if char in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    else:
        return "Consonant"


input = input("Enter a alphabet: ")
if len(input) == 1 and input.isalpha():
    result = check_vowel_consonant(input)
    print(f"The alphabet {input} is a {result}.")
else:
    print("Please enter a valid single alphabet.")