"""
SoftGraph - Interfaz Clásica
Autor: Grupo 24
"""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class SoftGraphClassic(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SoftGraph - Interfaz Clásica")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Interfaz Clásica de SoftGraph")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        info = QLabel("Aquí se implementaría la GUI clásica con todas sus funcionalidades.")
        info.setFont(QFont("Segoe UI", 12))
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info)

        close_btn = QPushButton("Cerrar")
        close_btn.setFixedHeight(36)
        close_btn.setStyleSheet(
            "background-color: #2196F3; color: white; border-radius: 8px; font-weight: 600;"
        )
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

def run_app():
    dialog = SoftGraphClassic()
    return dialog
