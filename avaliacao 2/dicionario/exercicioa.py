def main():
    listaUsuario = {}

    for i in range(2):
        nome = input('Insira o seu nome: ')
        dataNasc = input('Insira sua data de nascimento: ')
        endereco = input('Insira seu endereço: ')

        listaUsuario[nome] = (dataNasc, endereco)
        print()
        print()
        

    teste = 'leo'
    print(listaUsuario)
    if teste in listaUsuario.keys():
        print(listaUsuario[teste])


main()
