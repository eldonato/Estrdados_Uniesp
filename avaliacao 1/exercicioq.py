def tabuada(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero*i}')


def main():

    num = int(input('Digite um número de 1 a 10 pra fazer a tabuada: '))

    while(num < 1) or (num > 10):
        num = int(input('Ops.. O número deve ser entre 1 e 10!: '))

    tabuada(num)


main()
