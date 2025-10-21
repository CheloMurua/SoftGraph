"""
SoftGraph - Selector de interfaz
Autor: Grupo 24
Descripción:
Permite elegir al inicio si se quiere usar la interfaz clásica o el dashboard moderno.
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from gui.softgraph_gui import run_app as run_classic
from gui.dashboard_gui import run_dashboard

class SelectorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SoftGraph - Selección de Interfaz")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("Bienvenido a SoftGraph")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Botón interfaz clásica
        self.btn_clasico = QPushButton("Interfaz Clásica")
        self.btn_clasico.setFixedHeight(40)
        self.btn_clasico.setStyleSheet(
            "background-color: #2196F3; color: white; border-radius: 8px; font-weight: 600;"
        )
        self.btn_clasico.clicked.connect(self.lanzar_clasico)
        layout.addWidget(self.btn_clasico)

        # Botón dashboard moderno
        self.btn_dashboard = QPushButton("Dashboard Moderno")
        self.btn_dashboard.setFixedHeight(40)
        self.btn_dashboard.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 8px; font-weight: 600;"
        )
        self.btn_dashboard.clicked.connect(self.lanzar_dashboard)
        layout.addWidget(self.btn_dashboard)

        self.setLayout(layout)

    # ---------------- MÉTODOS ----------------
    def lanzar_clasico(self):
        self.hide()
        dialog = run_classic()
        dialog.finished.connect(self.show)  # volver a mostrar selector al cerrar
        dialog.exec()

    def lanzar_dashboard(self):
        self.hide()
        dialog = run_dashboard()
        dialog.finished.connect(self.show)  # volver a mostrar selector al cerrar
        dialog.exec()

def main():
    app = QApplication(sys.argv)
    selector = SelectorGUI()
    selector.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
