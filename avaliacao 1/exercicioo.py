'''
Dada uma sequência de números inteiros, imprimir seus quadrados.
Entradas do programa:
        nº de início da sequência = 0
        nº de fim da sequência = 4
Saída do programa:
         sequência : 0, 1, 4, 9, 16
'''


def mainFor():
    numInicio = int(input('Digite o primeiro número da sequência: '))
    numFinal = int(input('Digite o último número da sequencia: '))
    qtdNumeros = 0

    while (numInicio > numFinal):
        print('Ops, o número inicial não pode ser maior que o final. Digite novamente')
        numInicio = int(input('Número inicial: '))
        numFinal = int(input('Número final: '))

    qtdNumeros = numFinal - numInicio

    print('sequência:', end=' ')
    for i in range(0, qtdNumeros+1):
        print((numInicio+i)*(numInicio+i), end=' ')
    print()


def mainWhile():
    numInicio = int(input('Digite o primeiro número da sequência: '))
    numFinal = int(input('Digite o último número da sequencia: '))
    qtdNumeros = 0
    count = 0

    while (numInicio > numFinal):
        print('Ops, o número inicial não pode ser maior que o final. Digite novamente')
        numInicio = int(input('Número inicial: '))
        numFinal = int(input('Número final: '))

    qtdNumeros = numFinal - numInicio

    print('sequência:', end=' ')
    while (count <= qtdNumeros):
        print((numInicio+count)*(numInicio+count), end=' ')
        count += 1


mainFor()
mainWhile()
