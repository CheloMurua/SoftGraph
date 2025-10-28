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

Este documento describe cómo se aplican los conceptos de **Análisis Matemático** y **Matemática Discreta** dentro del código del proyecto, vinculando las operaciones lógicas, funciones, estructuras y relaciones que forman parte de su implementación.

---

## 2️⃣ Análisis Matemático – Funciones y Proporcionalidad

### 📍 Dónde se aplica
- En `pedido.py` → `calcular_total()`:
  ```python
  def calcular_total(self):
      return self.cantidad * self.precio_unitario
Se define una función matemática lineal entre las variables:

𝑡
𝑜
𝑡
𝑎
𝑙
=
𝑐
𝑎
𝑛
𝑡
𝑖
𝑑
𝑎
𝑑
×
𝑝
𝑟
𝑒
𝑐
𝑖
𝑜
_
𝑢
𝑛
𝑖
𝑡
𝑎
𝑟
𝑖
𝑜
total=cantidad×precio_unitario
Es una relación de proporcionalidad directa, ya que si se duplica la cantidad, el total también se duplica.

En presupuesto.py → calcular_total():

python
Copiar código
total = sum(p.calcular_total() for p in self.pedidos)
total_con_descuento = total * (1 - self.descuento/100)
Aquí se aplican funciones compuestas (suma de subtotales y porcentaje de descuento).
Además, existe proporcionalidad inversa: a mayor descuento, menor total final.

🧠 Conceptos aplicados
Funciones lineales: 
𝑓
(
𝑥
)
=
𝑘
𝑥
f(x)=kx

Funciones de porcentaje: 
𝑓
(
𝑥
)
=
𝑥
(
1
−
𝑑
/
100
)
f(x)=x(1−d/100)

Proporcionalidad directa e inversa.

3️⃣ Técnicas de Conteo y Lógica
📍 Dónde se aplica
En los DAOs (ClienteDAO, PedidoDAO, PresupuestoDAO) al listar o contar registros:

python
Copiar código
resultados = self.db.ejecutar_query("SELECT * FROM clientes")
return [Cliente(... ) for r in resultados]
Se realiza un conteo iterativo de registros, similar al principio de multiplicación de la combinatoria.

En las condiciones lógicas:

python
Copiar código
if resultado:
    return True, resultado[0]
return False, None
Se aplican operadores lógicos y condicionales, propios de la lógica proposicional:

Si la proposición “usuario existe” es verdadera, se ejecuta una acción.

Caso contrario, retorna falso.

🧠 Conceptos aplicados
Conteo de elementos en conjuntos.

Lógica proposicional (condiciones verdaderas o falsas).

Relaciones entre entidades (clientes → pedidos → presupuestos).

4️⃣ Álgebra y Estructuras Discretas
📍 Dónde se aplica
En la relación entre clases y objetos:
Las clases Cliente, Pedido y Presupuesto representan estructuras discretas, con relaciones definidas entre sí.

Ejemplo:

Un cliente puede tener varios pedidos → relación uno a muchos.

Cada pedido pertenece a un solo cliente → relación muchos a uno.

En la base de datos relacional (database.py, dao.py):
Las tablas y sus claves representan conjuntos finitos con operaciones definidas (insertar, eliminar, listar), como en un sistema algebraico cerrado.

🧠 Conceptos aplicados
Conjuntos y relaciones (R ⊆ A×B).

Estructuras discretas (tablas, objetos, relaciones).

Operaciones algebraicas (inserción = suma, eliminación = resta).

5️⃣ Sucesiones y Sistemas de Numeración
📍 Dónde se aplica
En los IDs autoincrementales:
Cada nuevo registro en la base de datos genera una sucesión aritmética:

𝑎
𝑛
=
𝑎
𝑛
−
1
+
1
a 
n
​
 =a 
n−1
​
 +1
En los totales acumulados:

python
Copiar código
total = sum(p.calcular_total() for p in self.pedidos)
Representa una sucesión finita de sumas parciales:

𝑆
𝑛
=
𝑝
1
+
𝑝
2
+
…
+
𝑝
𝑛
S 
n
​
 =p 
1
​
 +p 
2
​
 +…+p 
n
​
 
En los precios y descuentos, que utilizan el sistema decimal (base 10) para representar valores monetarios y porcentuales.

🧠 Conceptos aplicados
Sucesiones aritméticas.

Sumas de términos.

Sistema decimal aplicado a precios e identificadores.

🧾 Resumen General
Área Matemática	Dónde se Aplica	Concepto Principal
Análisis Matemático	Pedido.calcular_total(), Presupuesto.calcular_total()	Funciones lineales, proporciones, porcentajes
Técnicas de Conteo y Lógica	AuthService.login(), DAOs	Lógica proposicional, iteración, conteo de registros
Álgebra y Estructuras Discretas	Clases y relaciones en DAO y DB	Conjuntos, relaciones, estructuras algebraicas
Sucesiones y Sistemas de Numeración	IDs, sumatorias de totales	Sucesiones aritméticas, sistema decimal

💡 Conclusión
El proyecto integra múltiples conceptos matemáticos dentro de su estructura de software:

Las funciones permiten modelar operaciones de precios y descuentos.

La lógica se usa para validar condiciones y controlar el flujo del sistema.

Las estructuras discretas organizan datos y relaciones entre entidades.

Las sucesiones y sistemas numéricos aparecen en la gestión de identificadores, montos y fechas.

Estos elementos combinados reflejan cómo la matemática aplicada es esencial para el diseño de sistemas coherentes, funcionales y escalables.

    
