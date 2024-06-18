produto = {
    'nome': 'Caneta',
    'preço': 2.5,
    'categoria': 'Escritório'
}

dc = {
    # chave: valor 

    # chave: valor.upper() # -> retorna erro pq tem um float no dicionario
    # if isinstance(valor, str) else valor # -> essa linha evita o erro escrito na linha acima

    # outra alternativa:
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()

    for chave, valor 
    in produto.items()

    if chave == 'categoria' # -> Filtro!!!
}

print(dc)

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
]

dici = {
    chave: valor 
    for chave, valor in lista
}

print(dict(lista))

print(dici)



# SET COMPREHENSION


set1 = {num ** 2 for num in range(10)} # ou set(range(10))

print(set1)