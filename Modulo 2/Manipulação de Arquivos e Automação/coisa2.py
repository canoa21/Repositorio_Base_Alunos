import json
livro = {"titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano": 1954
}
livro_json = json.dumps(livro)
print(livro_json)