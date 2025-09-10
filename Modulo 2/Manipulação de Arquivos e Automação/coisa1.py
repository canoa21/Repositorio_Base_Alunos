import json

json_string = '{"nome": "Alice", "idade": 25, "cidade": "São Paulo"}'
python_string = json.loads(json_string)
print(python_string)
