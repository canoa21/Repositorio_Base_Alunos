import json
json_string = '[{"produto": "Caneta", "preco": 2.5}, {"produto": "Lápis", "preco": 1.2}]'
python_string = json.loads(json_string)
print(f"{python_string[0]["produto"]} {python_string[0]["preco"]}")
print(f"{python_string[1]["produto"]} {python_string[1]["preco"]} ")
