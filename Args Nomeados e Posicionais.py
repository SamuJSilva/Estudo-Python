def soma(x, y, z=None): # Valor padrão de argumento
    if z is not None:
        print (f'{x=} y={y} {z=}', ' | ', 'x + y - z =', x + y - z)
    else:
        print (f'{x=} y={y}', ' | ', 'x + y =', x + y)


# Argumentos Posicionais: os valores sãos distribuídos conforme a posição dos parâmetros declarados da função, sendo respectivamente x, y e z
soma(2,3,1)

# Argumentos Nomeados: Cada argumento tem seu valor nomeado, independente da ordem
soma(y=2, z=1, x=1)

# Quando existem valores padrão, não é obrigatório a passagem do valor ao chamar a função
soma(1,2)

soma (1, 2, 0)

# Obs: Todos os argumentos APÓS um argumento nomeado DEVEM ser
# nomeados também. Uma função aceita argumentos posicionais e 
# nomeados na mesma instância, mas os posicionais DEVEM vir antes
# dos nomeados. O mesmo se aplica para valores padrão na função

soma (10, 15, z=25)