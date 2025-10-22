# dashboard_gui.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame,
    QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database.database import Database
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.presupuesto_service import PresupuestoService
from services.auth_service import AuthService
from dao.dao import ClienteDAO, PedidoDAO, PresupuestoDAO
from dotenv import load_dotenv
import os

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
QTableWidget {
    background-color: rgba(255,255,255,0.05);
    gridline-color: rgba(255,255,255,0.2);
    border: none;
}
"""

class SoftGraphDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SoftGraph — Dashboard")
        self.resize(1000, 600)
        self.setStyleSheet(APP_STYLE)
        self.db = None
        self.auth_service = None
        self.cliente_service = None
        self.pedido_service = None
        self.presupuesto_service = None
        self._build_ui()
        self.show_login()

    def _build_ui(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(200)
        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)

        self.logo = QLabel("SoftGraph")
        self.logo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        self.logo.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(self.logo)
        self.sidebar_layout.addSpacing(20)

        # Sidebar Buttons
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setObjectName("sideBtn")
        self.btn_dashboard.setChecked(True)
        self.btn_dashboard.clicked.connect(self.show_dashboard)

        self.btn_clients = QPushButton("Clientes")
        self.btn_clients.setCheckable(True)
        self.btn_clients.setObjectName("sideBtn")
        self.btn_clients.clicked.connect(self.show_clientes)

        self.btn_pedidos = QPushButton("Pedidos")
        self.btn_pedidos.setCheckable(True)
        self.btn_pedidos.setObjectName("sideBtn")
        self.btn_pedidos.clicked.connect(self.show_pedidos)

        self.btn_presupuesto = QPushButton("Presupuestos")
        self.btn_presupuesto.setCheckable(True)
        self.btn_presupuesto.setObjectName("sideBtn")
        self.btn_presupuesto.clicked.connect(self.show_presupuestos)

        self.sidebar_layout.addWidget(self.btn_dashboard)
        self.sidebar_layout.addWidget(self.btn_clients)
        self.sidebar_layout.addWidget(self.btn_pedidos)
        self.sidebar_layout.addWidget(self.btn_presupuesto)
        self.sidebar_layout.addStretch()

        # Main Area
        self.main_area = QFrame()
        self.main_layout = QVBoxLayout()
        self.main_area.setLayout(self.main_layout)

        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.main_area)

    # --- LOGIN ---
    def show_login(self):
        login_widget = QWidget()
        layout = QVBoxLayout()
        login_widget.setLayout(layout)

        layout.addWidget(QLabel("Usuario:"))
        self.input_user = QLineEdit()
        layout.addWidget(self.input_user)

        layout.addWidget(QLabel("Contraseña:"))
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_pass)

        btn_login = QPushButton("Login")
        btn_login.clicked.connect(self.attempt_login)
        layout.addWidget(btn_login)

        self.clear_main()
        self.main_layout.addWidget(login_widget)

    def attempt_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()
        # Conectar DB paso a paso
        load_dotenv()
        try:
            self.db = Database(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.db.conectar()
        except Exception as e:
            QMessageBox.critical(self, "Error DB", str(e))
            return

        self.auth_service = AuthService(self.db)
        exito, usuario = self.auth_service.login(username, password)
        if not exito:
            QMessageBox.warning(self, "Login fallido", "Usuario o contraseña incorrectos")
            return

        # Inicializar servicios
        self.cliente_service = ClienteService(self.db)
        self.pedido_service = PedidoService(self.db)
        self.presupuesto_service = PresupuestoService(self.db, PresupuestoDAO(self.db))

        self.show_dashboard()
        QMessageBox.information(self, "Login correcto", f"¡Bienvenido {usuario['username']}!")

    # --- Funciones para sidebar ---
    def clear_main(self):
        for i in reversed(range(self.main_layout.count())):
            widget = self.main_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def show_dashboard(self):
        self.clear_main()
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout()
        card.setLayout(v)
        v.addWidget(QLabel("¡Bienvenido a SoftGraph!"))
        self.main_layout.addWidget(card)

    def show_clientes(self):
        
        self.clear_main()
        clientes = self.cliente_service.listar_clientes()
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout()
        card.setLayout(v)

        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Nombre", "DNI", "Email"])
        table.setRowCount(len(clientes))
        for i, c in enumerate(clientes):
            table.setItem(i, 0, QTableWidgetItem(c.nombre))
            table.setItem(i, 1, QTableWidgetItem(c.dni))
            table.setItem(i, 2, QTableWidgetItem(c.email or ""))
        v.addWidget(table)

        # Botones agregar / eliminar
        btn_add = QPushButton("Agregar Cliente")
        btn_add.clicked.connect(self.add_cliente)
        btn_del = QPushButton("Eliminar Cliente")
        btn_del.clicked.connect(self.del_cliente)
        v.addWidget(btn_add)
        v.addWidget(btn_del)

        self.main_layout.addWidget(card)
        if not self.cliente_service:
            QMessageBox.warning(self, "Error", "Debes iniciar sesión primero")
            return

    def add_cliente(self):
        nombre, ok1 = QInputDialog.getText(self, "Agregar Cliente", "Nombre:")
        if not ok1 or not nombre:
            return
        dni, ok2 = QInputDialog.getText(self, "Agregar Cliente", "DNI:")
        if not ok2 or not dni:
            return
        email, ok3 = QInputDialog.getText(self, "Agregar Cliente", "Email (opcional):")
        if not self.cliente_service.agregar_cliente(nombre, dni, email):
            QMessageBox.warning(self, "Error", "Cliente ya existe")
        else:
            QMessageBox.information(self, "Éxito", "Cliente agregado")
            self.show_clientes()

    def del_cliente(self):
        dni, ok = QInputDialog.getText(self, "Eliminar Cliente", "DNI del cliente:")
        if not ok or not dni:
            return
        cliente = self.cliente_service.cliente_dao.buscar_cliente_por_dni(dni)
        if not cliente:
            QMessageBox.warning(self, "Error", "Cliente no encontrado")
            return
        confirm = QMessageBox.question(self, "Confirmar", f"Eliminar {cliente.nombre}?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cliente_service.cliente_dao.eliminar_cliente(cliente.id)
            QMessageBox.information(self, "Éxito", "Cliente eliminado")
            self.show_clientes()

    def show_pedidos(self):
        self.clear_main()
        pedidos = self.pedido_service.listar_pedidos()
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout()
        card.setLayout(v)

        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Cliente ID", "Descripción", "Cantidad", "Precio Unit.", "Fecha"])
        table.setRowCount(len(pedidos))
        for i, p in enumerate(pedidos):
            table.setItem(i, 0, QTableWidgetItem(str(p.cliente_id)))
            table.setItem(i, 1, QTableWidgetItem(p.descripcion))
            table.setItem(i, 2, QTableWidgetItem(str(p.cantidad)))
            table.setItem(i, 3, QTableWidgetItem(str(p.precio_unitario)))
            table.setItem(i, 4, QTableWidgetItem(str(p.fecha)))
        v.addWidget(table)

        btn_add = QPushButton("Agregar Pedido")
        btn_add.clicked.connect(self.add_pedido)
        btn_del = QPushButton("Eliminar Pedido")
        btn_del.clicked.connect(self.del_pedido)
        v.addWidget(btn_add)
        v.addWidget(btn_del)

        self.main_layout.addWidget(card)

    def add_pedido(self):
        dni, ok1 = QInputDialog.getText(self, "Agregar Pedido", "DNI del cliente:")
        if not ok1 or not dni:
            return
        cliente = self.cliente_service.cliente_dao.buscar_cliente_por_dni(dni)
        if not cliente:
            QMessageBox.warning(self, "Error", "Cliente no encontrado")
            return
        descripcion, ok2 = QInputDialog.getText(self, "Agregar Pedido", "Descripción:")
        if not ok2 or not descripcion:
            return
        cantidad, ok3 = QInputDialog.getInt(self, "Agregar Pedido", "Cantidad:", 1, 1)
        if not ok3:
            return
        precio, ok4 = QInputDialog.getDouble(self, "Agregar Pedido", "Precio Unitario:", 0.0, 0.0)
        if not ok4:
            return
        self.pedido_service.agregar_pedido(cliente.id, descripcion, cantidad, precio)
        QMessageBox.information(self, "Éxito", "Pedido agregado")
        self.show_pedidos()

    def del_pedido(self):
        pid, ok = QInputDialog.getInt(self, "Eliminar Pedido", "ID del pedido:")
        if not ok:
            return
        self.pedido_service.pedido_dao.eliminar_pedido(pid)
        QMessageBox.information(self, "Éxito", "Pedido eliminado si existía")
        self.show_pedidos()

    def show_presupuestos(self):
        self.clear_main()
        card = QFrame()
        card.setObjectName("card")
        v = QVBoxLayout()
        card.setLayout(v)

        pedidos = self.pedido_service.listar_pedidos()
        descuento, ok = QInputDialog.getDouble(self, "Generar Presupuesto", "Porcentaje de descuento:", 0.0, 0, 100, 2)
        if not ok:
            return
        self.presupuesto_service.generar_presupuesto(pedidos, descuento)
        v.addWidget(QLabel(f"Presupuesto generado con {len(pedidos)} pedidos y {descuento}% de descuento"))
        self.main_layout.addWidget(card)

# --- Ejecutar ---
if __name__ == "__main__":
    print(">>> Dashboard GUI iniciado correctamente")
    app = QApplication(sys.argv)
    window = SoftGraphDashboard()
    window.show()
    sys.exit(app.exec_())
