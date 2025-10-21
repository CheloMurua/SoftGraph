"""
SoftGraph - Aplicación Principal
Ejecuta la interfaz de login y dashboard conectada a la base de datos.
"""

import sys
import os
from dotenv import load_dotenv
from PyQt6.QtWidgets import QApplication
from database.database import Database
from services.auth_service import AuthService
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from gui.dashboard_gui import LoginWindow

def main():
    # Cargar variables de entorno
    load_dotenv()

    # Conectar base de datos
    db = Database(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    db.conectar()

    # Inicializar servicios
    auth_service = AuthService(db)
    cliente_service = ClienteService(db)
    pedido_service = PedidoService(db)

    # Lanzar interfaz gráfica
    app = QApplication(sys.argv)
    ventana = LoginWindow(auth_service, cliente_service, pedido_service)
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
