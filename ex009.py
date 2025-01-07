real = float(input('quanto você tem de dinheiro na carteira? R$:'))
dolar = real / 6.12
print('com r${:.2f} você pode comprar us${:.2f}'.format(real, dolar))