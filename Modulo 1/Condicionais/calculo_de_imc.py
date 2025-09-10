while True:

    try:

        nome = input("digite seu nome: ")
        peso = int(input("digite seu peso (kg): "))
        altura  = float(input("digite sua altura (m): "))
        
        imc = peso /(altura * altura)
    
        if imc <= 18.5:
            print(f"o paciente {nome} esta com IMC de {imc}: abaixo do peso")

            
        elif imc <= 24.9:
            print(f"o paciente {nome} esta com IMC de {imc}: peso normal")

        elif imc <= 29.9 :
            print(f"o paciente {nome} esta com IMC de {imc}: sobre peso")

        elif imc <= 30.0:
            print(f"o paciente {nome} esta com IMC de {imc}: obesidade grau 1")

        elif imc <= 35.0:
            print(f"o paciente {nome} esta com IMC de {imc}: obesidade grau 2")

        elif imc <= 39.9:
            print(f"o paciente {nome} esta com o IMC de {imc}: obesidade grau 3")

        else:
            print(f"o paciente {nome} esta com IMC de {imc}: obesidade grau 3 (mórbida)")
        break
    except:
        print("alguma das informações está errada, digite novamente")
    
 