import random
n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('quatro aluno'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))