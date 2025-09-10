#Crie um programa que leia um arquivo chamado produtos.csv contendo duas colunas: 
# nome e preço. Imprima no terminal o nome e o preço de cada produto
import csv
with open('pedidos.csv', 'r', newline='') as arquivo:      
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)


    

       