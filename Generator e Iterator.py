import sys

# um Iterator __iter__ ou iter() retorna APENAS o valor ATUAL. Ele não consegue acessar o próximo valor e nem o anterior.
# Iterator apenas permite chamar a função next() ou __next__

iteravel = ['item 1', 'item 2', 'item 3']
iterador = iteravel.__iter__()# iter(iteravel) 
# print (next(iterador))

# Generator - funções que pausam sob determinada condição.

generator_lista = [i for i in range(30000)] # -> muitos valores salvos na memória
# mesmo se com um for, por exemplo, seja possível acessar um valor por vez, a lista inteira já estará salva na memória. No caso de uma lista grande ocupará muita memória

generator = (i for i in range(30000)) # -> NÃO EXISTE TUPLE COMPREHENSION!! A escrita dessa forma configura-se um generator!!

print(sys.getsizeof(generator_lista)) # Para observar a diferença entre ambos, essa função retorna o tamanho em bytes ocupado na memória
print(sys.getsizeof(generator))

# Quando o código é executado, a lista é criada e armazenada na memória, enquanto o generator cria aos poucos

for n in range(5):
    print(next(generator)) #-> funciona semelhante ao iterator