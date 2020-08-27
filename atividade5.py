# 5. Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o
# imposto sobre vendas.
print('\n CALCULA IMPOSTO')
def soma_imposto(taxa_imposto, custo):
    custo_total = custo + calcula_imposto(taxa_imposto,custo)
    return custo_total

def calcula_imposto(taxa_imposto,custo):
    valor_imposto = taxa_imposto * custo
    return valor_imposto



taxa_imposto = float(input('Informe a taxa: '))
custo = float(input('Informe o custo do produto: '))


print(f'\n CUSTO TOTAL: R$ {soma_imposto(taxa_imposto,custo)}')
print(f'\n '
      f'Você pagou R$ {calcula_imposto(taxa_imposto,custo)} de imposto.')