import tkinter as tk

lista_consultas = []
lista_quejas = []
ventana = tk.Tk()
ventana.title("Fitbot - Asistente Virtual")
ventana.geometry("600x700")
ventana.config(bg="#FF6D00")
respuesta = tk.Label(ventana, text="", font=("Arial", 13), fg="black", bg="#FF6D00")
respuesta.pack(pady=20)
def manejar_opcion(opcion):
    if opcion == 0:
        ventana.quit()
    elif opcion == 1:
        mostrar_catalogo()
    elif opcion == 2:
        mostrar_consultas()
    elif opcion == 3:
        mostrar_quejas()
    elif opcion == 4:
        armar_combo()
    else:
        respuesta.config(text="Opción inválida", fg="red")
def mostrar_catalogo():
    catalogo = """
    **** Catálogo de Productos ****
    Proteínas ISO:
    Son proteínas Isolatadas más puras, porcentaje 
    de proteína superior al 90% sin grasa ni lactosa
    y rápida absorción e ideal para fase de definición.
    - Kevin Levrone anabolic ISOwhey 5L --- $125
    - Nutrex Isofit 5L --- $111
    - Isolate Gold Standard 3L --- $98
    - Mutant ISO Surge 5L --- $87,15

    Proteínas Whey:
    Son proteínas obtenidas del suero de leche, contienen 
    grasa y lactosa, se absorben un poco más lento, 
    más económicas que las ISO e ideal para fase de volumen.
    - LevroWhey 10L --- $125
    - Levro Legendary Mass 6.6L --- $50
    - Mutant Mass 22L --- $112
    - Carnivore lean meal 4.34L --- $79

    Creatinas:
    Mejora el rendimiento, ayuda a ganar masa muscular 
    y acelera la recuperación muscular
    - Levromono 300g --- $21
    - CreaDragon 300g --- $35
    - Ronnie Coleman creatina XS 2.2L --- $63
    """
    respuesta.config(text=catalogo, fg="black")
def mostrar_consultas():
    consulta = consultas_quejas("Por favor, escribe tu consulta:")
    if consulta:
        lista_consultas.append(consulta)
        respuesta.config(
            text=f"Consulta recibida: {consulta}\nUn asesor se pondrá en contacto contigo.", fg="black")
def mostrar_quejas():
    queja = consultas_quejas("Por favor, escribe tu queja:")
    if queja:
        lista_quejas.append(queja)
        respuesta.config(
            text=f"Queja recibida: {queja}\nNuestro equipo se pondrá en contacto contigo.", fg="black")
def armar_combo():
    combo_ventana = tk.Toplevel(ventana)
    combo_ventana.title("Armar tu Combo")
    combo_label = tk.Label(combo_ventana, text="Selecciona tu presupuesto para el combo:")
    combo_label.pack(pady=10)
    def mostrar_combo_seleccionado(presupuesto):
        if presupuesto == 1:
            combo_info = ("Combo: Kevin Levrone ISO whey 5L + Ronnie Coleman creatina XS + Energy Ghost.\nPrecio total: $188")
        elif presupuesto == 2:
            combo_info = ("Combo: Mutant Mass 22L + CreaDragon 300g + Energy Ghost.\nPrecio total: $149")
        elif presupuesto == 3:
            combo_info = ("Combo: Carnivore lean meal + Levromono 300g + Energy Ghost.\nPrecio total: $100")
        else:
            combo_info = "Opción no válida."
        respuesta.config(text=combo_info, fg="black")
        combo_ventana.destroy()
    opciones = [("Mayor a $150", 1), ("Menor a $150", 2), ("Hasta $100", 3)]
    for texto, val in opciones:
        tk.Button(combo_ventana, text=texto, command=lambda p=val: mostrar_combo_seleccionado(p)).pack(pady=5)
def consultas_quejas(mensaje):
    ventana_menu = tk.Toplevel(ventana)
    ventana_menu.title("Entrada de Información")
    etiqueta = tk.Label(ventana_menu, text=mensaje)
    etiqueta.pack(pady=10)
    requerimientos = tk.Entry(ventana_menu)
    requerimientos.pack(pady=5)
    entrada_usuario = []
    def enviar():
        entrada_usuario.append(requerimientos.get())
        ventana_menu.destroy()
    tk.Button(ventana_menu, text="Enviar", command=enviar).pack(pady=10)
    ventana_menu.wait_ventana()
    return entrada_usuario[0] if entrada_usuario else None

def mostrar_menu_principal():
    menu_ventana = tk.Toplevel(ventana)
    menu_ventana.title("Fitbot - Menú Principal")
    menu_text = "¡Hola, Soy Fitbot! ¿En qué puedo ayudarte?"
    tk.Label(menu_ventana, text=menu_text).pack(pady=10)
    opciones = [
        ("1. Catálogo de productos", 1),
        ("2. Consultas", 2),
        ("3. Quejas", 3),
        ("4. Te armamos tu combo", 4),
        ("0. Salir", 0)
    ]
    for texto, opcion in opciones:
        tk.Button(menu_ventana, text=texto, command=lambda op=opcion: manejar_opcion(op)).pack(pady=5)
encabezado = tk.Label(ventana, text="Bienvenido al Asistente Virtual Fitbot", font=("Arial", 23), fg="#07121A", bg="#FF6D00")
encabezado.pack(pady=10)
boton_menu = tk.Button(ventana, text="Abrir menú", font=("Arial", 14), command=mostrar_menu_principal)
boton_menu.pack(pady=20)
ventana.mainloop()
