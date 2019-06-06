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

@app.route('/busca', methods=['GET','POST'])5
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

@app.route('/ver_carros',methods=['GET','POST'])
def ver_carros():
    return render_template('ver_carros.html')

@app.route('/reservar_carros',methods=['GET','POST'])
def reservar_carros():
    return render_template("usuario_incluir.html")

@app.route('/incluido' ,methods=['GET','POST'])
def usuario_incluido():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        conn = mysql.connect()
        cursor = conn.cursor()


        usuario_incluir(cursor,conn,login,senha)

        cursor.close()
        conn.close()
        return render_template('usuario_incluir.html', foi="Cadastro efetuado com sucesso!")

    else:
        return render_template('adm.html')


@app.route('/usuario_excluir',methods=['GET','POST'])
def usuario_excluir():
    return render_template('usuario_excluir.html')

@app.route('/anuncio_incluir', methods=['GET','POST'])
def anuncio_incluir_leo():
    return render_template('anuncio_incluir.html')

@app.route('/anuncio_incluirr', methods=['GET','POST'])
def anuncio_incluir_bia():
    if request.method == 'POST':
        carro = request.form.get('carro')
        cor = request.form.get('cor')
        placa = request.form.get('placa')
        ano = request.form.get('ano')
        preco = request.form.get('preco')
        marca = request.form.get('marca')

        conn = mysql.connect()
        cursor = conn.cursor()

        anuncio_incluir(cursor, conn, carro, cor, placa, ano, preco, marca)

        cursor.close()
        conn.close()
        return render_template('anuncio_incluir.html', foi="Anúncio adicionado com sucesso")

    else:
        return render_template('adm.html')

@app.route('/anuncio_excluir',methods=['GET','POST'])
def anuncio_excluir():
    return render_template('anuncio_excluir.html')

@app.route('/editar_top10',methods=['GET','POST'])
def editar_top10():
    return render_template('editar_top10.html')


if __name__ == '__main__':
    app.run(debug=True)
