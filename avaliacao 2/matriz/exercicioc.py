def main():
    matriz = [[38, 14, 27], [21, 83, 92], [31, 12, 43]]

    for i in range(len(matriz)):
        matriz[i].pop()

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


main()
