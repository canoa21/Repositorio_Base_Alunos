nome = input("digite seu nome: ")
email = int(input("digite deu email: "))
telefone = int(input("digite seu numero de telefone "))

with open('clientes.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    with open('clientes.csv', 'a', newline='', encoding='utf-8') as arquivo:
    
    escritor = csv.writer(arquivo)