nome = input("digite o bome: ")
email = input("digite o e-mail: ")

arquivo = open("pessoa.txt","a")
arquivo.write(nome + "|" + email + "\n")
arquivo.close()
