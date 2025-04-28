from flask import render_template, request
from app import App
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


@App.route('/')
def root():
    return render_template('index.html')


@App.route('/home')
def home():
    return render_template('home.html')


@App.route('/projetos')
def projetos():
    return render_template('projetos.html')


@App.route('/sobre')
def sobre():
    return render_template('sobre.html')


@App.route('/contatos')
def contatos():
    return render_template('contato.html')


@App.route('/mensagem', methods=['POST'])
def mensagem():
    email = request.form['email']
    message = request.form['texto']
    
    db_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME'),
        'port': int(os.getenv('DB_PORT'))
    }
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO contatos (email, mensagem) VALUES (%s, %s)", (email, message))
    user = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('index.html', show_alert=True)
