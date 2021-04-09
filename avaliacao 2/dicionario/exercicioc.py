def main():
    endereco = {}
    enderecoRev = {}

    for i in range(3):
        cep = int(input('Insira o CEP da rua: '))
        rua = input('Insira o nome da rua: ').lower()

        endereco[cep] = (rua)
        enderecoRev[rua] = (cep)

        print()
        print()

    buscaCep = int(input('Insira o CEP a ser buscado: '))
    if buscaCep in endereco.keys():
        print(f'O CEP inserido se refere a rua {endereco[buscaCep]}')
    else:
        print('CEP não encontrado')


    buscaRua = input('Insira nome da rua a ser buscada: ').lower()

    if buscaRua in enderecoRev.keys():
        print(f'A rua inserido se refere a rua {enderecoRev[buscaRua]}')
    else:
        print('Rua não encontrada')

    print(endereco)
    print(enderecoRev)
    

main()
