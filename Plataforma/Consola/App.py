
import os
import sys

def agregar_ruta_proyecto():
    """
    Agrega la ruta raíz del proyecto al sys.path para permitir importaciones de módulos internos.
    No recibe parámetros ni retorna valores.
    """
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

agregar_ruta_proyecto()
from Plataforma.BDD.BaseDeDatos import BaseDeDatos

def obtener_db_path():
    """
    Obtiene la ruta absoluta para el archivo de base de datos 'usuarios.db' en la carpeta principal del proyecto.
    Returns:
        str: Ruta absoluta del archivo de base de datos.
    """
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'usuarios.db')

db_path = obtener_db_path()
db = BaseDeDatos(nombre_db=db_path)

def menu():
    """
    Muestra el menú principal de opciones para la gestión de usuarios en la consola.
    Opciones del menú:
        1. Agregar usuario: Permite añadir un nuevo usuario al sistema.
        2. Eliminar usuario: Permite eliminar un usuario existente.
        3. Consultar usuarios: Muestra la lista de usuarios registrados.
        4. Salir: Finaliza la ejecución del programa.
    No recibe parámetros ni retorna valores.
    """
    print("\n--- Menú de Usuarios ---")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Consultar usuarios")
    print("4. Salir")

def agregar_usuario():
    """
    Solicita los datos de un nuevo usuario y lo agrega a la base de datos.
    Maneja errores de conversión y de base de datos.
    No recibe parámetros ni retorna valores.
    """
    nombre = input("Nombre: ")
    email = input("Correo: ")
    edad = input("Edad: ")
    try:
        db.agregar_usuario(nombre, email, int(edad))
        print("Usuario agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar usuario: {e}")

def eliminar_usuario():
    """
    Solicita el ID de un usuario y lo elimina de la base de datos.
    Maneja errores de conversión y de base de datos.
    No recibe parámetros ni retorna valores.
    """
    usuario_id = input("ID del usuario a eliminar: ")
    try:
        db.eliminar_usuario(int(usuario_id))
        print("Usuario eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")

def consultar_usuarios():
    """
    Consulta y muestra la lista de usuarios registrados en la base de datos.
    No recibe parámetros ni retorna valores.
    """
    usuarios = db.consultar_usuarios()
    print("\nID | Nombre | Correo | Edad")
    print("-" * 30)
    for u in usuarios:
        print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]}")
    print("-" * 30)

def cerrar_aplicacion():
    """
    Cierra la conexión con la base de datos y finaliza la aplicación.
    No recibe parámetros ni retorna valores.
    """
    db.cerrar()
    print("¡Hasta luego!")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_usuario()
    elif opcion == "2":
        eliminar_usuario()
    elif opcion == "3":
        consultar_usuarios()
    elif opcion == "4":
        cerrar_aplicacion()
        break
    else:
        print("Opción no válida. Intenta de nuevo.")