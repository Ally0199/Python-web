from flask import Flask, jsonify, render_template, request

from dbmysql import DBMySQL

app = Flask(__name__)

@app.route('/') # cuando se accesa al inicio de la aplicacion web
def index():
    return render_template('formulario.html')

@app.route('/procesa', methods=['POST'])
def procesa():
    base = request.form['base']
    limite = request.form['limite']
    data = ""
    for i in range(0 , int(limite) + 1):
        data += base + " * " + str(i) + " = " + str(int(base) * i) + "<br />"
    return data

@app.route('/api/departments')
def departments():
    db = DBMySQL()
    resultado = db.getAllDepartments()
    db.closeConnection()
    return jsonify(resultado)

@app.route('/api/findbyname')
def findByNameDepartments():
    db = DBMySQL() 
    nombre = request.args.get('nombre')
    resultado = db.findByNameDepartment(nombre)
    db.closeConnection()
    return jsonify(resultado)
  