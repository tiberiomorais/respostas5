#Faça um algoritmo para imprimir:
#para um n informado pelo usuário. Use uma função que receba um valor
#n inteiro e imprima até a n-ésima linha.

#qt = int(input('Informe a qt de vezes: '))


def montar(numero):
    parada_i = numero + 1
    resposta = ' '
    for i in range(1,parada_i):
        parada_j = i+1
        for j in range(1,parada_j):
            resposta = resposta + str(i) + ' '
        resposta = resposta + ' \n'
    return resposta
#montar(10)

#INICIO DO ALGORITMO
numero = int(input('digite'))
print(montar(numero))