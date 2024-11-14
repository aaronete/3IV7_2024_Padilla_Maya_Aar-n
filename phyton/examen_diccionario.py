import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# Lista de armas
armas = []

# Función para registrar un arma
def registrar_arma():
    nombre = simpledialog.askstring("Nombre", "Ingresa el nombre del arma:")
    calidad = simpledialog.askstring("Calidad", "Ingresa la calidad del arma:")
    dano = simpledialog.askfloat("Daño", "Ingresa el daño del arma:")
    cadencia = simpledialog.askfloat("Cadencia", "Ingresa la cadencia del arma:")
    capacidad_de_carga = simpledialog.askfloat("Capacidad", "Ingresa la capacidad de carga del arma:")
    tiempo_de_recarga = simpledialog.askfloat("Tiempo de Recarga", "Ingresa el tiempo de recarga del arma:")
    alcance = simpledialog.askfloat("Alcance", "Cuánto alcance tiene el arma:")
    municion = simpledialog.askstring("Munición", "Qué tipo de munición usa:")

    # Diccionario del arma
    arma = {
        "nombre": nombre,
        "calidad": calidad,
        "dano": dano,
        "cadencia": cadencia,
        "capacidad_de_carga": capacidad_de_carga,
        "tiempo_de_recarga": tiempo_de_recarga,
        "alcance": alcance,
        "municion": municion
    }

    # Añadir el arma a la lista (solo en memoria)
    armas.append(arma)

    # Guardar el arma en el archivo
    try:
        with open("armaslista.txt", "a") as file:
            file.write(f"{nombre},{calidad},{dano},{cadencia},{capacidad_de_carga},{tiempo_de_recarga},{alcance},{municion}\n")
        messagebox.showinfo("Éxito", "El arma se registró exitosamente")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al guardar el arma: {e}")

# Función para consultar las armas desde el archivo
def consultar_armas():
    archivo = "armaslista.txt"
    
    if not os.path.exists(archivo):
        messagebox.showinfo("No hay registros", "No se encontró el archivo de armas. Asegúrate de registrar al menos un arma primero.")
        return
    
    try:
        # Leer todas las armas desde el archivo
        with open(archivo, "r") as file:
            armas_en_archivo = file.readlines()

        if not armas_en_archivo:
            messagebox.showinfo("No hay registros", "No hay armas registradas en el archivo.")
        else:
            lista_armas = ""
            for arma in armas_en_archivo:
                # Leer la línea y separar los datos por comas
                datos = arma.strip().split(',')
                lista_armas += f"Nombre: {datos[0]}, Calidad: {datos[1]}, Daño: {datos[2]}, Cadencia: {datos[3]}, Capacidad: {datos[4]}, Tiempo de recarga: {datos[5]}, Alcance: {datos[6]}, Munición: {datos[7]}\n"
            messagebox.showinfo("Lista de Armas", lista_armas)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al leer el archivo: {e}")

# Función para editar un arma
def editar_arma():
    nombre = simpledialog.askstring("Editar Arma", "Ingresa el nombre del arma que deseas editar:")
    for arma in armas:
        if arma['nombre'] == nombre:
            arma['calidad'] = simpledialog.askstring("Calidad", "Ingresa la nueva calidad o presiona Enter para mantener el actual:", initialvalue=arma['calidad']) or arma['calidad']
            arma['dano'] = simpledialog.askstring("Daño", "Ingresa el nuevo daño o presiona Enter para mantener el actual:", initialvalue=arma['dano']) or arma['dano']
            arma['cadencia'] = simpledialog.askstring("Cadencia", "Ingresa la nueva cadencia o presiona Enter para mantener el actual:", initialvalue=arma['cadencia']) or arma['cadencia']
            arma['capacidad_de_carga'] = simpledialog.askstring("Capacidad", "Ingresa la nueva capacidad o presiona Enter para mantener el actual:", initialvalue=arma['capacidad_de_carga']) or arma['capacidad_de_carga']
            arma['tiempo_de_recarga'] = simpledialog.askstring("Tiempo de Recarga", "Ingresa el nuevo tiempo de recarga o presiona Enter para mantener el actual:", initialvalue=arma['tiempo_de_recarga']) or arma['tiempo_de_recarga']
            arma['alcance'] = simpledialog.askfloat("Alcance", "Ingresa el nuevo alcance o presiona Enter para mantener el actual:", initialvalue=arma['alcance']) or arma['alcance']
            arma['municion'] = simpledialog.askstring("Munición", "Ingresa el nuevo tipo de munición o presiona Enter para mantener el actual:", initialvalue=arma['municion']) or arma['municion']
            
            messagebox.showinfo("Éxito", "El arma fue editada exitosamente.")
            return
    messagebox.showerror("Error", "No se encontró el arma.")

# Función para eliminar un arma
def eliminar_arma():
    nombre = simpledialog.askstring("Eliminar Arma", "Ingresa el nombre del arma que deseas eliminar:")
    global armas
    armas = [arma for arma in armas if arma['nombre'] != nombre]
    messagebox.showinfo("Éxito", "El arma fue eliminada exitosamente.")

# Función para crear la ventana principal con los botones
def crear_ventana_principal():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Armas")

    # Establecer tamaño de la ventana
    root.geometry("400x300")

    # Crear un frame para organizar los botones
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Funciones asociadas a los botones
    def on_registrar():
        registrar_arma()

    def on_consultar():
        consultar_armas()

    def on_editar():
        editar_arma()

    def on_eliminar():
        eliminar_arma()

    # Botones en forma de tabla con color azul
    btn_registrar = tk.Button(frame, text="Registrar Arma", width=20, bg="blue", fg="white", command=on_registrar)
    btn_registrar.grid(row=0, column=0, pady=5)

    btn_consultar = tk.Button(frame, text="Consultar Armas", width=20, bg="blue", fg="white", command=on_consultar)
    btn_consultar.grid(row=1, column=0, pady=5)

    btn_editar = tk.Button(frame, text="Editar Arma", width=20, bg="blue", fg="white", command=on_editar)
    btn_editar.grid(row=2, column=0, pady=5)

    btn_eliminar = tk.Button(frame, text="Eliminar Arma", width=20, bg="blue", fg="white", command=on_eliminar)
    btn_eliminar.grid(row=3, column=0, pady=5)

    # Salir de la aplicación
    btn_salir = tk.Button(root, text="Salir", bg="red", fg="white", command=root.quit)
    btn_salir.pack(pady=10)

    # Ejecutar la ventana
    root.mainloop()

# Iniciar la aplicación
if __name__ == "__main__":
    crear_ventana_principal()
