from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/palindrome/<palabra>')
def palindrome(palabra):
    txt = palabra
    txt2 = txt.lower()
    if(txt2 == txt2[::-1]):
        txt_re = palabra + " es palindromo"
        return(txt_re)
    else:
        txt_re = palabra + " es no palindromo"
        return(txt_re)
@app.route('/multiplo/<numero1>/<numero2>')
def multiplo(numero1, numero2):
    n1 = int(numero1)
    n2 = int(numero2)
    if(n1 % n2 == 0):
        txt_res = str(n1) + " es múltiplo de " + str(n2)
        return txt_res
    else:
        txt_res = str(n1) + " es no múltiplo de " + str(n2)
        return txt_res

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/create_user/<nombre>/<apellido>/<contra>/<usuario>')
def create_user(nombre, apellido, contra, usuario):
    #crear un objeto (instancia de una clase)
    user = entities.User(
        name = nombre,
        fullname = apellido,
        password = contra,
        username = usuario
    )

    #Guardar el objeto en la capa decreate_user persistencia
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    return "User created!"

@app.route('/read_user')
def read_users():
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User)
    users = respuesta[:]
    i = 1
    imprime = ""
    for user in users:
        imprime += "\tN°" + str(i) + "\tNAME: " + user.name + "\tLASTNAME: " + user.fullname + "\tPASSWORD: " + user.password + "\tUSERNAME: " + user.username + "<br>" 
        print(i, "NAME: ", user.name, "\tLASTNAME: ", user.fullname, "\tPASSWORD: ", user.password, "\tUSERNAME: ", user.username)
        i+=1
    return imprime


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
