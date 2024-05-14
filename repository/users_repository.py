import pymysql
from pymysql.cursors import DictCursor
from model.users import Users

# variavel global
conexao = pymysql.connect(host='localhost',user='root',password='root1', database='bancodata')

class UsersRepository:
    def __init__(self):
        pass
    
    def gravar(self,user):
        try:
            with conexao.cursor() as cursor:
                cursor.execute("Insert into users (id,name,email,password,status) values (%s,%s,%s,%s,%s)", (user.id,user.name,user.email,user.password,user.status))
            conexao.commit()
            print("dados gravados")
            return 1
        except Exception as error:
            print(f"error:{str(error)}")
            return 0

    def listar_todos(self):
        try:
            with conexao.cursor(DictCursor) as cursor:
                cursor.execute("select id,name,email,password,status from Users")
                results = cursor.fetchall()
                usuarios=[]
                if results:
                    for result in results:
                        user = Users(result['id'],result['name'],result['email'],result['password'],result['status'])
                        usuarios.append(user.to_json())
                return usuarios
        except Exception as error:
            return f"error:{str(error)}"
    
    def buscar_id(self,user):
        try:
            with conexao.cursor(DictCursor) as cursor:
                cursor.execute("select id,name,email,password,status from Users where id=%s",(user.id))
                results = cursor.fetchall()
                if results:
                    for result in results:
                        user_resp = Users(result['id'],result['name'],result['email'],result['password'],result['status'])
                    return user_resp.to_json()
                else:
                    return {'mensagem':'nao encontrado'}
        except Exception as error:
            return f"error:{str(error)}"

