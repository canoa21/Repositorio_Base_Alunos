import json
dados = {"nome": "Carlos", "idade": 30, "email": "carlos@email.com"}
json_string = json.dumps(dados,indent =4)
print(json_string)