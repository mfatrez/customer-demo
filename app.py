import mariadb
import sys

from flask import Flask, render_template

app = Flask(__name__)

config = {
        'host': '10.77.4.145',
        'port': 3306,
        'user': 'docapostedemo',
        'password': 'd0cAp0st3_dem0!',
        'database': 'db_docaposte'
}

@app.route('/')
def index():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("INSERT INTO doca_test (id, data) VALUES (null, 1)")
    conn.commit()

    return render_template('index.html')

@app.route('/ping')
def monitoring():
    return "<p>OK</p>"
