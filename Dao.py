from Conexion import *

class Dao:
	global cn
	cn = Conexion.obtener_conexion()

	def select_all(query):
		try:
			with cn.cursor() as cursor:
				cursor.execute(query)
				request = cursor.fetchall()
			return request
			cn.close()
		except Exception as e:
			raise