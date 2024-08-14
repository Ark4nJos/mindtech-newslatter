from flask import Flask, request, render_template, redirect, url_for
import sqlite3 as sql
from pathlib import Path

diretorio_db = Path(__file__).parent.parent / 'database.db'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email', methods = ['POST'])
def add_email():
    if request.method == 'POST':
        email = request.form['email']
        try:
            with sql.connect(diretorio_db) as db:
                cur = db.cursor()
                cur.execute("INSERT into email(email) VALUES (?)", (email,))
                db.commit()
                msg = 'Obrigado por se inscrever na nossa newsletter!'
                return render_template('confirmacao.html', msg=msg)
        except sql.IntegrityError:
            msg = 'E-mail já cadastrado. Tente novamente'
            return render_template('error.html', msg=msg)
        except Exception as e:
            msg = f'Erro ao adicionar o e-mail: {e}'
            return redirect('error.html', msg=msg)

@app.route('/del_html')
def del_html():
    return render_template('delete.html')

@app.route('/del_email', methods = ['POST'])
def del_email():
    email = request.form['email']
    try:
        with sql.connect(diretorio_db) as db:
            cur = db.cursor()
            cur.execute("DELETE FROM email WHERE email= ?", (email,))
            db.commit()
            
            if cur.rowcount == 0:
                msg = 'E-mail não foi encontrado. Tente novamente.'
                return render_template('error.html', msg=msg)
            msg = f'E-mail {email} descadastrado com sucesso!'
            return render_template('confirmacao_del.html', msg=msg)
    except Exception as e:
        db.rollback()
        msg = 'E-mail não encontrado.'
        return render_template('error.html', msg=msg)



if __name__ == '__main__':
    app.run(debug=True)