def main():
    endereco = {}

    for i in range(3):
        cep = int(input('Insira o cep da rua: '))
        rua = input('Insira o nome da rua: ')

        endereco[cep] = (rua)

        print()
        print()

    print(endereco.keys)


main()
