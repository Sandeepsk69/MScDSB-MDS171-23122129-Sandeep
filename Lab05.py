# Sandeep Kumar G 23122129 Write a program for collecting a string from the user and counting the number of vowels.

def count_vowels(string):                              # Define function for string.
    vowels = "AaEeIiOoUu"
    vowel_count = 0
    total_strings = len(string)

    for char in string:                               # Use for loop for every string to chech for below condition
        if char in vowels:                            # Use if condition to chech if vowel is present in the string.
            vowel_count += 1                          # If yes count the vowel.

    return vowel_count, total_strings                 # Return to the function.

user_input = input("Enter a string: ")

user_input = user_input.replace(" ", "")              # To remove space and calculate total characters

vowel_count, total_strings = count_vowels(user_input)

print("Total count of vowels:", vowel_count)


percentage = (vowel_count / total_strings) * 100              # Caclulate Percentage of vowel from the given string input.
print(f"Percentage of vowels: {percentage:.2f}%")

