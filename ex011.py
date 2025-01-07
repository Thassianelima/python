preço = float(input('qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
