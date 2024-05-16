import tkinter as tk
import os
import subprocess
from tkinter import filedialog, ttk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PUICA")

        self.center_window(750, 550)  # Establece el tamaño de la ventana (ancho, alto)

        # Crear estilo
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Estilo personalizado para los botones
        self.style.configure(
            'Custom.TButton',
            font=('Trebuchet MS', 12, 'italic'),
            foreground='white',
            background='#007BFF',
            borderwidth=1,
            focusthickness=3,
            focuscolor='none'
        )
        self.style.map(
            'Custom.TButton',
            foreground=[('active', 'white'), ('disabled', 'gray')],
            background=[('active', '#0056b3'), ('disabled', '#007BFF')]
        )

        # Marco principal
        self.main_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Etiqueta para selección de archivo
        self.label_file = ttk.Label(self.main_frame, text="Selecciona una prueba", foreground='black')
        self.label_file.grid(row=0, column=0, pady=10, sticky='e')

        # Botón para seleccionar archivo
        self.btn_browse = ttk.Button(self.main_frame, text="Subir archivo", command=self.browse_file, style='Custom.TButton')
        self.btn_browse.grid(row=0, column=1, pady=10, padx=5, sticky='w')

        # Etiqueta para datos de entrada
        self.label_input = ttk.Label(self.main_frame, text="Datos de entrada", foreground='black', anchor='center')
        self.label_input.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

        # Botón para resolver
        self.btn_solve = ttk.Button(self.main_frame, text="Resolver", style='Custom.TButton')
        self.btn_solve.grid(row=2, column=0, pady=10, columnspan=2)

        # Cuadro de texto para entrada
        self.textbox = tk.Text(self.main_frame, height=10, width=60, foreground='black')
        self.textbox.grid(row=3, column=0, columnspan=2, pady=10, sticky='nsew')

        # Barra de desplazamiento vertical para el cuadro de texto
        scrollbar = ttk.Scrollbar(self.main_frame, command=self.textbox.yview)
        scrollbar.grid(row=3, column=2, sticky=(tk.N, tk.S))
        self.textbox.config(yscrollcommand=scrollbar.set)

        # Etiqueta para resultados
        self.label_result = ttk.Label(self.main_frame, text="Resultados pruebas:", foreground='black')
        self.label_result.grid(row=4, column=0, columnspan=2, pady=10)

        # Cuadro de texto para resultados
        self.result_textbox = tk.Text(self.main_frame, height=10, width=60, foreground='black')
        self.result_textbox.grid(row=5, column=0, columnspan=2, pady=10, sticky='nsew')

        # Barra de desplazamiento vertical para el cuadro de texto de resultados
        scrollbar_result = ttk.Scrollbar(self.main_frame, command=self.result_textbox.yview)
        scrollbar_result.grid(row=5, column=2, sticky=(tk.N, tk.S))
        self.result_textbox.config(yscrollcommand=scrollbar_result.set)

        # Configurar colores y fuentes
        for label in [self.label_file, self.label_input, self.label_result]:
            label.config(font=('Helvetica', 12, 'bold'))

        self.textbox.config(font=('Courier', 10))
        self.result_textbox.config(font=('Courier', 10))

        # Configurar expansión de filas y columnas
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(3, weight=1)
        self.main_frame.rowconfigure(5, weight=1)

    def center_window(self, width, height):
        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x, y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Establecer el tamaño de la ventana y la posición
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def browse_file(self):
        # Abre un cuadro de diálogo para seleccionar un archivo de texto (*.txt)
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, file.read())
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
