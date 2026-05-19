from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/lanche/<nome>")
def lanche(nome):

    nome = nome.lower()

    if nome == "pizza":
        mensagem = "Pizza quentinha saindo do forno!"

    elif nome == "hamburguer":
        mensagem = "Hambúrguer artesanal especial!"

    elif nome == "batata":
        mensagem = "Batata frita crocante!"

    elif nome == "milkshake":
        mensagem = "Milkshake delicioso!"

    else:
        mensagem = "Lanche não encontrado."

    return render_template(
        "lanche.html",
        nome=nome,
        mensagem=mensagem
    )

@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html")

@app.route("/cliente/<nome>/<cidade>")
def cliente(nome,cidade):

    if cidade.lower() == "natal":
        entrega = "Entrega disponível!"
    else:
        entrega = "Entrega indisponível."

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        entrega=entrega
    )

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)