from database.database import Database

db = Database(user='root', password='1234')  # Cambiar según tu configuración
db.conectar()

resultados = db.ejecutar_query("SELECT * FROM clientes")
for r in resultados:
    print(r)

db.desconectar()