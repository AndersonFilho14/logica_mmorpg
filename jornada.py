from random import randint
from boss import escolhe_monstro
from player import player
from batalha import batalhar

def main_root():
    """Vai dar inicio a todo o codigo aqui
    """
    loading()

def loading():
    print('\nInicio do game \n' )
    print('Parar parar o jogo escreva alguma letra\n')
    #tela escolha
    i = 1
    while True:
        try:
            route = int(input('Qual o nivel que vc quer?: 1/2/3/4/5: \n'))
            if route > 5:
                print('Numero deve ser menor que seis')
                continue  # Reinicia o loop se o número for maior que 5
            mons = rota(route)
            batalhar(mons)
            potion(i)
            i += 1
            

        except ValueError:
            print('\nFim de game\n')
            print('--Saldo de jogo:')
            print(f'Monstros abatidos {i}')
            print(f'Player level {player['level']}')
            break  # Encerra o loop e finaliza o jogo

    print('***********************    Jogo acabou    ***********************')

def rota(route):
    """Vai fazer o tipo de rota que iremos percorrer, escolhendo um caminho. Dentro do caminho vai ter um certo nivel de monstro
    :param _type_ route: qual caminho ira
    """
    if route == 1:
        mons = escolhe_monstro(2)
        return mons
    elif route == 2:
        mons = escolhe_monstro(4)
        return mons
    elif route == 3:
        mons =  escolhe_monstro(8)
        return mons
    elif route == 4:
        mons = escolhe_monstro(16)
        return mons
    elif route == 5:
        mons = escolhe_monstro(32)
        return mons


def potion(i):
    """Ira fazer o player ganhar hp
    """
    if i%2 != 0:
        luck = randint(0,8)
        if luck == 3:
            player['hp'] *= 1.8
            print('+'*5)
            print('Poção forte')
        elif luck == 2:
            print('+'*5)
            print('Potion media')
            player['hp'] *= 1.5
        elif luck == 1:
            print('+'*5)
            player['hp'] *= 1.3
            print('POção fraca')
        else:
            print('+'*5)
            print('Sem poção')
