import random


def inventario():
    global armas
    armas = {
        'espada': {'mensagem': 'Excelente escolha! Perfure seus inimigos!',
                   'dano': ['2d10']},
        'arco': {'mensagem': 'Seus inimigos não vão nem ver o que os atingiu! \
Muito bom!',
                 'dano': ['1d20']},
        'magia': {'mensagem': 'Deixe seus adversários pegando fogo! Ou o que \
sua imaginação permitir...',
                  'dano': ['1d10', '1d5']},
    }

    global jogador
    jogador = {
        'nome': '',
        'vida': 20,
        'inventario': [],
        'arma': '',
        'nome_arma': ''
    }

    global escolhas
    escolhas = {
        'positivos': 'simyes',
        'negativos': 'naonãono'
    }


def main():
    inventario()
    inicio()


def rolar(dados):
    resultado = 0
    for i in dados:
        dado = list(map(int, i.split('d')))
        rolagem = []
        for d in range(dado[0]):
            rolagem.append(random.randrange(1, ((dado[1])+1)))
            resultado += rolagem[d]
        # print(', '.join(list(map(str, rolagem)))) para imprimir cada roll
    return resultado


def texto(mensagem):
    print(mensagem, end='')
    input()


def confirmar_resposta(variavel, mensagem):
    primeira = True
    while True:
        if primeira:
            escolha = input('Confirma sua escolha? ')
            primeira = False
        else:
            escolha = input('Que foi, chefia? ')
        if escolha and escolha in escolhas['positivos']:
            break
        elif escolha and escolha in escolhas['negativos']:
            variavel = input(mensagem)
            confirmar_resposta(variavel, mensagem)
            break
    return variavel


def inicio():
    print('Olá jovem aventureiro!')
    texto('<Pressione Enter para continuar>')
    # Escolha do nome
    jogador['nome'] = input('Vamos começar com seu nome: ')
    jogador['nome'] = confirmar_resposta(jogador['nome'], 'Então seu nome é: ')
    print(jogador['nome'], '''parece o nome de um(a) verdadeiro \
aventureiro(a)!''', end='')
    input()
    texto(random.choice(['Será que você está preparado para o que lhe espera?',
                         'Boa sorte em sua jornada, você vai precisar...',
                         'Muito bem! Agora sim, à aventura...']))
    # Escolha da arma
    texto('''Você pode escolher entre uma espada, um arco, ou magia.''')
    while True:
        jogador['arma'] = input('Qual você escolhe? ')
        jogador['arma'] = confirmar_resposta(jogador['arma'],
                                             'Você tem certeza, grande? ')
        if jogador['arma'] not in armas:
            print('Escolha uma poderosíssima arma!')
        else:
            jogador['arma'] = armas[jogador['arma']]
            break
    # Escolha do nome da arma
    print(jogador['arma']['mensagem'])
    texto('Um poderoso guerreiro precisa de uma arma com um nome à altura!')
    jogador['nome_arma'] = input('Nomeie sua arma: ')
    print('O nome da sua arma letal é', jogador['nome_arma'])
    jogador['nome_arma'] = confirmar_resposta(jogador['nome_arma'],
                                              'Então a poderosa vai se chamar: ')


def saidas():
    num_saidas = random.randrange(4)
    portas = random.sample(['cima', 'direita', 'baixo', 'esquerda'],
                           n=num_saidas)
    for p in portas:
        if p == 'entrada':
            del (p)


def nova_sala():
    print(random.choice(['Você entra com sucesso em uma nova sala!',
                        '''Seus olhos demoram para se acostumar com a
                        escuridão da nova área...''']))
    random.choice([bau(), luta(), saida()])


def bau():
    texto('''À sua frente há um majestoso baú de ouro ornamentado com
    pedras preciosas. Você nunca viu algo tão lindo assim!''')
    print('O que você faz?')
    print('1. Abrir', '2. Chutar o baú', '3. Voltar')


def luta():
    ...


def saida():
    ...


if __name__ == '__main__':
    main()
