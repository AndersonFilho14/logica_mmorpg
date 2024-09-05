from random import randint
from player import player,mostrar_player,aumento_level,aumentar_xp
from boss import criar_monstro, criar_monstros, escolhe_monstro, exibir_lista_monstros, monsterList



def atacar_monstro(monstro):
    """Ataca o monstro diminuindo seu hp
    :param _type_ monstro: _description_
    """
    monstro['hp'] -= player['dano']
    atacar_player(monstro)

def atacar_player(monstro):
    """Diminui o Hp do player
    :param _type_ monstro: _description_
    """
    if monstro['hp'] > 0:
        player['hp'] -= monstro['dano']

def info_batalha(monstro):
    """Mostra as informações da batalha
    :param _type_ monstro: _description_
    """
    print(f'Player : {player['hp']}/{player['hp_max']}  \
          \n {monstro['nome']}: {monstro['hp']}/ {monstro['hp_max']} ')
    print('-'*10)

def batalhar(monster):
    """Começou a batalha
    :param _type_ monstro: _description_
    """

    while player['hp'] > 0 and monster['hp'] > 0:
        atacar_monstro(monster)
        info_batalha(monster)
    print('*'*25)
    if player['hp'] > 0:
        print(f"VITORIAA. \n Player ganhou de um monstro level {monster['nome']} ")
        aumentar_xp(monster)
        mostrar_player()
        #mostrar stratus e aumentar a experiencia
    elif monster['hp'] > 0 :
        print(f"Vc perdeu para um monstro level {monster['level']}")
        break
    else:
        print('-'*90)
        print('deu alguma merda')
        print('-'*90)
    print('-'*50)
