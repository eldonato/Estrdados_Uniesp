area = float(
    input('Qual o tamanho, em metros quadrados, da área a ser pintada? '))

coberturaLata = 54

qtdLata = area/coberturaLata

if (area % qtdLata) != 0:
    qtdLata = round(qtdLata+0.5)

precoTotal = qtdLata * 80

print(f'Quantidade de latas: {qtdLata}')
print(f'Preço: R${precoTotal:.2f}')
input()
