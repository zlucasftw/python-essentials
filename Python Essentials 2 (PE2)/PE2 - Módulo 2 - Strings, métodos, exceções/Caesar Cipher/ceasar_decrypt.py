# Quatro programas simples

# A cifra de César: decifrar uma mensagem

# Cesar chiper - decrypting a message.

chiper = input('Enter your cryptogram: ')
text = ''
for char in chiper:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
