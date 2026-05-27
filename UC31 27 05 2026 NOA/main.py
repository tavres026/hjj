from flask import flask, render_template, request

app = Flask(__name__)

@app.route('/login')

def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['Nome']
    email = request.form['Email']

    return "{} - {}".format(nome, email)

if __name__ = '__main__':
    app.run(debug=True)