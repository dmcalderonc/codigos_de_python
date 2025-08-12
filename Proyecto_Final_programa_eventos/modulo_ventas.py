from modulo_Reportes_resultados import calcular_presupuesto, mostrar_factura
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



def Volver_Login():
    global ventana_ventas
    ventana_ventas.destroy()
    from modulo_seguridad import Login
    Login()


def Salir_del_programa():

    respuesta = messagebox.askquestion(
        title="¿Estás seguro/a de que quieres salir del programa?",
        message="Para finalizar presione Sí caso contrario presione No"
    )
    if respuesta == "yes":
        ventana_ventas.destroy()

def Regresar_eventos():
     ventana_eventos.destroy()
     Crear_eventos()

def Regresar_recursos():
     ventana_pago.destroy()
     Recursos_disponibles()

def Regresar_capacidad_evento():
    for i in ventana_eventos.winfo_children():
        if i != marco_evento:
            i.place_forget()
    marco_evento.place(relx=0, rely=0, anchor="nw")

    Capacidad_evento()

def seleccionar_capacidad(valor):
    global capacidad_seleccionada
    capacidad_seleccionada = valor
    Recursos_disponibles()
    
def Comprar():
    global ventana_pago
    ventana_pago = tk.Toplevel(ventana_eventos)
    ventana_pago.title("EVENT MANAGE- Gestiona tus eventos como un profesional")
    ventana_pago.geometry("400x435")
    ventana_pago.config(bg="#f1ebfe")

    tk.Label(ventana_pago, text="Por favor ingrese sus datos", font=("monotype corsiva", 18), bg="#f1ebfe").pack()
    tk.Label(ventana_pago, text="Nombre y Apellido:", font=("monotype corsiva", 16), bg="#f1ebfe").pack()
    entry_nombre = tk.Entry(ventana_pago)
    entry_nombre.pack()
    tk.Label(ventana_pago, text="Número de Tarjeta (16 dígitos):", font=("monotype corsiva", 16), bg="#f1ebfe").pack()
    entry_tarjeta = tk.Entry(ventana_pago)
    entry_tarjeta.pack()
    tk.Label(ventana_pago, text="Clave de seguridad (3 dígitos):", font=("monotype corsiva", 16), bg="#f1ebfe").pack()
    entry_clave = tk.Entry(ventana_pago, show="*")
    entry_clave.pack()
    tk.Label(ventana_pago, text="Teléfono (10 dígitos):", font=("monotype corsiva", 16), bg="#f1ebfe").pack()
    entry_telefono = tk.Entry(ventana_pago)
    entry_telefono.pack()
    tk.Label(ventana_pago, text="Dirección:", font=("monotype corsiva", 16), bg="#f1ebfe").pack()
    entry_direccion = tk.Entry(ventana_pago)
    entry_direccion.pack()

    def validar_datos():
        nombre = entry_nombre.get().strip()
        tarjeta = entry_tarjeta.get().strip()
        clave = entry_clave.get().strip()
        telefono = entry_telefono.get().strip()
        direccion = entry_direccion.get().strip()

        if not (nombre.replace(" ", "").isalpha() and
                tarjeta.isdigit() and len(tarjeta) == 16 and
                clave.isdigit() and len(clave) == 3 and
                telefono.isdigit() and len(telefono) == 10):
            messagebox.showerror("Hay un error en sus datos, por favor verifique e intente de nuevo.")
            return
        ventana_pago.destroy()
        total_presupuesto = calcular_presupuesto(variables_recursos, recursos, capacidad_seleccionada)
        mostrar_factura(nombre, telefono, direccion, total_presupuesto, recursos, variables_recursos, capacidad_seleccionada, ventana_eventos)

    tk.Button(ventana_pago, text="Confirmar compra", font=("monotype corsiva", 14), bg="#A5D3F5", command=validar_datos).pack(pady=5)
    tk.Button(ventana_pago, text="Regresar", font=("monotype corsiva", 14), bg="#A5D3F5", command=Regresar_recursos).pack(pady=5)
    tk.Button(ventana_pago, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5", command=ventana_pago.destroy).pack()

def obtener_precios():
    return {
        "Staff": 1000,
        "Equipo técnico": 800,
        "Mobiliario": 5300,
        "Entretenimiento": 500,
        "Catering": 3200
    }
    
def Presupuesto():
    total = calcular_presupuesto(variables_recursos, recursos, capacidad_seleccionada)
    messagebox.showinfo("Presupuesto estimado", f"Su presupuesto estimado es: ${int(total)} para {capacidad_seleccionada} personas. No incluye IVA")

def Recursos_disponibles():
    global variables_recursos, recursos
    variables_recursos = []  

    aforo_eventos.place_forget()
    boton_doscientos.place_forget()
    boton_regresar_eventos.place_forget()
    boton_salir_cap_eventos.place_forget()
    boton_cincuenta.place_forget()
    boton_cien.place_forget()
    recursos = ["Staff", "Equipo técnico", "Mobiliario", "Entretenimiento", "Catering"]
    recursos_eventos = tk.Label(ventana_eventos, text="Recursos y servicios disponibles:", font=("monotype corsiva", 16), fg="black", bg="#f1ebfe")
    recursos_eventos.place(relx=0.49, rely=0.29, anchor="center")

    for i, recurso in enumerate(recursos):
        var = tk.BooleanVar()
        chk = tk.Checkbutton(ventana_eventos, text=recurso, font=("monotype corsiva", 14),
                             variable=var, bg="#f1ebfe", anchor="w", padx=10)
        chk.place(relx=0.22, rely=0.35 + i * 0.08, anchor="w")
        variables_recursos.append(var)

    boton_presupuesto = tk.Button(ventana_eventos, text="Calcular presupuesto", font=("monotype corsiva", 14), bg="#A5D3F5", command=Presupuesto)
    boton_presupuesto.place(relx=0.46, rely=0.75, anchor="center")
    def Cerrar_recursos_eventos():
            respuesta = messagebox.askquestion(
                title="¿Estás seguro/a de que quieres salir del programa?",
                message="Para finalizar presione Sí caso contrario presione No"
            )
            if respuesta == "yes":
                ventana_eventos.destroy()
    boton_salir_reg_eventos=tk.Button(ventana_eventos, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5", command=Cerrar_recursos_eventos)
    boton_salir_reg_eventos.place(relx=0.8, rely=0.86, anchor="center")
    boton_comp_cap_eventos=tk.Button(ventana_eventos, text="Comprar", font=("monotype corsiva", 14), bg="#A5D3F5",command=Comprar)
    boton_comp_cap_eventos.place(relx=0.8, rely=0.66, anchor="center")
    boton_reg_cap_eventos=tk.Button(ventana_eventos, text="Regresar", font=("monotype corsiva", 14), bg="#A5D3F5",command=Regresar_capacidad_evento)
    boton_reg_cap_eventos.place(relx=0.8, rely=0.76, anchor="center")
    
def Capacidad_evento():
        global  aforo_eventos, boton_doscientos, boton_regresar_eventos, boton_salir_cap_eventos, boton_cincuenta, boton_cien
        eventos_disponibles.place_forget()
        boton_gala.place_forget()
        boton_ceremonia.place_forget()
        boton_recepción.place_forget()
        boton_exposición.place_forget()
        boton_salir_eventos.place_forget()
        aforo_eventos=tk.Label(ventana_eventos, text="Tamaño de eventos disponibles:", font=("monotype corsiva", 16), fg="black", bg="#f1ebfe")
        aforo_eventos.place(relx=0.49, rely=0.29, anchor="center")
        boton_cincuenta=tk.Button(ventana_eventos, text="50 Personas", font=("monotype corsiva", 14), bg="#A5D3F5", command=lambda: seleccionar_capacidad(50))
        boton_cincuenta.place(relx=0.5, rely=0.40, anchor="center")
        boton_cien=tk.Button(ventana_eventos, text="100 Personas", font=("monotype corsiva", 14), bg="#A5D3F5", command=lambda: seleccionar_capacidad(100))
        boton_cien.place(relx=0.5, rely=0.50, anchor="center")
        boton_doscientos=tk.Button(ventana_eventos, text="200 Personas", font=("monotype corsiva", 14), bg="#A5D3F5", command=lambda: seleccionar_capacidad(200))
        boton_doscientos.place(relx=0.5, rely=0.60, anchor="center")
        boton_regresar_eventos=tk.Button(ventana_eventos, text="Regresar", font=("monotype corsiva", 14), bg="#A5D3F5",command=Regresar_eventos)
        boton_regresar_eventos.place(relx=0.8, rely=0.76, anchor="center")
        def Cerrar_capacidad_eventos():
            respuesta = messagebox.askquestion(
                title="¿Estás seguro/a de que quieres salir del programa?",
                message="Para finalizar presione Sí caso contrario presione No"
            )
            if respuesta == "yes":
                ventana_eventos.destroy()
        boton_salir_cap_eventos=tk.Button(ventana_eventos, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5", command=Cerrar_capacidad_eventos)
        boton_salir_cap_eventos.place(relx=0.8, rely=0.86, anchor="center")

def Crear_eventos():
    global ventana_eventos, eventos_disponibles, boton_gala, boton_ceremonia, boton_recepción, boton_exposición,boton_salir_eventos, marco_evento
    ventana_eventos=tk.Toplevel()
    ventana_eventos.title("EVENT MANAGE- Gestiona tus eventos como un profesional")
    ventana_eventos.geometry("401x551")
    ventana_eventos.config(bg="#f1ebfe")
    
    marco_eventos = Image.open("bienvenida_marco.png").resize((400, 550))
    marco_eventos = ImageTk.PhotoImage(marco_eventos)
    marco_evento = tk.Label(ventana_eventos, image=marco_eventos, bg="#f1ebfe")
    marco_evento.image = marco_eventos
    marco_evento.place(relx=0, rely=0, anchor="nw")

    eventos_disponibles=tk.Label(ventana_eventos, text="Lista de eventos disponibles:", font=("monotype corsiva", 16), fg="black", bg="#f1ebfe")
    eventos_disponibles.place(relx=0.5, rely=0.26, anchor="center")
    boton_gala=tk.Button(ventana_eventos, text="Galas", font=("monotype corsiva", 14), bg="#A5D3F5", command=Capacidad_evento)
    boton_gala.place(relx=0.5, rely=0.36, anchor="center")
    boton_ceremonia=tk.Button(ventana_eventos, text="Ceremonias", font=("monotype corsiva", 14), bg="#A5D3F5", command=Capacidad_evento)
    boton_ceremonia.place(relx=0.5, rely=0.46, anchor="center")
    boton_recepción=tk.Button(ventana_eventos, text="Recepciones", font=("monotype corsiva", 14), bg="#A5D3F5", command=Capacidad_evento)
    boton_recepción.place(relx=0.5, rely=0.56, anchor="center")
    boton_exposición=tk.Button(ventana_eventos, text="Exposiciones", font=("monotype corsiva", 14), bg="#A5D3F5", command=Capacidad_evento)
    boton_exposición.place(relx=0.5, rely=0.66, anchor="center")
    def Cerrar_eventos():
        respuesta = messagebox.askquestion(
            title="¿Estás seguro/a de que quieres salir del programa?",
            message="Para finalizar presione Sí caso contrario presione No"
        )
        if respuesta == "yes":
            ventana_eventos.destroy()
    boton_salir_eventos=tk.Button(ventana_eventos, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5",command=Cerrar_eventos)
    boton_salir_eventos.place(relx=0.8, rely=0.86, anchor="center")
def ventas():
    global ventana_ventas, imagen_eventos, eventos_mosaico
    ventana_ventas = tk.Tk()
    ventana_ventas.title("EVENT MANAGE- Gestiona tus eventos como un profesional")
    ventana_ventas.geometry("905x545")
    ventana_ventas.config(bg="#f1ebfe")

    barra_lateral = tk.Frame(ventana_ventas, width=198, bg="#A5D3F5", height=550)
    barra_lateral.place(relx=0, rely=0, anchor="nw")

    titulo_menu = tk.Label(ventana_ventas, text="Menú",
                           font=("monotype corsiva", 27, "italic"),
                           fg="black", bg="#A5D3F5")
    titulo_menu.place(relx=0.10, rely=0.12, anchor="center")

    eslogan = tk.Label(ventana_ventas, text="Organiza con propósito, impacta con pasión",
                       font=("monotype corsiva", 21, "italic"), fg="black", bg="#f1ebfe")
    eslogan.place(relx=0.61, rely=0.06, anchor="center")

    imagen_eventos = Image.open("eventos.png")
    imagen_eventos = ImageTk.PhotoImage(imagen_eventos)
    eventos_mosaico = tk.Label(ventana_ventas, image=imagen_eventos, bg="#f1ebfe")
    eventos_mosaico.image = imagen_eventos  # Mantener referencia
    eventos_mosaico.place(relx=0.611, rely=0.55, anchor="center")

    boton_salir_programa = tk.Button(ventana_ventas, text="Salir",
                                     font=("monotype corsiva", 14), bg="#f1ebfe", command=Salir_del_programa)
    boton_salir_programa.place(relx=0.1, rely=0.94, anchor="center")

    boton_regresar_login = tk.Button(ventana_ventas, text="Regresar",
                                    font=("monotype corsiva", 14), fg="black", bg="#f1ebfe", command=Volver_Login)
    boton_regresar_login.place(relx=0.1, rely=0.85, anchor="center")

    boton_crear_evento = tk.Button(ventana_ventas, text="Crear eventos",
                                   font=("monotype corsiva", 14), bg="#f1ebfe", command=Crear_eventos)
    boton_crear_evento.place(relx=0.1, rely=0.25, anchor="center")

    ventana_ventas.mainloop()


if __name__ == "__main__":
    ventas()
