from flask import Flask, request, make_response, jsonify
import mysql.connector
from usuario import Usuario
from invernadero import Invernadero
conexion = mysql.connector.connect(user="carlos",password="12345",database="invernadero")

cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/home/")
def hello():
	respuesta=make_response("Hello World!")
	respuesta.headers.add('Access-Control-Allow-Origin','*')
	return respuesta
	
#http://127.0.0.1:5000/login/?usuario=carlos&password=12345
@app.route("/login/", methods=['GET'])
def login():
	#print(request.args)
	usuario=request.args.get('usuario')
	password=request.args.get('password')
	
	userDB = Usuario(conexion,cursor)
	respuesta=make_response(str(userDB.login(usuario,password)))
	respuesta.headers.add('Access-Control-Allow-Origin','*')
	return respuesta
	#print(userDB.login(usuario, password))
	
	#print(usuario, password)
	#return usuario + " " + password
@app.route("/invernadero/", methods=['GET'])
def invernadero():
	usuario = request.args.get('usuario')
	print(usuario)
	inv = Invernadero(conexion, cursor)
	resultado = inv.buscar(usuario)
	print(resultado)
	
	return jsonify(resultado)
app.run(debug=True)