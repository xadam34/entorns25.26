from flask import Flask, jsonify, request

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
    return "getUserName"

if __name__ == '__main__':
    app.run(debug=True)