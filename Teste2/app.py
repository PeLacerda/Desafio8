from flask import Flask, request, jsonify

app = Flask(__name__)

veiculos = [
    {"id": 1, "placa": "ABC1D23", "horas": 2},
    {"id": 2, "placa": "XYZ9K88", "horas": 5}
]


def validar_entrada(placa, horas):
    if not placa:
        return False

    if horas <= 0:
        return False

    if horas > 12:
        return False

    return True


@app.route("/veiculos", methods=["GET"])
def listar_veiculos():
    return jsonify(veiculos), 200


@app.route("/entradas", methods=["POST"])
def registrar_entrada():
    dados = request.get_json()

    placa = dados.get("placa")
    horas = dados.get("horas")

    if not validar_entrada(placa, horas):
        return jsonify({"mensagem": "Entrada não pode ser registrada"}), 400

    novo_registro = {
        "id": len(veiculos) + 1,
        "placa": placa,
        "horas": horas
    }
    veiculos.append(novo_registro)

    return jsonify({"mensagem": "Entrada registrada com sucesso"}), 201


if __name__ == "__main__":
    app.run(debug=True)
