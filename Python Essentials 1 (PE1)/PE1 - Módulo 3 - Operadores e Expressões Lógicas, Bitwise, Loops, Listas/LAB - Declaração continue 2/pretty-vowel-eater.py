# LAB: A declaração continue - o Pretty Vowel Eater

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
