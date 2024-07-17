# LAB: A hipótese de Collatz

c0 = int(input("Digite um número inteiro: "))
steps = 0

while c0 != 1:

    if c0 > 0:

        if c0 % 2 == 0:
            c0 //= 2

        else:
            c0 = (3 * c0) + 1

    else:

        if c0 % 2 == 0:
            c0 /= 2

        else:
            c0 = (3 * c0) + 1

    steps += 1
    print(c0)

print(f"steps = {steps}")
