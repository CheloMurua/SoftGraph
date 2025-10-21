# main.py

from database.database import Database
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.presupuesto_service import PresupuestoService
from services.auth_service import AuthService
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def main():
    # Conexión a la base de datos
    db = Database(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    db.conectar()

    # Inicializar servicios
    auth_service = AuthService(db)
    cliente_service = ClienteService(db)
    pedido_service = PedidoService(db)
    presupuesto_service = PresupuestoService()

    # --- LOGIN ---
    print("=== Bienvenido a SoftGraph ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    exito, usuario = auth_service.login(username, password)
    if not exito:
        print("Usuario o contraseña incorrectos. Saliendo...")
        db.desconectar()
        exit()
    else:
        print(f"¡Bienvenido {usuario['username']}!")

    # --- MENÚ PRINCIPAL ---
    while True:
        print("\n=== Menú SoftGraph ===")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("4. Listar pedidos")
        print("5. Agregar pedido")
        print("6. Eliminar pedido")
        print("7. Generar presupuesto")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            break

        elif opcion == "1":
            clientes = cliente_service.listar_clientes()
            if clientes:
                for c in clientes:
                    print(c)
            else:
                print("No hay clientes registrados.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            email = input("Email: ")
            if cliente_service.agregar_cliente(nombre, dni, email):
                print("Cliente agregado con éxito.")

        elif opcion == "3":
            dni = input("DNI del cliente a eliminar: ")
            cliente = cliente_service.cliente_dao.buscar_cliente_por_dni(dni)
            if cliente:
                confirm = input(f"Eliminar {cliente.nombre}? (s/n): ")
                if confirm.lower() == "s":
                    cliente_service.cliente_dao.eliminar_cliente(cliente.id)
                    print("Cliente eliminado.")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            pedidos = pedido_service.listar_pedidos()
            if pedidos:
                for p in pedidos:
                    print(p)
            else:
                print("No hay pedidos registrados.")

        elif opcion == "5":
            dni = input("DNI del cliente: ")
            cliente = cliente_service.cliente_dao.buscar_cliente_por_dni(dni)
            if not cliente:
                print("Cliente no encontrado.")
                continue
            descripcion = input("Descripción del pedido: ")
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio unitario: "))
            pedido_service.agregar_pedido(cliente.id, descripcion, cantidad, precio_unitario)

        elif opcion == "6":
            pedido_id = int(input("ID del pedido a eliminar: "))
            pedido_service.pedido_dao.eliminar_pedido(pedido_id)
            print("Pedido eliminado si existía.")

        elif opcion == "7":
            pedidos = pedido_service.listar_pedidos()
            if not pedidos:
                print("No hay pedidos para generar presupuesto.")
                continue
            descuento = float(input("Porcentaje de descuento: "))
            presupuesto_service.generar_presupuesto(pedidos, descuento)

        else:
            print("Opción inválida. Intente nuevamente.")

    db.desconectar()
    print("¡Hasta luego!")


if __name__ == "__main__":
    main()