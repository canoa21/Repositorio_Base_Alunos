def contador(num):
    qauntidade = len(str(num))
    return qauntidade

num = int(input("digite um numero inteiro: "))

digitos = contador(num)
print(f"o numero {num} possui {digitos} digito(s)")

