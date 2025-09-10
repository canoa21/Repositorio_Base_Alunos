#Faça um programa que leia e valide as seguintes informações:
#nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


while True:
   
    idade = int(input("digite sua idade: "))
        if  idade >=0 or idade <=150:
            print("valido")
        break

        else: 
            print("invalido")
            
   