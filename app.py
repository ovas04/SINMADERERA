from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime
from Service import *
app = Flask(__name__)

#Conexion a base de datos NYSQL
app.config["MYSQL_HOST"] = "208.91.198.197"
app.config["MYSQL_USER"] = "nueva_era"
app.config["MYSQL_PASSWORD"] = "NuevaEra843*"
app.config["MYSQL_DB"] = "construcciones_db"
mysql = MySQL(app)
print("Conexión establecida exitosamente!")

#Configuracion
app.secret_key = "mysecretkey"

@app.route("/")
def home():
	return render_template("login.html")

@app.route("/dashboard")
def dashboard():
	data = ("Dashboard | Nueva Era","Dashboard")
	return render_template("dashboard.html", datos = data)

@app.route("/perfil")
def perfil():
	data = ("Mi Perfil | Nueva Era","Mi Perfil")
	return render_template("perfil.html", datos = data)

@app.route("/usuarios")
def usuarios():
	data = ("Usuarios | Nueva Era","Usuarios")
	return render_template("usuarios.html", datos = data)

@app.route("/roles")
def roles():
	data = ("Roles | Nueva Era","Roles")
	return render_template("roles.html", datos = data)

@app.route("/roles/permisos")
def permisos():
	data = ("Permisos | Nueva Era","Permisos")
	return render_template("permisos.html", datos = data)

@app.route("/actualizar")
def actualizar():
	data = ("Actualizar Info | Nueva Era","Actualizar información")
	return render_template("actualizar.html", datos = data)


#Construcciones privadas
@app.route("/construcciones_privadas")
def construc_priv():
	data = ("Construcciones Privadas | Nueva Era","Construcciones Privadas","functions_constructora.js")
	return render_template("construc_priv.html", datos = data)

@app.route("/list_construc_priv")
def list_construc_priv():
	data = Service.get_usuarios()
	data = [list(i) for i in data]
	for i in range(len(data)):
		if data[i][6] != None:
			data[i][6] = datetime.strftime(data[i][6],"%d-%m-%Y")
		else:
			data[i][6] = "No existe"

		if data[i][8] == "Activa":
			data[i][8] = '<span class="badge bg-info">Activa</span>'
		elif data[i][8] == "Vencida":
			data[i][8] = '<span class="badge bg-danger">Vencida</span>'
		else:
			data[i][8] = '<span class="badge bg-secondary">Duda</span>'

		data[i].append('<div class="text-center">'+
				'<button class="btn btn-warning btn-sm btn-ver-construc" rl="'+data[i][0]+'" title="Ver"><i class="fas fa-eye"></i></button> '+
				'<button class="btn btn-primary btn-sm btn-edit-construc" rl="'+data[i][0]+'" title="Comentar"><i class="fas fa-pencil-alt"></i></button> '+
				'<button class="btn btn-danger btn-sm btn-eli-construc" rl="'+data[i][0]+'" title="Eliminar"><i class="fas fa-trash-alt"></i></button> '+
				'</div>')
	return jsonify(data)

