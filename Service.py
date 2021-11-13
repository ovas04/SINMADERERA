from Dao import *

class Service:

	def get_usuarios():
		query = "call sp_listar_const_priv"
		request = Dao.select_all(query)
		return request
