# Quatro programas simples

# A Cifra César: encriptar uma mensagem

# Ceasar chiper.

text = input("Enter your message: ")
chiper = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    chiper += chr(code)

print(chiper)
