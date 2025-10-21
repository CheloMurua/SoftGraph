"""
DAO: maneja CRUD de clientes, pedidos y presupuestos.
Aplica técnicas de conteo, lógica y relaciones entre entidades.
"""

from models.cliente import Cliente
from models.pedido import Pedido

class ClienteDAO:
    def __init__(self, db):
        self.db = db

    def agregar_cliente(self, cliente: Cliente):
        query = "INSERT INTO clientes (nombre, dni, email) VALUES (%s, %s, %s)"
        return self.db.ejecutar_query(query, (cliente.nombre, cliente.dni, cliente.email))

    def listar_clientes(self):
        resultados = self.db.ejecutar_query("SELECT * FROM clientes")
        return [Cliente(r['nombre'], r['dni'], r['email'], r['id']) for r in resultados]

    def buscar_cliente_por_dni(self, dni):
        resultados = self.db.ejecutar_query("SELECT * FROM clientes WHERE dni=%s", (dni,))
        if resultados:
            r = resultados[0]
            return Cliente(r['nombre'], r['dni'], r['email'], r['id'])
        return None

class PedidoDAO:
    def __init__(self, db):
        self.db = db

    def agregar_pedido(self, pedido: Pedido):
        query = "INSERT INTO pedidos (cliente_id, descripcion, cantidad, precio_unitario, fecha) VALUES (%s, %s, %s, %s, %s)"
        return self.db.ejecutar_query(query, (pedido.cliente_id, pedido.descripcion, pedido.cantidad, pedido.precio_unitario, pedido.fecha))

    def listar_pedidos(self):
        resultados = self.db.ejecutar_query("SELECT * FROM pedidos")
        return [Pedido(r['cliente_id'], r['descripcion'], r['cantidad'], r['precio_unitario'], r['fecha'], r['id']) for r in resultados]
