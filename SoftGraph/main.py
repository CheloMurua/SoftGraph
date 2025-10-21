"""
SoftGraph - Dashboard moderno
Autor: Grupo 24
Descripción:
Ejecuta directamente el Dashboard moderno con login.
"""

import sys
from PyQt6.QtWidgets import QApplication
from gui.dashboard_gui import LoginWindow  # Importar clase de login directamente

def main():
    app = QApplication(sys.argv)
    ventana = LoginWindow()  # Crear ventana de login
    print("Abriendo login...")
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
