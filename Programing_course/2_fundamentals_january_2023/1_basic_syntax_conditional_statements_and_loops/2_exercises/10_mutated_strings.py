first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

new_word = ""

# Use the length of the shorter word as the range for the loop
for i in range(min(len(first_word), len(second_word))):
    if first_word[i] != second_word[i]:
        # Create the new word by swapping characters
        new_word = second_word[:i] + first_word[i] + second_word[(i+1):]
        # Print the new word
        print(new_word)
        # Break out of the loop if the new word is the same as the second word
        if new_word == second_word:
            break

# If the new word was not created in the loop, set it to the second word
if not new_word:
    new_word = second_word

# Print the final new word
print("Final new word:", new_word)