@app.route("/regis_contruc_priv")
def regis_construc_priv():
	if request.method == "POST":
		cur = mysql.connection.cursor()
		cur.execute("select max(id_const)+1 from construccion")
		codigo = cur.fetchall()
		nombre = request.form["nom_const"]
		apellidos = request.form["ape_emple"]
		dni = request.form["dni_emple"]
		fecha = request.form["fech_emple"]
		mail = request.form["mail_emple"]
		telefono = request.form["telef_emple"]
		distrito = request.form["distr_emple"]
		estado = request.form["estado"]
		cur.execute("insert into construccion values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(codigo,nombre,apellidos,dni,fecha,'',mail,telefono,distrito,estado))
		mysql.connection.commit()
		response = {"status":"True", "msj": "Construccion registrada correctamente!"}
		return jsonify(response)

@app.route("/buscar_construc_priv/<id_construc>", methods=["GET"])
def buscar_construc_priv(id_construc):
	cur = mysql.connection.cursor()
	cur.execute("call sp_buscar_const_priv(%s)", [id_construc])
	data = cur.fetchall()
	data = [list(i) for i in data]
	if data[0][6] != None:
		data[0][6] = datetime.strftime(data[0][6],"%Y-%m-%d")
	else:
		data[0][6] = "No existe"
	return jsonify(data[0])

@app.route("/actividad_construc_priv")
def actividad_construc_priv():
	data = ("Registrar Actividad | Nueva Era","Registrar Actividad",)
	return render_template("registrar_actividad_privada.html", datos = data)

#Construcciones publicas
@app.route("/construcciones_publicas")
def construc_pub():
	data = ("Construcciones Públicas | Nueva Era","Construcciones Públicas","functions_constructora.js")
	return render_template("construc_pub.html", datos = data)

@app.route("/list_construc_pub")
def list_construc_pub():
	cur = mysql.connection.cursor()
	cur.execute("call sp_listar_const_pub")
	data = cur.fetchall()
	data = [list(i) for i in data]
	for i in range(len(data)):
		if(data[i][6] == "Activa"):
			data[i][6] = '<span class="badge bg-info">Activa</span>'
		else:
			data[i][6] = '<span class="badge bg-danger">Inactiva</span>'

		data[i].append('<div class="text-center">'+
				'<button class="btn btn-warning btn-sm btn-ver-construc" rl="'+data[i][0]+'" title="Ver"><i class="fas fa-eye"></i></button> '+
				'<button class="btn btn-primary btn-sm btn-edit-construc" rl="'+data[i][0]+'" title="Comentar"><i class="fas fa-pencil-alt"></i></button> '+
				'<button class="btn btn-danger btn-sm btn-eli-construc" rl="'+data[i][0]+'" title="Eliminar"><i class="fas fa-trash-alt"></i></button> '+
				'</div>')
	return jsonify(data)
	cur.connection.close();

@app.route("/regis_contruc_pub")
def regis_construc_pub():
	if request.method == "POST":
		cur = mysql.connection.cursor()
		cur.execute("select max(id_const)+1 from construccion")
		codigo = cur.fetchall()
		nombre = request.form["nom_const"]
		apellidos = request.form["ape_emple"]
		dni = request.form["dni_emple"]
		fecha = request.form["fech_emple"]
		mail = request.form["mail_emple"]
		telefono = request.form["telef_emple"]
		distrito = request.form["distr_emple"]
		estado = request.form["estado"]
		cur.execute("insert into construccion values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(codigo,nombre,apellidos,dni,fecha,'',mail,telefono,distrito,estado))
		mysql.connection.commit()
		response = {"status":"True", "msj": "Construccion registrada correctamente!"}
		return jsonify(response)
		cur.connection.close();

@app.route("/buscar_construc_pub/<id_construc>", methods=["GET"])
def buscar_construc_pub(id_construc):
	cur = mysql.connection.cursor()
	cur.execute("call sp_buscar_const_pub(%s)", [id_construc])
	data = cur.fetchall()
	return jsonify(data[0])
	cur.connection.close();

@app.route("/actividad_construc_pub")
def actividad_construc_pub():
	data = ("Registrar Actividad | Nueva Era","Registrar Actividad",)
	return render_template("registrar_actividad_publica.html", datos = data)

#Empleados
@app.route("/empleados")
def empleados():
	data = ("Empleados | Nueva Era","Empleados","functions_empleado.js")
	return render_template("empleados.html", datos = data)

@app.route("/list_emple")
def list_emple():
	cur = mysql.connection.cursor()
	cur.execute("call sp_listar_empleados")
	data = cur.fetchall()
	data = [list(i) for i in data]
	for i in range(len(data)):
		data[i][4] = datetime.strftime(data[i][4],"%d-%m-%Y")
		if data[i][5] == "ACTIVO":
			data[i][5] = '<span class="badge bg-info">Activo</span>'
		else:
			data[i][5] = '<span class="badge bg-danger">Culminado</span>'

		data[i].append('<div class="text-center">'+
				'<button class="btn btn-success btn-sm btn-usu-emple" rl="'+data[i][0]+'" title="Crear Usuario"><i class="fas fa-user-plus"></i></button> '+
				'<button class="btn btn-warning btn-sm btn-ver-emple" rl="'+data[i][0]+'" title="Ver"><i class="fas fa-eye"></i></button> '+
				'<button class="btn btn-primary btn-sm btn-edit-emple" rl="'+data[i][0]+'" title="Editar"><i class="fas fa-pencil-alt"></i></button> '+
				'<button class="btn btn-danger btn-sm btn-eli-emple" rl="'+data[i][0]+'" title="Eliminar"><i class="fas fa-trash-alt"></i></button> '+
				'</div>')
	return jsonify(data)
	cur.connection.close();

@app.route("/regis_emple", methods=["POST"])
def regis_emple():
	if request.method == "POST":
		cur = mysql.connection.cursor()
		id = request.form["id_emple"]
		if id != "0":
			codigo = id
		else:
			cur.execute("select max(id_usuario)+1 from usuario")
			codigo = cur.fetchall()
		nombre = request.form["nom_emple"]
		apellidos = request.form["ape_emple"]
		dni = request.form["dni_emple"]
		fecha = request.form["fech_emple"]
		mail = request.form["mail_emple"]
		telefono = request.form["telef_emple"]
		distrito = request.form["distr_emple"]
		estado = request.form["estado"]
		cur.execute("call sp_regis_empleado(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(codigo,nombre,apellidos,dni,fecha,mail,telefono,distrito,estado))
		mysql.connection.commit()
		response = {"status":True, "msj":"Empleado registrado correctamente!"}
		return jsonify(response)
		cur.connection.close();

@app.route("/buscar_emple/<id_emple>", methods=["GET"])
def buscar_emple(id_emple):
	cur = mysql.connection.cursor()
	cur.execute("select*from usuario where id_usuario=%s", (id_emple))
	data = cur.fetchall()
	data = [list(i) for i in data]
	data[0][4] = datetime.strftime(data[0][4],"%Y-%m-%d")
	return jsonify(data[0])
	cur.connection.close();

@app.route("/elim_emple/<id_emple>", methods=["POST"])
def elim_emple(id_emple):
	cur = mysql.connection.cursor()
	cur.execute("delete from usuario where id_usuario=%s", [id_emple])
	mysql.connection.commit()
	response = {"status":"True", "msj":"Registro de empleado elminado!"}
	return jsonify(response)
	cur.connection.close();

@app.route("/elim_usuario/")
def elim_usuario():
	data = ("Eliminar Usuario | Nueva Era","Eliminar Usuario")
	return render_template("usuario_delete.html", datos = data)

@app.route("/actividad/<id_emple>", methods=["GET"])
def actividad(id_emple):
	data = ("Actividad | Nueva Era","Actividad de vendedor","functions_empleado.js")
	return render_template("actividad.html", datos = data)

#Vista PB
@app.route("/vista_pbi")
def vista_pbi():
	data = ("Vista PBI | Nueva Era","Vista Power BI","function_reporte.js")
	return render_template("vista_pbi.html", datos = data)

#Reportes
@app.route("/reportes")
def reportes():
	data = ("Reportes | Nueva Era","Reportes","function_reporte.js")
	return render_template("reportes.html", datos = data)

if __name__ == "__main__":
	app.run(debug=True)