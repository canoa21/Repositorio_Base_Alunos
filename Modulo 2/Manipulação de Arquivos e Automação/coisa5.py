import json
json_string = '{"nome": "Fernanda", "idade": 28, "email":"fernanda@email.com" }'
python_string = json.loads(json_string)

print(python_string)