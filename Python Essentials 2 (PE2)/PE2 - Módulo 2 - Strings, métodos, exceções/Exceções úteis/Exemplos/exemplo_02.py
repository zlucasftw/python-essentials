# Exceções úteis

# Exceções integradas - IndexError

# Localização: BaseException <- Exception <- LookupError <- IndexError

# É uma exceção concreta que é levantada quando se tenta
# acessar um elemento de uma sequência inexistente.

# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')
