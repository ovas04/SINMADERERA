import pymysql

class Conexion:
	def obtener_conexion():
		try:
			cn = pymysql.connect(
				host = "208.91.198.197",
				user = "nueva_era",
				password = "NuevaEra843*",
				db = "construcciones_db"
			)
			print("Conexion establecida exitosamente!")
			return cn
		except(pymysql.err.OperationalError, pymysql.InternalError) as e:
			print("Error en la conexion: ", e)


