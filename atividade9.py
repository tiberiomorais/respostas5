# 9. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721.


lista = []
palavra = input('Palavra ou Número: ')
tamanho = len(palavra   )


def reverso(nome):
    for i in range (tamanho-1,-1,-1):
        lista.append(palavra[i])
    print('\n', lista, '\n')
    print(''.join(lista))


reverso(palavra )
