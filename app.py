from flask import Flask,render_template, request
import mysql.connector
from dbmodules.mysql_db import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/insert', methods = ['POST', 'GET'])
def insert():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        email = request.form['email']
        address = request.form['address']
        salary = int(request.form['salary'])
        db_insert([(name, age, email, address, salary)])
        return  render_template('form.html',response="Insertion is done")

@app.route('/createtable')
def createtabel():

    result=create_table()
    return render_template('home.html',response=result)

@app.route('/getdata',methods=['GET','POST'])
def gettablesdata():
    tablename=""
    if request.method == "GET":
        if "tablename" in request.args:
            tablename = request.args['tablename']
    else:
        if "tablename" in request.form:
            tablename = request.form['tablename']
    res=""
    if tablename:
        res=select_table_data(tablename)
        
    return render_template('result.html',result=res)
if __name__ == '__main__':

    app.run(host='localhost', port=5000, debug=True)