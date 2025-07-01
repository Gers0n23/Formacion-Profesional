class Usario:
    def __init__(self, ):
        self.__username: str
        self.__profile: int
        self.__firstname: str
        self.__lastname: str
        
    def get_username(self):
        return self.__username
    def get_profile(self):
        return self.__profile
    def setUsername(self, username: str):
        self.__username = username
    def setProfile(self, profile: int):
        self.__profile = profile
    def getUsuario(self,email):
        sql=f'SELECT * FROM usuario WHERE email = "{email}"'
        
        os.environ["TNS_ADMIN"] = "C:/WALLET/Wallet_POODATABASE"
        conn=cx_Oracle.connect('TESTPOS','.Inacap.2023.','poodatabase_high')
        c=conn.cursor()
        c.execute(sql)
        
        pass
    def getUsuario(self,usuarios):
        sql='SELECT * FROM usuario'
        pass
    def addUsuario(self,usuario):
        sql=f'INSERT INTO usuario (username,profile,firstname,lastname) VALUES ("{usuario.get_username()}",{usuario.get_profile()},"{usuario.get_firstname()}","{usuario.get_lastname()}")'
        pass
    def delUsuario(self,usuario):
        sql=f'DELETE FROM usuario WHERE username = "{usuario.get_username()}"'
        pass
    def updUsuario(self,usuario):
        sql=f'UPDATE usuario SET username = "{usuario.get_username()}", profile = {usuario.get_profile()}, firstname = "{usuario.get_firstname()}", lastname = "{usuario.get_lastname()}" WHERE username = "{usuario.get_username()}"'
        pass
    def validaUsernamePassword(self,username,password):
        sql=f'SELECT * FROM usuario WHERE username = "{username}" AND password = "{password}"'
        pass
    

import cx_Oracle
import os

os.environ["TNS_ADMIN"] = "C:/WALLET/Wallet_POODATABASE"
conn=cx_Oracle.connect('TESTPOS','.Inacap.2023.','poodatabase_high')
c=conn.cursor()
c.execute('SELECT * FROM usuarios')
for row in c:
    print(row)
    