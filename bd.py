def get_idlogin(cursor,login,senha):
    cursor.execute(f'select idlogin from login where login="{login}"and senha="{senha}"')

    idlogin = cursor.fetchone()
    cursor.close()
    return idlogin

def get_idbusca(cursor,bia):
    cursor.execute(f'select carro, cor, placa, ano, preco, marca from carro where carro = "{bia}"')
    busca = cursor.fetchone()
    cursor.close()
    return busca

def usuario_incluir(cursor,conn,login,senha):
    cursor.execute(f'INSERT INTO login (login, senha) values("{login}","{senha}")')
    conn.commit()

def anuncio_incluir(cursor, conn, carro, cor, placa, ano, preco, marca):
    cursor.execute(f'INSERT INTO carro (carro, cor, placa, ano, preco, marca) values("{carro}","{cor}","{placa}","{ano}","{preco}","{marca}")')
    conn.commit()


