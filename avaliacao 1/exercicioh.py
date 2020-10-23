"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
1. salário bruto.
2. quanto pagou ao IPRF
3. quanto pagou ao INSS.
4. quanto pagou ao sindicato.
5. o salário líquido.
6. o valor descontado
"""


def calcSalario(qtdHoras, ganhoHora):
    return qtdHoras*ganhoHora


def calcImposto(bruto, taxa): #calcula todas as taxas
    return bruto * (taxa/100)


def salarioLiquido(bruto, descontos):
    return bruto-descontos


def main():
    qtdHoras = int(input('Digite a quantidade de horas trabalhadas: '))
    ganhoHora = float(input('Digite quanto você ganha por hora: '))
    salarioBruto = calcSalario(qtdHoras, ganhoHora)

    descontoIPRF = calcImposto(salarioBruto, 11)
    descontoINSS = calcImposto(salarioBruto, 8)
    descontoSindicato = calcImposto(salarioBruto, 5)

    descontoTotal = descontoINSS+descontoIPRF+descontoSindicato

    salarioLiq = salarioLiquido(salarioBruto, descontoTotal)

    print(f'Salário bruto: R${salarioBruto:.2f}')
    print(f'Desconto do Imposto de Renda: R${descontoIPRF:.2f}')
    print(f'Desconto do INSS: R${descontoINSS:.2f}')
    print(f'Desconto do Sindicato: R${descontoSindicato:.2f}')
    print(f'Salário liquido: R${salarioLiq:.2f}')
    print(f'Desconto total: R${descontoTotal:.2f}')


main()
