# dashboard_gui.py
import sys, os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QMessageBox, QStackedWidget, QFormLayout,
    QDialog, QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from decimal import Decimal
from dotenv import load_dotenv

# Importar tus servicios y DAOs
from database.database import Database
from services.auth_service import AuthService
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.presupuesto_service import PresupuestoService
from dao.dao import ClienteDAO, PedidoDAO, PresupuestoDAO

load_dotenv()

# ----------------- Estilos modernos -----------------
APP_STYLE = """
QWidget {background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #e0f0ff, stop:1 #ffffff); font-family: "Segoe UI";}
QFrame#card {background: #ffffff; border-radius: 10px; padding: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);}
QPushButton.primary {background-color:#2b6baf; color:#fff; border-radius:8px; padding:8px 12px; font-weight:600;}
QPushButton.ghost {background:transparent; border:1px solid rgba(43,107,175,0.6); border-radius:8px; padding:6px 10px; color:#2b6baf;}
QTableWidget {background:#f5faff; gridline-color:#d0e4ff;}
QHeaderView::section {background:#2b6baf; color:#fff; font-weight:600; padding:6px;}
QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {background:#f0f8ff; border:1px solid #d0e4ff; border-radius:6px; padding:6px;}
QLabel {color:#2b6baf;}
"""

# ----------------- Dashboard -----------------
class SoftGraphDashboard(QWidget):
    def __init__(self, db, auth_service, cliente_service, pedido_service, presupuesto_service):
        super().__init__()
        self.db = db
        self.auth_service = auth_service
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service
        self.presupuesto_service = presupuesto_service

        self.setWindowTitle("SoftGraph — Dashboard")
        self.resize(1200, 700)
        self.setStyleSheet(APP_STYLE)

        self._build_ui()
        self._refresh_summary()

    # ----------------- UI -----------------
    def _build_ui(self):
        main_layout = QHBoxLayout(self)

        # Sidebar
        sidebar = QFrame(); sidebar.setFixedWidth(220)
        v_sidebar = QVBoxLayout(sidebar)
        logo = QLabel("SoftGraph"); logo.setFont(QFont("Segoe UI",18,QFont.Bold)); v_sidebar.addWidget(logo); v_sidebar.addSpacing(12)

        self.btn_dashboard = QPushButton("Dashboard"); self.btn_dashboard.setCheckable(True); self.btn_dashboard.setChecked(True)
        self.btn_clients = QPushButton("Clientes"); self.btn_clients.setCheckable(True)
        self.btn_orders = QPushButton("Pedidos"); self.btn_orders.setCheckable(True)
        self.btn_quotes = QPushButton("Presupuestos"); self.btn_quotes.setCheckable(True)
        for b in [self.btn_dashboard,self.btn_clients,self.btn_orders,self.btn_quotes]: b.setObjectName("sideBtn")
        v_sidebar.addWidget(self.btn_dashboard); v_sidebar.addWidget(self.btn_clients)
        v_sidebar.addWidget(self.btn_orders); v_sidebar.addWidget(self.btn_quotes); v_sidebar.addStretch()
        logout_btn = QPushButton("Cerrar sesión"); logout_btn.clicked.connect(self.logout); v_sidebar.addWidget(logout_btn)

        # Stacked pages
        self.stack = QStackedWidget()
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack,stretch=1)

        # Crear páginas
        self.page_dashboard = self._make_dashboard_page()
        self.page_clients = self._make_clients_page()
        self.page_orders = self._make_orders_page()
        self.page_quotes = self._make_quotes_page()

        self.stack.addWidget(self.page_dashboard)
        self.stack.addWidget(self.page_clients)
        self.stack.addWidget(self.page_orders)
        self.stack.addWidget(self.page_quotes)

        # Conectar botones
        self.btn_dashboard.clicked.connect(lambda: self._switch(0))
        self.btn_clients.clicked.connect(lambda: self._switch(1))
        self.btn_orders.clicked.connect(lambda: self._switch(2))
        self.btn_quotes.clicked.connect(lambda: self._switch(3))

    # ----------------- Dashboard page -----------------
    def _make_dashboard_page(self):
        page = QFrame(); page.setObjectName("card")
        layout = QVBoxLayout(page)
        title = QLabel("Resumen")
        title.setFont(QFont("Segoe UI",18,QFont.Bold))
        layout.addWidget(title)

        # Cards
        cards_layout = QHBoxLayout()
        self.lbl_total_clients = self._stat_card("Clientes","0")
        self.lbl_total_orders = self._stat_card("Pedidos","0")
        self.lbl_total_quotes = self._stat_card("Presupuestos","0")
        cards_layout.addWidget(self.lbl_total_clients); cards_layout.addWidget(self.lbl_total_orders); cards_layout.addWidget(self.lbl_total_quotes)
        layout.addLayout(cards_layout)

        btn_refresh = QPushButton("Actualizar resumen"); btn_refresh.setProperty("class","ghost"); btn_refresh.clicked.connect(self._refresh_summary)
        layout.addWidget(btn_refresh,alignment=Qt.AlignLeft)
        return page

    def _stat_card(self,title,value):
        card = QFrame(); card.setObjectName("card"); v = QVBoxLayout(card)
        t = QLabel(title); t.setFont(QFont("Segoe UI",12,QFont.Bold))
        val = QLabel(value); val.setFont(QFont("Segoe UI",20,QFont.Bold))
        v.addWidget(t); v.addWidget(val); card.value_label = val
        return card

    def _refresh_summary(self):
        try:
            clients = self.cliente_service.listar_clientes() or []
            orders = self.pedido_service.listar_pedidos() or []
            quotes = self.presupuesto_service.presupuesto_dao.listar_presupuestos() or []
            self.lbl_total_clients.value_label.setText(str(len(clients)))
            self.lbl_total_orders.value_label.setText(str(len(orders)))
            self.lbl_total_quotes.value_label.setText(str(len(quotes)))
        except Exception as e:
            print("Error al refrescar resumen:", e)

    # ----------------- Pages helpers -----------------
    def _switch(self,index):
        self.stack.setCurrentIndex(index)
        for i,b in enumerate([self.btn_dashboard,self.btn_clients,self.btn_orders,self.btn_quotes]):
            b.setChecked(i==index)

    def logout(self):
        confirm = QMessageBox.question(self,"Cerrar sesión","¿Cerrar sesión y salir?",QMessageBox.Yes|QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try: self.db.desconectar()
            except: pass
            QApplication.quit()

# ----------------- Main -----------------
def main():
    db = Database(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),
                  password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
    db.conectar()

    auth_service = AuthService(db)
    cliente_service = ClienteService(db)
    pedido_service = PedidoService(db)
    presupuesto_service = PresupuestoService(db,PresupuestoDAO(db))

    app = QApplication(sys.argv)
    window = SoftGraphDashboard(db, auth_service, cliente_service, pedido_service, presupuesto_service)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
