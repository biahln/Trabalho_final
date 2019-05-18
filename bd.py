def get_idlogin(cursor,login,senha):
    cursor.execute(f'select idlogin from login where login="{login}"and senha="{senha}"')

    idlogin = cursor.fetchone()
    cursor.close()
    return idlogin