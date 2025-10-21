-- ==========================================================
-- Script: softgraph.sql
-- Proyecto: SoftGraph - Gestión y Automatización de Presupuestos en Imprentas
-- ==========================================================

-- 1️⃣ Crear base de datos
CREATE DATABASE IF NOT EXISTS softgraph;
USE softgraph;

-- 1️⃣ Tabla de usuarios (para autenticación)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- 2️⃣ Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100)
);

-- 3️⃣ Tabla de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    descripcion TEXT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- 4️⃣ Tabla de presupuestos
CREATE TABLE IF NOT EXISTS presupuestos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    descuento DECIMAL(5,2) DEFAULT 0,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- 5️⃣ Opcional: tabla intermedia pedido_presupuesto si se quieren vincular varios pedidos a un presupuesto
CREATE TABLE IF NOT EXISTS pedido_presupuesto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    presupuesto_id INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (presupuesto_id) REFERENCES presupuestos(id) ON DELETE CASCADE
);

-- ==========================================================
-- Datos de ejemplo (opcional)
-- ==========================================================
INSERT INTO clientes (nombre, dni, email) VALUES
('Maria Jose Castro', '25920011', 'maria@email.com'),
('Yamila Noelia Belen Angelo', '38654685', 'yamila@email.com');

INSERT INTO pedidos (cliente_id, descripcion, cantidad, precio_unitario) VALUES
(1, 'Impresión Flyers', 500, 2.5),
(2, 'Impresión Tarjetas', 300, 1.8);

INSERT INTO presupuestos (cliente_id, total, descuento) VALUES
(1, 1250.00, 0),
(2, 540.00, 10);

-- Ejemplo de usuario
INSERT INTO usuarios (username, password) VALUES
('admin', '1234'); -- en producción, usar hash

