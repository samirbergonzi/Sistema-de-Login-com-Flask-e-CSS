from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário fictício para fins de demonstração
usuario_ficticio = {'username': 'admin', 'password': 'senha123'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == usuario_ficticio['username'] and password == usuario_ficticio['password']:
        return f'Bem-vindo, {username}!'
    else:
        return 'Credenciais inválidas. Tente novamente.'

if __name__ == '__main__':
    app.run(debug=True)
