from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:henrique123@localhost/agenda'
db = SQLAlchemy(app)

class agenda(db.Model):
    __tablename__ = 'contato'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

db.create_all()

@app.route("/teste")
def teste():
    return 'Olá Mundo'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        telefone = (request.form.get("telefone"))
        if nome:
            f = agenda(nome,telefone)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/listar")
def listar():
    agendas = agenda.query.all()
    return render_template("listar.html", agenda=agendas)


if __name__ == "__main__":
    app.run(debug=True)
