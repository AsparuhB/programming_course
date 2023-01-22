letters = input()
counter = 0

for letter in range(0, len(letters)):
    if letters[letter] == "a":
        counter += 1
    if letters[letter] == "e":
        counter += 2
    if letters[letter] == "i":
        counter += 3
    if letters[letter] == "o":
        counter += 4
    if letters[letter] == "u":
        counter += 5

print(counter)