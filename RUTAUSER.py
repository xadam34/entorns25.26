from flask import Flask, jsonify, request

class User:
    def __init__(self, username, nom,  password, rol,  email):
        self.username = username
        self.email = email
        self.password = password
        self.rol = rol
        self.nom = nom
    def __str__(self):
        return self.nom
#user1 = User(username="alex", nom="John Doe", password="12345", rol="admin", email="alex@gmail.com")
#print(user1)

users = [
    User(username="alex", nom="John Doe", password="12345", rol="admin", email="alex@gmail.com")
]
app = Flask(__name__)

@app.route('/user/', methods=['GET'])
def user():

    # Si els paràmetres 
    username = request.args.get('username', default="")
    #Anar al DAO Server i cercar User per Usename
    # respondre amb dades Usuari si trobat
    if username != "":
        resposta = "username: " + username
    else:
        resposta = "No username provided"
    # Si els paràmetres NO OK
    # respondre error
    return "Holaaaaa"

if __name__ == '__main__':
    app.run(debug=True)

