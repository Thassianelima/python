velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('Multado! voce excedeu o limite!')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um dia dirija com segurança')