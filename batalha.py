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

def batalhar(n):
    """Começou a batalha
    :param _type_ monstro: _description_
    """
    tal_monstro = escolhe_monstro(n)
    print('*'*25)
    while player['hp'] > 0 and tal_monstro['hp'] > 0:
        atacar_monstro(tal_monstro)
        info_batalha(tal_monstro)
    print('*'*25)
    if player['hp'] > 0:
        print(f"VITORIAA. \n Player ganhou de um monstro level {tal_monstro['nome']} ")
        aumentar_xp(tal_monstro)
        mostrar_player()
        #mostrar stratus e aumentar a experiencia
    elif tal_monstro['hp'] > 0 :
        print(f"Vc perdeu para um monstro level {tal_monstro['level']}")
    else:
        print('deu alguma merda')
    print('-'*50)

print(escolhe_monstro(1))