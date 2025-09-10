#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = int(input("digite uma nota: "))
    if nota >=0 and nota <=10:
        break
    print("valor invalido")

