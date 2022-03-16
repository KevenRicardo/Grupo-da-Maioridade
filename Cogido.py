import time
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for dat in range (1,5):
    naceu = int(input('Em que ano {} pessoa naceu:'.format(dat)))
    idade = atual - naceu
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
time.sleep(2)
print()
print('carregando...')
print()
time.sleep(2)
print('='*36)
print('Ao todo tivemos \033[31m{}\033[m de pessoas de maior de idade'.format(totalmaior))
print('Ao todo tivemos \033[31m{}\033[m de pessoas menor de idade'.format(totalmenor))
print('='*36)
