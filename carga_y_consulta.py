def cargar_herramientas(inventario):
    while True:
        try:
            cantidad_de_herramientas_ingresadas = int(input("Ingrese la cantidad de herramientas: "))
            
            if cantidad_de_herramientas_ingresadas < 0:
                raise ValueError("La cantidad no puede ser negativa")

            break
        except ValueError as only_num:
            print(f"Error: {only_num}")

    for _ in range(cantidad_de_herramientas_ingresadas):
        while True:
            try:
                nombre_herramienta_ingresada = input("Ingrese el nombre de la herramienta: ")

                if not nombre_herramienta_ingresada.strip():
                    raise ValueError("Ingrese un nombre válido")

                for herramienta in inventario:
                    if herramienta['herramienta'] == nombre_herramienta_ingresada:
                        raise ValueError(f"{herramienta['herramienta']} ya existe en el inventario")

                break
            except ValueError as error:
                print(f"Error: {error}")

        while True:
            try:
                stock_herramienta_ingresada = int(input("Ingrese el stock de la herramienta: "))

                if stock_herramienta_ingresada < 0:
                    raise ValueError("El stock no puede ser negativo")

                break
            except ValueError as error:
                print(f"Error: {error}")

    inventario.append({'herramienta': nombre_herramienta_ingresada, 'cantidad': stock_herramienta_ingresada})