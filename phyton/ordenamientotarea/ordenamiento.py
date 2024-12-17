import tkinter as tk
from tkinter import messagebox
import time

# Función de ordenamiento (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Función principal que se llama al presionar el botón de ordenar
def ordenar_lista():
    try:
        # Obtener la lista de números del usuario
        nums = list(map(int, entry_nums.get().split(',')))

        if len(nums) > 40:
            messagebox.showerror("Error", "La lista debe tener máximo 40 números.")
            return

        # Mostrar la lista original
        original_list_label.config(text=f"Lista Original: {nums}")

        # Ordenar usando el algoritmo Bubble Sort
        start_time = time.time()
        sorted_list = bubble_sort(nums.copy())
        end_time = time.time()

        # Calcular el tiempo de ejecución
        time_taken = end_time - start_time

        # Mostrar la lista ordenada y el tiempo de ejecución
        sorted_list_label.config(text=f"Lista Ordenada: {sorted_list}")
        time_label.config(text=f"Tiempo de Ejecución: {time_taken:.6f} segundos")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números separados por coma.")

# Configuración de la interfaz gráfica con tkinter
root = tk.Tk()
root.title("Ordenador de Listas - Bubble Sort")

# Etiquetas e interfaz
label_instructions = tk.Label(root, text="Ingresa una lista de hasta 40 números, separados por coma:")
label_instructions.pack(pady=10)

entry_nums = tk.Entry(root, width=50)
entry_nums.pack(pady=10)

# Botón para ordenar
button_ordenar = tk.Button(root, text="Ordenar Lista", command=ordenar_lista)
button_ordenar.pack(pady=20)

# Etiquetas para mostrar los resultados
original_list_label = tk.Label(root, text="Lista Original: ")
original_list_label.pack(pady=10)

sorted_list_label = tk.Label(root, text="Lista Ordenada: ")
sorted_list_label.pack(pady=10)

time_label = tk.Label(root, text="Tiempo de Ejecución: ")
time_label.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
