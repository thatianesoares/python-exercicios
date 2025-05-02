from time import sleep
n = int(input('Digite um número: '))
print('Analisando....')
sleep(1)
resultado = n % 2
if resultado == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
