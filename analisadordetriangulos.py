from time import sleep
print('---'*20)
print('Analisador de triângulos')
print('---'*20)
r1 = float(input('insira o primeiro segmento:'))
r2 = float(input('insira o segundo segmento:'))
r3 = float(input('insira o terceiro segmento:'))
print('Aguarde....')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
