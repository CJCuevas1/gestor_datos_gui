# app_gui_basica.py

import tkinter as tk
from tkinter import messagebox

class AppGUIBasica(tk.Tk):
    def __init__(self):
        super().__init__()
        # Se definen las propiedades iniciales de la ventana
        self.title("Gestor de Datos - GUI Mejorada")
        self.geometry("480x360")
        self.resizable(False, False)

        # Se define la paleta de colores para la interfaz
        self.color_fondo = "#D9EFF7"
        self.color_acento_claro = "#9BBBFB"
        self.color_texto_principal = "#4741A6"
        self.color_acento_amarillo = "#F9CE69"
        
        # Se aplica el color de fondo a toda la ventana
        self.config(bg=self.color_fondo)

        # Se crea y posiciona la etiqueta del título principal
        lbl_titulo = tk.Label(
            self, 
            text="Ingrese un dato y agréguelo a la lista", 
            font=("Segoe UI", 12, "bold"),
            bg=self.color_fondo,
            fg=self.color_texto_principal
        )
        lbl_titulo.grid(row=0, column=0, columnspan=3, pady=(12, 6), padx=12, sticky="w")

        # Se crea la etiqueta para el campo de entrada de datos
        tk.Label(
            self, text="Dato:", 
            bg=self.color_fondo, 
            fg=self.color_texto_principal
        ).grid(row=1, column=0, padx=(12, 6), pady=6, sticky="e")
        
        # Se configura el campo de texto donde el usuario ingresará los datos
        self.var_texto = tk.StringVar()
        self.entry = tk.Entry(
            self, 
            textvariable=self.var_texto, 
            width=36,
            bg="white",
            fg=self.color_texto_principal,
            relief="flat"
        )
        self.entry.grid(row=1, column=1, padx=6, pady=6, sticky="we")
        self.entry.focus()

        # Se crea el botón para agregar un nuevo elemento a la lista
        btn_agregar = tk.Button(
            self, 
            text="Agregar", 
            width=12, 
            command=self.agregar,
            bg=self.color_texto_principal,
            fg="white",
            activebackground=self.color_acento_claro,
            activeforeground=self.color_texto_principal,
            relief="flat",
            borderwidth=0
        )
        btn_agregar.grid(row=1, column=2, padx=(6, 12), pady=6)

        # Se crea el botón para limpiar el campo de texto y la selección
        btn_limpiar = tk.Button(
            self, 
            text="Limpiar", 
            width=12, 
            command=self.limpiar,
            bg=self.color_acento_amarillo,
            fg=self.color_texto_principal,
            activebackground=self.color_acento_claro,
            activeforeground=self.color_texto_principal,
            relief="flat",
            borderwidth=0
        )
        btn_limpiar.grid(row=2, column=2, padx=(6, 12), pady=(0, 6))

        # Se crea la etiqueta para la lista de datos
        tk.Label(
            self, text="Lista de datos:", 
            bg=self.color_fondo, 
            fg=self.color_texto_principal
        ).grid(row=2, column=0, columnspan=2, padx=12, sticky="w")

        # Se crea un marco para organizar la lista y la barra de desplazamiento
        frame_lista = tk.Frame(self, bg=self.color_fondo)
        frame_lista.grid(row=3, column=0, columnspan=3, padx=12, pady=6, sticky="nsew")

        # Se crea la lista donde se mostrarán los datos ingresados
        self.listbox = tk.Listbox(
            frame_lista, 
            height=10, 
            selectmode=tk.EXTENDED,
            bg="white",
            fg=self.color_texto_principal,
            selectbackground=self.color_acento_claro,
            selectforeground="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        # Se añade una barra de desplazamiento vertical a la lista
        scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Se configura la columna central para que se expanda si la ventana cambia de tamaño
        self.grid_columnconfigure(1, weight=1)

        # Se asocian eventos del teclado a funciones específicas
        self.entry.bind("<Return>", lambda e: self.agregar())
        self.listbox.bind("<Delete>", lambda e: self.eliminar_seleccion())

    # Se plantea la función para agregar el texto del campo de entrada a la lista
    def agregar(self):
        texto = self.var_texto.get().strip()
        if not texto:
            messagebox.showinfo("Atención", "Ingrese un dato antes de agregar.")
            return
        self.listbox.insert(tk.END, texto)
        self.var_texto.set("")
        self.entry.focus()

    # Se plantea la función para eliminar los elementos seleccionados de la lista
    def eliminar_seleccion(self):
        seleccion = list(self.listbox.curselection())
        for idx in reversed(seleccion):
            self.listbox.delete(idx)

    # Se plantea la función para limpiar el campo de texto y la selección de la lista
    def limpiar(self):
        self.var_texto.set("")
        self.eliminar_seleccion()

# Se asegura que la aplicación solo se ejecute cuando el script es el archivo principal
if __name__ == "__main__":
    AppGUIBasica().mainloop()