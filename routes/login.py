from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.contas_db import CONTA

login_route = Blueprint('login', __name__)

@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Pega os dados do formulário
        username = request.form['username']
        password = request.form['password']

        # Verifica se existe uma conta com o login e senha fornecidos
        for conta in CONTA:
            if conta['login'] == username and conta['senha'] == password:
                # Redireciona para a página principal após login bem-sucedido
                return redirect(url_for('principal.principal'))  # Redireciona para a rota 'principal'

        # Se não encontrar a conta, exibe uma mensagem de erro
        flash('Usuário ou senha inválidos, tente novamente!', 'error')

    # Renderiza a página de login novamente caso haja falha no login
    return render_template('login.html')
