string = 'banana'
metodo = "upper"
# debug console (somente em modo debug) --> dir(string) --> mostra todos os atributos e métodos do objeto string 

print(string)

# hasattr(...) -> checa se o objeto possui o atributo, com um mecanismo de busca
if hasattr(string, 'upper'):
    print (string.upper())
    print(getattr(string, metodo)) # getattr retorna local da memória
    print(getattr(string, metodo)()) # getattr executa o método
