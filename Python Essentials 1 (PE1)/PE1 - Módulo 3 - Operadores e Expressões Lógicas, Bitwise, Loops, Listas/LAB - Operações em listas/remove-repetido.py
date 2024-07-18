# LAB: Operações com listas - noções básicas

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for numbers in my_list:
    if numbers in my_list:
        del my_list[numbers]
    if numbers not in my_list:
        my_list = my_list[numbers]

my_list.sort()

print("The list with unique elements only:")
print(my_list)
