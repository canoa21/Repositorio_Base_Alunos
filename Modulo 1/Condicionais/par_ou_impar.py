#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. 
#Imprima os três vetores.

lista = []
par = []
impar = []

for i in range (20):
    numero = int(input(f"digite o {i+1}° numero: "))
    lista.append(numero)
    
    if numero %2 == 0:
        par.append(numero)
    
    else:
        impar.append(numero)

print(f"numero impar: {impar}")
print(f"numero par: {par}")




