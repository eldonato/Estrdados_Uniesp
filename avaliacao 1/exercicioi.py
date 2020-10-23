'''
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
'''


def valueCheck(n1):
    if (n1 > 0):
        return("O número é positivo")
    elif(n1 < 0):
        return("O número é negativo")
    else:
        return("O número é nulo")


def main():
    valor = int(input("Insira um número: "))
    print(valueCheck(valor))


main()
