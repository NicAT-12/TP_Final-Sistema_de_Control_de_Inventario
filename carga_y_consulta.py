def cargar_herramientas(inventario):
    while True:
        try:
            cantidad_de_herramientas_ingresadas = int(input("Ingrese la cantidad de herramientas: "))
            
            if cantidad_de_herramientas_ingresadas < 0:
                raise ValueError("La cantidad no puede ser negativa")

            break
        except ValueError as only_num:
            print(f"Error: {only_num}")