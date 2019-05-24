from flask import Flask, render_template,request
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql =MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='trabalho'

@app.route('/')
def inicio():
    return render_template ('first.html')

@app.route('/adm', methods=['GET','POST'])
def adm():
    if request.method == 'POST':
        login=request.form.get('login')
        senha=request.form.get('senha')

        cursor = mysql.get_db().cursor()
        idlogin = get_idlogin(cursor, login, senha)
        if idlogin is None:
            return render_template('first.html', erro='Usuário não cadastrado')
        else:
            return render_template('adm.html')
    else:
        return render_template('first.html')

@app.route('/ver_carros')
def ver_carros():
    return render_template('ver_carros.html')

@app.route('/usuario_incluir')
def usuario_incluir():
    return render_template('usuario_incluir.html')

@app.route('/usuario_excluir')
def usuario_excluir():
    return render_template('usuario_excluir.html')

@app.route('/anuncio_incluir')
def anuncio_incluir():
    return render_template('anuncio_incluir.html')

@app.route('/anuncio_excluir')
def anuncio_excluir():
    return render_template('anuncio_excluir.html')

@app.route('/editar_top10')
def editar_top10():
    return render_template('editar_top10.html')

@app.route('/busca', methods=['GET','POST'])
def busca ():
    if request.method == 'POST':
        bia = request.form.get('bia')
        cursor = mysql.get_db().cursor()
        teste = get_idbusca(cursor, bia)

        if teste is None:
            return render_template('first.html', erro='Nenhum carro encontrado')
        else:
            cursor = mysql.get_db().cursor()
            return render_template('busca.html', busca=get_idbusca(cursor, bia))
    else:
        return render_template('first.html')


if __name__ == '__main__':
    app.run(debug=True)
