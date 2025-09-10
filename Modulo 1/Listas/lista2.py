cadastro = []


while True:
    escolha = int(input(" [1] cadastrar pessoa \n [2] listar pessoa \n [3] excluir pessoa \n [0] sair \n opções:"))
 
    if escolha == 1:
        nome = input("digite seu nome: ")
        cadastro.append(nome)
    
    elif escolha == 2:
        print(cadastro)
    
    elif escolha == 3:
        remover = input("digite um nome para ser excluido: ")
        cadastro.remove(remover)
    
    elif escolha == 0:
       print("muito obrigado por se cadastrar")
        
    break

