import json
lista = []

nome = input("digite seu nome: ")
produto = input("digite qual seu produto: ")
quantidade = int(input("digite qual a quantidade = do seu produto: "))
status = input("qual o estado do seu produto?: ")

pedido = {
    "nome": nome,
    "produto": produto,
    "quantidade": quantidade,
    "status":"enviado"

}

lista.append (pedido)
with open("pedido.json", "w", encoding="utf-8") as arquivo:
    json.dump (lista,arquivo,indent=2, ensure_ascii=False)
print("pedido salvo com sucesso")