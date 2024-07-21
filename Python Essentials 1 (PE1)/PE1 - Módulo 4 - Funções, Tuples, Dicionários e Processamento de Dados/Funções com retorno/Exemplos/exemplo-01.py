# Devolver um resultado de uma função

# Utilização da instrução return sem expressão

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


# happy_new_year()
happy_new_year(False)
