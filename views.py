from flask import render_template, request, redirect, url_for, jsonify

from models.encriptador import Encriptador
from models.opcoes import Opcoes
from app import app

@app.route('/')
def index():
    return render_template('index.html', titulo='Purple choc')

@app.route('/processa', methods=['POST',])
def processa(opcoes: dict=None):
    site = request.form['site']
    senha_original = request.form['senha']
    salt = request.form['salt']
    tamanho = int(request.form['tamanho'])
    maiusculas = "maiusculas" in request.form
    minusculas = "minusculas" in request.form
    numeros = "numeros" in request.form
    simbolos = "simbolos" in request.form

    opcoes = Opcoes(tamanho, maiusculas, minusculas, numeros, simbolos).get_opcoes()

    senha_crypt = Encriptador.gera_senha_criptografada(site, senha_original, salt, opcoes)
    senha_crypt = Encriptador.vigenere(senha_crypt, salt, opcoes)

    return jsonify({'resultado': senha_crypt})