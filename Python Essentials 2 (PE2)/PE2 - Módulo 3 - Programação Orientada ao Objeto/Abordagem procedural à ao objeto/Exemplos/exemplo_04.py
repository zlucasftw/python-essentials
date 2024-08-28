# Uma curta viagem da abordagem processual à abordagem ao objeto

# A stack - a abordagem ao objeto

# Qualquer componente da classe que possui um nome
# começando com dois underscores (__), significa
# que o componente é privado. Ou seja, só pode ser
# acessado somente dentro e pela própria classe.
# Essa é a maneira de realizar o conceito de
# encapsulamento no Python. A partir desse momento
# esse componente (atributo, método, etc)
# não é visível fora de sua classe.

# Nesse caso tentaremos acessar um atributo
# privado da classe stack de maneira direta
# o que causará uma exceção.

class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.__stack_list))
