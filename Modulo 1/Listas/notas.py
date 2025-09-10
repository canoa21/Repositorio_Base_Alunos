#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
nome = input("digite seu nome: ")

for i in range(4):
    nota = float(input(f"digite a {i+1}° nota: "))
    notas.append(nota)

media = (sum(notas))/4

with open("pessoa.txt", "a") as arquivo:
   arquivo.write (f"nome do aluno: {nome} \n a mdeia de nota : {media}")