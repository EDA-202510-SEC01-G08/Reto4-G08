import sys
import time
import csv
from App import logic as lg
import tabulate as tb
from DataStructures.Graph import digraph as gr     
from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as mp  
from DataStructures.List import array_list as al


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return lg.new_logic()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    file = input("Ingrese el nombre del archivo a cargar: ")
    file_path = f"Data/Data/deliverytime_{file}.csv" 

    resumen = lg.load_data(control, file_path)

    print("\nResumen de la carga de datos:")
    print(f"• Número total de domicilios procesados: {resumen['total_domicilios']}")
    print(f"• Número total de domiciliarios identificados: {resumen['total_domiciliarios']}")
    print(f"• Número total de nodos en el grafo creado: {resumen['total_nodos']}")
    print(f"• Número de arcos en el grafo creado: {resumen['total_arcos']}")
    print(f"• Número de restaurantes identificados por su ubicación geográfica: {resumen['total_restaurantes']}")
    print(f"• Número de ubicaciones donde han llegado los domiciliarios: {resumen['total_destinos']}")
    print(f"• Promedio de tiempo de entrega de todos los domicilios procesados: {resumen['promedio_tiempo']:.2f} minutos")



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    origen = input("Ingrese la ubicación de origen (ejemplo: lat,lon): ")
    destino = input("Ingrese la ubicación de destino (ejemplo: lat,lon): ")
    resultado = lg.req_1(control, origen, destino)

    if "mensaje" in resultado:
        print(resultado["mensaje"])
    else:
        headers = ["Tiempo", "Cantidad_de_puntos", "Dominiciliarios", "Secuencia_de_ubicaciones","Restaurante"]
        data = resultado[0]["elements"]
        print(f"\n MENSAJE")
        print(tb.tabulate(data, headers, tablefmt="pretty"))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    punto = input("Ingrese la ubicación (ejemplo: lat,lon): ")
    resultado = lg.req_3(control, punto)

    if "mensaje" in resultado:
        print(resultado["mensaje"])
    else:
        headers = ["Domiciliario_mas_popular", "Pedidos_totales", "Vehiculo_mas_usado", "Tiempo"]
        data = resultado[0]["elements"]
        print(f"\n MENSAJE")
        print(tb.tabulate(data, headers, tablefmt="pretty"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    punto_a = input("Ingrese la ubicación de inicio (ejemplo: lat,lon): ")
    punto_b = input("Ingrese la ubicación de destino (ejemplo: lat,lon): ")
    resultado = lg.req_4(control, punto_a, punto_b)

    if "mensaje" in resultado:
        print(resultado["mensaje"])
    else:
        headers = ["Camino_simple", "Domiciliarios_comunes", "Tiempo"]
        data = resultado[0]["elements"]
        print(f"\n MENSAJE")
        print(tb.tabulate(data, headers, tablefmt="pretty"))
   


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
