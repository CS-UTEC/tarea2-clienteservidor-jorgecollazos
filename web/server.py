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
    if(txt == txt[::-1]):
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

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
