def main():
    matriz = [[1, 2, 3, 4], [5, 6, 7, 8]]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

    print(""*2)

    for i in range(len(matriz)):
        valor = int(input('Insira um valor: '))
        matriz[i].append(valor)
    
    print(""*2)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    
    
main()