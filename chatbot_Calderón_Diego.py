import os
os.system('cls' if os.name == 'nt' else 'clear')
print("                      ______   ")
print("                     |      |   ")
print("                   |¬|  O O |¬|  ")
print("                     |   ^  |          ")            
print("        __           | ¬¬¬¬ |          __")
print("       |__|   __     |______|    __   |__|")
print("        |    |  |      | |      |  |    |")
print("        |____|__|______| |______|__|____|")
print("                    |_______|")
print("+" , "-"*52 , "+")   
print("|       Hola, Soy Fitbot ¿En qué le puedo ayudar?      |")
print("| Estoy aquí para facilitar su experiencia de usuario. |")
print("+" , "-"*52 , "+") 
while True:
    print("Por favor, de las siguientes opciones, seleccione el número que se ajuste a su requerimiento .")
    print("1. Catálogo de productos.")
    print("2. Consultas.")
    print("3. Quejas.")
    print("4. Te armamos tu combo.")
    print("0. Salir.")
    opcion_txt = input("Digite el número correspondiente: ")
    if not opcion_txt.isdigit():
       os.system('cls' if os.name == 'nt' else 'clear')
       print("Opción inválida, por favor intenta de nuevo.")
       print("___________________________________________")
       continue
    else:
        opcion=int(opcion_txt)
        if opcion == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encantados de atenderte.")
            print("Selecciona el qué rango que se ajuste a su presupuesto y armaremos un super combo para usted.")
            while True:
                print("1. Su presupuesto es mayor a $150.")
                print("2. Su presupuesto es menor a $150.")
                print("3. Su presupuesto es de hasta $100.")
                print("0. Regresar.")
                combo_txt = input("Digite el número correspondiente: ")
                if not combo_txt.isdigit():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Opción inválida, por favor intenta de nuevo.")
                    print("___________________________________________")
                    continue
                else:
                    combo=int(combo_txt)  
                    if combo ==3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print ("Tu combo tendría una Carnivore lean meal 4.34L, una Levromono  300g y de regalo un Energy Ghost y un shaker." )
                        print("Por solo $100.")
                        print("Si desea más información, déjanos su información de contacto.")
                        print ("Para volver al menu principal escriba 's'")
                        comprar = input("Ingresa tu información aquí: ").strip().lower()
                        if comprar == "s":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Volviendo al menú principal.")
                            print("___________________________________________")
                            break
                        else :
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Estamos para ayudarte, pronto uno de nuestros asesores se contactará con usted.")
                            volver_menu_1 = False  
                            while True:
                                salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                                if salir == "s":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Volviendo al menú principal.")
                                    print("___________________________________________")
                                    volver_menu_1 = True
                                    break 
                                elif salir == "n":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Gracias por visitarnos. Es un placer atenderte.")
                                    print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                                    exit()
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Opción inválida, por favor intenta de nuevo.")
                                    print("___________________________________________")     
                            if volver_menu_1:
                                break  
                    elif combo == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Tu combo tendría una Mutant Mass 22L, una CreaDragon 300g y de regalo un Energy Ghost y un shaker.")
                        print("Por solo $147.")
                        print("Si desea más información, déjanos su información de contacto.")
                        print ("Para volver al menu principal escriba 's'")
                        comprar = input("Ingresa tu información aquí: ").strip().lower()
                        if comprar == "s":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Volviendo al menú principal.")
                            print("___________________________________________")
                            break  
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Gracias por elegirnos, pronto uno de nuestros asesores se contactará con usted.")
                            volver_menu_1 = False  
                            while True:
                                salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                                if salir == "s":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Volviendo al menú principal.")
                                    print("___________________________________________")
                                    volver_menu_1 = True
                                    break 
                                elif salir == "n":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Gracias por visitarnos. Es un placer atenderte.")
                                    print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                                    exit()
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Opción inválida, por favor intenta de nuevo.")
                                    print("___________________________________________")     
                            if volver_menu_1:
                                break  
                    elif combo == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Tu combo tendría una Kevin Levrone anabolic ISO whey 5L, un Ronnie Coleman creatina XS 2.2L y de regalo un Energy Ghost y un shaker.")
                        print("Por solo $188.")
                        print("Si desea más información, déjanos su información de contacto.")
                        print ("Para volver al menu principal escriba 's'")
                        comprar = input("Ingresa tu información aquí: ").strip().lower()
                        if comprar == "s":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Volviendo al menú principal.")
                            print("___________________________________________")
                            break
                        else :
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Gracias por elegirnos, pronto uno de nuestros asesores se contactará contigo.")
                            volver_menu_1 = False  
                            while True:
                                salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                                if salir == "s":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Volviendo al menú principal.")
                                    print("___________________________________________")
                                    volver_menu_1 = True
                                    break 
                                elif salir == "n":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Gracias por visitarnos. Es un placer atenderte.")
                                    print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                                    exit()
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Opción inválida, por favor intenta de nuevo.")
                                    print("___________________________________________")     
                            if volver_menu_1:
                                break  
                    elif combo == 0:
                         os.system('cls' if os.name == 'nt' else 'clear')
                         print("Volviendo al menú principal.")
                         print("___________________________________________")
                         break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Opción inválida, por favor intenta de nuevo.")
                        print("___________________________________________")
        elif opcion == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encantados de atenderte.")
            print("Por favor, escribe tu queja y tu infornación de contacto. Pronto uno de nuestros asesores le atenderá.")
            print ("Para volver al menu principal escriba 's'")
            queja = input("¿En qué podemos ayudarte?: ").strip().lower()
            if queja == "s":
               os.system('cls' if os.name == 'nt' else 'clear')
               print("Volviendo al menú principal.")
               print("___________________________________________")
               continue
            else :
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Gracias, su opinion nos importa, pronto uno de nuestros asesores se contactará con usted.")
                volver_menu_1 = False  
                while True:
                    salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                    if salir == "s":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Volviendo al menú principal.")
                        print("___________________________________________")
                        volver_menu_1 = True
                        break 
                    elif salir == "n":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Gracias por visitarnos. Es un placer atenderte.")
                        print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                        exit()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Opción inválida, por favor intenta de nuevo.")
                        print("___________________________________________")     
                if volver_menu_1:
                    continue  
        elif opcion == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encantados de atenderte.")
            print("Por favor, escribe tu requerimiento y tu infornación de contacto. Pronto uno de nuestros asesores le atenderá.")
            print ("Para volver al menu principal escriba 's'")
            duda = input("¿En qué podemos ayudarte?: ").strip().lower()
            if duda == "s":
               os.system('cls' if os.name == 'nt' else 'clear')
               print("Volviendo al menú principal.")
               print("___________________________________________")
               continue
            else :
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Estamos para ayudarte, pronto uno de nuestros asesores se contactará con usted.")
                volver_menu_1 = False  
                while True:
                    salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                    if salir == "s":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Volviendo al menú principal.")
                        print("___________________________________________")
                        volver_menu_1 = True
                        break 
                    elif salir == "n":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Gracias por visitarnos. Es un placer atenderte.")
                        print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                        exit()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Opción inválida, por favor intenta de nuevo.")
                        print("___________________________________________")     
                if volver_menu_1:
                    continue 
        elif opcion == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encantados de ayudarte.")
            print("Este es nuestro catalogo de productos.")
            proteinas_ISO = ["> Kevin Levrone anabolic ISOwhey 5L---$125", "> Nutrex Isofit 5L--------------------$111", "> Isolate Gold Standard 3L------------$98", "> Mutant ISO Surge 5L-----------------$87,15"]
            proteinas_whey = ["> LevroWhey 10L---------------$125", "> Levro Legendary Mass 6.6L---$50", "> Mutant Mass 22L-------------$112", "> Carnivore lean meal 4.34L---$79"]
            creatinas = ["> Levromono  300g-------------------$21", "> CreaDragon 300g-------------------$35", "> Ronnie Coleman creatina XS 2.2L---$63"]
            while True:
                print("Disponemos de las siguientes proteínas:")
                print("_______________________________________")
                print("**** Proteinas ISO ****")
                print("Son proteínas Isolatadas más puras, porcentaje de proteína superior al 90% sin grasa ni lactosa y rápida absorción e ideal para fase de definición.")
                for producto in proteinas_ISO:
                    print(producto)
                print("_______________________________________")
                print("**** Proteinas whey ****")
                print("Son proteínas obtenidas del suero de leche, contienen grasa y lactosa, se absorben un poco más lento, más económicas que las ISO e ideal para fase de volumen.")
                for producto in proteinas_whey:
                    print(producto)
                print("_______________________________________")  
                print("_______________________________________")    
                print("Disponemos de las siguientes creatinas:")
                print("_______________________________________")
                print("**** Creatina ****")  
                print("Mejora el rendimiento, ayuda a ganar masa muscular y acelera la recuperación muscular.")
                for producto in creatinas:
                    print(producto)
                print("___________________________________________")
                print("Si deseas más información de nuestros productos, déjanos su información de contacto.")
                print ("Para volver al menu principal escriba 's'")
                comprar = input("Ingresa tu información aquí: ").strip().lower()
                if comprar =="s":
                     os.system('cls' if os.name == 'nt' else 'clear')
                     print("Volviendo al menú principal.")
                     print("___________________________________________")
                     break
                else:
                     os.system('cls' if os.name == 'nt' else 'clear')
                     print("Estamos para ayudarte, pronto uno de nuestros asesores se contactará contigo.")
                     volver_menu_1 = False  
                     while True:
                         salir = input("¿Hay algo más en lo que le pueda ayudar? (Escriba 's' para sí o 'n' para no): ").strip().lower()
                         if salir == "s":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Volviendo al menú principal.")
                            print("___________________________________________")
                            volver_menu_1 = True
                            break 
                         elif salir == "n":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Gracias por visitarnos. Es un placer atenderte.")
                            print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
                            exit()
                         else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Opción inválida, por favor intenta de nuevo.")
                            print("___________________________________________")     
                     if volver_menu_1:
                        break 
        elif opcion == 0:
             os.system('cls' if os.name == 'nt' else 'clear')
             print("Gracias por visitarnos. Es un placer atenderte.")
             print("Siempre para ayudarte: Fitbot, tu asistente virtual de suplementos fitness")
             break
        else:
             os.system('cls' if os.name == 'nt' else 'clear')
             print("Opción inválida, por favor intenta de nuevo.")
             print("___________________________________________")   