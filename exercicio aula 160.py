from copy import deepcopy

produtos = [
    {'nome': 'Produto 4', 'preco': 38.55},
    {'nome': 'Produto 3', 'preco': 9.99},
    {'nome': 'Produto 1', 'preco': 12.36},
    {'nome': 'Produto 5', 'preco': 22.00},
    {'nome': 'Produto 2', 'preco': 38.89},
]

# TODO: aumente o preço dos produtos em 10% e gere uma nova_lista com deep copy

def aumenta_preco_10(produto):
    for prod in produto:
        produto['preco'] = round(produto['preco'] * 1.10, 2)
    return produto
        
lista_copia = deepcopy(produtos)
nova_lista = []

for produto in lista_copia:
    nova_lista.append(aumenta_preco_10(produto))
    
#print(*nova_lista, sep='\n')

# TODO: ordene os produtos por nome decrescente e gere produtos_ordenados_por_nome com deep copy

def ordenar_nome(dicionario):
    return dicionario['nome']

produtos_ordenados_por_nome = sorted(
    deepcopy(nova_lista), 
    key=ordenar_nome, 
    reverse = True
    )


# print(*produtos_ordenados_por_nome, sep='\n')

# TODO: ordene os produtos por valor crescente e gere produtos_ordenados_por_preco com deep copy

def ordenar_preco(dicionario):
    return dicionario['preco']

produtos_ordenados_por_valor = sorted(
    deepcopy(nova_lista), 
    key=ordenar_preco, 
    )

# print(*produtos_ordenados_por_valor, sep ='\n')

print('LISTA ORIGINAL:')
print(*produtos, sep = '\n')
print()
print('NOVA LISTA:')
print(*nova_lista, sep='\n')
print()
print('ORDENADA POR NOME DECRESCENTE:')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('ORDENADA POR VALOR CRESCENTE:')
print(*produtos_ordenados_por_valor, sep ='\n')
