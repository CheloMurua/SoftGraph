# services/auth_service.py
from database.database import Database

class AuthService:
    def __init__(self, db: Database):
        self.db = db

    def login(self, username, password):
        query = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
        resultado = self.db.ejecutar_query(query, (username, password))
        if resultado:
            return True, resultado[0]
        return False, None
