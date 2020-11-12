def main():
    matriz = []
    matrizTemp = []
    matrizTrans = []

    tamanho = int(input('Insira o tamanho da matriz: '))

    for i in range(tamanho):
        for j in range(tamanho):
            valor = int(input('Insira um número: '))
            matrizTemp.append(valor)

        matriz.append(matrizTemp[:])

        matrizTemp.clear()

        print("")


    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matrizTemp.append(matriz[j][i])

        matrizTrans.append(matrizTemp[:])

        matrizTemp.clear()

        print("\n"*2)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    
    print("\n"*2)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matrizTrans[i][j], end=" ")
        print()


main()
