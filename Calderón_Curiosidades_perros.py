import tkinter as tk

ventana = tk.Tk()
ventana.title("Portal curiosidades sobre perros") 
ventana.geometry("800x400")
ventana.config(bg="#AADBAA")

encabezado = tk.Label(ventana, text ="Bienvenido a datos curiosos sobre perros", font=("Knight",20) , fg="#07121A",bg="#AADBAA")
encabezado.pack(pady=10)

usuario = tk.Label(ventana, text="Ingrese su nombre de usuario de 5 caracteres:",bg="#AADBAA")
usuario.pack()

entrada = tk.Entry(ventana, width=20)
entrada.pack(pady=10)
   
contraseña = tk.Label(ventana, text="Ingrese su contraseña de 4 caracteres:",bg="#AADBAA")
contraseña.pack()

entrada2 = tk.Entry(ventana, width=20)
entrada2.pack(pady=10)

respuesta = tk.Label(ventana, text="", font=("Calibri", 11),bg="#AADBAA")
respuesta.pack(pady=10)

def credenciales():
    user = entrada.get()
    clave = entrada2.get()

    if len(user) == 5 and len(clave) == 4:
        dato =(f"¡Hola {user}!\n\n"
    "¿Sabías que los perros pueden soñar como los humanos?\n\n"
    "¿Sabías que los Schnauzer pasaron de ser cazadores de ratas "
    "a convertirse en perros apreciados por la realeza?"
        )
        respuesta.config(text=dato)  
    else:
        respuesta.config(text="Su usuario o contraseña es incorrecto.")

boton_entrar = tk.Button(
    ventana,
    text="Entrar",
    command=credenciales
)
boton_entrar.pack(pady=10)

ventana.mainloop()

