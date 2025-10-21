"""
Clase Cliente: representa un cliente de la imprenta.
Aplica lógica de entidades y relaciones con pedidos/presupuestos.
"""

class Cliente:
    def __init__(self, nombre, dni, email=None, id=None):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.email = email

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"
