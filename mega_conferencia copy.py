import json

lista = []                              # CRIA LISTA VAZIA
lp = 'i'                                # VARIAVEL PARA VERIACAR SAÍDA

def run(lp,lista):                      
    while lp != 'q':                    # ENQUANTO lp DIFERENTE DE q
        jogo = []
        jogo = input('\t- Digite o numero ou "q" para sair: ').split()
        lista.append(jogo)              # COPIAR LISTA JOGO PARA LISTA 
        for sair in jogo:               
            if sair == 'q':             # VERIFICAR SE HA ALGUMA LETRA q , SE HOUVER SAIR DO PROGRAMA
                lista.pop()
                lp = 'q'

def json_read(lista):
    filename = 'numeros.json'
    with open(filename, 'w') as f_obj:
        json.dump(lista, f_obj, indent=1)

    with open(filename, 'r') as f_obj:
        jogos = json.load(f_obj)

    print(f'\n\n- Os jogos são:')
    for game in jogos:
        print(f'\t{game}')

def conferencia(resultado):
    filename = 'numeros.json'
    with open(filename, 'r') as f_obj:
        file = json.load(f_obj)

    for list in file:
        cont = 0
        for valor in list:
            for comp in resultado:
                comp = int(comp)
                valor = int(valor)
                if comp == valor:
                    cont += 1
        if cont < 4:
            print(f'\t{list} \t= {cont} ')
        elif cont == 4:
            print(f'\t{list} \t= {cont} QUADRA !!!! ')
        elif cont == 5:
            print(f'\t{list} \t= {cont} QUINA  !!!!! ')
        elif cont == 6:
            print(f'\t{list} \t= {cont} SENA   !!!!!!! ')

menu = int(input('[1] Adicionar os jogos/apostas \n[2] Conferir resultado \n\nOpção:  '))
if menu == 1:
    print('\n\n')
    run(lp,lista)
    json_read(lista)
elif menu == 2:
    print('\n\n')
    resultado = input('\nDigite o resultado da mega sena com espaços: ').split()
    conferencia(resultado)
else:
    print('\n\nDigitou número errado !!!')

