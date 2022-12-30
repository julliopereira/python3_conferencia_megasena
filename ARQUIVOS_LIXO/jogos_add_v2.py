# COLETA INFORMACOES DE JOGOS E ADICIONA NO ARQUIVO numeros.json
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

run(lp,lista)
json_read(lista)