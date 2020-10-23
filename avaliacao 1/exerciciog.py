"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo.
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.
"""

def primeiroCalculo(n1, n2):
    return (n1*2)*(n2/2)

def segundoCalculo(n1,n3):
    return (n1*3)+n3

def terceiroCalculo(n3):
    return n3**3

def main():
    num1 = int(input("número 1: "))
    num2 = int(input("número 2: "))
    num3 = int(input("número 3: "))
    
    print(f'1º cálculo: {primeiroCalculo(num1, num2)}')
    print(f'2º cálculo: {segundoCalculo(num1, num3)}')
    print(f'3º cálculo: {terceiroCalculo(num3)}')

main()

