# COLETA INFORMACOES DE JOGOS E ADICIONA NO ARQUIVO numeros.json
import json

lista = []
lp = 'i'
qty = int(input('\nQuantos números tem os jogos ? [6|7|8|9|10...]: '))

def run(qty,lp,lista):
    while lp != 'q':
        jogo = []
        qtyt = qty
        try:
            while qtyt != 0:
                num = int(input('\t- Digite o numero: '))
                jogo.append(num)
                qtyt -= 1
        except ValueError:
            print(f'valor incorreto: {num}')
        if len(jogo) == qty:
            lista.append(jogo)
        lp = input('\n\n- Para encerrar tecle "q": ')

def json_read(lista):
    filename = 'numeros.json'
    with open(filename, 'w') as f_obj:
        json.dump(lista, f_obj)

    with open(filename, 'r') as f_obj:
        jogos = json.load(f_obj)

    print(f'\n\n- Os jogos são:')
    for game in jogos:
        print(f'\t{game}')

run(qty,lp,lista)
json_read(lista)