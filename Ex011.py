print('Calculo de tinta por Metro Quadrado')
valor1 = int(input('Digite a largura de sua parede: '))
valor2 = int(input('Digite a altura de sua parede: '))
area = int(valor1 * valor2)
tinta = float(area / 2)
print('A área de sua parede é igual a {} e a quantidade necessária de tinta para pinta-la é de exatos {:.1f} litros de tinta por metro quadrado'.format(area, tinta))
