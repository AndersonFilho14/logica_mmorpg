from random import randint

monsterList = []


def criar_monstro(level=int):
    """Cria um monstro basedo no level que vc atribui"""     
    novo_monstro = {
        "nome" : f'Monstro {level}º',
        "level" : level,
        "dano" : 7 * level,
        "hp_max" : 100 * level,
        "hp" : 100 * level 
    }
    return novo_monstro

def criar_monstros(n_npcs= int):
    """Recebe a quantidade de monstros que vc quer e gera monstros
    :param list n_npcs: int
    """
    for i in range(n_npcs):
        monstro = criar_monstro(i+1)
        monsterList.append(monstro)

def exibir_lista_monstros():
    """Exibe a lista de monstro que foram feitos
    """
    for i in monsterList:
        print(f'Nome: {i['nome']} // level: {i['level']}  \
              // Dano igual a {i['dano']} // Hp {i['hp']}')

def escolhe_monstro(n = int):
    """Gera ate o numero de level que vc quer, e faz a escolha elatoria com qual vc luta

    :param _type_ n: _description_, defaults to int
    """
    criar_monstros(n)
    tal_monstro = monsterList[randint(0,(n-1))]
    return tal_monstro
