# Función para pedir productos con **kwargs y una tupla
def pedir_elementos(cantidad, **kwargs):  # Define una función que recibe una cantidad y argumentos clave-valor opcionales
    mensaje = kwargs.get("mensaje", "Ingrese el producto")  # Obtiene el mensaje personalizado si se pasó como argumento, o usa uno por defecto
    elementos = tuple(input(f"{mensaje} #{i + 1}: ") for i in range(cantidad))  # Solicita al usuario que ingrese 'cantidad' de productos, usando input dentro de una comprensión de tuplas
    return elementos  # Devuelve los productos como una tupla

# Función para definir listas usando *args
def mostrar_lista(*listas):  # Define una función que puede recibir múltiples listas como argumentos
    for datos, lista in enumerate(listas, start=1):  # Itera sobre cada lista recibida, junto con un índice que empieza en 1
        print(f"\nLista de compras #{datos}:")  # Imprime el número de la lista (por si hay varias)
        for i, item in enumerate(lista, start=1):  # Itera sobre los elementos de la lista con su índice
            print(f"{i}. {item}")  # Muestra cada producto con su número correspondiente

# Función para eliminar un producto usando **kwargs
def eliminar_producto(compras, **kwargs):  # Define una función que recibe una lista de compras y argumentos opcionales 
    confirmar = kwargs.get("confirmar", True)  # Obtiene si se debe pedir confirmación antes de eliminar, por defecto True
    compras_lista = list(compras)  # Convierte la tupla de compras a una lista para poder modificarla

    if not compras_lista:  # Verifica si la lista está vacía
        print("La lista está vacía.")  # Muestra mensaje de lista vacía
        return tuple(compras_lista)  # Devuelve la lista (vacía) como tupla

    mostrar_lista(compras_lista)  # Muestra la lista actual de productos

    try:  # Intenta ejecutar el siguiente bloque de código que podría fallar
        posicion = int(input("Ingrese el número del producto que quiere eliminar: "))  # Pide al usuario un número de producto para eliminar
        if 1 <= posicion <= len(compras_lista):  # Verifica si el número está dentro del rango válido
            if confirmar:  # Si se requiere confirmación
                respuesta = input(f"¿Seguro que desea eliminar '{compras_lista[posicion - 1]}'? (s/n): ").lower()  # Pide confirmación al usuario
                if respuesta != "s":  # Si el usuario no confirma con "s"
                    print("No se eliminó nada.")  # Informa que no se eliminó
                    return tuple(compras_lista)  # Devuelve la lista original sin cambios
            eliminado = compras_lista.pop(posicion - 1)  # Elimina el producto en la posición indicada
            print(f"Producto eliminado: {eliminado}")  # Informa qué producto fue eliminado
        else:
            print("Número inválido. No se eliminó ningún producto.")  # El número está fuera de rango
    except ValueError: #si el usuario ingresa algo que no sea un número entero
        print("La entrada no es válida. No se eliminó nada.")  # Informa que la entrada no fue válida
    
    return tuple(compras_lista)  # Devuelve la lista resultante como tupla

# Función principal del programa
def ejecutar_lista_compras():  # Define la función que controla todo el flujo del programa
    while True:  # Bucle infinito para repetir el menú hasta que el usuario decida salir
        print("\n--- MENÚ DE LISTA DE COMPRAS ---")  # Muestra título del menú
        print("1. Crear nueva lista")  # Opción 1
        print("2. Salir")  # Opción 2
        opcion = input("Elige una opción (1 o 2): ")  # Solicita al usuario que elija una opción

        if opcion == "1":  # Si elige la opción 1
            # Crear la lista de compras con 4 elementos
            compras = pedir_elementos(4, mensaje="Producto a añadir")  # Llama a pedir_elementos con mensaje personalizado
            mostrar_lista(compras)  # Muestra la lista creada

            # Preguntar si desea eliminar algún producto de la lista
            decision = input("\n¿Desea eliminar algún producto? (s/n): ").lower()  # Pregunta al usuario si desea eliminar algo

            if decision == "s":  # Si responde que sí
                compras = eliminar_producto(compras, confirmar=True)  # Llama a eliminar_producto con confirmación habilitada
            else:
                print("No se ha eliminado nada.")  # Si no desea eliminar, lo informa

            mostrar_lista(compras)  # Muestra la lista final (ya sea editada o no)

        elif opcion == "2":  # Si elige salir
            print("Saliendo del programa.")  # Informa que se está cerrando el programa
            break  # Rompe el bucle y termina la función

        else:  # Si no elige una opción válida
            print("Opción no válida. Intente de nuevo.")  # Informa que la opción no es válida

# Ejecutar el programa
ejecutar_lista_compras()  # Llama a la función principal para iniciar el programa
 