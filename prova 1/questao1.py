def diaDoProgramador(ano):
    if (ano < 1918):
        if ((ano % 4) == 0):
            return "12.09."+str(ano)
        else:
            return "13.09."+str(ano)
    elif (ano > 1918):
        if ((ano % 4 == 0) and (ano % 100 != 0)):
            return "12.09."+str(ano)
        else:
            return "13.09."+str(ano)
    elif (ano == 1918):
        return "27.09."+str(ano)


def main():
    ano = int(input('Insira o ano que você quer viajar: '))
    while (ano>2700 or ano < 1700) :
        ano = int(input('Ops! Ano indispínivel, por favor insira novamente [1700 - 2700]: '))

    data = diaDoProgramador(ano)
    print(data)


main()
