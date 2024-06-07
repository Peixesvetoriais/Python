print('Aluguel de Carro')
Km = float(input('Quantos quilometros foram rodados? KM'))
Dia = int(input('A quantos dias o carro foi alugado?'))
print('O valor da fatura do carro alugado é R${:.2f}'.format((60 * Dia) + (Km * 0.15)))