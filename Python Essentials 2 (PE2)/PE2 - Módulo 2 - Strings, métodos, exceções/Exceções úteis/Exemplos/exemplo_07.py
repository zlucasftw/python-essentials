# Exceções úteis

# Exceções integradas - KeyError

# Localização: BaseException <- Exception <- LookupError <- KeyError

# É uma exceção concreta lenvatada quando se tenta acessar
# a um elemento inexistente de uma coleção.

# How to abuste the dictionariy
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)
