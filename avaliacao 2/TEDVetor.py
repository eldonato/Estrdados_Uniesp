'''
Crie uma agenda eletrônica que contenha dois vetores: 
um array com o nome dos seus amigos e outro com as suas respectivas datas de aniversário.
Tente inserir e remover as informações da agenda de maneira dinâmica 
(apagando pelo nome ou posição, inserindo n usuários por vez caso queira, etc...). 
'''
agendaEletronica = {}


def visualizarAgenda():
    if agendaEletronica:
        print('NOME | DATA DE ANIVERSARIO')
        print(agendaEletronica)
    else:
        print('A agenda está vazia')


def adicionarContato():
    editar = 's'
    while (editar.lower() == 's'):
        nome = input('Digite o nome: ')
        data = input('Insira a data: ')
        agendaEletronica[nome] = data
        editar = input('Deseja continuar adicionando contatos? [s/n] ')
    print('\n\n\n\n')


def excluirContato():
    editar = 's'
    while (editar.lower() == 's'):
        nome = input('Digite o nome do contato a ser excluído: ')
        agendaEletronica.pop(nome, 'Contato não existe')
        editar = input('Deseja continuar adicionando contatos? [s/n]')
    print('\n\n\n\n')


def main():
    print(
        'Visualizar Agenda [1] | Adicionar Contato [2] | Excluir Contato [3] | Sair da agenda [4]')
    opcao = int(input())

    if (opcao == 1):
        visualizarAgenda()
    elif(opcao == 2):
        adicionarContato()
    elif(opcao == 3):
        excluirContato()
    elif(opcao == 4):
        exit()


while True:
    main()
