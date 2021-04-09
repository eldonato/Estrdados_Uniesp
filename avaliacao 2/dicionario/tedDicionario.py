listaCliente = []
cadCliente = {} 
continuar = True

def regCliente():
    print("\n"*2)
    print('--- Registrar Cliente ---')
    print()
    nome = input('Insira o nome do cliente: ')
    divida = float(input('Insira a dívida do cliente: '))
    telefone = input('Insira o telefone do cliente: ')
    endereco = input('Insira o endereço do cliente: ')
    
    cadCliente = {'nome': nome, 'divida': divida, 'telefone': telefone, 'endereço': endereco}
    
    listaCliente.append(cadCliente)

    print('Cliente devedor cadastrado com sucesso!!')


def attDivida():
    print("\n"*2)
    print('--- Alterar a dívida ---')
    print()
    nome = input('Insira o nome do cliente: ')
    for i in listaCliente:
        if i['nome'] == nome:
            print(f"O cliente {nome} deve: R${i['divida']} ")
            divida = float(input('Insira a nova dívida: '))
            i['divida'] = divida
            print('Valor alterado com sucesso!!')
    input()


def rmvCliente():
    print("\n"*2)
    print('---Remover Cliente---')
    print()
    nome = input('Insira o nome do cliente: ')
    for i in range(len(cadCliente)):
        cliente  = cadCliente[i]
        if nome == cliente['nome']:
            global rmv
            rmv = i
    listaCliente.pop(rmv)

def buscaCliente():
    print("\n"*2)
    print('---Buscar Cliente---')
    print()
    nome = input('Insira o nome do cliente: ')
    for i in listaCliente:
        if i['nome'] == nome:
            print(f"O cliente {nome} deve: R${i['divida']} ")
    input()

def sair():
    global continuar
    continuar = False


    
    
            
def main():

    while continuar:
        print('1- Registrar Cliente \n2- Atualizar valor da dívida'+
            '\n3- Remover cliente que já pagou \n4- Buscar cliente \n5- Sair')
        opcao = int(input('Insira sua opção: '))
        
        if opcao == 1:
            regCliente()

        if opcao == 2:
            attDivida()

        if opcao == 3:
            rmvCliente()

        if opcao == 4:
            buscaCliente()

        if opcao == 5:
            sair()


main()
