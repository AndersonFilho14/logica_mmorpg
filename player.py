player = {
    'nome' : 'Ande',
    'level' : 10,
    'exp' : 0,
    'exp_max' : 50,
    'hp' : 100,
    'hp_max' : 100,
    'dano' : 25
    }


def mostrar_player():
    """Estado atual do player
    """
    print(f' Hp: {player["hp"]} , Hp max: {player["hp_max"]} , Dano {player["dano"]} \
           \n Level: {player["level"]}, Xp: {player['exp']} . Xp maximo: {player["exp_max"]},')

def aumentar_xp(tal_monstro):
    """Recebe o monstro e faz a soma com seus dados
    
    :param _type_ tal_monstro: _description_
    """
    player['exp'] += (tal_monstro['level'] * 10)
    if player['exp'] >= player['exp_max']:
         aumento_level()
         player['exp'] = 0
         player['exp_max'] *= 2

def aumento_level():
    """Aumenta o level
    """
    player['dano'] *= 3
    player['hp_max'] *= 3
    player['hp'] = player['hp_max']
    player['level'] += 1
