"""
Service de Cliente: maneja la lógica de negocio sobre clientes.
Valida duplicados y aplica reglas antes de llamar al DAO.
"""
print("Dashboard GUI iniciado correctamente")
from dao.dao import ClienteDAO
from models.cliente import Cliente

class ClienteService:
    def __init__(self, db):
        self.cliente_dao = ClienteDAO(db)

    def agregar_cliente(self, nombre, dni, email=None):
        # Validación: no duplicar DNI
        if self.cliente_dao.buscar_cliente_por_dni(dni):
            print("El cliente ya existe")
            return False
        cliente = Cliente(nombre, dni, email)
        return self.cliente_dao.agregar_cliente(cliente)

    def listar_clientes(self):
        return self.cliente_dao.listar_clientes()
