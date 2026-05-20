from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route('/')
def formulario():
    return render_template('index.html')

# Rota de resultado
@app.route('/resultado')
def resultado():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    idade = request.args.get('idade')

    return render_template(
        'resultado.html',
        nome=nome,
        curso=curso,
        cidade=cidade,
        idade=idade
    )

if __name__ == '__main__':
    app.run(debug=True)