name = "Edy";
password = "2";

intentos = 0;
salir = False;

persona = {"nombre":"Mario", "edad":35, "Color favorito":"Rojo"}; 

while intentos <= 2 and not salir:
    print(salir);
    v_name = input("Ingrese su nombre: \n");
    v_pass = input("Ingrese su Contraseña: \n");

    if v_name == name and v_pass == password:
        intentos

        opcion = "";

        while opcion != 5:
            opcion = int(input(F"""
                Selecciona una opcion: \n
                1. Condicional
                2. Bucles
                3. Listas
                4. Diccinarios
                5. Salir       
            """));

            if opcion == 1:
                print("opcion1");
                print("vamos a crear una condicion:");
                places = [];
                cont = 1;
                while cont <= 3:
                    place = input("Ingresa 3 lugares que desearias conocer: \n")
                    places.append(place);
                    cont += 1;    

                cont = 0;
                while cont <= 2:
                    prefer = input(f"""
                    {places[cont]} es tu primera eleccion?\n Y/N               
                                """)
                    if prefer == "y" or prefer == "Y":
                        print(places[cont], " es genial, tambien me gustaria conocerlo");
                        break;
                    else:
                        print("Dato no valido");
                    cont += 1;

            elif opcion == 2:
                option_b = 0;
                print(" Creemos un bucle");
                option_b = int(input("Cual prefieres con for(1) o while(2)\n"));
                if option_b == 1:
                    cont = 0;
                    fruit_list = [];
                    cant = int(input("Creemos una lista con frutas \n Cuantas quieres agregar?"));
                    while cont < cant:
                        fruit = input("Ingresa fruta")
                        fruit_list.append(fruit);
                        print(fruit_list);
                        cont += 1;

                    print("Ahora usamos un for para recorrer el array");
                    for i in fruit_list:
                        print(f"""
                        Posicion {fruit_list.index(i)} es {i}
                        """)
                        
                elif option_b == 2:
                    num = int(input(f"Contemos hasta:\n "));
                    cont = 1;
                    while cont <= num:
                        print(f"{cont}");
                        cont +=1;

                else:
                    print("Opcion no valida");
                                
            elif opcion == 3:
                new_color = ["Blanco", "Negro", "Marron"];
                colors_list = ["Azul", "Rojo", "Verde", "Amarillo"];
                option_list = int(input(f""" Teniendo esta lista {colors_list} que deseas hacer
                    1. Agregar Color
                    2. Eliminar Color
                    """));
                if option_list == 1:                    
                    color = int(input(f"""Selecciona un color para agregar
                                1. Blanco
                                2. Negro
                                3. Marron"""));
                    if color ==1:
                        colors_list.append(new_color[color-1]);
                        print(f"""El color {color} se agregado a tu lista""");
                        for position, color in enumerate(colors_list):
                            print(f"{position+1}.{color}");
                    elif color == 2:
                        colors_list.append(new_color[color-1]);
                        print(f"""El color {color} se agregado a tu lista""");
                        for position, color in enumerate(colors_list):
                            print(f"{position+1}. {color}");                        
                    elif color == 3:
                        colors_list.append(new_color[color-1]);
                        print(f"""El color {color} se agregado a tu lista""");
                        for position, color in enumerate(colors_list):
                            print(f"{position+1}. {color}");
                    else:
                        print("Dato no valido");
                elif option_list == 2:
                    print("Colores en lista: \n");
                    for position, color in enumerate(colors_list):
                        print(f"{position+1}. {color}");                                   
                    color = int(input("Selecciona el color que deseas eliminar de la lista\n"));
                    if color <= len(colors_list):
                        del_color = colors_list[color-1];
                        new_color.append(del_color);
                        colors_list.pop(color-1);
                        print(f"El color {del_color} se ha eliminado de la lista {colors_list}")

                else:
                    print("Dato no valido");
            

            elif opcion == 4:

                opciones = int(input(f"""Selecciona una opicon
                            1. Consultar informacion
                            2. Agregar informacion
                            3. Eliminar dato
                            4. Salir\n"""));

                cont = 1;
                salir = False;
                while cont <= 3 and not salir:
                    if opciones == 1:
                        print(persona);
                        salir = True;

                    elif opciones == 2:
                        dato1 = input("Que dato deseas ingresar: \n");
                        valor =  input("Ingrese el valor que tendra");
                        persona[dato1] = valor;
                        print (f"Se agregado {dato1} con valor {valor} al diccionario {persona} \n");
                        salir = True;
                    elif opciones == 3:
                        del_dato = input(f"Seleccione el dato desea eliminar de {persona}\n");
                        persona.pop(del_dato);
                        print(f"Se a eliminado {del_dato} del diccinario {persona}\n");
                        salir = True
                    elif opciones == 4:
                        cont = 4;
                    else:
                        print("dato no valido\n");
                        

                        
            elif opcion == 5:
                print("Bye");
                salir = True;
                break;
            else:
                print("Opicion no valida");

            
    else:
        if (2 - intentos) > 0 and (v_name != name or v_pass != password):
            print("Usuario a contraseña incorrectos, intenta de nuevo \n te quedan ", 2 -intentos, " intentos");
            intentos += 1;

        else:
            print("Acceso denegado");
            break;















