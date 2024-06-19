lista = ['a', 10, 2.5, (1,2,3), True, {1,2,3}, {'nome': 'Batata'}]

for item in lista:
    print(item, isinstance(item, set))