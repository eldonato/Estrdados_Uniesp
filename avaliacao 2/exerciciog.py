''' Crie um array que o conteúdo seja nomes das cores. 
Em seguida remova apenas a cor "vermelho”, se houver.'''


def main():
    nomeDasCores = ['azul', 'vermelho', 'roxo']

    for i in range(0, 5):
        cor = input('Insira o nome de uma cor: ')
        nomeDasCores.append(cor)

    while 'vermelho' in nomeDasCores:
        indice = nomeDasCores.index('vermelho')
        nomeDasCores.pop(indice)

    print(nomeDasCores)


main()
