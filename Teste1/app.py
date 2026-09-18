from flask import Flask, request, jsonify

app = Flask(__name__)

eventos = [
    {"id": 1, "nome": "Festival de Tecnologia", "local": "Centro de Eventos", "vagas": 100},
    {"id": 2, "nome": "Feira de Empregos", "local": "Ginásio Municipal", "vagas": 50}
]


def validar_inscricao(nome, idade, quantidade):
    if not nome:
        return False

    if idade < 16:
        return False

    if quantidade <= 0:
        return False

    if quantidade > 4:
        return False

    return True


@app.route("/eventos", methods=["GET"])
def listar_eventos():
    return jsonify(eventos), 200


@app.route("/inscricoes", methods=["POST"])
def criar_inscricao():
    dados = request.get_json()

    nome = dados.get("nome")
    idade = dados.get("idade")
    quantidade = dados.get("quantidade")

    if not validar_inscricao(nome, idade, quantidade):
        return jsonify({"mensagem": "Inscrição não pode ser realizada"}), 400

    return jsonify({"mensagem": "Inscrição realizada com sucesso"}), 201


if __name__ == "__main__":
    app.run(debug=True)
