""" Crie um programa no qual o usuário digitará 5 nomes. 
Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:
a) Mostre o que o usuário digitou na tela;
b) O programa pedirá outro nome, que será adicionado no fim do vetor "registros”;
c) O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
d) Imprima o resultado na tela. """


def main():
    registros = []
    print('Insira 5 nomes')

    for i in range(0, 5):
        nome = input(f'Insira o {i+1}º nome: ')
        registros.append(nome)

    print(registros)

    nome = input('Insira um nome (ele será adicionado no fim do vetor): ')
    registros.append(nome)

    nome = input(
        'Insira um nome (ele será adicionado na 2ª posição do vetor): ')
    registros.insert(1, nome)

    print(registros)


main()
