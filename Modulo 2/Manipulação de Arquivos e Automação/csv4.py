import csv 

produtos = [
    {'produto': ' arroz' , 'quantidade':1 , 'preço': 4.50},
    {'produto': ' arroz' , 'quantidade':2 , 'preço': 5.50},
    {'produto': ' arroz' , 'quantidade':3 , 'preço': 6.50},
    {'produto': ' arroz' , 'quantidade':4 , 'preço': 7.50}
]


with open('relatorio.csv', 'w', newline='', encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['produto',' quantidade','total'])
    for item in produtos:
        total = item['quantidade'] * item['preço']
        writer.writerow([item['produto'], item['quantidade'], f'{total:.2f}'])
        print(total)
 
   



