# l1 = list(range(10))

l1 = []

for num in range(10):
    l1.append(num)


l1 = [1 for num in range(10)] # numero 1 10x
l1 = [num for num in range(10)] # num 10x
l1 = [num ** 2 for num in range(10)] # num ao quadrado 10x

# print(l1)

#       MAPEAMENTO DE DADOS COM LIST COMPREHENSION
# mapeamento = cópia de um iterável, de mesmo tamanho com valores modificados (ou não)

produtos = [
    {'nome': 'p1', 'valor': 15},
    {'nome': 'p2', 'valor': 25},
    {'nome': 'p3', 'valor': 20}
]

# novos_produtos = [produto['valor'] for produto in produtos]

# novos_produtos = [{**produto, 'valor': produto['valor'] * 1.05} for produto in produtos] # adiciona + 5% ao valor

novos_produtos = [
    {**produto, 'valor': produto['valor'] * 1.05}
    if produto['valor'] > 20 else {**produto} 
    for produto in produtos
    if produto['valor'] > 15 # -> FILTRO!!!!!!!!!!
]

print (*novos_produtos, sep='\n')

lista = [n for n in range(10) if n <= 5] # -> FILTRO!!!!!!!!
print(lista)

# list comprehension com + de 1 for

# lista = [
#     (x, y)
#     for x in range(3)
#     for y in range (3)
# ]

lista = [
    [(x, l) for l in "Joui"]
    for x in range(3) # para cada x, a linha acima é executada
]

print(lista)

