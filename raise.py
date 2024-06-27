def dividir(numero, divisor):
    if divisor == 0 or numero == 0:
        raise ZeroDivisionError ('Tentando dividir por zero') 
    # Um erro é lançado. Pode ser usado para forçar um erro antes de dar um erro em sí, como por exemplo em uma condicional
    
    return numero / divisor
div = dividir(2,0)

print(div)