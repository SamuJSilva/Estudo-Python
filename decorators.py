# funções decoradoras decoram outras funções
# decorar = adicionar, remover, restringir, alterar
# Ou seja, eles alteram o comportamento de uma função, com mudanças mínimas no código
# @ - Syntax Sugar

def create_function(func):
    def internal(*args, **kwargs):
        
        print('Decorando ...')
        
        for arg in args:           
            is_string(arg)
        
        result = func(*args, **kwargs)
        
        print('Decorado!')
        # possível incluir lógica antes ou depois do resultado
        
        return result
    return internal


def is_string(par):
    if not isinstance(par, str):
        raise TypeError('param is not a string')
    
@create_function # ao usar o @, o Python entende que eu quero usar a função x junto com essa, mesmo que ela não seja chamada diretamente        
def invert_str (string):
    return string[::-1]


reversed = invert_str('Joel')
print(reversed)

# reverse_if_str = create_function(invert_str)
# reversed_string = reverse_if_str('123')
# print(reversed_string)