# from module import sum1, prod1

# import module

# print(module.counter)

from sys import path

path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.sum1(zeroes))
print(module.prod1(ones))

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(sum1(zeroes))
# print(prod1(ones))
