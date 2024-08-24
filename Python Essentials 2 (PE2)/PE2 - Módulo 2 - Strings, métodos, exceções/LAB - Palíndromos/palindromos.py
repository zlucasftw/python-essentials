# LAB: Palíndromos

texto = input("Digite um texto e veja se é um palíndromo: ")

texto = texto.replace(" ", "").lower()
palindromo = ''
tamanho = len(texto) - 1

while tamanho >= 0:
    palindromo += texto[tamanho]
    tamanho -= 1

if texto == '' or texto == texto.isspace():
    print("It's not a palindrome")
elif texto == palindromo:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
