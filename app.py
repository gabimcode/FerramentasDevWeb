#importando as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

#criando o método de envio de emails
app = Flask(__name__)
app.secret_key = 'gabimc'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA")
    #o email e a senha estarão em um outro arquivo, de onde o importamos para que não fique aparecendo no código
}

app.config.update(mail_settings)

mail = Mail(app)
#criação da class contato
class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
#rota do app
@app.route('/')
def index():
    return render_template('index.html')

#captura os dados que a pessoa inseriu no portfolio e reproduz uma mensagem nos emails cadastrados abaixo
@app.route('/send', methods=('GET', 'POST'))
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender = app.config.get("MAIL_USERNAME"),
            recipients= ['gabriellembarros1@gmail.com', app.config.get("MAIL_USERNAME")],
            body= f'''

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:
            
            {formContato.mensagem}   



            '''
        )
#quando o email for enviado com sucesso, colocar essa mensagem na tela
        mail.send(msg)
        flash('Mensagem enviada!')
    return redirect('/')

#usando para conseguir acessar o host local sem precisar voltar ao vscode toda hora para executar o arquivo
if __name__ == '__main__':
    app.run(debug=True)