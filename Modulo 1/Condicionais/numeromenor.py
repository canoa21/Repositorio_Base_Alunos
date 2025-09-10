n1 = int(input("digite um numero"))
n2 = int(input("digite outro numero"))
n3 = int(input("digite o ultimo numero"))

#maior
if n1 > n2 and n2 < n1:
    print(f"o mior numero:{n1}")
    

elif n2 > n3 and n3 < n2:
    print(f"o maior numero:{n2}")
    

else:
    print(f"maior numero:{n3}")




#menor
if n1 < n2 and n2 > n1:
    print(f"o menor numero é:{n1}")

elif n2 < n3 and n3 > n2:
    print(f"o menor numero é: {n2}")

else:
    print(f"o menor numero é:{n3}")