import DatabaseController

db = DatabaseController
#db.Users().insert(dict(name="Carlos", birth="10/10/2020", cpf="111.111.111-11", height=1.67))
print(db.Users().list(db.Users().get(True, {})))
#print(list(db.Users().get(False, {})))