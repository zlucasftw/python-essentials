# LAB: Ler ints em segurança


def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    value = int(input(prompt))
    assert value >= -10 and value <= 10
    return value


try:
    v = read_int("Enter a number from -10 to 10: ", -10, 10)

    print("The number is:", v)

except ValueError:
    print('Error: wrong input')
except AssertionError:
    print('Error: the value is not within permitted range (-10..10)')
