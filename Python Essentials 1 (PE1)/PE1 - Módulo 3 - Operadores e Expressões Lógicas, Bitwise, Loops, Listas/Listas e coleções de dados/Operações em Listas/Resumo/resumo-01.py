# Resumo da seccção - Key takeaways

# Cópia da lista - atribuição apenas aponta para a mesma lista na memória

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one)  # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0]  # deletes 'car'
print(vehicles_two)  # outputs: ['bicycle', 'motor']
