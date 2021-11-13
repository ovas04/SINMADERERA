import pymysql
from config import obtener_nombre_base_datos
def obtener_conexion():
	return pymysql.connect(host="localhost",user="root",password="root",db=obtener_nombre_base_datos())

'''class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host = "localhost",
			user = "root",
			password = "root",
			db = "nuevaeraprueba"
		)

		self.cursor = self.connection.cursor()
		print("Conexion establecida exitosamente!")

	def select_users(self):
		sql = "select*from usuario"
		try:
			self.cursor.execute(sql)
			users = self.cursor.fetchall()
			for user in users:
				print("id_usuario: ", user[0])
				print("id_persona: ", user[1])
				print("id_rol: ", user[3])
				print("estado: ", user[5])
				print("\n")
		except Exception as e:
			raise
	

database = DataBase()
database.select_users()'''