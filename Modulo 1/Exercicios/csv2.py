#Crie um programa que receba do usuário três nomes e idades, e salve esses 
# dados no arquivo pessoas.csv, com as colunas nome e idade.
import csv
lista=[]

repetidor = 0
while repetidor < 3:
    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")
    lista.append({"nome": nome, "idade": idade})
    repetidor += 1

print(lista)
with open('pessoas.csv', 'w', newline='') as arquivo:      
    colunas = ['nome','idade']
    leitor = csv.DictWriter(arquivo, fieldnames= colunas, delimiter= ' ')

    leitor.writeheader()
    leitor.writerows(lista)

     
          
