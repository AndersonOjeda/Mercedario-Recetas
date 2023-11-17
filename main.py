import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


class Ingrediente:
    def __init__(self, nombre, unidad, valor_unidad, sitio_compra, calorias_unidad):
        self.nombre = nombre
        self.unidad = unidad
        self.valor_unidad = valor_unidad
        self.sitio_compra = sitio_compra
        self.calorias_unidad = calorias_unidad

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_unidad(self):
        return self.unidad

    def set_unidad(self, nueva_unidad):
        self.unidad = nueva_unidad

    def get_valor_unidad(self):
        return self.valor_unidad

    def set_valor_unidad(self, valor_unidad):
        self.valor_unidad = valor_unidad

    def get_sitio_compra(self):
        return self.sitio_compra

    def set_sitio_compra(self, sitio_compra):
        self.sitio_compra = sitio_compra

    def get_calorias_unidad(self):
        return self.calorias_unidad

    def set_calorias_unidad(self, calorias_unidad):
        self.calorias_unidad = calorias_unidad

    def __str__(self):
        return f'Ingrediente [nombre={self.nombre}, cantidad={self.unidad}, valorUnidad={self.valor_unidad} COP, sitioCompra={self.sitio_compra}, caloriasUnidad={self.calorias_unidad}]'


class Receta:
    def __init__(self, nombre_receta, tiempo_preparacion, numero_personas, lista_ingredientes, descripcion):
        self.nombre_receta = nombre_receta
        self.tiempo_preparacion = tiempo_preparacion
        self.numero_personas = numero_personas
        self.lista_ingredientes = lista_ingredientes
        self.descripcion = descripcion

    def get_nombre_receta(self):
        return self.nombre_receta

    def set_nombre_receta(self, nombre_receta):
        self.nombre_receta = nombre_receta

    def get_tiempo_preparacion(self):
        return self.tiempo_preparacion

    def set_tiempo_preparacion(self, tiempo_preparacion):
        self.tiempo_preparacion = tiempo_preparacion

    def get_numero_personas(self):
        return self.numero_personas

    def set_numero_personas(self, numero_personas):
        self.numero_personas = numero_personas

    def get_lista_ingredientes(self):
        return self.lista_ingredientes

    def set_lista_ingredientes(self, lista_ingredientes):
        self.lista_ingredientes = lista_ingredientes

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'Receta [nombreReceta={self.nombre_receta}, tiempoPreparacion={self.tiempo_preparacion} Minutos, numeroPersonas={self.numero_personas}, listaIngredientes={self.lista_ingredientes}, descripcion={self.descripcion}]'


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Configurar colores
        bg_color = "#8A2BE2"  # morado
        text_color = "white"   # Blanco
        entry_bg_color = "#ffb6c1"  # Rosado claro

        # Usuarios y contraseñas almacenados
        self.users = {"admin": "admin"}

        # Crear y configurar el frame principal
        self.frame = tk.Frame(self.master, bg=bg_color)
        self.frame.pack(expand=True, fill="both")

        # Texto informativo
        self.label_info = tk.Label(self.frame, text="BIENVENIDO A RESTAURANTE MERCEDARIO",
                                   bg=bg_color, fg=text_color)
        self.label_info.pack(pady=(20, 10))

        # Cuadro para el usuario
        self.label_username = tk.Label(self.frame, text="Usuario:", bg=bg_color, fg=text_color)
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.frame, bg=entry_bg_color, fg=text_color)
        self.entry_username.pack(pady=5)

        # Cuadro para la contraseña
        self.label_password = tk.Label(self.frame, text="Contraseña:", bg=bg_color, fg=text_color)
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.frame, show="*", bg=entry_bg_color, fg=text_color)
        self.entry_password.pack(pady=5)

        # Botón de iniciar sesión
        self.btn_login = tk.Button(self.frame, text="Iniciar Sesión", command=self.login, bg=entry_bg_color, fg=text_color)
        self.btn_login.pack(pady=10)

        # Botón para restaurar contraseña
        self.btn_restore_password = tk.Button(self.frame, text="Restaurar Contraseña", command=self.restore_password, bg=entry_bg_color, fg=text_color)
        self.btn_restore_password.pack(side="left", anchor="sw", padx=10, pady=10)

        # Botón para crear un nuevo usuario
        self.btn_new_user = tk.Button(self.frame, text="Crear Nuevo Usuario", command=self.create_new_user, bg=entry_bg_color, fg=text_color)
        self.btn_new_user.pack(side="right", anchor="se", padx=10, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verificar las credenciales
        if username in self.users and self.users[username] == password:
            self.master.destroy()
        else:
            # Mostrar mensaje de error con fondo rosado
            error_message = "Credenciales inválidas. No se permite el acceso al sistema."
            error_title = "Error de inicio de sesión"

            # Configurar el color de fondo de la ventana de error
            error_window = tk.Toplevel(self.master)
            error_window.title(error_title)
            error_window.configure(bg="#FFDAB9")  # Color de fondo rosado claro
            tk.Label(error_window, text=error_message, bg="#ff9999", fg="black").pack(padx=10, pady=10)

    def create_new_user(self):
        # Crear una nueva ventana para ingresar los detalles del nuevo usuario
        new_user_window = tk.Toplevel(self.master)
        new_user_window.title("Nuevo Usuario")

        # Etiquetas y cuadros de texto para ingresar los detalles del nuevo usuario
        label_new_username = tk.Label(new_user_window, text="Nuevo Usuario:")
        label_new_username.pack(pady=5)
        entry_new_username = tk.Entry(new_user_window)
        entry_new_username.pack(pady=5)

        label_new_password = tk.Label(new_user_window, text="Nueva Contraseña:")
        label_new_password.pack(pady=5)
        entry_new_password = tk.Entry(new_user_window, show="*")
        entry_new_password.pack(pady=5)

        # Botón para confirmar la creación del nuevo usuario
        btn_confirm = tk.Button(new_user_window, text="Confirmar", command=lambda: self.add_new_user(entry_new_username.get(), entry_new_password.get(), new_user_window))
        btn_confirm.pack(pady=10)

    def add_new_user(self, username, password, window):
        # Verificar si el usuario ya existe
        if username in self.users:
            messagebox.showerror("Error", "El usuario ya existe.")
        else:
            # Agregar el nuevo usuario al diccionario
            self.users[username] = password
            messagebox.showinfo("Nuevo Usuario", "Usuario creado con éxito.")
            window.destroy()

    def restore_password(self):
        messagebox.showinfo("Restaurar Contraseña", "Funcionalidad para restaurar contraseña aún no implementada.")

if __name__ == "__main__":
    root_login = tk.Tk()
    login_window = LoginWindow(root_login)
    root_login.mainloop()
class InterfazIngredientes:
    def __init__(self, master):
        self.master = master
        self.master.title("Mercedario Recetas")

        # Configurar el frame principal
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=1, fill="both")

        # Cambiar el color de fondo directamente
        self.frame.configure(bg="#4B0082")  # Morado oscuro

        # Crear el widget de pestañas
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(expand=1, fill="both")

        # Pestaña de Ingredientes
        self.pestana_ingredientes = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_ingredientes, text="Ingredientes")

        self.ingredientes = []
        self.crear_interfaz_ingredientes()

        # Pestaña de Recetas
        self.pestana_recetas = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_recetas, text="Recetas")

        self.recetas = []
        self.crear_interfaz_recetas() 

    def crear_interfaz_recetas(self):
        # Crear y configurar la tabla para mostrar las recetas
        self.tabla_recetas = ttk.Treeview(self.pestana_recetas, columns=(
            "ID", "Nombre", "Tiempo de Preparación", "Número de Personas", "Descripción"))
        self.tabla_recetas.heading("#0", text="ID")
        self.tabla_recetas.heading("Nombre", text="Nombre")
        self.tabla_recetas.heading("Tiempo de Preparación", text="Tiempo de Preparación")
        self.tabla_recetas.heading("Número de Personas", text="Número de Personas")
        self.tabla_recetas.heading("Descripción", text="Descripción")
        self.tabla_recetas.pack(padx=10, pady=10)

        # Botones para recetas
        self.btn_agregar_receta = tk.Button(self.pestana_recetas, text="Agregar Receta", command=self.agregar_receta)
        self.btn_agregar_receta.pack(pady=5)
        self.btn_eliminar_receta = tk.Button(self.pestana_recetas, text="Eliminar Receta", command=self.eliminar_receta)
        self.btn_eliminar_receta.pack(pady=5)
        self.btn_editar_receta = tk.Button(self.pestana_recetas, text="Editar Receta", command=self.editar_receta)
        self.btn_editar_receta.pack(pady=5)
        self.btn_cocinar_receta = tk.Button(self.pestana_recetas, text="Cocinar Receta", command=self.cocinar_receta)
        self.btn_cocinar_receta.pack(pady=5)

        self.actualizar_tabla_recetas()

    def crear_interfaz_ingredientes(self):

        # Crear y configurar la tabla para mostrar los ingredientes
        self.tabla = ttk.Treeview(self.master, columns=(
        "ID", "Nombre", "Unidad", "Valor Unidad", "Sitio de Compra", "Calorías Unidad"))
        self.tabla.heading("#0", text="ID", anchor="center")
        self.tabla.heading("Nombre", text="Nombre", anchor="center")
        self.tabla.heading("Unidad", text="Unidad", anchor="center")
        self.tabla.heading("Valor Unidad", text="Valor Unidad", anchor="center")
        self.tabla.heading("Sitio de Compra", text="Sitio de Compra", anchor="center")
        self.tabla.heading("Calorías Unidad", text="Calorías Unidad", anchor="center")
        self.tabla.pack(padx=10, pady=10)

        # Botones para acciones
        self.btn_agregar = tk.Button(self.master, text="Agregar Ingrediente", command=self.agregar_ingrediente)
        self.btn_agregar.pack(pady=5)
        self.btn_eliminar = tk.Button(self.master, text="Eliminar Ingrediente", command=self.eliminar_ingrediente)
        self.btn_eliminar.pack(pady=5)
        self.btn_editar = tk.Button(self.master, text="Editar Ingrediente", command=self.editar_ingrediente)
        self.btn_editar.pack(pady=5)
        self.btn_actualizar = tk.Button(self.master, text="Actualizar Lista", command=self.actualizar_tabla)
        self.btn_actualizar.pack(pady=5)

        # Llenar la tabla con datos iniciales
        self.actualizar_tabla()

    def cocinar_receta(self):
        # Obtener el índice seleccionado en la tabla de recetas
        seleccion = self.tabla_recetas.selection()

        if seleccion:
            # Obtener el índice de la primera columna (ID)
            idx = int(self.tabla_recetas.item(seleccion)['values'][0])

            # Obtener la receta correspondiente
            if 0 < idx <= len(self.recetas):
                receta = self.recetas[idx - 1]

                # Verificar si los ingredientes de la receta están en la lista de ingredientes
                ingredientes_faltantes = [ingrediente for ingrediente in receta.lista_ingredientes if ingrediente not in self.ingredientes]

                if not ingredientes_faltantes:
                    # Si no hay ingredientes faltantes, mostrar una alerta
                    messagebox.showinfo("Cocinar Receta", f"¡Se cocinó con éxito la receta '{receta.nombre_receta}'!")
                else:
                    # Si hay ingredientes faltantes, mostrar una alerta indicando cuáles faltan
                    ingredientes_faltantes_nombres = [ingrediente.get_nombre() for ingrediente in ingredientes_faltantes]
                    messagebox.showwarning("Ingredientes Faltantes", f"No se puede cocinar la receta '{receta.nombre_receta}'. Faltan los siguientes ingredientes: {', '.join(ingredientes_faltantes_nombres)}")
    def agregar_ingrediente(self):
        # Solicitar al usuario que ingrese los detalles del nuevo ingrediente
        nombre = simpledialog.askstring("Agregar Ingrediente", "Nombre del ingrediente:")
        unidad = simpledialog.askstring("Agregar Ingrediente", "Unidad del ingrediente:")
        valor_unidad = simpledialog.askfloat("Agregar Ingrediente", "Valor por unidad:")
        sitio_compra = simpledialog.askstring("Agregar Ingrediente", "Sitio de compra:")
        calorias_unidad = simpledialog.askfloat("Agregar Ingrediente", "Calorías por unidad:")

        # Crear un nuevo objeto Ingrediente con los datos ingresados
        nuevo_ingrediente = Ingrediente(nombre, unidad, valor_unidad, sitio_compra, calorias_unidad)

        # Agregar el nuevo ingrediente a la lista
        self.ingredientes.append(nuevo_ingrediente)

        # Actualizar la tabla con los datos actualizados
        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Borrar todos los elementos de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar los datos actualizados en la tabla
        for idx, ingrediente in enumerate(self.ingredientes, start=1):
            self.tabla.insert("", "end", values=(
            idx, ingrediente.nombre, ingrediente.unidad, ingrediente.valor_unidad, ingrediente.sitio_compra,
            ingrediente.calorias_unidad))

    def eliminar_ingrediente(self):
        # Obtener el índice seleccionado en la tabla
        seleccion = self.tabla.selection()

        if seleccion:
            # Obtener el índice de la primera columna (ID)
            idx = int(self.tabla.item(seleccion)['values'][0])

            # Eliminar el ingrediente de la lista
            if 0 < idx <= len(self.ingredientes):
                del self.ingredientes[idx - 1]

                # Actualizar la tabla con los datos actualizados
                self.actualizar_tabla()

    def editar_ingrediente(self):
        # Obtener el índice seleccionado en la tabla
        seleccion = self.tabla.selection()

        if seleccion:
            # Obtener el índice de la primera columna (ID)
            idx = int(self.tabla.item(seleccion)['values'][0])

            # Obtener el ingrediente correspondiente
            if 0 < idx <= len(self.ingredientes):
                ingrediente = self.ingredientes[idx - 1]

                # Solicitar al usuario que ingrese los nuevos detalles del ingrediente
                nuevo_nombre = simpledialog.askstring("Editar Ingrediente", "Nuevo nombre del ingrediente:",
                                                      initialvalue=ingrediente.nombre)
                nuevo_unidad = simpledialog.askstring("Editar Ingrediente", "Nueva unidad del ingrediente:",
                                                      initialvalue=ingrediente.unidad)
                nuevo_valor_unidad = simpledialog.askfloat("Editar Ingrediente", "Nuevo valor por unidad:",
                                                           initialvalue=ingrediente.valor_unidad)
                nuevo_sitio_compra = simpledialog.askstring("Editar Ingrediente", "Nuevo sitio de compra:",
                                                            initialvalue=ingrediente.sitio_compra)
                nuevo_calorias_unidad = simpledialog.askfloat("Editar Ingrediente", "Nuevas calorías por unidad:",
                                                              initialvalue=ingrediente.calorias_unidad)

                # Actualizar los detalles del ingrediente
                ingrediente.set_nombre(nuevo_nombre)
                ingrediente.set_unidad(nuevo_unidad)
                ingrediente.set_valor_unidad(nuevo_valor_unidad)
                ingrediente.set_sitio_compra(nuevo_sitio_compra)
                ingrediente.set_calorias_unidad(nuevo_calorias_unidad)

                # Actualizar la tabla con los datos actualizados
                self.actualizar_tabla()

    def agregar_receta(self):
        # Solicitar al usuario que ingrese los detalles de la nueva receta
        nombre_receta = simpledialog.askstring("Agregar Receta", "Nombre de la receta:")
        tiempo_preparacion = simpledialog.askinteger("Agregar Receta", "Tiempo de preparación (minutos):")
        numero_personas = simpledialog.askinteger("Agregar Receta", "Número de personas:")

        # Llamar a la función para seleccionar ingredientes
        ingredientes_seleccionados = self.seleccionar_ingredientes()

        # Verificar si la selección de ingredientes fue cancelada (lista vacía)
        if not ingredientes_seleccionados:
            return

        # Crear un nuevo objeto Receta con los datos ingresados
        nueva_receta = Receta(nombre_receta, tiempo_preparacion, numero_personas, ingredientes_seleccionados, "")

        # Agregar la nueva receta a la lista
        self.recetas.append(nueva_receta)

        # Actualizar la tabla de recetas con los datos actualizados
        self.actualizar_tabla_recetas()

    def seleccionar_ingredientes(self):
        # Esta función maneja la selección de ingredientes para una receta
        ingredientes_seleccionados = []
        for i in range(3):
            # Solicitar al usuario que seleccione un ingrediente
            ingrediente = simpledialog.askstring("Seleccionar Ingrediente", f"Ingrediente {i + 1}:", initialvalue="")
            if ingrediente:
                # Buscar el ingrediente en la lista de ingredientes
                ingrediente_encontrado = next((ing for ing in self.ingredientes if ing.get_nombre() == ingrediente),
                                              None)
                if ingrediente_encontrado:
                    ingredientes_seleccionados.append(ingrediente_encontrado)
                else:
                    # Mostrar un mensaje de advertencia si el ingrediente no se encuentra
                    messagebox.showwarning("Ingrediente no encontrado",
                                           f"Ingrediente '{ingrediente}' no encontrado. Intente de nuevo.")
                    return []  # Devolver una lista vacía para cancelar la operación
        return ingredientes_seleccionados

    def eliminar_receta(self):
        # Obtener el índice seleccionado en la tabla de recetas
        seleccion = self.tabla_recetas.selection()

        if seleccion:
            # Obtener el índice de la primera columna (ID)
            idx = int(self.tabla_recetas.item(seleccion)['values'][0])

            # Eliminar la receta de la lista
            if 0 < idx <= len(self.recetas):
                del self.recetas[idx - 1]

                # Actualizar la tabla de recetas con los datos actualizados
                self.actualizar_tabla_recetas()

    def editar_receta(self):
        # Obtener el índice seleccionado en la tabla de recetas
        seleccion = self.tabla_recetas.selection()

        if seleccion:
            # Obtener el índice de la primera columna (ID)
            idx = int(self.tabla_recetas.item(seleccion)['values'][0])

            # Obtener la receta correspondiente
            if 0 < idx <= len(self.recetas):
                receta = self.recetas[idx - 1]

                # Solicitar al usuario que ingrese los nuevos detalles de la receta
                nuevo_nombre = simpledialog.askstring("Editar Receta", "Nuevo nombre de la receta:",
                                                      initialvalue=receta.nombre_receta)
                nuevo_tiempo_preparacion = simpledialog.askinteger("Editar Receta",
                                                                  "Nuevo tiempo de preparación (minutos):",
                                                                  initialvalue=receta.tiempo_preparacion)
                nuevo_numero_personas = simpledialog.askinteger("Editar Receta", "Nuevo número de personas:",
                                                               initialvalue=receta.numero_personas)
                nueva_descripcion = simpledialog.askstring("Editar Receta", "Nueva descripción de la receta:",
                                                           initialvalue=receta.descripcion)

                # Actualizar los detalles de la receta
                receta.set_nombre_receta(nuevo_nombre)
                receta.set_tiempo_preparacion(nuevo_tiempo_preparacion)
                receta.set_numero_personas(nuevo_numero_personas)
                receta.set_descripcion(nueva_descripcion)

                # Actualizar la tabla de recetas con los datos actualizados
                self.actualizar_tabla_recetas()

    def actualizar_tabla_recetas(self):
        # Código de la función actualizar_tabla_recetas
        # Actualiza la tabla de recetas con los datos actualizados
        for item in self.tabla_recetas.get_children():
            self.tabla_recetas.delete(item)

        for idx, receta in enumerate(self.recetas, start=1):
            ingredientes = ', '.join(ingrediente.get_nombre() for ingrediente in receta.lista_ingredientes)
            self.tabla_recetas.insert("", "end", values=(
                idx, receta.nombre_receta, receta.tiempo_preparacion, receta.numero_personas, ingredientes, receta.descripcion))



if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazIngredientes(root)
    root.mainloop()