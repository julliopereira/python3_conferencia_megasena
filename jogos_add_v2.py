# COLETA INFORMACOES DE JOGOS E ADICIONA NO ARQUIVO numeros.json
import json

lista = []
lp = 'i'

def run(lp,lista):
    while lp != 'q':
        jogo = []
        jogo = input('\t- Digite o numero ou "q" para sair: ').split()
        lista.append(jogo)
        for sair in jogo:
            if sair == 'q':
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