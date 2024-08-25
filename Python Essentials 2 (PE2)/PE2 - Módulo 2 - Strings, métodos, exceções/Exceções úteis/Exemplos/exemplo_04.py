# Exceções úteis

# Exceções integradas - MemoryError

# Localização: BaseException <- Exception <- MemoryError

# É uma exceção concreta levantada quando uma operação
# não pode ser concluída devido a falta de memória.

# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')
