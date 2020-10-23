def checarLimite(valor, limiteMenor, limiteMaior):
    if (type(valor) is list):
        for i in valor:
            if (i < limiteMenor or i > limiteMaior):
                return True
    else:
        if (valor < limiteMenor or valor > limiteMaior):
            return True


def main():
    biggest = 0
    count = 0
    qtdVelas = int(input('Insira a quantidade de velas: '))
    velasAltura = []

    while (checarLimite(qtdVelas, 1, 10**5)):
        qtdVelas = int(
            input('O número inserido está fora dos limites, insira novamente [1 - 10⁵]'))

    velasAlturaString = input('Insira a altura das velas: ')

    for i in velasAlturaString.split():
        if (int(i) > biggest):
            count = 1
            biggest = int(i)
        elif (int(i) == biggest):
            count = count+1
        velasAltura.append(int(i))

    while (checarLimite(velasAltura, 1, 10**7)):
        velasAltura.clear()
        biggest = 0
        print('Ops, a altura de uma das velas está fora dos limites [1 - 10⁷]')
        velasAlturaString = input('Insira novamente a altura das velas: ')

        for i in velasAlturaString.split():
            if (int(i) > biggest):
                count = 1
                biggest = int(i)
            elif (int(i) == biggest):
                count = count+1

            velasAltura.append(int(i))

    print(f'Número de velas com a altura máxima = {count}')


main()
