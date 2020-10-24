""" Crie um array referente aos anos de nascimento das 5 pessoas mais próximas a você. 
Em seguida:
- Ordene o array  na ordem crescente e mostre o resultado;
- Ordene o array na ordem decrescente e mostre o resultado; """


def main():
    anosNascimento = [1997, 2000, 1945, 1965, 2000]

    anosNascimento.sort()
    print(anosNascimento)

    anosNascimento.sort(reverse=True)
    print(anosNascimento)


main()
