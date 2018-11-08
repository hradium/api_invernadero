class Invernadero:
	def __init__(self,conexion,cursor):
		self.conexion=conexion
		self.cursor=cursor
		
	def crear(self, nombre, ubicacion, id_dueno):
		try:
			insertar=("INSERT INTO invernadero(nombre,ubicacion,id_dueno) VALUES(%s,%s,%s)")
			self.cursor.execute(insertar,(nombre, ubicacion, id_dueno))
			self.conexion.commit()
		except:
			print("Ocurrio algo al insertar")
			
	def recuperar(self):
		select = ("SELECT *FROM invernadero")
		self.cursor.execute(select)
		return self.cursor.fetchall()
		
	def buscar(self, usuario):
		invernaderos = []
		self.cursor.execute("SELECT id FROM usuario WHERE correo = %s", (usuario,))
		id = self.cursor.fetchall()
		
		if id:
			select = ("SELECT id_inv FROM usuarioinvernadero WHERE id_usuario = %s")
			self.cursor.execute(select,(id[0][0],))
			for i in self.cursor.fetchall():
				self.cursor.execute("SELECT *FROM invernadero WHERE id=%s", (i[0],))
				inv_object = self.cursor.fetchone()
				inv = {
					'id': inv_object[0],
					'nombre': inv_object[1],
					'ubicacion': inv_object[2],
					'id_dueno': inv_object[3]
				}
				invernaderos.append(inv)
				
		return invernaderos