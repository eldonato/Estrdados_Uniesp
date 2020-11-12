def main():
    matriz = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
    count = 0

    for i in range(2):
        print(f'{i+1}ª matriz:')
        for j in range(4):
            matriz[i][j] = int(input(f'Digite o {j+1}º número da matriz: '))

    print(matriz)

    for i in range(len(matriz)):
        for j in len(matriz[i]):
            if matriz[i][j] > 10:
                count += 1

    print(f'A quantidade de valores maior que dez inseridos foi: {count}')
        

main()