# 3. Faça um programa, com uma função que necessite de três argumentos, e
# que forneça a soma desses três argumentos.

def adicao(a,b,c):
    soma = a + b + c
    return soma

num1 = int(input('Informe o numero 1: '))
num2 = int(input('Informe o numero 2: '))
num3 = int(input('Informe o numero 3: '))

somar = adicao(num1,num2,num3)

print(f'A soma é: {somar}')