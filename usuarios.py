import sqlite3
import hashlib

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT,
    clave_hash TEXT
)
""")

nombre = "Matias Gallegos"
clave = input("Crea una contraseña para Matias Gallegos: ")
clave_hash = hashlib.sha256(clave.encode()).hexdigest()

cursor.execute("INSERT INTO usuarios (nombre, clave_hash) VALUES (?, ?)", (nombre, clave_hash))
conn.commit()

print("Usuario guardado correctamente.")

login_nombre = input("Ingrese usuario: ")
login_clave = input("Ingrese contraseña: ")
login_hash = hashlib.sha256(login_clave.encode()).hexdigest()

cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND clave_hash=?", (login_nombre, login_hash))
resultado = cursor.fetchone()

if resultado:
    print("Acceso concedido")
else:
    print("Acceso denegado")

conn.close()