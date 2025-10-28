# 🚀 SoftGraph - Gestión de Imprentas

![Python](https://img.shields.io/badge/Python-3.13-blue) 
![MySQL](https://img.shields.io/badge/MySQL-8.0-green) 
![License](https://img.shields.io/badge/License-MIT-orange)
![Logo](https://drive.google.com/uc?export=view&id=1f_lBwux7cw0JwBUGhqHSn1MGdMSPtRNk)
---

## 📌 Descripción

**SoftGraph** es un sistema en **Python** para la gestión de clientes, pedidos y presupuestos en imprentas.
Forma parte del Proyecto ABP del ISPC de la materia Elementos de Matemática y Lógica.  

Carátula: 
[PDF]https://drive.google.com/file/d/1kGaC_PEkCRD5rPItyMu20uWG26Sx1t7M/view?usp=sharing

Estructura ABP:
[PDF]https://drive.google.com/file/d/1LXbpDhooGl1qMrPr1SiucrE_G6GNr0lu/view?usp=sharing



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
├── dashboard_gui.py
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


# 🧮 Aplicación de Conceptos Matemáticos en el Proyecto

Este documento describe cómo se aplican los conceptos de Análisis Matemático y Matemática Discreta dentro del código del proyecto, vinculando las operaciones lógicas, funciones, estructuras y relaciones que forman parte de su implementación.

---

🧮 2. Análisis Matemático – Funciones y Proporcionalidad

“En la parte del cálculo de pedidos y presupuestos se aplican funciones matemáticas y proporcionalidad directa e inversa.”

💻 Ejemplo en el código:
def calcular_total(self):
    return self.cantidad * self.precio_unitario


📊 “Esta es una función lineal donde el total es directamente proporcional a la cantidad.
Si duplicamos la cantidad, el total también se duplica.”

✏️ “En el caso del presupuesto, se aplica una función compuesta que incluye un descuento,
por ejemplo: total_final = total × (1 - descuento / 100).
Ahí aparece una proporcionalidad inversa: si aumento el descuento, el total final disminuye.”

🔎 Conclusión:
“Estas funciones reflejan relaciones matemáticas reales dentro del modelo de negocio.”

🔢 3. Técnicas de Conteo y Lógica

🗣️ “Otro punto clave fue la aplicación de la lógica proposicional y las técnicas de conteo.”

💻 Ejemplo:
if resultado:
    return True, resultado[0]
return False, None

🧠 “Acá se aplica una condición lógica: si el usuario existe, la proposición es verdadera y se permite el acceso; si no, es falsa y se deniega. Es un ejemplo directo de lógica booleana.”

📈 “También se aplican técnicas de conteo en las funciones que listan o recorren registros, como al mostrar todos los clientes o los pedidos de un usuario.”

🔎 Conclusión:
“La lógica y el conteo son esenciales para el control de flujo y la organización de los datos.”

🧩 4. Álgebra y Estructuras Discretas

“En el diseño del sistema se usaron estructuras discretas y relaciones algebraicas entre conjuntos de datos.”

📘 “Por ejemplo, un cliente puede tener muchos pedidos y cada pedido pertenece a un solo cliente.
Esto representa una relación uno a muchos, que podemos interpretar como un conjunto de pares ordenados dentro de la matemática discreta.”

📂 “Además, las tablas de la base de datos funcionan como conjuntos finitos con operaciones definidas —insertar, eliminar, modificar— que son equivalentes a operaciones algebraicas en un sistema cerrado.”

🔎 Conclusión:
“Las estructuras discretas permiten mantener coherencia y orden en los datos.”

🔁 5. Sucesiones y Sistemas de Numeración

“Otro concepto presente son las sucesiones y los sistemas de numeración.”

💻 Ejemplo:

IDs autoincrementales → Sucesión aritmética:

an​=an−1​+1
	​

Totales acumulados → Sumatoria:

Sn​=p1​+p2​+...+pn​
	​

📊 “Cada vez que se crea un nuevo cliente o pedido, el sistema genera un ID consecutivo, formando una sucesión aritmética.
Y cuando calculamos el total de varios pedidos, estamos aplicando una sumatoria de términos.”

🔎 Conclusión:
“Estas operaciones representan cómo los conceptos matemáticos se traducen en operaciones reales del software.”

📌 Resumen breve:

Funciones y proporcionalidad: Cálculos de totales y descuentos.

Lógica proposicional: Validaciones de usuarios y condiciones.

Estructuras discretas: Clases, tablas y relaciones entre datos.

Sucesiones y conteo: IDs, registros y sumatorias.

🎯 Gracias a estos conceptos, el sistema no solo es funcional, sino también coherente, escalable y matemáticamente consistente.

    
