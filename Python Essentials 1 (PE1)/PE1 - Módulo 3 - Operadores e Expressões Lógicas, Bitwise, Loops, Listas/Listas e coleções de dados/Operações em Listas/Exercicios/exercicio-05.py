# Exercício 5

# Insira in ou not in em vez de ??? para que o código faça output do resultado esperado.

my_list = [1, 2, "in", True, "ABC"]

# print(1 ??? my_list)  # outputs True
# print("A" ??? my_list)  # outputs True
# print(3 ??? my_list)  # outputs True
# print(False ??? my_list)  # outputs False

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 in my_list)  # outputs True
print(False in my_list)  # outputs False

# Terceira resposta incorreta pois o operador not in verifica se não está na lista retornando
# True ou False de acordo com o resultado e o in verifica se está presente na lista retornando
# True ou False, o que explica por que '3 in my_list' retornou False pois não esta na lista
# então deveria ser not in para retornar o output esperado, que é True

print(3 not in my_list)  # outputs True
