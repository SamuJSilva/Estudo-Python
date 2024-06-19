#  Em Python, os valores truthy e falsy se referem a valores que são avaliados como True ou False em um contexto booleano. Isso significa que, em expressões condicionais, loops e outras operações que exigem um valor booleano, esses valores serão tratados como verdadeiros ou falsos.

# EXEMPLOS DE FALSY

# MUTÁVES
listaf = []
dicionariof = {}
tuplaf = ()
# IMUTÁVES
strf = ''
inteirof = 0
floatf = 0.0
nada = None
bolf = False
rangef = range(0)

# OBS: Valores VAZIOS em tipos MUTÁVEIS sempre será Falsy (como no exemplo acima), mas se existir qualquer valor ou objeto dentro do mutável ele será Truthy, exemplo, lista = [0] --> Truthy
