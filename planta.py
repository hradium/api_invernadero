class Planta:
	def __init__(self, conexion, cursor):
		self.conexion = conexion
		self.cursor = cursor
		
	def agregar(self, cultivo, fecha, id_clasi, id_inv):
		insertar=("INSERT INTO planta(cultivo, fecha, id_clasi, id_inv) VALUES(%s, %s, %s, %s)")
		
		self.cursor.execute(insertar, (cultivo, fecha, id_clasi, id_inv))
		
		self.conexion.commit()
		
	def buscar(self, id_inv):
		plantas = []
		select = ("SELECT * FROM planta WHERE id_inv = %s")
		self.cursor.execute(select, (id_inv,))
		for p in self.cursor.fetchall():
			planta = {
				'id': p[0],
				'cultivo': p[1],
				'fecha': p[2],
				'id_clasi': p[3],
				'id_inv': p[4]
			}
			plantas.append(planta)
			
		return plantas