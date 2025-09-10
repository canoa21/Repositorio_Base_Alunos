numero = int(input("digite um numero: "))
numero2 = int(input("digite o segundo numero:"))

with open("pessoa.txt", "a") as arquivo:
    arquivo.write(f"{numero} \n  {numero2}")

if numero > numero2:
    print(f"maior numero é o numero:{numero}")

else:
    print(f"menor numero é o numero:{numero2}")