#Utilize a função csv.DictReader para ler um arquivo alunos.csv com as colunas nome, nota1 e nota2. 
# Calcule a média de cada aluno e imprima no terminal.

import csv 


with open('alunos.csv', 'r', newline='') as arquivo:      
   arquivo = csv.DictReader(arquivo)
   for row in arquivo:
        print(f'{row["nota1"]} / {row["nota2"]} / {row["nome"]}')
        nota1 = float(row['nota1'])
        nota2 = float(row['nota2'])
        media = (nota1 + nota2)/2
        print(media)
     
    
