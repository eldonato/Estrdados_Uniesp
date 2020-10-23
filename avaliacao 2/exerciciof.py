""" Crie um programa no qual o usuário digitará 5 nomes num vetor (OBRIGATÓRIO TER SEU NOME INCLUÍDO NO VETOR).
 Em seguida:
a) Mostre os valores na tela. 
b) Adicione seu sobrenome na posição do seu nome no array.
c) Imprima o resultado na tela. """


def main():
    nomes = ['leo']

    for i in range(0, 5):
        nome = input(f'Insira o {i+1}º nome: ')
        nomes.append(nome)

    print(nomes)

    nomes[0] += ' donato'

    print(nomes)


main()
