def rota(route):
    """Vai fazer o tipo de rota que iremos percorrer, escolhendo um caminho. Dentro do caminho vai ter um certo nivel de monstro
    :param _type_ route: qual caminho ira
    """

    if route == 1:
        escolhe_monstro(2)
    elif route == 2:
        escolhe_monstro(4)
    elif route == 3:
        escolhe_monstro(8)
    elif route == 4:
        escolhe_monstro(16)
    elif route == 5:
        escolhe_monstro(32)

def potion():
    
    luck = randint(0,3)
    if luck == 3:
        player['hp'] *= 1.8
        print('Poção forte')
    elif luck == 2:
        print('Potion media')
        player['hp'] *= 1.5
    elif luck == 1:
        player['hp'] *= 1.3
        print('POção fraca')
    else:
        print('Sem poção')

def main_root():
    """Vai dar inicio a todo o codigo aqui
    """
    a = 2
