while True:
    try:
        nome = input("digite seu nome: ")
        peso = int(input("digite seu peso: "))
        altura = float(input("digite sua altura: "))
 
        imc = peso /(altura * altura)    
        def 
        if imc >=30:
            print("cuidado")
        elif imc <=18.5:
            print("abaixo do peso")
        
        elif imc <= 24.9:
            print("peso normal")

        elif imc <= 29.9:
            print("sobre peso")

        elif imc <=34.9:
            print("obesidade grau 1")

        elif imc <= 39.9:
            print("obesidade grau 2")

        else:
            print("obesidade grau 3")
        break
    
    except ValueError:
        print("digite um peso ou uma altura valida")


with open("pessoa.txt", "a") as arquivo:
    arquivo.write(f"o paciente {nome}  esta com o imc de: {imc}")