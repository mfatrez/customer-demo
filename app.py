import mariadb
import sys

from flask import Flask, render_template

app = Flask(__name__)

try:
    conn = mariadb.connect(
        user="docapostedemo",
        password="d0cAp0st3_dem0!",
        host="10.77.4.145",
        port=3306,
        database="db_docaposte"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')
