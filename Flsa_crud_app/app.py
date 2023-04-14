import phone as phone
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import email

app = Flask(__name__)
app.secret_key = 'flash message'

## Mysql connection ##

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sretest'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Completed Successfully Insert  Data")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(debug=True)