# 7. Faça um programa que use a função valorPagamento para determinar o valor a
# ser pago por uma prestação de uma conta.
#
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias
# em atraso
#
# e passar estes valores # para a função valorPagamento, que calculará o valor a ser
# pago e devolverá este valor ao programa que a chamou.
#
# O programa deverá então exibir o valor a ser # pago na tela.
#
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
# até que seja informado um valor igual a zero para a # prestação.
#
# Neste momento o programa deverá ser encerrado, exibindo o relatório
# do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
#
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem
# atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
# mais 0,1% de juros por dia de atraso.


lista=[]
def valor_pagamento(valor_prestacao, qt_dias_atraso=0):
    multa = valor_prestacao * 0.03
    juros = qt_dias_atraso * 0.01

    if qt_dias_atraso == 0:
        total_a_pagar = valor_prestacao
        return total_a_pagar
    else:
        total_a_pagar = valor_prestacao + multa + juros
        return total_a_pagar

valor_prestacao = 1


while valor_prestacao != 0:
    valor_prestacao = float(input('\n Valor da Prestação (Digite 0 para sair): '))
    if valor_prestacao == 0:
        print(lista)
        print(f'\n TOTAL DE PRESTAÇÕES: {round(sum(lista),2)}')
        break
    qt_dias_atraso = float(input('\n Quantidade de dias em atraso: '))
    total = round(valor_pagamento(valor_prestacao,qt_dias_atraso),2)
    lista.append(total)