# lista = [1,0,8,84,503,4,53,453,698,21,2,654,7,65]

# lista2 = sorted(lista) # -> cria uma cópia rasa da lista original

# # print (lista)
# lista.sort() # -> mexe na lista original
# print (lista)



lista = [
    {'nome': 'Julio', 'sobrenome': 'Barreto'},
    {'nome': 'Maria', 'sobrenome': 'Augusta'},
    {'nome': 'Thiago', 'sobrenome': 'Vinicius'},
    {'nome': 'João', 'sobrenome': 'Gabriel'},
    {'nome': 'Magal', 'sobrenome': 'Silva'}
]

# lista.sort() -> Retorna um erro porque o Python não consegue organizar em tipos dict


#       ORDENAÇÃO POR FUNÇÃO NOMEADA

# def ordenar(dicionario):
#     return dicionario['sobrenome'] # -> Ordena por nome

# lista.sort(key=ordenar)


#       ORDENAÇÃO POR FUNÇÃO LAMBDA

# lista.sort (key= lambda item: item['sobrenome'])
# # lista2 =  sorted (lista, key= lambda item: item['sobrenome'])

# for item in lista:
#     print(item)



def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = executa(lambda m: lambda n: m * n, 2)

# funcao = lambda parametro: parametro # -> MÁ PRÁTICA!!

print(
    executa(lambda x, y: x + y, 2, 3),
    executa(soma, 2, 3),
    soma(2,3)
)

print(duplicar(3))

print(
    executa(
        lambda *args: sum(args),
        1,7, 9, 65, 24
    )
)