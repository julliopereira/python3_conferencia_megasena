import json

resultado = input('Digite o resultado espacos entre os numeros: ').split()
print('\n')
filename = 'numeros.json'
with open(filename, 'r') as f_obj:
    file = json.load(f_obj)

for lista in file:
    cont = 0
    for valor in lista:
        for comp in resultado:
            comp = int(comp)
            valor = int(valor)
            if comp == valor:
                cont += 1
    if cont < 4:
        print(f'\t{line} \t= {cont} ')
    elif cont == 4:
        print(f'\t{line} \t= {cont} QUADRA !!!! ')
    elif cont == 5:
        print(f'\t{line} \t= {cont} QUINA  !!!!! ')
    elif cont == 6:
        print(f'\t{line} \t= {cont} SENA   !!!!!!! ')