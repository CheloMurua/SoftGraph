"""
SoftGraph - Interfaz gráfica moderna con PyQt6
Incluye login y dashboard conectado a la base de datos.
"""

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


# ==============================
# Ventana de Login
# ==============================
class LoginWindow(QWidget):
    def __init__(self, auth_service, cliente_service, pedido_service):
        super().__init__()
        self.auth_service = auth_service
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SoftGraph - Login")
        self.setGeometry(500, 300, 350, 250)

        titulo = QLabel("Iniciar sesión")
        titulo.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Ingresar")
        btn_login.clicked.connect(self.verificar_login)

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(btn_login)
        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.username_input.text()
        contrasena = self.password_input.text()
        exito, datos = self.auth_service.login(usuario, contrasena)
        if exito:
            QMessageBox.information(self, "Acceso correcto", f"Bienvenido, {usuario}")
            self.hide()
            self.dashboard = Dashboard(self.cliente_service, self.pedido_service)
            self.dashboard.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")


# ==============================
# Ventana Principal (Dashboard)
# ==============================
class Dashboard(QWidget):
    def __init__(self, cliente_service, pedido_service):
        super().__init__()
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SoftGraph - Panel Principal")
        self.setGeometry(300, 150, 700, 500)

        titulo = QLabel("Dashboard SoftGraph")
        titulo.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_clientes = QPushButton("Listar Clientes")
        btn_clientes.clicked.connect(self.mostrar_clientes)

        btn_pedidos = QPushButton("Listar Pedidos")
        btn_pedidos.clicked.connect(self.mostrar_pedidos)

        btn_salir = QPushButton("Cerrar")
        btn_salir.clicked.connect(self.close)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Dato 1", "Dato 2"])

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(btn_clientes)
        layout_botones.addWidget(btn_pedidos)
        layout_botones.addWidget(btn_salir)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(titulo)
        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(self.tabla)
        self.setLayout(layout_principal)

    def mostrar_clientes(self):
        clientes = self.cliente_service.listar_clientes()
        self.tabla.setRowCount(len(clientes))
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "DNI", "Email"])
        for i, c in enumerate(clientes):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(c.id)))
            self.tabla.setItem(i, 1, QTableWidgetItem(c.nombre))
            self.tabla.setItem(i, 2, QTableWidgetItem(c.dni))
            self.tabla.setItem(i, 3, QTableWidgetItem(c.email))

    def mostrar_pedidos(self):
        pedidos = self.pedido_service.listar_pedidos()
        self.tabla.setRowCount(len(pedidos))
        self.tabla.setHorizontalHeaderLabels(["ID", "Cliente ID", "Descripción", "Total"])
        for i, p in enumerate(pedidos):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(p.id)))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(p.cliente_id)))
            self.tabla.setItem(i, 2, QTableWidgetItem(p.descripcion))
            self.tabla.setItem(i, 3, QTableWidgetItem(f"${p.cantidad * p.precio_unitario:.2f}"))
