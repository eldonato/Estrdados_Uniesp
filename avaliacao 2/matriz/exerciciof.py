def main():
    dadosGeral = []
    dadosAluno = []

    for i in range(3):
        nome = input('Insira o nome: ')
        matricula = int(input('Insira a matricula: '))
        nascimento = input('Insira o nascimento: ')
        print(""*2)

        dadosAluno.append(nome)
        dadosAluno.append(matricula)
        dadosAluno.append(nascimento)

        dadosGeral.append(dadosAluno[:])

        dadosAluno.clear()

    print(dadosGeral)


main()