# gui/dashboard_gui.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from datetime import datetime

class LoginWindow(QWidget):
    def __init__(self, auth_service, cliente_service, pedido_service):
        super().__init__()
        self.auth_service = auth_service
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service

        self.setWindowTitle("SoftGraph - Login")
        self.setFixedSize(350, 200)
        layout = QVBoxLayout()

        title = QLabel("Iniciar sesión")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.DemiBold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Usuario")
        layout.addWidget(self.input_user)

        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Contraseña")
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_pass)

        self.btn_login = QPushButton("Ingresar")
        self.btn_login.clicked.connect(self.login)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def login(self):
        username = self.input_user.text()
        password = self.input_pass.text()
        exito, usuario = self.auth_service.login(username, password)
        if exito:
            self.hide()
            self.dashboard = Dashboard(self.cliente_service, self.pedido_service)
            self.dashboard.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

class Dashboard(QWidget):
    def __init__(self, cliente_service, pedido_service):
        super().__init__()
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service

        self.setWindowTitle("SoftGraph - Dashboard")
        self.setFixedSize(600, 400)
        layout = QVBoxLayout()

        title = QLabel("Dashboard SoftGraph")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.DemiBold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Botones
        btn_layout = QHBoxLayout()

        self.btn_list_clients = QPushButton("Listar Clientes")
        self.btn_list_clients.clicked.connect(self.listar_clientes)
        btn_layout.addWidget(self.btn_list_clients)

        self.btn_add_client = QPushButton("Agregar Cliente")
        self.btn_add_client.clicked.connect(self.agregar_cliente)
        btn_layout.addWidget(self.btn_add_client)

        layout.addLayout(btn_layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

    def listar_clientes(self):
        clientes = self.cliente_service.listar_clientes()
        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Nombre", "DNI", "Email"])
        self.table.setRowCount(len(clientes))
        for row, c in enumerate(clientes):
            self.table.setItem(row, 0, QTableWidgetItem(c.nombre))
            self.table.setItem(row, 1, QTableWidgetItem(c.dni))
            self.table.setItem(row, 2, QTableWidgetItem(c.email if c.email else ""))

    def agregar_cliente(self):
        from PyQt6.QtWidgets import QInputDialog
        nombre, ok1 = QInputDialog.getText(self, "Agregar Cliente", "Nombre:")
        if not ok1 or not nombre:
            return
        dni, ok2 = QInputDialog.getText(self, "Agregar Cliente", "DNI:")
        if not ok2 or not dni:
            return
        email, ok3 = QInputDialog.getText(self, "Agregar Cliente", "Email:")
        if not ok3:
            email = None

        if self.cliente_service.agregar_cliente(nombre, dni, email):
            QMessageBox.information(self, "Éxito", "Cliente agregado correctamente")
            self.listar_clientes()
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar el cliente o ya existe")
