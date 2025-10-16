# Manual de Usuario - Aplicación de Escritorio

La aplicación de escritorio permite gestionar usuarios almacenados en la base de datos SQLite `usuarios.db`. Puedes agregar, consultar y eliminar usuarios desde una interfaz gráfica.

## Requisitos previos
- Python 3.x instalado
- Librería estándar `tkinter` disponible (viene incluida con Python oficial)
- Archivo `usuarios.db` creado automáticamente en la raíz del proyecto al ejecutar la app

## Cómo ejecutar la aplicación
1. Abre una terminal en la carpeta raíz del proyecto `CursoAlumnosOctubre2025`.
2. Ejecuta el siguiente comando:
	```powershell
	python .\Plataforma\Escritorio\App.py
	```
3. Se abrirá la ventana "Gestión de Usuarios".

## Funcionalidades principales

### Agregar usuario
1. Completa los campos **Nombre**, **Correo** y **Edad** en el formulario superior.
2. Haz clic en el botón **Agregar**.
3. El usuario se guardará en la base de datos y aparecerá en la tabla inferior.

### Consultar usuarios
- La tabla muestra todos los usuarios registrados con sus columnas **ID**, **Nombre**, **Correo** y **Edad**.
- Cada vez que se agrega o elimina un usuario, la tabla se actualiza automáticamente.

### Eliminar usuario
1. Selecciona una fila en la tabla.
2. Haz clic en el botón **Eliminar Seleccionado**.
3. El usuario se eliminará de la base de datos y la tabla se refrescará.

## Cierre de la aplicación
- Al cerrar la ventana, la conexión a la base de datos se cierra de forma segura.

## Posibles errores
- "No se pudo agregar el usuario": revisa que el correo sea válido y no exista ya en la base.
- "No se pudo eliminar el usuario": asegúrate de seleccionar un registro antes de eliminarlo.

¡Listo! Con esto puedes gestionar usuarios fácilmente desde la aplicación de escritorio.
