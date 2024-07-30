#       MINHA SOLUÇÃO:

# def soma(x):
#     def numero(y):
#         return x+y
#     return numero

# def multiplica (x):
#     def multiplicador(y):
#         return x*y
#     return multiplicador

# def executa(funcao, *args):
#     return funcao(*args)

# soma_com_5 = executa(soma, 5)
# multiplica_10 = executa(multiplica, 10)

# resultado_soma = soma_com_5(10)
# resultado_multiplica = multiplica_10(5)

# print(
#     f"""
#     Resultado Soma: {resultado_soma}
#     Resultado Multiplicação: {resultado_multiplica}
#     """
# )

#       SOLUÇÃO PROFESSOR

def soma(x,y):
    return x+y

def multiplica(x, y):
    return x*y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_5 = criar_funcao(soma, 5)
multiplica_10 = criar_funcao(multiplica, 10)

print(soma_com_5(10))
print(multiplica_10(2))