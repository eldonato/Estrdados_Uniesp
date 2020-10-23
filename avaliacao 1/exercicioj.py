'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Gênero Inválido. 
'''


def checkSexo(sexo):
    if (sexo.lower() == "m"):
        return("Gênero masculino")
    elif (sexo.lower() == 'f'):
        return("Gênero feminino")
    else:
        return('Gênero inválido')


def main():
    sexo = input("Insira seu sexo? (F/M) ")
    print(checkSexo(sexo))


main()
