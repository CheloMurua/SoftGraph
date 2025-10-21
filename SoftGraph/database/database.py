"""
Clase Database: maneja la conexión a MySQL y ejecución de queries.
Aplica estructuras de datos y lógica centralizando acceso a la información.
"""

import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host='localhost', user='root', password='', database='softgraph'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """Abre la conexión a la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a MySQL")
        except Error as e:
            print(f"Error al conectar: {e}")

    def desconectar(self):
        """Cierra la conexión"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def ejecutar_query(self, query, params=None):
        """Ejecuta una consulta SELECT o modifica datos"""
        if not self.connection or not self.connection.is_connected():
            print("No hay conexión activa")
            return None
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error en la consulta: {e}")
            return None
        finally:
            cursor.close()
