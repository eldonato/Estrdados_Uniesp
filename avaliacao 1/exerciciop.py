def fatorialFor(num):
    fatorial = 1
    for i in range(1, num+1):
        fatorial = fatorial*i

    return fatorial


def fatorialWhile(num):
    count = 1
    fatorial = 1

    while (count <= num):
        fatorial = fatorial * count
        count += 1

    return fatorial


def main():
    num = int(input('Digite um número para calcular o fatorial: '))

    print(f'{num}! = {fatorialFor(num)}')
    print(f'{num}! = {fatorialWhile(num)}')


main()
