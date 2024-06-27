a = "a" 
b = "b"


# try:
#     print('linha 1')
#     c = a ** b
#     # Quando um erro é encontrado em try, o código é interrompido e transferido para o except, ou seja, o código abaixo não será executado
#     # A desvantagem é que, quando usado dessa forma, o try - except silencia todos os erros que estão contidos nesse trecho do código.
#     # Por exemplo, se a variável b não for declarada irá gerar outro tipo de erro
#     print('linha 2')
#     print('aaaaaaaaaa')
    
# except:
#     print('ERRO ENCONTRADO')
    
# Uma melhor prática é especificar qual o erro esperado e tratá-lo individualmente, dessa forma:    
# try:
#     print('linha 1')
#     c = a ** b
#     print('linha 2')
#     print('aaaaaaaaaa')
# except TypeError:
#     print('Impossível dividir duas letras')
# except NameError:
#     print('Variável não definida')
# except (IndentationError, ImportError) as error: # Classe recebe a instância
#     print('IdentationError OR ImportError')
#     print('MSG: ', error)
#     print('ERROR: ', error.__class__.__name__) # Cada exception é derivada de uma classe


# print('FIM...')

try:
    print('linha 1')
    c = a ** b

except TypeError:
    print('Impossível dividir duas letras')
    
else: # executa quando o código executa sem erro
    print('Não deu erro')
    
finally: # Sempre será executado, mesmo que ocorra um erro
    print('linha 2')
    print('aaaaaaaaaa')

    