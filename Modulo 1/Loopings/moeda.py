while True:
    try:

        def converterDolarRel(valor,converter):
            if converter == 1:
                convertido = valor * 5.8
            elif converter == 2:
                convertido = valor/5.8
            else:
                convertido = "nenhuma opção valida"
        
            return convertido

        converter = int(input("converter dolar para real digite 1:\n converter real para dolar digite 2:"))
        valor= float (input("digite valor a ser convertido: "))
        break   

    except:
        print:("digite um valor valido")

print (converterDolarRel(valor,converter))
