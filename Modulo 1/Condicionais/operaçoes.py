#fazer um program capz de realizar 4 operaçoes atemticas utilizando uma funçao

def calculadora(escolha,n1,n2):

    if escolha == 1:
        resultado = n1+n2
    elif escolha == 2:
        resultado =n1 - n2
    elif escolha == 3:
        resultado = n1 * n2
    elif escolha == 4:
        resulatdo = n1/n2

    return resultado 

escolha = int(input("escolha uma das operaçoes: \n soma: \n subtração: \n multiplicação: \n divisão: "))
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
 
print(calculadora(escolha,n1,n2))

