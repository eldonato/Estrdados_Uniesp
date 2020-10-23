'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar.
Sabendo que a decisão é sempre pelo mais barato.
'''


def main():
    valorProduto = 100000
    ordemProduto = 0

    for i in range(0, 3):
        preco = float(input(f'Insira o valor do produto {i+1}: '))

        if (valorProduto > preco):
            valorProduto = preco
            ordemProduto = i+1

    print(
        f'O produto {ordemProduto} é o mais barato, custando R${valorProduto:.2f}')


main()
