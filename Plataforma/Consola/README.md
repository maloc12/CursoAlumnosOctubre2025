# Manual de Usuario: Aplicación de Consola

Esta aplicación de consola permite gestionar usuarios en una base de datos SQLite. Puedes agregar, eliminar y consultar usuarios fácilmente desde la terminal.

## Requisitos

- Python 3.x instalado
- Estructura de carpetas del proyecto intacta

## Ejecución

1. Abre una terminal en la carpeta `Consola`.
2. Ejecuta el siguiente comando:

	```bash
	python App.py
	```

## Menú de Opciones

Al iniciar la aplicación, verás el siguiente menú:

```
--- Menú de Usuarios ---
1. Agregar usuario
2. Eliminar usuario
3. Consultar usuarios
4. Salir
```

## Funcionalidades

### 1. Agregar usuario
Permite registrar un nuevo usuario solicitando:
- Nombre
- Correo
- Edad

Si el correo ya existe, se mostrará un mensaje de error.

### 2. Eliminar usuario
Solicita el ID del usuario que deseas eliminar. Si el ID no existe, se mostrará un mensaje de error.

### 3. Consultar usuarios
Muestra una tabla con todos los usuarios registrados, incluyendo:
- ID
- Nombre
- Correo
- Edad

### 4. Salir
Cierra la aplicación y la conexión con la base de datos.

## Notas

- La base de datos se guarda en la carpeta principal del proyecto como `usuarios.db`.
- Si tienes problemas de importación, asegúrate de ejecutar el script desde la carpeta `Consola`.

## Ejemplo de uso

```
--- Menú de Usuarios ---
1. Agregar usuario
2. Eliminar usuario
3. Consultar usuarios
4. Salir
Selecciona una opción: 1
Nombre: Juan
Correo: juan@email.com
Edad: 25
Usuario agregado correctamente.
```
