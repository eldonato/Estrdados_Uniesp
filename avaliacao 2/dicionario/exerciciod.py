def main():
    codigos = {123: ['maçã', 1.3], 124: ['banana', 1.5], 125: ['uva', 1.0],
               126: ['cajá', 2.0], 127: ['acerola', 5.0], 120: ['manga', 3.0]}

    print(codigos)
    print()

    del codigos[127]
    del codigos[120]

    print(f'Valores alterados: \n{codigos}')
    print()

    deletar = []

    for key, value in codigos.items(): #procura pela chave referente ao nome dos produtos e armazena

        if value[0] == 'cajá':
            deletar.append(key)
        if value[0] == 'uva':
            deletar.append(key)

    for i in deletar: #deleta as chaves armazenadas referente aos produtos
        del codigos[i]

    print(f'Valores alterados: \n{codigos}')


main()
