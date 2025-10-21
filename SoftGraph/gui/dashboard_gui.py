"""
SoftGraph - Dashboard moderno
Autor: Grupo 24
Descripción:
Dashboard moderno con login, clientes y pedidos simulados.
"""

from PyQt6.QtWidgets import (
    QWidget, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QStackedWidget, QFrame,
    QInputDialog
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# ------------------ LOGIN ------------------
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - SoftGraph")
        self.setFixedSize(360, 220)
        self.setStyleSheet("background-color: #f7f9fc; border-radius: 8px;")

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 16, 24, 16)

        title = QLabel("SoftGraph")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.DemiBold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #1e293b;")
        layout.addWidget(title)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")
        self.username_input.setFixedHeight(34)
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(34)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Iniciar sesión")
        login_btn.setFixedHeight(36)
        login_btn.setStyleSheet("""
            QPushButton { background-color: #0ea5e9; color: white; border-radius: 8px; font-weight: 600; }
            QPushButton:hover { background-color: #0284c7; }
        """)
        login_btn.clicked.connect(self.check_login)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # Usuario de prueba
        if username == "admin" and password == "1234":
            self.accept()
            self.dashboard = Dashboard(username=username)
            self.dashboard.show()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos.")


# ------------------ DASHBOARD ------------------
class Dashboard(QWidget):
    def __init__(self, username: str = ""):
        super().__init__()
        self.setWindowTitle(f"SoftGraph - Dashboard ({username})")
        self.setFixedSize(900, 600)
        self.setStyleSheet("background-color: #ffffff;")

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        # --- Menu lateral ---
        self.menu_frame = QFrame()
        self.menu_frame.setFixedWidth(220)
        self.menu_frame.setStyleSheet("background-color: #0b64a0;")
        menu_layout = QVBoxLayout()
        menu_layout.setContentsMargins(16, 16, 16, 16)
        menu_layout.setSpacing(12)
        menu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        logo = QLabel("SoftGraph")
        logo.setFont(QFont("Segoe UI", 18, QFont.Weight.DemiBold))
        logo.setStyleSheet("color: white;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menu_layout.addWidget(logo)

        self.btn_clientes = QPushButton("Clientes")
        self.btn_clientes.clicked.connect(lambda: self.display_section(0))
        menu_layout.addWidget(self.style_menu_btn(self.btn_clientes))

        self.btn_pedidos = QPushButton("Pedidos")
        self.btn_pedidos.clicked.connect(lambda: self.display_section(1))
        menu_layout.addWidget(self.style_menu_btn(self.btn_pedidos))

        menu_layout.addStretch()

        self.btn_logout = QPushButton("Cerrar sesión")
        self.btn_logout.clicked.connect(self.logout)
        menu_layout.addWidget(self.style_menu_btn(self.btn_logout))

        self.menu_frame.setLayout(menu_layout)
        main_layout.addWidget(self.menu_frame)

        # --- Área principal (stacked) ---
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Páginas
        self.setup_clientes_page()
        self.setup_pedidos_page()

        self.display_section(0)

    def style_menu_btn(self, btn: QPushButton) -> QPushButton:
        btn.setFixedHeight(40)
        btn.setStyleSheet("""
            QPushButton { background-color: #1181c9; color: white; border-radius: 8px; font-weight: 600; }
            QPushButton:hover { background-color: #0a66a0; }
        """)
        return btn

    # ------------------ SECCIONES ------------------
    def setup_clientes_page(self):
        self.page_clientes = QWidget()
        layout = QVBoxLayout()
        header = QLabel("Clientes")
        header.setFont(QFont("Segoe UI", 14, QFont.Weight.DemiBold))
        layout.addWidget(header)

        self.table_clientes = QTableWidget()
        layout.addWidget(self.table_clientes)

        btns_row = QHBoxLayout()
        btn_agregar = QPushButton("Agregar cliente")
        btn_agregar.clicked.connect(self.agregar_cliente)
        btns_row.addWidget(btn_agregar)

        btn_refresh = QPushButton("Refrescar")
        btn_refresh.clicked.connect(self.refresh_clientes)
        btns_row.addWidget(btn_refresh)
        layout.addLayout(btns_row)

        self.page_clientes.setLayout(layout)
        self.stack.addWidget(self.page_clientes)
        self.refresh_clientes()

    def setup_pedidos_page(self):
        self.page_pedidos = QWidget()
        layout = QVBoxLayout()
        header = QLabel("Pedidos")
        header.setFont(QFont("Segoe UI", 14, QFont.Weight.DemiBold))
        layout.addWidget(header)

        self.table_pedidos = QTableWidget()
        layout.addWidget(self.table_pedidos)

        btns_row = QHBoxLayout()
        btn_agregar = QPushButton("Agregar pedido")
        btn_agregar.clicked.connect(self.agregar_pedido)
        btns_row.addWidget(btn_agregar)

        btn_refresh = QPushButton("Refrescar")
        btn_refresh.clicked.connect(self.refresh_pedidos)
        btns_row.addWidget(btn_refresh)
        layout.addLayout(btns_row)

        self.page_pedidos.setLayout(layout)
        self.stack.addWidget(self.page_pedidos)
        self.refresh_pedidos()

    # ------------------ FUNCIONES ------------------
    def display_section(self, index: int):
        self.stack.setCurrentIndex(index)

    def logout(self):
        confirm = QMessageBox.question(self, "Cerrar sesión", "¿Cerrar la sesión actual?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            self.close()
            self.login = LoginWindow()
            self.login.show()

    # ---- CLIENTES ----
    def refresh_clientes(self):
        self.table_clientes.clear()
        self.table_clientes.setColumnCount(3)
        self.table_clientes.setHorizontalHeaderLabels(["ID", "Nombre", "Email"])
        self.table_clientes.setRowCount(3)
        for i in range(3):
            self.table_clientes.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.table_clientes.setItem(i, 1, QTableWidgetItem(f"Cliente {i+1}"))
            self.table_clientes.setItem(i, 2, QTableWidgetItem(f"cliente{i+1}@mail.com"))
        self.table_clientes.resizeColumnsToContents()

    def agregar_cliente(self):
        nombre, ok1 = QInputDialog.getText(self, "Agregar cliente", "Nombre:")
        if not ok1 or not nombre.strip(): return
        email, ok2 = QInputDialog.getText(self, "Agregar cliente", "Email:")
        if not ok2: return
        QMessageBox.information(self, "Éxito", f"Cliente '{nombre}' agregado (simulado).")
        self.refresh_clientes()

    # ---- PEDIDOS ----
    def refresh_pedidos(self):
        self.table_pedidos.clear()
        self.table_pedidos.setColumnCount(3)
        self.table_pedidos.setHorizontalHeaderLabels(["ID", "Cliente", "Descripción"])
        self.table_pedidos.setRowCount(3)
        for i in range(3):
            self.table_pedidos.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.table_pedidos.setItem(i, 1, QTableWidgetItem(f"Cliente {i+1}"))
            self.table_pedidos.setItem(i, 2, QTableWidgetItem(f"Pedido {i+1}"))
        self.table_pedidos.resizeColumnsToContents()

    def agregar_pedido(self):
        descripcion, ok = QInputDialog.getText(self, "Agregar pedido", "Descripción:")
        if not ok or not descripcion.strip(): return
        QMessageBox.information(self, "Éxito", f"Pedido '{descripcion}' agregado (simulado).")
        self.refresh_pedidos()
