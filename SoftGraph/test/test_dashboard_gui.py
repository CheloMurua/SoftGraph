# dashboard_gui.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# --- Estilos ---
APP_STYLE = """
QWidget {
    background-color: #0f1724;
    color: #e6eef8;
    font-family: "Segoe UI", Arial;
    font-size: 13px;
}

#sidebar {
    background-color: #0b1b2a;
    border-right: 1px solid rgba(255,255,255,0.04);
}

QPushButton#sideBtn {
    background: transparent;
    color: #cfe7ff;
    border: none;
    padding: 10px 14px;
    text-align: left;
}
QPushButton#sideBtn:hover {
    background: rgba(255,255,255,0.03);
    color: #ffffff;
}
QPushButton#sideBtn:checked {
    background: #2b6baf;
    color: #041429;
    font-weight: bold;
}

QFrame#card {
    background-color: rgba(255,255,255,0.03);
    border-radius: 10px;
    padding: 12px;
}
"""

# --- Ventana principal ---
class SoftGraphDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SoftGraph — Dashboard")
        self.resize(900, 600)
        self.setStyleSheet(APP_STYLE)
        self._build_ui()

    def _build_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Sidebar
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        logo = QLabel("SoftGraph")
        logo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        logo.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(logo)
        sidebar_layout.addSpacing(20)

        # Botones sidebar
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setObjectName("sideBtn")
        self.btn_dashboard.setChecked(True)

        self.btn_clients = QPushButton("Clientes")
        self.btn_clients.setCheckable(True)
        self.btn_clients.setObjectName("sideBtn")

        sidebar_layout.addWidget(self.btn_dashboard)
        sidebar_layout.addWidget(self.btn_clients)
        sidebar_layout.addStretch()

        # Área principal
        self.main_area = QFrame()
        self.main_layout = QVBoxLayout()
        self.main_area.setLayout(self.main_layout)

        # Tarjeta de ejemplo
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout()
        card.setLayout(v)
        title = QLabel("Resumen de clientes")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        v.addWidget(title)
        v.addWidget(QLabel("Total: 0"))
        self.main_layout.addWidget(card)

        layout.addWidget(sidebar)
        layout.addWidget(self.main_area)

# --- Ejecutar ---
if __name__ == "__main__":
    print(">>> Dashboard GUI iniciado correctamente")
    app = QApplication(sys.argv)
    window = SoftGraphDashboard()
    window.show()
    sys.exit(app.exec_())
