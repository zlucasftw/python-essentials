# Importar um módulo - math

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.999999999
    else:
        return None


from math import sin, pi

print(sin(pi / 2))
