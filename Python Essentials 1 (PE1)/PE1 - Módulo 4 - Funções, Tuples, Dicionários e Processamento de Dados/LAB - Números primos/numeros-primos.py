# LAB: Números primos - como encontrá-los

def is_prime(num):

    if num > 1:

        prime = True

        for number in range(2, num):

            if num % number == 0:
                prime = False

        if prime:
            return True
        else:
            return False
    else:
        return False


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

print()
