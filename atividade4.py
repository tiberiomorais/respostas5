# 4. Faça um programa, com uma função que necessite de um argumento. A
# função retorna o valor de caractere ‘P’, se seu argumento for positivo, e
# ‘N’, se seu argumento for zero ou negativo.


def avaliar(caractere):
    positivo = caractere > 0
    if positivo:
        return 'P'
    else:
        return 'N'

caractere = float(input('Informe o valor:'))
print(avaliar(caractere))
