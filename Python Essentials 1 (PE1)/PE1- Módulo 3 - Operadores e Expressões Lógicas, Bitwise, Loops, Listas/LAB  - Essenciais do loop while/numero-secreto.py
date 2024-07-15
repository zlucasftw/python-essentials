# LAB: Essenciais do loop while - Adivinhe o número secreto

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

numero = int(input("Digite um número inteiro para adivinhar o número secreto: "))

while numero != secret_number:

    print("Ha ha! You're stuck in my loop!")

    numero = int(input("Digite novamente um número inteiro para adivinhar o número secreto: "))

print(f"O número secreto é: {secret_number}")
print("Well done, muggle! You are free now.")
