# Exercício 3

# Crie um programa com um loop for e uma declaração break. O programa deve iterar sobre os
# caracteres de um endereço de e-mail, sair do loop quando chegar ao símbolo @, e imprimir
# a parte antes de @ numa linha. Use o código escrito

# name = ""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Line of code.
#     # Line of code.
#         break
#     name += ch
# print(name)


for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
