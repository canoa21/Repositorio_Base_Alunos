#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input("digite eu nome: ")
senha = int(input("digite sua senha: "))
while True:
    if nome == senha:
        print("informaçoes invalidas")
    break




