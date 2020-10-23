'''
Crie um programa que o usuário digite uma sequência de valores
(de tamanho dinâmico) numa única variável, chamada registro.
Em seguida, mostre os valores armazenados.
'''


def main():
    qtd = int(input('Quantidade de números a ser inserido: '))
    registro = []

    for i in range(qtd):
        registro.append(int(input(f'{i+1}º valor: ')))

    print(registro)


main()
2