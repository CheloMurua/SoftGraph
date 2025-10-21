# main.py
import sys
from dotenv import load_dotenv
import os
from PyQt6.QtWidgets import QApplication

from database.database import Database
from services.auth_service import AuthService
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from gui.dashboard_gui import LoginWindow  # <- Importar clase LoginWindow

# Cargar variables de entorno
load_dotenv()

def main():
    # Conexión DB
    db = Database(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    db.conectar()

    # Servicios
    auth_service = AuthService(db)
    cliente_service = ClienteService(db)
    pedido_service = PedidoService(db)

    # Crear app Qt
    app = QApplication(sys.argv)

    # Instanciar login pasando servicios
    ventana = LoginWindow(auth_service, cliente_service, pedido_service)
    ventana.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
