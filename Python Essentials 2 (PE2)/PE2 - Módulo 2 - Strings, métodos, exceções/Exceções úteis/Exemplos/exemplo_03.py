# Exceções úteis

# Exceções integradas - KeyboardInterrupt

# Localização: BaseException <- KeyboardInterrupt

# Exceção concreta levantada quando o utilizador
# utiliza um atalho de teclado que tem o objetivo
# de terminar a execução de um programa.

# This code cannot be terminated
# by pressing Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
