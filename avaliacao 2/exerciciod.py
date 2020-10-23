""" Elabore um programa que cria um array de nomes de países e outro array com nomes de cidades.
Cada uma das criações devem ser feitas com métodos diferentes. """

def main():
    listaPaises = []
    listaCidades = []

    qtd = int(input('Quantos países vc quer inserir? '))
    for i in range(0,qtd):
        pais = input('Insira o nome de um país: ')
        listaPaises.append(pais)
    
    qtd = int(input('Quantos cidades vc quer inserir? '))
    for i in range(0,qtd):
        cidade = input('Insira o nome de um país: ')
        listaCidades.append(cidade)
    
    print(listaPaises)
    print(listaCidades)
    
main()

