def main():
    dados = {}
    conjDados = []

    for i in range(3):
        print(f'{i+1}º usuário: ')

        nome = input('Insira o nome: ')
        endereco = input('Insira o endereço: ')
        cpf = input('Insira o cpf: ')

        dados = {'nome': nome, 'endereco': endereco, 'cpf': cpf}
        conjDados.append(dados)
    
    print(conjDados)

main()
