from model.users import Users
from repository.users_repository import UsersRepository


if __name__=='__main__':
    users = Users()
    users.id = 'bf152742-6618-42b7-9d19-06563e1e2bda'
    #users.password = users._criptografia()
    #print(users)
    repository = UsersRepository()
    #print(repository.gravar(users))
    print(repository.listar_todos())
    print(f"encontrado por id:{repository.buscar_id(users)}")
