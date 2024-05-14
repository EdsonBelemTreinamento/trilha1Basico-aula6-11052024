import hashlib
import uuid

class Users:
    def __init__(self,id=None, name=None,email=None,password=None, status=None):
        self.id=id 
        self.name = name
        self.email= email
        self.password= password
        self.status = status

    def __str__(self):
        return f"{self.id},{self.name},{self.email},{self.password},{self.status}"
    
    def to_json(self):
        return {
                'id':self.id,
                'name':self.name,
                'email':self.email,
                'password':self.password,
                'status':self.status
        }
    
    def _criptografia(self):
        md51 = hashlib.md5()
        md51.update(self.password.encode())
        hash1= md51.hexdigest()

        md52 = hashlib.md5()
        md52.update('minha palavra secreta ...;profoedsob@gmail.com;www.com.br;1+1=1'.encode())
        hash2= md52.hexdigest()
        return "".join([hash1, hash2])
    
    def _gerar_uuid(self):
        self.id = str(uuid.uuid4())
        return self.id
        


##users = Users(name="luis",password='123456',status='created')
#users.password = users._criptografia()
#users.id = users._gerar_uuid()
#print(f"Quantidade : {len(users.password)}")
#print(users.to_json())