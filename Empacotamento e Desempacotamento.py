# o sinal * antes dos args = empacotamento. O 'resto' dos argumentos são empacotados em uma tupla, podendo ser 1, 2 ou mais argumentos.

# x, y, *ababa = 1, 2, 3, 4, 5, 6, 7, 8

# # print (
# # f'''{x}
# # {y}
# # {ababa}'''
# #     )

# def soma(*args):
#     total = 0
#     for lista in args:
#         for numero in lista:
#             total += numero

#     print (total)

# soma(ababa)



def mult(*nums):
    total = 1
    for num in nums:
        total *= num
    
    return total


print(mult(5, 9, 7, 5))
