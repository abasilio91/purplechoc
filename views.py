from flask import render_template, request, jsonify

from models.encriptador import Encriptador
from models.opcoes import Opcoes
from app import app

@app.route('/')
def index():
    return render_template('index.html', titulo='Purple choc')

@app.route('/processa', methods=['POST',])
def processa(opcoes: dict=None):
    site = request.form['site']
    senha = request.form['senha']
    salt = request.form['salt']
    tamanho = int(request.form['tamanho'])
    maiusculas = "maiusculas" in request.form
    minusculas = "minusculas" in request.form
    numeros = "numeros" in request.form
    simbolos = "simbolos" in request.form

    opcoes = Opcoes(tamanho, maiusculas, minusculas, numeros, simbolos).get_opcoes()
    
    senha = Encriptador.gera_senha_criptografada(site, senha, salt, opcoes)
    senha = Encriptador.vigenere(senha, salt, opcoes)

    return jsonify({'resultado': senha})