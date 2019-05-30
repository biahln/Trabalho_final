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
