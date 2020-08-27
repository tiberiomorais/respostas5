# #6. Faça um programa que converta da notação de 24 horas para a notação
# de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação
# A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal para registrar se é A.M.
# ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para
# novos valores de entrada todas as vezes que desejar.


print('\n CONVERTENDO FORMATO DE HORA 24 PARA 12')
chave = True

def converter_hora(hora):
    if hora >= 1 and hora <=12:
        return str(hora)
    elif hora >=13 and hora <=23:
        return str(hora - 12)

def seguir(continuar):
    if continuar == 1:
        chave = True
    else:
        chave = False


while chave is True:
    hora = int(input('\n Informe a hora: '))
    minuto = int(input('\n Informe os minutos: '))

    def imprimir(hora, minuto):
        if hora >= 1 and hora <=12:
            hora_convertida = converter_hora(hora) + ':' + str(minuto) +  ' A.M.'
            return hora_convertida
        elif hora >= 13 and hora <= 23:
            hora_convertida = converter_hora(hora) + ':' + str(minuto) +  ' P.M.'
            return hora_convertida


    print(f'\n A hora convertida é: {imprimir(hora,minuto)}')

    continuar = int(input('\n Digite 1 para continuar e 0 para sair: '))
    seguir(continuar)
