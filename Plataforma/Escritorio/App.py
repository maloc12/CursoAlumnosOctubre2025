import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

from Plataforma.BDD.BaseDeDatos import BaseDeDatos


class App(tk.Tk):
    def __init__(self):
        """Inicializa la ventana principal y configura la conexión con la base de datos."""
        super().__init__()
        self.title("Gestión de Usuarios")
        self.geometry("720x460")
        self.resizable(False, False)

        self.db = BaseDeDatos(nombre_db=os.path.join(ROOT_PATH, "usuarios.db"))
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.crear_widgets()
        self.actualizar_grid()

    def crear_widgets(self):
        """Crea y posiciona los controles de captura, la tabla y los botones de la interfaz."""
        frame_form = tk.Frame(self)
        frame_form.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_nombre = tk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(frame_form, text="Correo:").grid(row=0, column=2, padx=5, pady=2, sticky="e")
        self.entry_correo = tk.Entry(frame_form, width=30)
        self.entry_correo.grid(row=0, column=3, padx=5, pady=2, sticky="ew")

        tk.Label(frame_form, text="Edad:").grid(row=0, column=4, padx=5, pady=2, sticky="e")
        self.entry_edad = tk.Entry(frame_form, width=10)
        self.entry_edad.grid(row=0, column=5, padx=5, pady=2, sticky="w")

        tk.Button(frame_form, text="Agregar", command=self.agregar_usuario, width=15).grid(row=0, column=6, padx=5, pady=2, sticky="e")

        for col in range(7):
            frame_form.grid_columnconfigure(col, weight=1 if col in (1, 3) else 0)

        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Correo", "Edad"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Edad", text="Edad")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Nombre", width=200)
        self.tree.column("Correo", width=260)
        self.tree.column("Edad", width=90, anchor="center")
        self.tree.pack(expand=True, fill="both", pady=10, padx=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Eliminar Seleccionado", command=self.eliminar_usuario).pack()

    def actualizar_grid(self):
        """Recarga el árbol con los usuarios almacenados en la base de datos."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for usuario in self.db.consultar_usuarios():
            self.tree.insert("", "end", values=usuario)

    def agregar_usuario(self):
        """Valida los datos ingresados y agrega un nuevo usuario a la base de datos."""
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        edad = self.entry_edad.get().strip()

        if not nombre or not correo or not edad.isdigit():
            messagebox.showerror("Error", "Ingrese un nombre, correo y una edad válida.")
            return

        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "Ingrese un correo electrónico válido.")
            return

        try:
            self.db.agregar_usuario(nombre, correo, int(edad))
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo agregar el usuario: {error}")
            return

        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.actualizar_grid()

    def eliminar_usuario(self):
        """Elimina el usuario seleccionado en la tabla después de confirmar la selección."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return

        usuario_id = self.tree.item(seleccion[0])["values"][0]
        try:
            self.db.eliminar_usuario(usuario_id)
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo eliminar el usuario: {error}")
            return

        self.actualizar_grid()

    def on_close(self):
        """Cierra la conexión de base de datos antes de destruir la ventana."""
        self.db.cerrar()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()