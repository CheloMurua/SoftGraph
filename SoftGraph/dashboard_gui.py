# dashboard_gui_moderno.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame,
    QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from database.database import Database
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.presupuesto_service import PresupuestoService
from services.auth_service import AuthService
from dao.dao import ClienteDAO, PedidoDAO, PresupuestoDAO
from dotenv import load_dotenv
import os

# --- Estilo moderno tipo Material / Bootstrap ---
APP_STYLE = """
QWidget {
    background-color: #f5f6fa;
    color: #2f3640;
    font-family: "Segoe UI", Arial;
    font-size: 13px;
}
#sidebar {
    background-color: #2f3640;
    color: #f5f6fa;
}
QPushButton#sideBtn {
    background: transparent;
    color: #f5f6fa;
    border: none;
    padding: 12px 20px;
    text-align: left;
}
QPushButton#sideBtn:hover {
    background-color: #57606f;
    color: #fff;
}
QPushButton#sideBtn:checked {
    background-color: #00a8ff;
    color: #fff;
    font-weight: bold;
}
QFrame#card {
    background-color: #dcdde1;
    border-radius: 10px;
    padding: 15px;
}
QTableWidget {
    background-color: #ffffff;
    gridline-color: #dcdde1;
    border: 1px solid #dcdde1;
}
QPushButton#actionBtn {
    background-color: #00a8ff;
    color: #fff;
    border-radius: 6px;
    padding: 6px 14px;
    font-weight: bold;
}
QPushButton#actionBtn:hover {
    background-color: #0097e6;
}
QLabel#titleCard {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 10px;
}
"""

class SoftGraphDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SoftGraph — Dashboard Moderno")
        self.resize(1200, 700)
        self.setStyleSheet(APP_STYLE)

        # Inicialización de servicios
        self.db = None
        self.auth_service = None
        self.cliente_service = None
        self.pedido_service = None
        self.presupuesto_service = None

        self._build_ui()
        self.show_login()

    # --- Construcción UI ---
    def _build_ui(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(250)
        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)

        self.logo = QLabel("SoftGraph")
        self.logo.setFont(QFont("Segoe UI", 24, QFont.Bold))
        self.logo.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(self.logo)
        self.sidebar_layout.addSpacing(40)

        # Botones sidebar con iconos
        self.btn_dashboard = QPushButton("🏠 Dashboard")
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setObjectName("sideBtn")
        self.btn_dashboard.setChecked(True)
        self.btn_dashboard.clicked.connect(self.show_dashboard)

        self.btn_clients = QPushButton("👥 Clientes")
        self.btn_clients.setCheckable(True)
        self.btn_clients.setObjectName("sideBtn")
        self.btn_clients.clicked.connect(self.show_clientes)

        self.btn_pedidos = QPushButton("🛒 Pedidos")
        self.btn_pedidos.setCheckable(True)
        self.btn_pedidos.setObjectName("sideBtn")
        self.btn_pedidos.clicked.connect(self.show_pedidos)

        self.btn_presupuesto = QPushButton("💰 Presupuestos")
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
        self.clear_main()
        login_widget = QFrame()
        layout = QVBoxLayout()
        login_widget.setLayout(layout)
        login_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        lbl_title = QLabel("Iniciar Sesión")
        lbl_title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        lbl_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_title)

        layout.addSpacing(20)
        layout.addWidget(QLabel("Usuario:"))
        self.input_user = QLineEdit()
        layout.addWidget(self.input_user)

        layout.addWidget(QLabel("Contraseña:"))
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_pass)

        btn_login = QPushButton("Entrar")
        btn_login.setObjectName("actionBtn")
        btn_login.clicked.connect(self.attempt_login)
        layout.addWidget(btn_login)
        layout.addStretch()

        self.main_layout.addWidget(login_widget)

    def attempt_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()
        try:
            load_dotenv()
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

        try:
            self.auth_service = AuthService(self.db)
            exito, usuario = self.auth_service.login(username, password)
            if not exito:
                QMessageBox.warning(self, "Login fallido", "Usuario o contraseña incorrectos")
                return

            # Inicializar servicios
            self.cliente_service = ClienteService(self.db)
            self.pedido_service = PedidoService(self.db)
            self.presupuesto_service = PresupuestoService(self.db, PresupuestoDAO(self.db))

            QMessageBox.information(self, "Login correcto", f"¡Bienvenido {usuario['username']}!")
            self.show_dashboard()
        except Exception as e:
            QMessageBox.critical(self, "Error Servicios", str(e))

    # --- Funciones generales ---
    def clear_main(self):
        for i in reversed(range(self.main_layout.count())):
            widget = self.main_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def _create_card(self, title, widgets):
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout()
        card.setLayout(layout)
        lbl_title = QLabel(title)
        lbl_title.setObjectName("titleCard")
        layout.addWidget(lbl_title)
        for w in widgets:
            layout.addWidget(w)
        return card

    # --- DASHBOARD ---
    def show_dashboard(self):
        self.clear_main()
        widgets = [
            QLabel("Bienvenido a SoftGraph Moderno!"),
            QLabel("Navega por Clientes, Pedidos y Presupuestos usando el sidebar."),
        ]
        card = self._create_card("Dashboard", widgets)
        self.main_layout.addWidget(card)

    # --- CLIENTES ---
    def show_clientes(self):
        self.clear_main()
        if not self.cliente_service:
            QMessageBox.warning(self, "Error", "Debes iniciar sesión primero")
            return
        try:
            clientes = self.cliente_service.listar_clientes()
            table = QTableWidget()
            table.setColumnCount(3)
            table.setHorizontalHeaderLabels(["Nombre", "DNI", "Email"])
            table.setRowCount(len(clientes))
            for i, c in enumerate(clientes):
                table.setItem(i, 0, QTableWidgetItem(c.nombre))
                table.setItem(i, 1, QTableWidgetItem(c.dni))
                table.setItem(i, 2, QTableWidgetItem(c.email or ""))

            btn_add = QPushButton("Agregar Cliente")
            btn_add.setObjectName("actionBtn")
            btn_add.clicked.connect(self.add_cliente)
            btn_del = QPushButton("Eliminar Cliente")
            btn_del.setObjectName("actionBtn")
            btn_del.clicked.connect(self.del_cliente)

            card = self._create_card("Clientes", [table, btn_add, btn_del])
            self.main_layout.addWidget(card)
        except Exception as e:
            QMessageBox.critical(self, "Error Clientes", str(e))

    def add_cliente(self):
        try:
            nombre, ok1 = QInputDialog.getText(self, "Agregar Cliente", "Nombre:")
            if not ok1 or not nombre: return
            dni, ok2 = QInputDialog.getText(self, "Agregar Cliente", "DNI:")
            if not ok2 or not dni: return
            email, ok3 = QInputDialog.getText(self, "Agregar Cliente", "Email (opcional):")
            if not self.cliente_service.agregar_cliente(nombre, dni, email):
                QMessageBox.warning(self, "Error", "Cliente ya existe")
            else:
                QMessageBox.information(self, "Éxito", "Cliente agregado")
                self.show_clientes()
        except Exception as e:
            QMessageBox.critical(self, "Error Agregar Cliente", str(e))

    def del_cliente(self):
        try:
            dni, ok = QInputDialog.getText(self, "Eliminar Cliente", "DNI del cliente:")
            if not ok or not dni: return
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
        except Exception as e:
            QMessageBox.critical(self, "Error Eliminar Cliente", str(e))

    # --- PEDIDOS ---
    def show_pedidos(self):
        self.clear_main()
        if not self.pedido_service:
            QMessageBox.warning(self, "Error", "Debes iniciar sesión primero")
            return
        try:
            pedidos = self.pedido_service.listar_pedidos()
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

            btn_add = QPushButton("Agregar Pedido")
            btn_add.setObjectName("actionBtn")
            btn_add.clicked.connect(self.add_pedido)
            btn_del = QPushButton("Eliminar Pedido")
            btn_del.setObjectName("actionBtn")
            btn_del.clicked.connect(self.del_pedido)

            card = self._create_card("Pedidos", [table, btn_add, btn_del])
            self.main_layout.addWidget(card)
        except Exception as e:
            QMessageBox.critical(self, "Error Pedidos", str(e))

    def add_pedido(self):
        try:
            dni, ok1 = QInputDialog.getText(self, "Agregar Pedido", "DNI del cliente:")
            if not ok1 or not dni: return
            cliente = self.cliente_service.cliente_dao.buscar_cliente_por_dni(dni)
            if not cliente:
                QMessageBox.warning(self, "Error", "Cliente no encontrado")
                return
            descripcion, ok2 = QInputDialog.getText(self, "Agregar Pedido", "Descripción:")
            if not ok2 or not descripcion: return
            cantidad, ok3 = QInputDialog.getInt(self, "Agregar Pedido", "Cantidad:", 1, 1)
            if not ok3: return
            precio, ok4 = QInputDialog.getDouble(self, "Agregar Pedido", "Precio Unitario:", 0.0, 0.0)
            if not ok4: return
            self.pedido_service.agregar_pedido(cliente.id, descripcion, cantidad, precio)
            QMessageBox.information(self, "Éxito", "Pedido agregado")
            self.show_pedidos()
        except Exception as e:
            QMessageBox.critical(self, "Error Agregar Pedido", str(e))

    def del_pedido(self):
        try:
            pid, ok = QInputDialog.getInt(self, "Eliminar Pedido", "ID del pedido:")
            if not ok: return
            self.pedido_service.pedido_dao.eliminar_pedido(pid)
            QMessageBox.information(self, "Éxito", "Pedido eliminado si existía")
            self.show_pedidos()
        except Exception as e:
            QMessageBox.critical(self, "Error Eliminar Pedido", str(e))

    # --- PRESUPUESTOS ---
    def show_presupuestos(self):
        self.clear_main()
        if not self.presupuesto_service or not self.pedido_service:
            QMessageBox.warning(self, "Error", "Debes iniciar sesión primero")
            return
        try:
            pedidos = self.pedido_service.listar_pedidos()
            descuento, ok = QInputDialog.getDouble(self, "Generar Presupuesto",
                                                   "Porcentaje de descuento:", 0.0, 0, 100, 2)
            if not ok: return
            self.presupuesto_service.generar_presupuesto(pedidos, descuento)
            card = self._create_card("Presupuestos", [QLabel(f"Presupuesto generado con {len(pedidos)} pedidos y {descuento}% de descuento")])
            self.main_layout.addWidget(card)
        except Exception as e:
            QMessageBox.critical(self, "Error Presupuestos", str(e))


# --- Ejecutar ---
if __name__ == "__main__":
    print(">>> Dashboard Moderno iniciado correctamente")
    app = QApplication(sys.argv)
    window = SoftGraphDashboard()
    window.show()
    sys.exit(app.exec_())
