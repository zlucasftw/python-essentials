# Resumo da secção - Key takeaways

# 4. Uma lista pode ser o resultado/retorno de uma função

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


print(create_list(5))
