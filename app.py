from flask import Flask, render_template
import mariadb

app = Flask(__name__)

conn = mariadb.connect(host='172.16.3.156',
                       port= 3306,
                       user='docapostedemo',
                       password='d0cAp0st3_dem0!',
                       database='db_docaposte')
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')
