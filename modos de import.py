# import = importa o módulo inteiro

# import sys
# print (sys.platform)



# partes = importa partes do módulo

# from sys import exit, platform
# print (platform)

# platform = 'outro' # CUIDADO! valores importados em partes podem ser subscritos 
# print(platform)



# as = renomeia o módulo
# import sys as sistema
# print(sistema.platform)

from sys import platform as plataforma
from sys import exit as sair

print(plataforma)
sair()