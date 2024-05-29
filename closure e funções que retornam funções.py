# def criar_saudacao(msg, nome):
#     def saudar():
#         return f'{msg}, {nome}!!!'
#     return saudar # -> Retornando a função sem (), ela apenas 
# referencia os valores da função mãe, ou seja, ela referencia o 
# local de memória onde estão salvos os argumentos usados 
# previamente, de forma que cada variável aponta um local de 
# memória diferente dependendo dos argumentos utilizados.

def criar_saudacao(msg): 
    def saudar(nome): # -> Um Closure SALVA args usados previamente, mas não proíbe que outros args sejam utilizados nas funções seguintes 
        return f'{msg}, {nome}!!!'
    return saudar


saudacao_bom_dia = criar_saudacao('Bom dia')
saudacao_boa_noite = criar_saudacao('Boa Noite')
print(saudacao_bom_dia("Celso")) # -> CLOSURE!!!! a função saudar será executada, e seus args já estão salvos
print(saudacao_boa_noite("Celso"))
