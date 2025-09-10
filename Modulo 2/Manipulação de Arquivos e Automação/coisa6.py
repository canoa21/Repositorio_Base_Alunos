import json
json_string = '''
[
{"nome": "Lucas", "nota": 8.5},
{"nome": "Marina", "nota": 5.0},
{"nome": "Pedro", "nota": 9.0}
]
'''
lista = json.loads(json_string)
print()

for pessoa in lista:
    if pessoa["nota"] > 7:
        print(f'{pessoa["nome"]} passou de ano com nota :{pessoa["nota"]}')

