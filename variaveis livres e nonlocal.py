def fora():
    a = 5 # -> a = variável livre, porque não está definida no escopo da função dentro
       
    # def dentro(y):
    #     a += y # retorna um erro, porque uma variável livre NÃO PODE ser alterada em uma função interna, apenas lida
    #     return a
    # return dentro
    
    
    def dentro(y):
        nonlocal a 
        a += y # essa operação vai concatenar com a variável 'a', mas o valor vai continuar salvo na variável 'a'
        
        # Exemplo, se Y = 10, o valor de a continuará 15, mesmo durante outra execução da função
        return a
    return dentro

resultado1 = fora()
# resultado2 = fora()

print(resultado1(5), resultado1(5), resultado1(5), sep="\n") # -> Retorna valores diferentes em cada instância