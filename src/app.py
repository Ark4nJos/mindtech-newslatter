from flask import Flask, request, render_template, redirect, url_for
import sqlite3 as sql
from pathlib import Path

# define o caminho para o banco de dados
diretorio_db = Path(__file__).parent.parent / 'database.db'

app = Flask(__name__)

# Roda principal para home
@app.route('/')
def index():
    return render_template('index.html')

# Rota que adiciona um e-mail ao banco de dados com tratamente de erros
@app.route('/add_email', methods = ['POST'])
def add_email():
    if request.method == 'POST':
        email = request.form['email']
        try:
            # define a conexão com o banco de dados
            with sql.connect(diretorio_db) as db:
                cur = db.cursor()
                cur.execute("INSERT into email(email) VALUES (?)", (email,))
                db.commit()
                msg = 'Obrigado por se inscrever na nossa newsletter!'
                return render_template('confirmacao.html', msg=msg)
            # verifica erros e/ou se o e-mail já se encontra no banco de dados
        except sql.IntegrityError:
            msg = 'E-mail já cadastrado. Tente novamente'
            return render_template('error.html', msg=msg)
        except Exception as e:
            msg = f'Erro ao adicionar o e-mail: {e}'
            return redirect('error.html', msg=msg)

@app.route('/del_html')
def del_html():
    return render_template('delete.html')

# Rota que deleta um e-mail do banco de dados com verificações de possiveis erros.
@app.route('/del_email', methods = ['POST'])
def del_email():
    email = request.form['email']
    try:
        with sql.connect(diretorio_db) as db:
            cur = db.cursor()
            cur.execute("DELETE FROM email WHERE email= ?", (email,))
            db.commit()
            #verifica se o e-mail está n banco de dados
            if cur.rowcount == 0:
                msg = f'E-mail {email} não encontrado no banco de dados.'
                return render_template('error.html', msg=msg)
            else:
                msg = f'E-mail {email} descadastrado com sucesso!'
                return render_template('confirm_del.html', msg=msg)
    except Exception as e:
        msg = f'E-mail {e} não encontrado.'
        return render_template('error.html', msg=msg)



if __name__ == '__main__':
    app.run(debug=True)