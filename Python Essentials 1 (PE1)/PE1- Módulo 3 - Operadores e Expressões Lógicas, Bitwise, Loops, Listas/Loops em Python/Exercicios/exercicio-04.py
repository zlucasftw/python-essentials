# Exercício 4

# Crie um programa com um loop for e uma declaração continue. O programa deve iterar sobre uma
# string de dígitos, substituir cada 0 com x e imprimir a string modificada na tela.
# Usar o código já escrito

# for digit in "0165031806510":
#     if digit == "0":
#         # Line of code.
#         # Line of code.
#         digit = "x"
#         continue
#     # Line of code.
#     print(digit, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
