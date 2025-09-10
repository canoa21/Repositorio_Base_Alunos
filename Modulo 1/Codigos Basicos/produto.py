# receber o nome do pruduto/valor/desconto/caucular o valor do desconto/valor final e nome 

nome = input("digite o nome do produto: ")
valor_produto = float(input("digite o valor do produto: "))
desconto = int(input("digite o desconto: "))

valor_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_desconto

print(f"o {nome} ficara no valor R${valor_final}")

