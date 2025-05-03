print('Olá, bem-vindo(a) a calculadora de salários!')
nome=input('Qual o seu nome?')
print('Seja bem-vindo(a), {}!'.format(nome))
salario=float(input('Qual o salário do funcionário que você deseja avaliar ? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario,novo))
