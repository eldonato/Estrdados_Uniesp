'''
Entrei no banco e quero saber o meu tempo médio de espera.
Faça um programa que calcule e mostre a média aritmética de um cliente
baseado nos tempos de espera dos clientes anteriores (máximo 5  clientes). 
'''


def calculaTempo(tempo, qtd):
    return (tempo/qtd)


def main1():
    qtdCliente = int(input('Quantos clientes na fila? '))
    while (qtdCliente > 5):
        qtdCliente = int(
            input('Quantidade excedendo os limites, digite novamente: '))

    count = 0
    tempoEspera = 0

    while (count < qtdCliente):
        tempoEspera += float(
            input(f'Insira o tempo de espera (minutos) do {count+1}° cliente: '))
        count += 1

    esperaMedia = calculaTempo(tempoEspera, qtdCliente)

    print(f'Seu tempo médio de espera é: {esperaMedia:.2f} minutos')


main1()


def main2():
    qtdCliente = int(input('Quantos clientes na fila? '))

    while (qtdCliente > 5):
        qtdCliente = int(
            input('Quantidade excedendo os limites, digite novamente: '))

    tempoEspera = 0
    
    for i in range(0, qtdCliente):
        tempoEspera += float(
            input(f'Insira o tempo de espera (minutos) do {i+1}° cliente: '))

    esperaMedia = calculaTempo(tempoEspera, qtdCliente)

    print(f'Seu tempo médio de espera é: {esperaMedia:.2f} minutos')


main2()
