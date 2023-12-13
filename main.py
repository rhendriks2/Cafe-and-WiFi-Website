from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vdsevhsbeqkHHJJJ'
Bootstrap5(app)


def db_connection():
    db = sqlite3.connect("cafes.db")
    db.row_factory = sqlite3.Row
    return db


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def show_cafes():
    cafes_db = db_connection()
    cafes = cafes_db.execute('SELECT * FROM cafe').fetchall()
    cafes_db.close()
    return render_template("cafes.html", cafes=cafes)


@app.route("/explore")
def explore_cafe():
    return render_template("explore.html")


if __name__ == "__main__":
    app.run(debug=True)
