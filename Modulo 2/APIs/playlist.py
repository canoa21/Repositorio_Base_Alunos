from flask import Flask, jsonify, request
 

app = Flask(__name__)

playlist = [
     {"id": 1, "titulo": "shape of you", "artista": "ed sheeran"},
     {"id":2, "titulo": "bohemian rhapsody", "artista":"queen"}

]

@app.route('/musicas', methods = ['GET'])
def get_musicas():
    return jsonify({"playlist": playlist,"total": len(playlist)})

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica =request.json
    nova_musica["id"] = len(playlist)+1
    playlist.append(nova_musica)
    return jsonify({"mensagem": "musica adicionada!","musica": nova_musica}),201

@app.route("/musicas/<artista>", methods = ["GET"])
def get_musica_hy_id(artista):
    for musica in playlist:
        if musica["artista"] ==artista:
            return jsonify({"mensagem":"o artista foi encontrado", "musica": musica}) 

    return jsonify({"mensagem": "musica nao encontrada"})
@app.route('/musicas/<int:id>', methods=["PUT"])
def update_musica(id):
    dados = request.json 
    for musica in playlist:
        if musica["id"] == id:
            musica.update(dados)
            return jsonify({"mensagem":"musica atualizadaa" })
        return jsonify({"erro": "musica nao encontrada"}), 404
        

@app.route("/musicas/<int:id>", methods=["DELETE"])
def delete_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            playlist.remove(musica)
            return jsonify ({"mensagem":"musica deletada"})
        return jsonify ( {"mensagem": "musica nao encontrada"})

if __name__ == '__main__':
    app.run(debug=True)


