from flask import Flask, request, render_template
import sqlite3 as sql
from pathlib import Path

diretorio = Path(__file__).parent.parent / 'database.db'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email', methods = ["POST"])
def add_email():
    msg = ''
    try:
        if request.method == "POST":
            email = request.form["email"]
            with sql.connect(diretorio) as db:
                cur = db.cursor()
                cur.execute("INSERT into email(email) VALUES (?)", (email,))
                db.commit()
                msg = 'E-mail cadastrado com sucesso!!'
    except sql.IntegrityError:
        msg = 'E-mail já cadastrado.'
    except Exception as e:
        msg = f'Erro ao adicionar o e-mail: {e}'
    finally:
        return render_template('confirmacao.html', msg=msg)



if __name__ == '__main__':
    app.run(debug=True)