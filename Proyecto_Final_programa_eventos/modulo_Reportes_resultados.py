# modulo_Reportes_resultados.py
import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
import mss

fecha = datetime.now().strftime("%Y-%m-%d")

def capturar_pantalla(archivo="captura.png"):
    with mss.mss() as sct:
        sct.shot(output=archivo)

def obtener_precios():
    return {
        "Staff": 1000,
        "Equipo técnico": 800,
        "Mobiliario": 5300,
        "Entretenimiento": 500,
        "Catering": 3200
    }

def obtener_factor(capacidad_seleccionada):
    if capacidad_seleccionada == 200:
        return 1.0
    elif capacidad_seleccionada == 100:
        return 0.5
    elif capacidad_seleccionada == 50:
        return 0.25
    else:
        return 1.0

def calcular_presupuesto(variables_recursos, recursos, capacidad_seleccionada):
    precios = obtener_precios()
    factor = obtener_factor(capacidad_seleccionada)
    total = 0
    for i, var in enumerate(variables_recursos):
        if var.get():
            recurso = recursos[i]
            total += precios[recurso]
    return total * factor

def factura_pdf(
    nombre, telefono, direccion,
    total_presupuesto, recursos, variables_recursos, capacidad_seleccionada,
    archivo="factura.pdf"
):
    c = canvas.Canvas(archivo, pagesize=A4)
    ancho, alto = A4

    x_margen = 30 * mm
    y = alto - 30 * mm

    def datos_factura(texto, tamaño=14, negrita=False, y_espacio=18):
        nonlocal y
        if negrita:
            c.setFont("Helvetica-Bold", tamaño)
        else:
            c.setFont("Helvetica", tamaño)
        c.drawString(x_margen, y, texto)
        y -= y_espacio
    factor = obtener_factor(capacidad_seleccionada)
    precios = obtener_precios()
    datos_factura("                               Event Manage", tamaño=20, negrita=True, y_espacio=24)
    datos_factura("                                   Optimiza con propósito, impacta con pasión", tamaño=12, negrita=False, y_espacio=24)
    datos_factura(f"Nombre: {nombre}", tamaño=12)
    datos_factura(f"Teléfono: {telefono}", tamaño=12)
    datos_factura(f"Dirección: {direccion}", tamaño=12)
    datos_factura(f"Fecha: {fecha}", tamaño=12)
    datos_factura("", y_espacio=12)
    datos_factura("Detalle de servicios", tamaño=14, negrita=True, y_espacio=20)
    for i, var in enumerate(variables_recursos):
        if var.get():
            recurso = recursos[i]
            costo = precios[recurso] * factor
            c.setFont("Helvetica", 12)
            c.drawString(x_margen, y, recurso)
            c.drawRightString(ancho - x_margen, y, f"${costo:.2f}")
            y -= 16

    y -= 10

    iva = total_presupuesto * 0.15
    total_con_iva = total_presupuesto + iva

    c.setFont("Helvetica", 12)
    c.drawRightString(ancho - x_margen, y, f"Subtotal: ${total_presupuesto:.2f}")
    y -= 16
    c.drawRightString(ancho - x_margen, y, f"IVA (15%): ${iva:.2f}")
    y -= 16
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(ancho - x_margen, y, f"Total: ${total_con_iva:.2f}")

    c.save()

def factura_de_captura(nombre_pdf="factura_visual.pdf", nombre_captura="captura_factura.png"):
    # Captura la pantalla completa (ajusta si quieres capturar sólo la ventana)
    capturar_pantalla(nombre_captura)
    c = canvas.Canvas(nombre_pdf, pagesize=A4)
    imagen = ImageReader(nombre_captura)
    c.drawImage(imagen, 50, 200, width=500, preserveAspectRatio=True)
    c.save()
    # Elimina la imagen temporal
    if os.path.exists(nombre_captura):
        os.remove(nombre_captura)

def nombre_factura():
    ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
    home = os.path.expanduser("~")
    nombre_pdf = f"factura_{ahora}.pdf"
    ruta_completa = os.path.join(home, nombre_pdf)
    return ruta_completa

def mostrar_factura(nombre, telefono, direccion, total_presupuesto, recursos, variables_recursos, capacidad_seleccionada, ventana_eventos):
    factor = obtener_factor(capacidad_seleccionada)
    factura = tk.Toplevel(ventana_eventos)
    factura.title("Factura")
    factura.geometry("500x600")
    factura.config(bg="white")
    tk.Label(factura, text="Event Manage", font=("Arial", 20, "bold"), bg="white").pack(pady=10)
    tk.Label(factura, text="Optimiza con propósito, impacta con pasión", font=("Arial", 12), bg="white").pack(pady=5)
    tk.Label(factura, text=f"Nombre: {nombre}", bg="white", anchor="w").pack(fill="x", padx=20, pady=2)
    tk.Label(factura, text=f"Teléfono: {telefono}", bg="white", anchor="w").pack(fill="x", padx=20, pady=2)
    tk.Label(factura, text=f"Dirección: {direccion}", bg="white", anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Fecha actual dinámicamente al abrir la ventana
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    tk.Label(factura, text=f"Fecha: {fecha_actual}", bg="white", anchor="w").pack(fill="x", padx=20, pady=2)
    tk.Label(factura, text="Detalle de servicios", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
    frame_detalle = tk.Frame(factura, bg="white")
    frame_detalle.pack()
    precios = obtener_precios()
    row = 0
    for i, var in enumerate(variables_recursos):
        if var.get():
            recurso = recursos[i]
            costo = precios[recurso] * factor
            tk.Label(frame_detalle, text=recurso, bg="white", anchor="w", width=25).grid(row=row, column=0, sticky="w", padx=10)
            tk.Label(frame_detalle, text=f"${costo:.2f}", bg="white", anchor="e", width=10).grid(row=row, column=1, sticky="e", padx=10)
            row += 1
    iva = total_presupuesto * 0.15
    total_con_iva = total_presupuesto + iva
    tk.Label(factura, text=f"Subtotal: ${total_presupuesto:.2f}", bg="white", anchor="e").pack(fill="x", padx=20, pady=5)
    tk.Label(factura, text=f"IVA (15%): ${iva:.2f}", bg="white", anchor="e").pack(fill="x", padx=20, pady=5)
    tk.Label(factura, text=f"Total: ${total_con_iva:.2f}", font=("Arial", 12, "bold"), bg="white", anchor="e").pack(fill="x", padx=20, pady=10)

    def guardar():
        nombre_pdf = nombre_factura()
        factura_pdf(nombre, telefono, direccion, total_presupuesto, recursos, variables_recursos, capacidad_seleccionada, archivo=nombre_pdf)
        messagebox.showinfo("PDF generado", f"Factura guardada como:\n{nombre_pdf}")
    imprimir = tk.Button(factura, text="Imprimir", font=("monotype corsiva", 14), command=guardar)
    imprimir.place(relx=0.8, rely=0.9, anchor="center")
