from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
# Importar configuraciones y variables de entorno
from settings import *

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_HOST'] = DB_HOST
app.config['MYSQL_USER'] = DB_USER
app.config['MYSQL_PASSWORD'] = DB_PASSWORD
app.config['MYSQL_DB'] = DB_NAME

@app.route('/')
def Index():
    return 'Hello, World!'

@app.route('/add_contact')
def add_contact():
    return 'Añadir contacto'

@app.route('/edit')
def edit_contact():
    return 'Editar contacto'

@app.route('/delete')
def delete_contact():
    return 'Eliminar contacto'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
