# def generator(n=0):
#     yield '01' # pausa
#     print('Próximo ...')
#     yield '02' # pausa
#     print('Próximo ...')
#     yield '03' # pausa
#     print ('Última')
#     return 'ACABOU'

# def generator(n=0, max=10):
#     while True:
#         yield n

#         if n >= max:
#             return
        
#         n+=1

# gen = generator()

# # print(next(gen)) # retorna 01
# # print(next(gen)) # retorna print e 02

# for n in gen:
#     print(n)


#    GEN FROM

def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g1 = gen1()    
g2 = gen2()

print('gen 1')
for n in g1:
    print (n)

print ()

print('gen 2')
for n in g2:
    print (n)