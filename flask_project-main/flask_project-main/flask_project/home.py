from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
def sample():
    return "welcome"

@app.route('/index', methods=['GET','POST'])
def index():
    con=sqlite3.connect("details.db")
    try:
        con.execute("create table user(name text, age int)")
    except:
        pass
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        # print(name,age)
        con.execute("insert into user(name,age) values(?,?)",(name,age))
        con.commit()
        return redirect('index')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
app.run()
