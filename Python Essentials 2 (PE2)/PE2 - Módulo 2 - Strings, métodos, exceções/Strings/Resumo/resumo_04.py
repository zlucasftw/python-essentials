# Resumo da secção - Key takeaways

# As funções chr() e ord() podem ser utilizadas
# para criar um caractere usando o seu codepoint,
# e para determinar um codepoint correspondente a um caractere.

charachter = ' '
codepoint = 32

# As seguintes expressões sempre serão verdadeiras

print(chr(ord(charachter)) == charachter)
print(ord(chr(codepoint)) == codepoint)
