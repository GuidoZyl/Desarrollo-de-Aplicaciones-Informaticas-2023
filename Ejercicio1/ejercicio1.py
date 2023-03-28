import pandas as pd

df = pd.read_csv("presupuestos.csv")

lista = []
for i in df.index:
    presupuesto = [df['Nombre'][i], df['Colegio'][i], df['Cantidad de viajeros'][i], df['Acompañantes'][i], df['Precio'][i]]
    lista.append(presupuesto)

while True:
    print("1: Nuevo presupuesto\n2: Lista de presupuestos\nQ: Salir")
    opcion = input("Seleccione una opción: ")

    if (opcion == "1"):
        nombre = input("\nIngrese su nombre: ")
        colegio = input("Ingrese su colegio: ")
        
        cant_viajeros = int(input("Ingrese la cantidad de viajeros: "))
        acompañantes = 1 + int(cant_viajeros / 30)
        precio = (cant_viajeros + acompañantes) * 50000
        
        print("Precio: $" + str(precio) + "\n")

        presu = [nombre, colegio, cant_viajeros, acompañantes, precio]

        lista.append(presu)

        df = df.append(pd.DataFrame([presu], columns=["Nombre", "Colegio", "Cantidad de viajeros", "Acompañantes", "Precio"]), ignore_index=True)
        df.to_csv('presupuestos.csv')

    elif (opcion == "2"):
        count = 1
        print("-----------------")
        for presupuesto in lista:
            print("Presupuesto " + str(count) + "\n")
            print("Nombre: " + str(presupuesto[0]) + "\nColegio: " + str(presupuesto[1]) + "\nCantidad de Viajeros: " + str(presupuesto[2]) + 
                  "\nAcompañantes: " + str(presupuesto[3]) + "\nPrecio: $" + str(presupuesto[4]))
            print("-----------------")
            count += 1

    elif (opcion == "q" or opcion == "Q"):
        break

    else: 
        print("\nIngrese una opción valida\n")

