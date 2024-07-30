# def decorator(func):
#     print('Decoradora 1')
    
#     def inner(*args, **kwargs):
#         print('Aninhada / Interna')
    
#         result = func(*args, **kwargs)
        
#         return result
#     return inner

# @decorator
# def soma (x, y):
#     return x+y

# multiply = decorator(lambda x,y: x*y)
# multiplica_10_2 = multiply(10,2)
# print(multiplica_10_2)

# soma_10_5 = soma (10, 5)
# print(soma_10_5)

# DECORADORES CONCATENAM, principalmente no caso de usar mais de 1 decorador

def param_decorator(name):
    def decorator(func):
        print('Decorador:', name)
        
        def new_function(*args, **kwargs):
        
            result = func(*args, **kwargs)
            final = f'{result}, {name}'
            
            return final
        return new_function
    return decorator

# a execução é de baixo pra cima
@param_decorator(name='segundo')
@param_decorator(name='primeiro')
def soma (x, y):
    return x+y


soma_10_5 = soma (10, 5)
print('RESULTADO FINAL: ', soma_10_5)