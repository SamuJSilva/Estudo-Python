pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Silva'
}

# (a1, a2), b = pessoa.items()
# # a, b = pessoa.items()

# print (a1, a2, b)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa= {
    'idade': 19,
    'peso': 85
}

pessoa_completa = {**pessoa, **dados_pessoa}

def mostra_args( **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_args(**pessoa_completa)