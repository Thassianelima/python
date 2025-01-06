#nome = input('qual é o seu nome')
#print('prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input("um valor:"))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1/n2
d1 = n1//n2
e = n1 ** n2
print('a soma vale {}'.format(n1+n2))
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('divisão inteira é {} e potência {}'.format(d1, e))