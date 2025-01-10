distancia = float(input('qual é a distancia da sua viagem?'))
print('você esta prestes  a começar uma  viagem de {}km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('e o preço da sua passagem será de r${:.2f}'.format(preço))