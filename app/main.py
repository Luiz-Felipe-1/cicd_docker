from flask import Flask, jsonify

app = Flask(__name__)


def calcular_total(valor, desconto):
    """Aplica desconto percentual (0 a 100) sobre o valor."""
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto deve estar entre 0 e 100")
    return round(valor * (1 - desconto / 100), 2)


@app.route("/")
def home():
    return jsonify(mensagem="Ola, CI/CD com Docker Hub!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/total/<float:valor>/<float:desconto>")
def total(valor, desconto):
    return jsonify(total=calcular_total(valor, desconto))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
