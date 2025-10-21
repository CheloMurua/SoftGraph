# 🚀 SoftGraph - Gestión de Imprentas

![Python](https://img.shields.io/badge/Python-3.13-blue) ![MySQL](https://img.shields.io/badge/MySQL-8.0-green) ![License](https://img.shields.io/badge/License-MIT-orange)
![Banner](SoftGraph/assets/softgraph_banner.png)
---

## 📌 Descripción

**SoftGraph** es un sistema en **Python** para la gestión de clientes, pedidos y presupuestos en imprentas.  
Funciona actualmente en **consola**, pero está diseñado para evolucionar a una interfaz gráfica.

✅ Funcionalidades:

- CRUD completo de **clientes** y **pedidos**  
- Generación de **presupuestos** con descuentos aplicables  
- Conexión a **MySQL** mediante DAO centralizado  
- Configuración segura de credenciales con `.env`  

---

## 🛠 Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3.13 | Lenguaje principal |
| MySQL 8.x | Base de datos relacional |
| python-dotenv | Gestión de variables de entorno |
| mysql-connector-python | Conexión a MySQL |
| pytest | Testing (opcional) |

---

## ⚡ Instalación

1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/SoftGraph.git
cd SoftGraph

softgraph/
│
├── main.py
├── requirements.txt
│
├── database/
│   └── database.py
│
├── models/
│   ├── cliente.py
│   ├── pedido.py
│   └── presupuesto.py
│
├── dao/
│   └── dao.py
│
├── services/
│   ├── cliente_service.py
│   ├── pedido_service.py
│   └── presupuesto_service.py
│
├── utils/
│   └── funciones.py
│
└── data/
    └── softgraph.sql

    ---

    
