
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


ventana = None
respuesta_validacion = None
intentos = 0

usuario_correcto = "Usuario1"
clave_correcta = "1234"

def Validar_clave(ingresar_clave, ingresar_usuario):
    global intentos
    usuario_ingresado = ingresar_usuario.get()
    clave_ingresada = ingresar_clave.get()

    if clave_ingresada == clave_correcta and usuario_ingresado == usuario_correcto:
        print("Login OK")
        respuesta_validacion.config(text="Acceso concedido")
        ventana.after(400, abrir_ventas_y_cerrar_login)
    else:
        intentos += 1
        if intentos >= 3:
            respuesta_validacion.config(text="Superó el número de intentos.")
            ventana.after(500, ventana.destroy)
        else:
            respuesta_validacion.config(
                text=f"Usuario o contraseña incorrectos. Intento {intentos}/3"
            )


def abrir_ventas_y_cerrar_login():
    ventana.destroy()
    from modulo_ventas import ventas
    ventas()

def Salir_del_programa():
    respuesta = messagebox.askquestion(
        title="¿Estás seguro/a de que quieres salir del programa?",
        message="Para finalizar presione Sí caso contrario presione No"
    )
    if respuesta == "yes":
        ventana.destroy()

def Ingreso():
    global boton_iniciar_sesion, salir_programa, respuesta
    boton_iniciar_sesion.place_forget()
    salir_programa.place_forget()
    respuesta.config(text="Inicie sesión para acceder al menú principal", font=("monotype corsiva", 18), bg="#f1ebfe")
    respuesta.place(relx=0.42, rely=0.28, anchor="center")
    tk.Label(ventana, text="Ingrese usuario:", font=("monotype corsiva", 16), bg="#f1ebfe").place(relx=0.44, rely=0.42, anchor="se")
    ingrese_usuario = tk.Entry(ventana, width="30")
    ingrese_usuario.place(relx=0.75, rely=0.42, anchor="se")
    tk.Label(ventana, text="Ingrese contraseña:", font=("monotype corsiva", 16), bg="#f1ebfe").place(relx=0.44, rely=0.50, anchor="se")
    ingrese_clave = tk.Entry(ventana, show="*", width="30")
    ingrese_clave.place(relx=0.75, rely=0.50, anchor="se")
    ingrese_clave_boton = tk.Button(ventana, text="Ingresar", bg="#A5D3F5", font=("monotype corsiva", 14), command=lambda: Validar_clave(ingrese_clave, ingrese_usuario))
    ingrese_clave_boton.place(relx=0.89, rely=0.72, anchor="se")
    tk.Button(ventana, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5", command=Salir_del_programa).place(relx=0.32, rely=0.72, anchor="se")

def Login():
    global ventana, respuesta, respuesta_validacion, boton_iniciar_sesion, salir_programa
    ventana = tk.Tk()
    ventana.title("EVENT MANAGE- Gestiona tus eventos como un profesional")
    ventana.geometry("625x625")
    ventana.config(bg="#f1ebfe")
    marco_login_img = Image.open("bienvenida_marco.png").resize((600, 600))
    marco_login_img = ImageTk.PhotoImage(marco_login_img)
    marco_bienvenida = tk.Label(ventana, image=marco_login_img, bg="#f1ebfe")
    marco_bienvenida.image = marco_login_img  # guarda referencia para que no se borre la imagen
    marco_bienvenida.place(relx=0.01, rely=0.02, anchor="nw")
    respuesta = tk.Label(ventana, text="¡Bienvenido/a a Event Manage!", font=("monotype corsiva", 25), fg="black", bg="#f1ebfe")
    respuesta.place(relx=0.76, rely=0.38, anchor="se")
    respuesta_validacion = tk.Label(ventana, text="", font=("monotype corsiva", 18), bg="#f1ebfe")
    respuesta_validacion.place(relx=0.56, rely=0.61, anchor="center")
    boton_iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", font=("monotype corsiva", 14), bg="#A5D3F5", command=Ingreso)
    boton_iniciar_sesion.place(relx=0.60, rely=0.65, anchor="se")
    salir_programa = tk.Button(ventana, text="Salir", font=("monotype corsiva", 14), bg="#A5D3F5", command=Salir_del_programa)
    salir_programa.place(relx=0.55, rely=0.75, anchor="se")
    ventana.mainloop()

if __name__ == "__main__":
    Login()


    