'''
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''


def checkNota(media, qtdNotas):
    media = media/qtdNotas
    if (media == 10):
        return("Aprovado com distinção.")
    elif (media >= 7):
        return("Aprovado")
    else:
        return("Reprovado")


def main():
    media = 0
    i = 0
    while(i < 2):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        if (nota >= 0 and nota <= 10):
            media += nota
            i += 1
        else:
            print('Nota inválida, digite novamente.')
    print(checkNota(media, i))


main()
