anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Erro, como a função input() retorna sempre uma string
# ou uma sequência de caracteres não se deve usar
# seu retorno como argumento de qualquer operação aritmética, por exemplo