import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_db='usuarios.db'):
        self.conn = sqlite3.connect(nombre_db)
        self.crear_tabla()

    def crear_tabla(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    edad INTEGER
                )
            ''')

    def agregar_usuario(self, nombre, email, edad):
        with self.conn:
            self.conn.execute(
                'INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)',
                (nombre, email, edad)
            )

    def eliminar_usuario(self, usuario_id):
        with self.conn:
            self.conn.execute(
                'DELETE FROM usuarios WHERE id = ?',
                (usuario_id,)
            )

    def consultar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nombre, email, edad FROM usuarios')
        return cursor.fetchall()

    def cerrar(self):
        self.conn.close()

