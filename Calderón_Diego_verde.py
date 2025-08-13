import tkinter as tk
from tkinter import messagebox

ventana= tk.Tk()
ventana.title("Vivero")
ventana.geometry("625x625")
ventana.config(bg="#9FC131")
titulo = tk.Label(ventana, text="¡Bienvenido/a a viveros", font=("monotype corsiva", 35), fg="black", bg="#9FC131")
titulo.place(relx=0.5, rely=0.05, anchor="center")

def obtener_precio():
    return {
            "Arbol frutal": 40,
            "Planta medicinal": 15,
            "Semillas de hortaliza": 8,
            "Tierra abonada": 12,
            "Fertilizante ecológico": 18,
            "Herramientas de jardinería": 25
        }

class pedido:
    def __init__(self):
        self.productos =[]
        self.total =0

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))
        self.total += precio

    def mostrar_resumen(self):
        detalle = "Resumen de productos comprados:\n"
        total=0
        for nombre, precio in self.productos: 
            detalle += f" - {nombre}: ${precio}\n"
            total += precio   
        detalle +=f"\nTotal: ${total}"
        messagebox.showinfo("Resumen",detalle)
    
recursos = ["Arbol frutal", "Planta medicinal", "Semillas de hortaliza", "Tierra abonada", "Fertilizante ecológico", "Herramientas de jardinería"]
opciones_productos = tk.Label(ventana, text="Productos disponibles:", font=("monotype corsiva", 25), fg="black", bg="#9FC131") 
opciones_productos.place(relx=0.48, rely=0.22, anchor="center")
lista_productos = []
for i, producto in enumerate(recursos):
    variable = tk.BooleanVar()
    chek_lista = tk.Checkbutton(ventana, text=producto, font=("monotype corsiva", 20),
                             variable=variable, fg="black", bg="#9FC131", anchor="w", padx=10)
    chek_lista.place(relx=0.22, rely=0.35 + i * 0.08, anchor="w")
    lista_productos.append((producto, variable))
comprar = pedido()

def agregar_productos ():
    comprar.productos.clear()
    comprar.total=0
    precios =obtener_precio()
    selecionados = [var.get() for _, var in lista_productos]
    if selecionados.count(True)==0:
        messagebox.showwarning("No ha seleccionado ningun producto","Por vafor seleccione un elemento de la lista")
        return
    for nombre, insumo in lista_productos:
        if insumo.get():
            precio= precios.get(nombre, 0)
            comprar.agregar_producto(nombre, precio)

boton_comprar=tk.Button (ventana, text="Calcular total", font=("monotype corsiva", 14),command=lambda: [agregar_productos(), comprar.mostrar_resumen()], bg="#D6D58E" )
boton_comprar.place(relx=0.5, rely=0.95, anchor="center")
ventana.mainloop()

