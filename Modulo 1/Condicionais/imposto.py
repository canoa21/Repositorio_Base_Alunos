#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
#expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaimposto(taxaimposto,altera):

    custo_imposto = custo + ( custo * taxaimposto / 100)
    return custo_imposto

taxa = float(input ("digite a taxa de imposto cobrada: "))
custo = int(input("digite o custo do produto: "))

resultado = somaimposto(taxa, custo)
print(f"o valor real d produto é: {resultado}")